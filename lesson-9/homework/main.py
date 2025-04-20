
# 1. Circle Class

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

    def perimeter(self):
        return 2 * 3.14 * self.radius


# 2. Person Class

from datetime import datetime

class Person:
    def __init__(self, name, country, dob):  # dob = "YYYY-MM-DD"
        self.name = name
        self.country = country
        self.dob = datetime.strptime(dob, "%Y-%m-%d")

    def age(self):
        today = datetime.today()
        return today.year - self.dob.year - ((today.month, today.day) < (self.dob.month, self.dob.day))


# 3. Calculator Class

class Calculator:
    def add(self, x, y): return x + y
    def subtract(self, x, y): return x - y
    def multiply(self, x, y): return x * y
    def divide(self, x, y): return x / y if y != 0 else "Error: divide by zero"


# 4. Shape and Subclasses


import math

class Shape:
    def area(self): pass
    def perimeter(self): pass

class Circle(Shape):
    def __init__(self, r): self.r = r
    def area(self): return math.pi * self.r ** 2
    def perimeter(self): return 2 * math.pi * self.r

class Square(Shape):
    def __init__(self, s): self.s = s
    def area(self): return self.s ** 2
    def perimeter(self): return 4 * self.s

class Triangle(Shape):
    def __init__(self, a, b, c): self.a, self.b, self.c = a, b, c
    def perimeter(self): return self.a + self.b + self.c
    def area(self):  # Heron's formula
        s = self.perimeter() / 2
        return (s*(s-self.a)*(s-self.b)*(s-self.c)) ** 0.5


# 5. Binary Search Tree Class


class Node:
    def __init__(self, val): self.val = val; self.left = None; self.right = None

class BST:
    def __init__(self): self.root = None

    def insert(self, val):
        def _insert(node, val):
            if not node: return Node(val)
            if val < node.val: node.left = _insert(node.left, val)
            else: node.right = _insert(node.right, val)
            return node
        self.root = _insert(self.root, val)

    def search(self, val):
        def _search(node):
            if not node: return False
            if val == node.val: return True
            return _search(node.left) if val < node.val else _search(node.right)
        return _search(self.root)


# 6. Stack

class Stack:
    def __init__(self): self.items = []
    def push(self, item): self.items.append(item)
    def pop(self): return self.items.pop() if self.items else None


# 7. Linked List

class Node:
    def __init__(self, data): self.data = data; self.next = None

class LinkedList:
    def __init__(self): self.head = None

    def insert(self, data):
        new = Node(data)
        if not self.head: self.head = new
        else:
            temp = self.head
            while temp.next: temp = temp.next
            temp.next = new

    def delete(self, key):
        temp = self.head
        if temp and temp.data == key: self.head = temp.next; return
        while temp and temp.next and temp.next.data != key: temp = temp.next
        if temp.next: temp.next = temp.next.next

    def display(self):
        temp = self.head
        while temp: print(temp.data, end=" -> "); temp = temp.next
        print("None")

# 8. Shopping Cart

class ShoppingCart:
    def __init__(self): self.items = {}

    def add_item(self, item, price): self.items[item] = price
    def remove_item(self, item): self.items.pop(item, None)
    def total(self): return sum(self.items.values())


# 10. Queue

class Queue:
    def __init__(self): self.queue = []
    def enqueue(self, val): self.queue.append(val)
    def dequeue(self): return self.queue.pop(0) if self.queue else None


