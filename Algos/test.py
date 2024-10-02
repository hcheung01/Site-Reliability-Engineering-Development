from data import array


# arrays and list

# structs

# hashmap and tables

# link list

    # singly
    
    # doubly

# graph

# stack

# queue

# bubble sort

def bubbleSort(arr):
    n = len(arr)
    
    for i in range(n-1):
        for j in range(i+1, n):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
            print(arr)
    
    return arr
        
    

# insertion sort
# selection sort
# count sort
# divide & conquer sort
# quick sort

# bubble sort




# binary search - recursive

def binarySearch(arr, num):
    
    def helper(l, h, num):
        if l <= h:
            m = l + ((h - l) // 2)
            print(f"low={l} high={h} mid={m}, num={num} arr={arr}")
            if arr[m] == num:
                return m
            
            if num < arr[m]:
                return helper(l, m - 1, num)
            else:
                return helper(m + 1, h, num)
        return None
            
    return helper(0, len(arr) - 1, num)

# binary search - iterative

def binarySearch2(arr, num, low, high):
    
    while low <= high:
        mid = low + (high - low) // 2
        if arr[mid] == num:
            return mid
        if num < arr[mid]:
            high = mid - 1
        elif num > arr[mid]:
            low = mid + 1
    return None

if __name__ == "__main__":
    import sys
    
    # Binary Search - Recursive and Iterative
    # num = int(sys.argv[1])
    # answer = binarySearch(arr, num)
    # answer = binarySearch2(arr, num, 0, len(arr)-1)
    # if answer and type(answer) is int:
    #     print(f"Index of num is {answer} for {arr[answer]}")
    # else:
    #     print("Answer is None")
    
    
    arr = [7, 2, 5, 1, 8, 100, 14, 55, 44]
 
    
    # Bubble Sorts
    answer = bubbleSort(array)
    
    print(f"Sorted Array: {answer}")