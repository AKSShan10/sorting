'''
In this sort, the best case is O(n) as the array will be sorted in ascending order. The worst case is O(n^2)
We use flag to optimze the code. In this case, we break the code if the swapping does not occur.
link: https://www.geeksforgeeks.org/bubble-sort/
'''

arr = [16,14, 5,6,8]
n = len(arr)

for i in range(n-1):
    flag = 0
    for j in range(0,n-1-i):
        if arr[j] > arr[j+1]:
            arr[j],arr[j+1] = arr[j+1],arr[j]
            flag = 1

    if flag == 0:
        break

print("Sorted array: ", arr)

