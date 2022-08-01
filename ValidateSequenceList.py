#method 1::::


def validateSequence(array,seq):
    check = 0
    result = False
    for i in (array):
        if seq[check]==i:
            check += 1
            if check == len(seq):
                result = True
                break
   # return check == len(seq)        
    return result  
Sequence =  validateSequence([5,1,22,25,6,-1,8,10],[1,6,8,10])  
print(Sequence)

# time O(n) and space complixity O(1)

#method 2


def validateSequence(array,seq):
    check = 0
      for i in (array):
        if seq[check]==i:
            check += 1
            if check == len(seq):
                break
     return check == len(seq)        
   
Sequence =  validateSequence([5,1,22,25,6,-1,8,10],[1,6,8,10])  
print(Sequence)

# time O(n) and space complixity O(1)
