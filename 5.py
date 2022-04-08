def check(m, n):
    res = 0
    dic = {}
    
    for i in m:
        if i not in dic:
            dic[i] = 0
        dic[i] += 1
    print(dic)
    for i in n:
        if i in dic:
            if dic[i] > 0:
                dic[i] -= 1
            else:
                res += 1
        else:
            res += 1
    print(dic)
    for i in dic.values():
        res += i
        
    return res
    
if __name__ == "__main__":
    m, n = input(), input()
    print(check(m,n))
    