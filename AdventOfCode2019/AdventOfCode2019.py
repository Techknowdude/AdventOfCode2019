def dayOne():
	print("Day 1");
	input = [142536,103450,101545,133505,112476,62461,108718,93376,149609,147657,120888,85008,82501,122988,109493,91656,70001,130308,140298,104623,103542,129220,67381,143889,105384,139467,129004,89271,123863,108567,95453,109698,139953,107458,69734,106036,126036,
			 84832,68715,51484,92833,50734,58267,109650,137004,77709,95073,84817,55711,95408,148990,51697,129180,56196,72692,77049,124294,85102,124400,75981,135842,119561,79871,98771,134213,141322,131828,65692,113994,104632,129273,118023,54700,148185,61618,
			 132304,88308,121386,119548,115527,76627,63168,137582,113598,100899,100167,134345,90716,55476,113403,52745,78755,73421,93337,71171,122979,134298,123117,111244,122177]

	def getGas(mass):
		gas = mass / 3
		gas -= 2
		if gas > 0:	
			return gas + getGas(gas) 
		else:
			return 0

	def parseInput(input):
		totalGas = 0
		for i in input:
			totalGas += getGas(i)
		return totalGas



	test = [12,14,1969,100756,16,17]
	result = parseInput(input)
	print(result)
    
targetVal = 19690720

def doAction(operation, code, paramOne, paramTwo, outputPlace):
    if(outputPlace >= len(code)): 
        return outputPlace

    if operation == 1:
        add1 = code[paramOne]
        add2 = code[paramTwo]
        total = add1 + add2
        code[outputPlace] = total

    elif operation == 2:
        mult1 = code[paramOne]
        mult2 = code[paramTwo]
        total = mult1 * mult2
        code[outputPlace] = total

    return 0

def interpretCode(code):
    placeinCode = 0;

    while True:
        opCode = code[placeinCode]
        if(opCode == 99):
            break
        firstValue = code[placeinCode+1]
        secondValue = code[placeinCode+2]
        outputPlace = code[placeinCode+3]
        error = doAction(opCode, code, firstValue, secondValue, outputPlace)
        if(error != 0): return error
        placeinCode += 4
    return code[0]
    
def GetValueOfCode(input1, input2, code):
    code[1] = input1
    code[2] = input2
    output = interpretCode(code)
    result = [output,input1,input2, abs(targetVal - output)]
    return result

def dayTwo(input):
    
    def partOne():
        print("Day 2 - Part 1")


        interpretCode(input)
        
        print(input)
        print ("All Done")
        print(input[0])

    def IsGettingCloser(current, last, target):
        return abs(target-current) < abs(target-last)

    def FindParameterValues(code):

        for input1 in range(0,100):
            for input2 in range(0,100):
                print("Using " + str(input1) + " and " + str(input2))
                result = GetValueOfCode(input1,input2,list(code))

                print("Result: " + str(result))
                if(result[3] == 0): 
                    return "Used " + str(input1) + " and " + str(input2) + " to get: " + str(result) + " for an answer of: " + str(100 * input1 + input2)

    def partTwo(code):
        
        return FindParameterValues(code)

    return partTwo(input)

#input = [1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,10,1,19,1,19,9,23,1,23,13,27,1,10,27,31,2,31,13,35,1,10,35,39,2,9,39,43,2,43,9,47,1,6,47,51,1,10,51,55,2,55,13,59,1,59,10,63,2,63,13,67,2,67,9,71,1,6,71,75,2,75,9,79,1,79,5,83,2,83,13,87,1,9,87,91,1,13,91,95,1,2,95,99,1,99,6,0,99,2,14,0,0]

#dayTwoResult = dayTwo(input)
#print("DayTwo part 2 : " + str(dayTwoResult))