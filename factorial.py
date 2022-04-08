def fact(num):
    if num == 1:
        return 1
    else :
        return (num*fact(num-1))
        
if __name__ == '__main__':
    num = int(input("Enter integer: "))
    print("Factorial of {} is {}".format(num,fact(num)))
    