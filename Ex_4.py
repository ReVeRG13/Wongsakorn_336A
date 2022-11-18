Result = 0
FactorialCount = 8
for Integer in range(0,FactorialCount+1):
    Result += (1/(Integer+1))
    print(f"Limit : {Integer+1} , Value : {Result}")
def Factorial(FactorialCount):
    if FactorialCount == 0:
        return 1 
    else:
        return FactorialCount*Factorial(FactorialCount-1)