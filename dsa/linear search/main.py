def linearSearch(number:list[int], target):
     for i in range(len(number)):
          if[i]==target:
            return i
       
     return None
    


def verify(index):
     if index is not None:
         print("value found in list")
     else:
         print('value not found ')


number=  [1,2,3,4,5,6,7,8]
target= 1

verify(linearSearch(number,target))
