import re

def pass_check( pass_):
    flag = 0
    
    while True:
        if len(pass_) < 6 or len(pass_) > 12:
            flag = 1
            print("len break")
            break
        elif not re.search("[a-z]", pass_):
            flag = 1
            print("a-z break")
            break
        elif not re.search('[$#@]', pass_):
            flag = 1
            print('lst break')
            break
        elif not re.search("[A-Z]", pass_):
            flag = 1
            print('A-Z break')
            break
        elif not re.search("[0-9]", pass_):
            flag = 1
            print('0-9 break')
            break
        else :
            return pass_
            
    if flag == 1:
        return " {} : password is not valid".format(pass_)
        
        
if __name__ == "__main__":
    lst = []
    valid_pass = list()
    '''
    while True:
        inp = input()
        if inp == 'Q' or inp =='q':
            break
        else:
            lst.append(inp)
    '''
    inp = input()
    lst = inp.split(',')
    for inp in lst:
        valid_pass.append(pass_check(inp))
        
    print(valid_pass)
        