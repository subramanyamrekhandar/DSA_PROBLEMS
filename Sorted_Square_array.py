def sortedSquaredArray(array):
    # Write your code here.
    SquareValue = [0 for _ in array]
    SmallValueIdx = 0
    LargeValueIdx = len(array) - 1
    for idx in reversed(range(len(array))):
        SmallValue = array[SmallValueIdx]
        LargeValue = array[LargeValueIdx]
        if abs(SmallValue) > abs(LargeValue):
            SquareValue[idx] = SmallValue * SmallValue
            SmallValueIdx += 1
        else :
            SquareValue[idx] = LargeValue * LargeValue
            LargeValueIdx -=1
    return SquareValue      
    
    
    
    
main =  sortedSquaredArray([1,2,3,4,5,6,7,8,9])  
print(main)

#output : [1, 4, 9, 16, 25, 36, 49, 64, 81]
