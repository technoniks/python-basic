
class TreeNode:
  def __init__(self, data):
    self.data = data
    self.children = []
    self.parent = None
  
  def add_child(self, child):
    child.parent = self
    self.children.append(child)

  def print_tree(self):
    spaces = " " * self.get_level()
    prefix = spaces + "|=->" if self.parent else ""
    print(prefix, self.data)
    if self.children:
      for child in self.children:
        child.print_tree()

  def get_level(self):
    level = 0
    p = self.parent
    while p:
      level += 1
      p = p.parent
    return level

class BinarySearchTree:
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None

  def add_child(self, data):
    if data == self.data:
      return
    
    if data < self.data:
      if self.left:
        self.left.add_child(data)
      else:
        self.left = BinarySearchTree(data)
    else:
      if self.right:
        self.right.add_child(data)
      else:
        self.right = BinarySearchTree(data)

  def in_order_traversal(self):
    elements = []
    # visit left tree
    if self.left:
      elements += self.left.in_order_traversal()
    # visit base node
    elements.append(self.data)
    # visit right tree
    if self.right:
      elements += self.right.in_order_traversal()

    return elements
  
  def search(self, val):
    if self.data == val:
      return True
    
    if val < self.data:
      if self.left:
        return self.left.search(val)
      else:
        return False
    if val > self.data:
      if self.right:
        return self.right.search(val)
      else:
        return False
      
  def min_value(self):
    if self.left is None:
      return self.data
    return self.left.min_value()
  
  def max_value(self):
    if self.right is None:
      return self.data
    return self.right.max_value()

  def delete(self, val):
    if val < self.data:
      if self.left:
        self.left.delete(val)
    elif val > self.data:
      if self.right:
        self.right.delete(val)
    else:
      if self.left is None and self.right is None:
        return None
      if self.left is None:
        return self.right
      if self.right is None:
        return self.left

def build_product_tree():
  root = TreeNode("Electonics")

  laptop = TreeNode("Laptop")
  laptop.add_child(TreeNode("Mac"))
  laptop.add_child(TreeNode("ThinkPad"))
  laptop.add_child(TreeNode("Surface"))
  root.add_child(laptop)

  cellphone = TreeNode("Cellphono")
  cellphone.add_child(TreeNode("iPhone"))
  cellphone.add_child(TreeNode("Google Pixel"))
  cellphone.add_child(TreeNode("Vivo"))
  root.add_child(cellphone)

  tv = TreeNode("TV")
  tv.add_child(TreeNode("Samsung"))
  tv.add_child(TreeNode("LG"))
  tv.add_child(TreeNode("iPlus+"))
  root.add_child(tv)

  return root

def build_binary_tree(elements):
  root = BinarySearchTree(elements[0])
  for i in range(1, len(elements)):
    root.add_child(elements[i])
  
  return root

if __name__ == '__main__':
  # root = build_product_tree()
  # root.print_tree()

  numbers = [17, 4, 1, 20, 9, 23, 18, 34]
  countries = ["India", "China", "Pakistan", "UK", "USA"]
  numbers_tree = build_binary_tree(numbers)
  countries_tree = build_binary_tree(countries)
  print(numbers_tree.in_order_traversal())
  numbers_tree.delete(20)
  print(numbers_tree.in_order_traversal())
  print(numbers_tree.search(20))
  print(numbers_tree.search(99))

  print(countries_tree.in_order_traversal())
  print(countries_tree.search("UK"))
  print(countries_tree.search("NEPAL"))