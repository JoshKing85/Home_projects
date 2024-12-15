class Node():
    def __init__(self, data= None ):

        self.data = data
        self.next_node = None


class LinkedList():
    
    
    def __init__(self):

        self.head = Node()

    def append(self, data):
        new_node = Node(data)
        cur = self.head
        
        while cur.next_node != None:
            cur = cur.next_node
        
        cur.next_node = new_node
     
    def prepend(self, data):
        new_node = Node(data)
        new_node.next_node = self.head.next_node
        self.head.next_node = new_node

    def length(self):
        cur = self.head
        count = 0

        while cur.next_node is not None:
            cur = cur.next_node
            count += 1

        return count
    
    def display(self):
        elems = []
        
        if self.length() > 1:
            cur = self.head
            while cur.next_node != None:
                cur = cur.next_node
                elems.append(cur.data)
                
            for i in elems:
                print(i, end= ' ')
        
        else:
            print('List is empty other than head node.')
        
        print()

    def delete_node(self, data):
        prev_node = None
        cur = self.head

        while cur.next_node is not None:
            
            if data == cur.data:
                cur = cur.next_node
                break

            else:
                prev_node = cur
                cur = cur.next_node
        
        prev_node.next_node = cur
        cur.next_node = cur.next_node




        




my_linked_list = LinkedList()

my_linked_list.display()

my_linked_list.append('sausages')
my_linked_list.append('bacon')
my_linked_list.append('cheese')
my_linked_list.append('beans')



my_linked_list.display()
my_linked_list.prepend('black pudding')
my_linked_list.display()

my_linked_list.delete_node('cheese')
my_linked_list.display()
            

