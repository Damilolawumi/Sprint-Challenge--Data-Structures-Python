class BinarySearchTree:
  def __init__(self, value):
      self.value = value
      self.left = None
      self.right = None
  # Insert the given value into the tree
  def insert(self, value):
    #left case  
    if value < self.value:
      if self.left == None:
        self.left = BinarySearchTree(value)
      else:
        return self.left.insert(value)
    #right case
    elif value >= self.value:
      if self.right == None:
        self.right = BinarySearchTree(value)
      else:
        return self.right.insert(value)
    return value
    # Return True if the tree contains the value
    # False if it does not
  def contains(self, target):
    #base case 
    if target == self.value:
      return True
    elif target < self.value:
      if self.left != None:
        return self.left.contains(target)
      else: 
        return False
    elif target >= self.value: 
      if self.right != None:
        return self.right.contains(target)
      else: 
        return False
    else: 
      return False
      