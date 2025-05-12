def recursive_binary(number:list,target:int):
    if len(number) ==0:
        return False
    else:
     midpoint = len(number)//2 
     if number[midpoint] == target:
        return True
     elif number[midpoint] < target:
        return recursive_binary(number[midpoint +1:],target)
     else:
        return recursive_binary(number[:midpoint],target)
      
        

def verify(reasult):
   print("Target found",reasult)


number= [1,2,3,4,5,6,7,8,9]
target  = 5

verify(recursive_binary(number,target))
    


number= [1,2,3,4,5,6,7,8,9]
target  = 12

verify(recursive_binary(number,target))