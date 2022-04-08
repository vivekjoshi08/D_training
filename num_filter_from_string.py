def check(inp):
    lst = inp.split()
    final_lst = list()
    for num in lst:
        if num.isnumeric():
            final_lst.append(num)
            
    return final_lst
    
if __name__ == '__main__':
    inp = input()
    print(check(inp))