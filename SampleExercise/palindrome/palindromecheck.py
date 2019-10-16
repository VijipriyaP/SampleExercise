

# function which return reverse of a string 
def reverse(s): 
	return s[::-1] 
  
def isPalindrome(s): 
	# Calling reverse function 
	rev = reverse(s) 
	  
	# Checking if both string are equal or not 
	if (s == rev): 
		return True
	return False

def main(txt_tocheck):

	### String captilization can cause invalid response, hence convert in to strandard format e.g., string Lower
	txt_tocheck = txt_tocheck.lower()

	response_format = "Input '{}' is {} Palidrome."

	print("*************** TEST RESULT *********************")
	
	if txt_tocheck:

		result = isPalindrome(txt_tocheck) 
	
		if result: 
		    print(response_format.format(txt_tocheck,'a')) 
		    return True
		else: 
		    print(response_format.format(txt_tocheck,'NOT')) 
		    return False
	else:
		print("invalid input")
		return True

	

if __name__ == '__main__':
	try:
		txt_tocheck = input("Please enter a word to check if Palidrome or not: ")
		main(txt_tocheck)
	except Exception as e:
		print(e)
	
