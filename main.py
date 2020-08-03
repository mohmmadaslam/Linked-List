#Create the node class
class Node:
    def __init__(self, data):
        self.item = data   # item is the data value in the linked list
        self.ref = None    # ref is the reference of next linked list in linked list

# Creating the singly linked list class
#This class will contain the methods to insert, remove, traverse and sort the list. Initially, the class will only contain one member start_node that will point to the starting or first node of the list. The value of start_node will be set to null using the constructor since the linked list will be empty at the time of creation.
class LinkedList:
    def __init__(self):
        self.start_node = None

    # Traversing Linked List Items
    def traverse_list(self):
    #it checks whether the linked list is empty or not.
      if self.start_node is None:
        print("List has no element")
        return
    #Otherwise if the list has an item, the following piece of code will execute:
    else:
      n = self.start_node
      while n is not None:
        print(n.item , " ")
        n = n.ref