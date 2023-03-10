#input: 
#DEPTH CAP: number(e.g. '5')
#WIDTH: number(e.g. '5')
#EXAMPLES: list(e.g. '2->11,3->15')
#output:
#FORMULA: formula(e.g. ((input+1)*2))
#Input Parameters: input examples, depth (number of operations), 
#width (valid numbers for operations)
#Now we prune based on equivalency
validOperations = ['+','-','*','/']
additiveOps = ['+','-']
multiplicativeOps =['*','/']

seenAnswers = []
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
def findSolution(inputs, outputs, depthCap, currDepth, currString, validNums):
	if currDepth >= depthCap:
		return ''	
	for op in validOperations:
		for num in validNums:
			tempString = '(' + currString
			tempString += op
			tempString +=num +')' 
			#if for all inputs the awnser is equivalent to something already seen, then reset tempstring and continue

			results = evaluateSolutions(inputs, tempString)
			if results ==outputs:
				print("FORMULA: "+ tempString)

			if results in seenAnswers:
				continue
			else:
				seenAnswers.append(results)
			
			findSolution(inputs, outputs, depthCap, currDepth+1, tempString, validNums)
	
#input:: str[], operation:: str
def evaluateSolutions(input, operation):
	evalList = []
	for i in range(len(input)):
		newOperation = operation.replace("input", input[i])
		result = eval(newOperation)
		evalList.append(str(result))
	return evalList

def findFunction():
	print('DEPTH CAP: ')
	depthCap = int(input())
	print('WIDTH: ')
	width = int(input())
	validNums =[]
	for i in range(1, width+1):
			validNums.append(str(i)) 
	print('EXAMPLES (e.g. \'2->11,3->14\'): ')
	examples= input()
	ioList = extractInputsOutputs(examples)
	findSolution(ioList[0],ioList[1],depthCap,0,'input', validNums)
	print("End of Found Formulas")

def main():
	while(True):
		findFunction()
	
if __name__ == "__main__":
	main()