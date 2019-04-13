import random
def mergeSort(data):
    if len(data) <= 1:
        return data[0:int(len(data))]
    mid = len(data) / 2
    blen = len(data)
    return merge(mergeSort(data[0:int(mid)]), mergeSort(data[int(mid):int(blen)]))


def merge(a, b):
    res = [None] * (len(a) + len(b))
    i = j = k = 0
    while (i < len(a) and j < len(b)):
        if a[i] < b[j]:
            res[k] = a[i]
            i = i+1
            k = k+1
        else:
            res[k] = b[j]
            k = k+1
            j = j+1
    while (i < len(a)):
        res[k] = a[i]
        k = k+1
        i = i+1
    while(j < len(b)):
        res[k] = b[j]
        k = k+1
        j = j+1
    return res


print(mergeSort([random.random() for _ in range(100000)]))
