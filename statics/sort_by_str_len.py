
arr_strings = ["GeeksforGeeeks", "I", "from", "am"]
str2_lengths = [];

for str1 in arr_strings:
    str2_lengths.append(len(str1))

print(str2_lengths)



high = len(str2_lengths)

def merge(arr, l, m, r):

    print("in merge");
    print(l)
    print(m) 
    n1 = m - l + 1
    n2 = r- m 
  
    # create temp arrays 
    L = [0] * (n1) 
    R = [0] * (n2) 
  
    # Copy data to temp arrays L[] and R[] 
    for i in range(0 , n1): 
        L[i] = arr[l + i] 
  
    for j in range(0 , n2): 
        R[j] = arr[m + 1 + j] 
  
    # Merge the temp arrays back into arr[l..r] 
    i = 0     # Initial index of first subarray 
    j = 0     # Initial index of second subarray 
    k = l     # Initial index of merged subarray 
  
    while i < n1 and j < n2 : 
        if L[i] <= R[j]: 
            arr[k] = L[i] 
            i += 1
        else: 
            arr[k] = R[j] 
            j += 1
        k += 1
  
    # Copy the remaining elements of L[], if there 
    # are any 
    while i < n1: 
        arr[k] = L[i] 
        i += 1
        k += 1
  
    # Copy the remaining elements of R[], if there 
    # are any 
    while j < n2: 
        arr[k] = R[j] 
        j += 1
        k += 1
  
# l is for left index and r is right index of the 
# sub-array of arr to be sorted 
def mergeSort(arr,l,r): 
    if l < r: 
  
        # Same as (l+r)/2, but avoids overflow for 
        # large l and h 
        m = (l+(r-1))/2
        print(l)
        print(m)
        # Sort first and second halves 
        mergeSort(arr, l, m) 
        print("first half")
        mergeSort(arr, m+1, r) 
        merge(arr, l, m, r)
    else:
        print("else part" + str(l)+str(r))

mergeSort(str2_lengths,0,high-1)

print(str2_lengths)