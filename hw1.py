import math

#input: num, num
# ex: 5,2
while(a := input()):
	b = a.split(',')	
	output =   b[0] + " "
	firstNum = int(b[0])
	secondNum = int(b[1])

	if firstNum > secondNum:
		
	        output += " - " + str(firstNum-secondNum)
	elif firstNum < secondNum:
		multNum = int(secondNum / firstNum)
		plusNum = secondNum % firstNum
		if multNum > 1:
			output += "* " + str(multNum)
		if plusNum >0: 
			output += " + " + str(plusNum)

	print(output) 
	print("evalution: " + str(eval(output)))

