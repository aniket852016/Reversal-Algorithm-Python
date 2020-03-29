def reverseArray(array, start, end): 
    while (start<end): 
        temp = array[start]
        array[start]= array[end]
        array[end]= temp 
        start+=1
        end -= 1
def lefRotation(array, d):
    n= len(array)
    reverseArray(array, 0, d-1)
    reverseArray(array, d, n-1)
    reverseArray(array, 0, n-1)
def PrintArray(array): 
    for i in range(0, len(array)): 
        print(array[i])
array = [1,2,3,4,5,6,7]
lefRotation(array, 2)
PrintArray(array)
