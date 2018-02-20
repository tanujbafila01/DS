
class Node:
    def __init__(self,data=None):
        self.data=data      #data
        self.next=None      #pointer to next data point

class LinkedList:
    def __init__(self):
        self.head = Node()  #first element of list

    def Append(self,data):
        new_node = Node(data)
        cur = self.head
        while cur.next!=None:
            cur = cur.next
        cur.next = new_node

    def Length(self):
        cur = self.head
        total=0
        while cur.next!=None:
            total+=1
            cur=cur.next
        return total

    def Display(self):
        elems=[]
        cur_node=self.head
        while cur_node.next!=None:
            cur_node = cur_node.next
            elems.append(cur_node.data)
        print(elems)

    def Get(self,index):
        if index>=self.Length():
            print("ERROR: 'Get' Index out of Range")
            return None
        cur_idx=0
        cur_node=self.head
        while True:
            cur_node=cur_node.next
            if cur_idx==index:
                return cur_node.data
            else:
                cur_idx+=1

    def Erase(self,index):
        if index>=self.Length():
            print("ERROR: 'Get' Index out of Range")
            return
        cur_idx=0
        cur_node=self.head
        while True:
            last_node = cur_node
            cur_node=cur_node.next
            if cur_idx==index:
                last_node.next = cur_node.next
                return
            cur_idx +=1

my_list = LinkedList()
my_list.Append(1)
my_list.Append(2)
my_list.Append(3)
my_list.Append(4)

my_list.Display()
my_list.Erase(2)
my_list.Display()

