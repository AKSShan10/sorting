'''
In this probelem, we check first index with all other index, and we put it in the first index
Time complexity for the best case, and worst case is O(n^2)
Space complexity for the problemn is O(1)
LInk: https://www.geeksforgeeks.org/selection-sort/
'''

arr = [7,4,10,8,3,1]
print("Input array: ", arr)

n = len(arr)

for i in range(0,n-1):
    min_index = i
    for j in range(i+1,n):
        if arr[j] < arr[min_index]:
            min_index = j

    if min_index != i:
        arr[i], arr[min_index] = arr[min_index], arr[i]

print("Sorted array: ",arr)

