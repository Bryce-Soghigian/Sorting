# TO-DO: Complete the selection_sort() function below 

# a = [16, 19, 11, 15, 10, 12, 14]
# const insertion_sort = (ar) => {
#     for(let i=0;i<ar.length;i++){
#         j=a.index(i)
#         while(j>0):
#             if (a[j-1]> a[j]){
#                 a[j-1],a[j] = a[j],a[j-1]
#             }else{
#                 break
#             j = j-1
#             }
#             return ar
#     }
# }
# insertion_sort(a)
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(len(arr)):
        min = i 
        for j in range(i+1,len(arr)):
            if arr[min] > arr[j]:
                min = j

        arr[i], arr[min] = arr[min],arr[i]




    return arr

#kw is some keyword 
#array is some data structure
"""
const linear_search = (arr, kw) => {
    for(let i = 0; i<arr.length; i++){
        if(i===kw){
            return kw
        }else{
            return "keyword doesn't exist within arr"
        }
    }
} 
"""

def linear_search(arr,kw):
    for i in range(0, len(arr)-1):
        if i == kw:
            return kw
        else:
            return f"Keyword doesn't exist in the array"


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    lastUnsorted = len(arr) -1
    isSorted = False
    while not isSorted:
        isSorted = True
        for i in range(lastUnsorted):
            if arr[i]> arr[i+1]:
                arr[i+1],arr[i] = arr[i],arr[i+1]
                isSorted = False
            
    lastUnsorted -= 1


    


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr