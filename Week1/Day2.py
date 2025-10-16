#Day 2-Python Basics
def day2():
    print("Multiplacation table using For loop")
    n=int(input("Enter number to print table : "))
    for i in range(1,11):
        print(f"{n}*{i}={n*i}")
    print("Multiplacation table using While loop")
    i=1  
    while(i<=10):
        print(f"{n}*{i}={n*i}")
        i+=1

day2()

