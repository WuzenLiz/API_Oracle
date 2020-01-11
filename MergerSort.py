def merge(start,end):
    a=[]
    i = j = 0
    while i < len(start) and j < len(end):
        if start[i] <= end[j]:
            a.append(start[i])
            i += 1

        else:
            a.append(end[j])
            j += 1

    a += start[i:]
    a += end[j:]

    return a

def sort(a):
    if len(a) == 1:
        return a

    mid = len(a)//2
    start = a[:mid]
    end = a[mid:]

    start = sort(start)
    end = sort(end)

    return list(merge(start,end))

if __name__ == '__main__':
    A=[9,7,8,3,2,1]
    print(sort(A))