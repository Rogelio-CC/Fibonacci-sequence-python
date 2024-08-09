class Fibonacci:
    #The constructor of the class is declared.
    def __init__(self, firstNumber=0, secondNumber=1):
        self.firstNumber = firstNumber
        self.secondNumber = secondNumber
        self.result = [self.firstNumber, self.secondNumber]

    def iterative_sequence(self, limitNumber):
        #Evaluates whether the limit number is 0 or negative
        if limitNumber <= 0:
            print('Only positive numbers, please')
            return []
        
        #Begins the fibonacci sequence
        while len(self.result) < limitNumber:
            next_value = self.result[-1] + self.result[-2]
            self.result.append(next_value)
        
        return self.result[:limitNumber] 


# Prints the results
limitNumber = int(input('What number would you like as the limit number for the Fibonacci sequence?' ))
fibonacci = Fibonacci()
if limitNumber > 0:
    print("-------------Fibonacci sequence-------------")
    print(fibonacci.iterative_sequence(limitNumber))
else:
    print(fibonacci.iterative_sequence(limitNumber))
