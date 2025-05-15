class Node: 
    """An object  for sorting  a single node of a linked  list
    Model two  attributes  data and the link to  the next node in the list """


    data= None
    next_node = None

    def __init__(self,data):
        self.data= data 

    def __repr__(self):
        return "<Node data: %s" % self.data



class LinkedList:
    """singly linked list"""
    def __init__(self):
        self.head =None
    
    def is_empty(self):
        return self.head == None
    
    def size(self):
        current = self.head 
        count = 0
        while current: 
            count +=1
            current =  current.next_node
        return count

    def add(self,data):
         new_node = Node(data)
         new_node.next_node= self.head
         self.head =new_node
    
    def __repr__(self):
        nodes = []

        current = self.head
        while current :
            if current is self.head:
                nodes.append("[Head %s]"% current.data)
            elif current.next_node is None:
                nodes.append("[Tail: %s]"% current.data)
            else:
                nodes.append("[%s]"% current.data)
         
            current = current.next_node
        return"->".join(nodes)
        

# N1 = Node(10)
# N2 =Node(20)
# N1.next_node =N2
# print(N1.next_node)