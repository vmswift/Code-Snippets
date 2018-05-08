#Code example of a recursive fibonacci series function.
#Written using PyCharm IDE and Python 3
def fibonacci(n):
    if n<0:
        print("Wrong Value for N")
    elif n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)


def main():
    iterations=input("How many iterations would like? ")
    for i in range(1,int(iterations)+1):
        #type conversion with extra +1 to produce correct number of iterations
        print(fibonacci(i), end=" ")

#run code in main function.
if __name__ == '__main__':
    main()