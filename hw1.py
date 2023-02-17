import math

#input: num->num, num->num etc..
# ex: 2-> 11, 3->14   --- (input+2)*3 - 1
#Input Parameters: input examples, depth (number of operations), 
#width (valid numbers for operations)
validOperations = ['+','-','*','/']

def extractInputsOutputs(examples):
	exampleList = examples.split(',')
	ioList =[]
	inputs = []
	outputs = []
	for example in exampleList:
		inout = example.split('->')
		inputs.append(inout[0])
		outputs.append(inout[1])
	ioList.append(inputs)
	ioList.append(outputs)
	return ioList
#inputs:: str[], outputs::str[], depthCap::int, currDepth::int, currString::string, width::int
#make width an outer function, pass valid nums to inner function
def findSolution(inputs, outputs, depthCap, currDepth, currString, width):
	validNums = []
	print(currString)
	print(currDepth)
	if currDepth >= depthCap:
		return ''
	tempString = '(' + currString
	for i in range(1, width+1):
		validNums.append(str(i)) 
	
	for op in validOperations:
		for num in validNums:
			tempString += op
			tempString +=num +')' 
			if(validateSolutions(inputs, outputs, tempString)):
				return tempString

			sol = findSolution(inputs, outputs, depthCap, currDepth+1, tempString, width)
			if sol:
				print(sol)
				return sol
			tempString = '(' + currString
#input:: str[], output::str[], operation:: str
def validateSolutions(input, output, operation):
	for i in range(len(input)):
		newOperation = operation.replace("input", input[i])
		result = eval(newOperation)
		if result != int(output[i]):
			return False
	return True
print('DEPTH CAP: ')
depthCap = input()
print('WIDTH: ')
width = input()
print('EXAMPLES (e.g. \'2->11,3->14\'): ')
examples= input()
ioList = extractInputsOutputs(examples)
output = findSolution(ioList[0],ioList[1],5,0,'input', 5)
print("FORMULA: "+ output)