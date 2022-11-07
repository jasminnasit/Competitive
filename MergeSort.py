def MergeSort(list, l,r):
    if l<r :
        mid = int((l+r)/2)
        
        MergeSort(list, l , mid)
        MergeSort(list, mid + 1, r)

        merge(list, l, mid, r)


def merge(list, l , mid, r):
    s1 = mid - l + 1
    s2 = r - mid


    list1 = [None] * s1
    list2 = [None] * s2

    for it1 in range(s1):
        list1[it1] = list[l + it1]
    
    for it2 in range(s2):
        list2[it2] = list [mid + 1 + it2]


    i = 0
    j = 0

    k = l

    while i < s1 and j < s2 :
        if list1[i] < list2[j]:
            list[k] = list1[i]
            k += 1
            i += 1
        else:
            list[k] = list2[j]
            j+=1
            k+=1
    
    while i < s1:
        list[k] = list1[i]
        k+=1
        i+=1
    
    while j < s2:
        list[k] = list2[j]
        k+=1
        j+=1




list = [12,3,4,5,9,7,15,21]

MergeSort(list, 0, 7)

print(list)