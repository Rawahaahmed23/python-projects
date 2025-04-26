def linear_search(list, target):
    for i in range(0, len(list)):
        if list[i]== target:
            return i
    return None 


def verify(index):
    if index is not None:
        print('target font at index: "',index)
    else:
        print('target not fonund')

numbers= [1,2,3,4,5,6,7,8,]
reasult = linear_search(numbers,5)
verify(reasult)

