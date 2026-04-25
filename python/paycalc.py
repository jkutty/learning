hours = 0
rate_1 = 10
rate_2 = 15
pay = 0

hours = raw_input("Please enter your number of hours worked: ")
try :
	if hours <= 40 :
		pay = int(hours) * rate_1
	elif hours > 40 :
		pay = (40 * rate_1) + (int(hours) - 40) * rate_2
	print(pay)
except:
	print("Please enter a number")
