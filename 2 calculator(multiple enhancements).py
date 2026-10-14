

def add(numbers):
    y =0
    for x in numbers:
         y+=x    
    return y

def subtract(numbers):
    if not numbers:
        return 0
    x=numbers[0]
    for y in numbers[1:]:
        x=x-y
    return x

def multiply(numbers):
    y=1
    for x in numbers:
        y *= x
    return y

def divide(numbers):
    if not numbers:
        return 0
    x=numbers[0]
    for y in numbers[1:]:
        if y==0:
            return "Division by zero not possible"
        x=x/y
        return x
        
def power(numbers):
    x=1
    for y in numbers:
        x**=y
        return y

def average(numbers):
    x=len(numbers)
    y=add(numbers)
    n=[y,x]
    z=divide(n)
    return z
# later updating adding more operations




history=[]
r=1
while True:
    break_=1
    print("1.Addition")
    print("2.Substraction")
    print("3.Multiplication")
    print("4.Division")
    print("5.Average")
    print("6.History")
    print("7.Exit")

    choice = int(input("Choice the operation's number which you want do. "))
    
    if choice==7:
        print("Thank you for visiting")

    elif choice==6:
         for x in history:
          print(x)

    elif choice<8 and choice>0 and choice!=6 :
        print("proceed")

    
    else:
        print("choice appropriate option")
        continue
    while True:
        if choice==6:
            break

        history.append(r)

        nums=list(map(float, input("Enter your nums separated by space: ").split()))

        history.append(nums)

    #x= float(input("enter your first number "))
    #y= float(input("enter your second number "))
        if choice==1 :
            history.append("Addition")
            a=(add(nums))
            history.append(a)
            print(a)
        elif choice==2:
            history.append("Subtraction")
            a=(subtract(nums))
            history.append(a+"\n")
            print(a)
        elif choice==3:
            history.append("Multication")
            a=(multiply(nums))
            history.append(a)
            print(a)
        elif choice==4:
            history.append("Division")
            a=(divide(nums))
            history.append(a)
            print(a)
        elif choice==5:
            history.append("Average")
            a=(average(nums))
            history.append(a)
            print(a)

        r+=1
        break
        
    
    while True:
            break_-=1
            choice_2=str(input("Do you want to continue ? (yes/no)")).lower()
            if choice_2=="yes":
                break

            elif choice_2=="no":
             break_=1
             break

            else:
                ("invalid chioce choice try again")
                continue
    if break_==1:
            break
