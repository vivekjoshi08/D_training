def bubble_sort(lst):
    for i in range(len(lst)-1, 0, -1):
        for j in range(i):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
    return lst
    
if __name__ == "__main__":
    lst = [4,6,2,1]
    print(bubble_sort(lst))