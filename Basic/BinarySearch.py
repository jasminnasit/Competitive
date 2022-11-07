def BinarySearch(list, start, end, num):
    mid = int((start+end)/2)
    if list[mid] == num :
        return mid
    elif list[mid] < num :
        return BinarySearch(list, mid+1, end, num)
    else :
        return BinarySearch(list, start, mid-1, num)

list = [11,25,35,37,49]

print(BinarySearch(list,0,4,25))