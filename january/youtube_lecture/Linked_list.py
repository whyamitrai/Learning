class Node:
    def __init__(self, item=None, next=None):
        self.item = item
        self.next = next
        
class SLL:
    def __init__(self, start=None):
        self.start = start
         
    def is_empty(self):
        return self.start == None
    
    def insert_at_start(self, data=None):
        n = Node(data, self.start)
        self.start = n
        
    def insert_at_last(self, data):
        n = Node(data)
        if self.is_empty():
            self.start = n
        else:
            temp = self.start
            while temp.next is not None:
                temp = temp.next
            temp.next = n
        
    def search(self, data):
        temp = self.start
        while temp is not None:
            if temp.item == data:
                return temp 
            temp = temp.next
        return None
    
    def insert_after(self, temp, data):
        if temp is not None:
            n = Node(data, temp.next)
            temp.next = n
            
    def display(self):
        temp = self.start
        while temp is not None:
            print(temp.item, end = "\n")
            temp = temp.next
            
    def delete_first(self):
        if self.start is not None:
            self.start = self.start.next
            
    def delete_last(self):
        if self.start is not None:
            if self.start.next is None:
                self.start = None
            else:
                temp = self.start 
                while temp.next.next is not None:
                    temp = temp.next 
                temp.next = None
        
    def delete_item(self, data):
        if self.start is None:
            return 
        elif self.start.next is None:
            if data == self.start.item:
                self.start = None
            else:
                print("Invalid value provided")
        else:
            temp = self.start 
            if temp.item == data:
                self.start = temp.next
            else:
                while temp.next is not None:
                    if temp.next.item == data:
                        temp.next = temp.next.next
                        return
                    temp = temp.next
        
        
        
            
myList = SLL()
myList.insert_at_start(10)
myList.insert_at_start(20)
myList.insert_at_last(30)
myList.insert_after(myList.search(20), 50)
myList.display()
myList.delete_first()
print("After deleting first element:")
myList.display()
myList.delete_last()
print("After deleting last element:")
myList.display()
print("delete specific item")
myList.delete_item(50)
print("-------------")
myList.display()