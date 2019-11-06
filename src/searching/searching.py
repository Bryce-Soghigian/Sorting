# STRETCH: implement Linear Search				
def linear_search(arr, target):
  for i in arr:
    if i == target:
      return i
    else:
      return -1
  

   


# STRETCH: write an iterative implementation of Binary Search 
def binary_search(arr, target):

  if len(arr) == 0:
    return -1 # array empty
  low = 0
  high = len(arr) -1
  while low <= high:
    mid = (low+high)/2
    if target < arr[mid]:
      high = mid-1
    if target > arr[mid]:
      low = mid+1
    else: 
      return mid
  return -1
  





# STRETCH: write a recursive implementation of Binary Search 
def binary_search_recursive(arr, target, low, high):
  
  middle = (low+high)//2

  if len(arr) == 0:
    return -1 # array empty
  # TO-DO: add missing if/else statements, recursive calls
