def add(x,y):
    return x+y

def sub(x,y):
    return x-y

def mul(x,y):
    return x*y
def remainder(x,y):
    return x%y
def power(x,y):
    return x**y

def divide(x,y):
    if (y !=0):
        return x/y
    else: 
        return "Error! Division by zero."

result=0
while True:
    try:
        if(result==0):
            operator=""
        else:
            operator=input(" Choose +-/*^% or enter exit: ") #This is for taking operators like +-*/^%
    except ValueError:
        print("Invalid input! Please enter a valid operator between */+-^%")
        continue
    
    if(operator=="exit"):
        print("Good bye!")
        break
    try:
        n=int(input(" Enter number: "))
    except ValueError:
        print("Enter a valid number")
        continue

    
    
    if(result==0):
        result=n
        continue
    elif(operator=="+"):
        result=add(result,n)
        print(f"{result-n}{operator}{n}={result}")
    elif(operator=="-"):
        result=sub(result,n)
        print(f"{result+n}{operator}{n}={result}")
    elif(operator=="*"):
        result=mul(result,n)
        print(f"{result/n}{operator}{n}={result}")
    elif(operator=="/"):
        result=divide(result,n)
        print(f"{result*n}{operator}{n}={result}")
    elif(operator=="%"):
        result=remainder(result,n)
        print(f"{result+n}{operator}{n}={result}")
    elif(operator=="^"):
        result=power(result,n)
        print(f"{result**1/n}{operator}{n}={result}")
    else:
        print("Invalid input! Please enter a valid operator.")
    if(result==0):
        continue
    else:
        print(f"Current result={result}")
