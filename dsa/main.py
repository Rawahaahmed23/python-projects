def arr(num:list[int],target:int):
  i = 0
  while i < len(num):
     j = i + 1
     while j < len(num):
      if num[i] + num[j] == target:
        
        print(i,j)
        
        print(i)
        
        break
      return
     j+= 1
    
     i+=1
    
      
     
   
num = [1,2,3,4,5,5,5,6]
target = 2

arr(num ,target)




        



# num = [1,3,4,5,5,6,6,7]
# target = 5


# num3 = num[1] + num[4]