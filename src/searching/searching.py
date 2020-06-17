# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == target:
            return mid
        elif target < arr[mid]:
            return binary_search(arr[start:mid],target,start, mid)
        else:
            return binary_search(arr[mid:end],target,mid,end)
    return -1

# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
def agnostic_binary_search(arr, target):
    # Your code here
    pass
if __name__ == "__main__":
    arr1 = [-9, -8, -6, -4, -3, -2, 0, 1, 2, 3, 5, 7, 8, 9]
    print(binary_search(arr1, 0, 0, len(arr1)-1))
