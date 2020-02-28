class Node:
  def __init__(self, value=None, next_node=None):
    # the value at this linked list node
    self.value = value
    # reference to the next node in the list
    self.next_node = next_node

  def get_value(self):
    return self.value

  def get_next(self):
    return self.next_node

  def set_next(self, new_next):
    # set this node's next_node reference to the passed in node
    self.next_node = new_next

class LinkedList:
  def __init__(self):
    # reference to the head of the list
    self.head = None

  def add_to_head(self, value):
    node = Node(value)
    if self.head is not None:
      node.set_next(self.head)
    
    self.head = node

  def contains(self, value):
    if not self.head:
      return False
    # get a reference to the node we're currently at; update this as we traverse the list
    current = self.head
    # check to see if we're at a valid node 
    while current:
      # return True if the current value we're looking at matches our target value
      if current.get_value() == value:
        return True
      # update our current node to the current node's next node
      current = current.get_next()
    # if we've gotten here, then the target node isn't in our list
    return False

  def reverse_list(self):
    # TO BE COMPLETED
   # Check if head or there is a next for the head to prevent entering the Loop
        # return the initial head
    previous_node = None
    current_node = self.head #define variable to hold the node on the initial head

    while current_node is not None:

      next_node = current_node.next_node #create a var to hold the next node of the current_node  

      current_node.next_node = previous_node #set the current_node next_node to the previous_node

      previous_node = current_node #update the previous_node to the current_node

      current_node = next_node #update the current_node to the next_node

      self.head = previous_node #set the head to the current previous_node which would be the last node in the initial list
    
    