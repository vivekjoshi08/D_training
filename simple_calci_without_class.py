def add(num_lst):
    result = 0
    for num in num_lst:
        result += num
        
    return result
    
    
def sub(num1, num2):
    return num1-num2
    
def div(num1, num2):
    return num1/num2
    
def div_rem(num1,num2):
    return num1%num2
    
def mul(num_lst):
    result = 0
    for num in num_lst:
        result *= num
        
    return result
    
if __name__ == "__main__":
    choice = input("Press 1 for Addition\nPress 2 for subtraction\nPress 3 for division\nPress 4 for remainder of division\nPress 5 for multiplication: ")
    if choice == '1':
        inp = input("Enter comma seperated values you want to add: ")
        num_lst = (int(x) for x in inp.split(','))
        print("Addition of all num is {}".format(add(num_lst)))
    elif choice == '2':
        num1, num2 = int(input()), int(input())
        print("Subtraction of nums is {}".format(sub(num1, num2)))
    elif choice == '3':
        num1, num2 = int(input()), int(input())
        print("division of num1 and num2 is {}".format(div(num1,num2)))
    elif choice == '4':
        num1, num2 = int(input()), int(input())
        print("remainder is {}".format(div_rem(num1, num2)))
    elif choice == '5':
        inp = input("Enter comma seperated values you want to multiply: ")
        num_lst = (int(x) for x in inp.split(','))
        print("multiplication of all num is {}".format(mul(num_lst)))
    