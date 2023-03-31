def merge_sort(iterable):
    n = len(iterable)
    if n <= 1:
        return

    mid = n // 2
    array1 = iterable[:mid]
    array2 = iterable[mid:]
    merge_sort(array1)
    merge_sort(array2)

    l1 = 0
    l2 = 0
    listnum = 0

    while l1 < len(array1) and l2 < len(array2):
        if array1[l1] < array2[l2]:
            iterable[listnum] = array1[l1]
            l1 += 1
            listnum += 1
        else:
            iterable[listnum] = array2[l2]
            l2 += 1
            listnum += 1

    while l1 < len(array1):
        iterable[listnum] = array1[l1]
        l1 += 1
        listnum += 1
    
    while l2 < len(array2):
        iterable[listnum] = array2[l2]
        l2 += 1
        listnum += 1
    
test = [3, 30, 27, 21, 15, 12, 6, 9, 24, 18]
merge_sort(test)
print(test)

