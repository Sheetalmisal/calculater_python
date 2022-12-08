def addition(a,b):
    res=a+b
    print(f"Additions of {res}")

def substration(a,b):
    res=a-b
    print(f"substration {res}")

def multiplication(a,b):
    res=a*b
    print(f"multiplication {res}")

def division(a,b):
    res=a/b
    print(f"division {res}")


def calculater():
    while(True):
        print('''
        1.addition
        2.subtraction
        3.multiplication
        4.division
        '''
        )
choice=input("Enter the choice")

if(choice==1):
    addition(a,b)

elif(choice==2):
    substration(a,b)

elif(choice==2):
    multiplication(a,b)
    
elif(choice==2):
    division(a,b)
else:
    print("you choice wrong number please chack..!")

calculater()