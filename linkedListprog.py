class Node:
    def __init__(self,value):
        self.data=value
        self.next=None

class SLL:
    def __init__(self):
        self.head=None


    def append(self,new_node):
        if(self.head==None):
            self.head=new_node
        

        else:
            temp=self.head
            while temp.next:
                temp=temp.next
            temp.next=new_node

    def print(self):
        temp=self.head
        while temp:
            print(temp.data)
            temp=temp.next

    def insert(self,new_node,pos):
        if(pos==1):
            new_node.next=self.head
            self.head=new_node

        else:
            p=1
            temp=self.head
            while(p!=pos-1):
                temp=temp.next
                p+=1
            new_node.next=temp.next
            temp.next=new_node

    def delete(self,value):
        temp=self.head
        if(temp.data==value):
                self.head=self.head.next
        else:
            while(temp.data!=value):
                prev=temp
                temp=temp.next
                if temp==None:
                    print("value not present in the list")
                    return

            prev.next=temp.next
            temp=None



    def middleno(self):
        temp1=self.head
        temp2=self.head

        while(temp2 and temp2.next):
            temp1=temp1.next
            temp2=temp2.next.next

        if(temp1):
            print(temp1.data)
        else:
            print("list is empty")

    def reverse(self):
        prev=None
        temp=self.head

        while temp:
            next_node=temp.next
            temp.next=prev
            prev=temp
            temp=next_node

        self.head=prev

    def sumofcons(self):
        temp=self.head
        while temp and temp.next:
            total=temp.data+temp.next.data
            print(total)
            temp=temp.next
            



list1=SLL()
n1=Node(10)
n2=Node(20)
print("appended the node")
list1.append(n1)
list1.append(n2)
list1.print()
print()

print("node inserted at given position")
list1.insert(Node(30),2)
list1.print()
print()

print("list after node deletion")
list1.delete(20)
list1.print()
print()

print("the middle no in list is")
list1.middleno()
print()

print("reverse list is")
list1.reverse()
list1.print()
print()

print("sum of consecutive node value")
list1.sumofcons()


