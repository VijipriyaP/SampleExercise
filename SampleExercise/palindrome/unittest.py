
import palindromecheck as pal



def valid_scenario_1():
	
	assert pal.main("madam")
		

def valid_scenario_2():

	assert pal.main("MAdam")


def invalid_scenario_1():
	assert not pal.main("afsf124")

def invalid_scenario_2():
	assert not pal.main("")



if __name__ == '__main__':
	try:
		# Prefer to use Pytest.  some issue with my laptop.
		
		
		valid_scenario_1()
		valid_scenario_2()
		invalid_scenario_1()
		invalid_scenario_2()
	
	except Exception as e:
		print(e)

