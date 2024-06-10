'''
Insertion Sort we assume that the input is sorted in ascending order. We assume that the first one is sorted, then the sorting start from the second index, and check it every time.
If the second index is greater than the first index, there will not be any swap operations. The array in descending order, then the time complexity is O(n^2)
will be worst O(n^2), If it is in ascending order, then the time complexity is O(n).
link: https://www.geeksforgeeks.org/insertion-sort/
'''

arr = [5,4,10,1,6,2]
print("original array: ", arr)
n = len(arr)

if n<=1:
    print("Sorted array: ", arr)

for i in range(1,n):
    temp = arr[i]
    j = i-1
    while j >= 0 and temp < arr[j]:
        arr[j+1] = arr[j]
        j-=1
    arr[j+1] = temp

print("Sorted array:",arr)