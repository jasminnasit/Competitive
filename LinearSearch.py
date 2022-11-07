def LinearSearch(list,n):
    le = len(list)
    for i in range(le):
        if list[i] == n :
            return i
    
    return -1


list = [1,2,5,4,3]

x = LinearSearch(list,5)
print(x)