# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    a = 0
    b = 0
    c = 0
    while a < len(arrA) and b < len(arrB):
        if arrA[a]< arrB[b]:
            merged_arr[c] = arrA[a]
            a += 1
        else:
            merged_arr[c] = arrB[b]
            b += 1
    return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    start = 0
    end = len(arr) -1
    result = []
    if end < 2:
        return arr
    mid = (start - end) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
   
    merge(left,right)
    return result

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
def merge_in_place(arr, start, mid, end):
    # Your code here
    pass

def merge_sort_in_place(arr, l, r):
    # Your code here
    pass

if __name__ == "__main__":
    print(merge([1],[2]))