'''
Divide and conquer the process. Time complexity is O(nlogn)
'''


def conquer(left, right):
    i = 0
    j = 0
    arr = []

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            arr.append(left[i])
            i+=1
        else:
            arr.append(right[j])
            j+=1

    while i < len(left):
        arr.append(left[i])
        i += 1

    while j< len(right):
        arr.append(right[j])
        j += 1

    return arr


def divide(arr):
    if len(arr)<=1:
        return arr

    mid = len(arr)//2
    #print(mid)
    left_array = divide(arr[:mid])
    right_array = divide(arr[mid:])
    return conquer(left_array,right_array)

#if __name__ == '__main__':
array = [10, 7, 8, 9, 1, 5]
print("Initial array: ", array)
#n = len(array)
#print(n)

sorted= divide(array)
print("Sorted array: ", sorted)