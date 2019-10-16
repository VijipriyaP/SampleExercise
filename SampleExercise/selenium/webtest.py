import os  
from selenium import webdriver  
from selenium.webdriver.common.keys import Keys  
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException  
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time


def waitforpagetoload(id, driver):
	timeout = 10 ## this can be changed. This is functionality checking hence keeping it higer
	try:
		element_present = EC.presence_of_element_located((By.ID, id))
		WebDriverWait(driver, timeout).until(element_present)
	except TimeoutException:
		print("Timed out waiting for page to load")
		return False
	finally:
		print("Page loaded")
		return True

	

def main():
	try:
		driver = webdriver.Chrome()  
		driver.get("http://the-internet.herokuapp.com")
		print("Page Load check......")
		main_page_loaded = waitforpagetoload('content',driver)
		
		if main_page_loaded:
			print("Finding first link")
			link = driver.find_element_by_partial_link_text("JavaScript Alerts")
			if link.is_displayed():  
				print("Found first Link")
				link.click()
				### finding second page
				second_page_loaded = waitforpagetoload('flash-messages',driver)
				if second_page_loaded:
					buttonfind = driver.find_element_by_xpath('//button[normalize-space()="Click for JS Confirm"]')
					buttonfind.click()
					time.sleep(2)
					driver.switch_to.alert.accept()
					resultelement =driver.find_element_by_xpath("/html/body/div[2]/div/div/p[2]")
					print(resultelement.text)
					if resultelement.text == 'You clicked: Ok':
						return True
					else:
						return False


			else:
				print("Link not found")
				return False
		else:
			print("Error")
			return False
	except:
		print("Excepion occured")

testresult = main()
print("******** Test Result *********")
if testresult:
	print("Test Success")
else:
	print("Test Failure")


