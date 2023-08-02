
class Node:

    def __init__(self, data=None):

        self.data = data
        self.next = None
        self.prev = None



class DoublyCircularLinkedList:


    def __init__(self):

        self.head = None

    
    def is_empty(self):
        
        return self.head is None


    def _list_items(self):

        if self.is_empty():
            return
        
        items_list = list()

        current = self.head

        items_list.append(current)

        while current.next is not self.head:

            current = current.next
            items_list.append(current)
            

        return items_list


    def print_list(self):

        if self.is_empty():
            return print('Empty list')

        items_list = [x.data for x in self._list_items()]
        print(', '.join(items_list))


    def print_nodes(self):

        if self.is_empty():
            return
    
        items_list = self._list_items()

        for i in items_list:

            if i is self.head:

                print(f'Head: {i.data}\nNext: {i.next.data}\nPrev: {i.prev.data}\n')
            
            else:
                print(f'Node: {i.data}\nNext: {i.next.data}\nPrev: {i.prev.data}\n')


    def _get_nodes(self, data):

        occurrences = list()
        _get_position = 0
    

        current = self.head

        if current.data == data:
            occurrences.append(_get_position)

        current = current.next
        _get_position += 1        

        # Traverse all the list collection occurrences of the data searched
        while current is not self.head:                       

            if current.data == data:
                occurrences.append(_get_position)

            current = current.next
            _get_position += 1


        # Handling multiple scenarios
        # if not found
        if len(occurrences) == 0:
            return print(f"'{data}' was not found in the list")
        
        # if just appears once
        elif len(occurrences) == 1:
            new_node_position = occurrences[0]

        # Multiple occurrences
        else:                    
            occurrences_positions = [str(x) for x in occurrences]

            print(f"'{data}' appears in positions: {', '.join(occurrences_positions)} ")

            new_node_position = int(input('Which of these are the Node of interest: '))

            while new_node_position not in [int(x) for x in occurrences_positions]:

                print(f'\n{new_node_position} is an invalid position\nPlease select a valid position')

                print(f"'{data}' appears in positions: {', '.join(occurrences_positions)}\n ")

                new_node_position = int(input('Which of these are the Node of interest: '))

        return new_node_position


    def len(self):
        
        if self.is_empty():
            return 0
        
        return len(self._list_items())


    def _index_handler(self, index):

            if self.is_empty():
                return

            if index > (self.len()-1) or index < -self.len():
                raise IndexError('Index out of range')
            

            # converting the index into a positive index
            if index < 0: 

                norm_index = range(self.len())
                inv_index = range(-len(norm_index),0)
                dict_index = {k:v for k,v in zip(inv_index, norm_index)}

                return dict_index[index]

            else:

                return index   


    def append(self, data):

        new_node = Node(data)

        if self.is_empty():

            self.head = new_node
            self.head.next = self.head
            self.head.prev = self.head
            return
        
        current = self.head

        while current.next is not self.head:
            current = current.next

        current.next = new_node

        new_node.prev = current
        new_node.next = self.head
        self.head.prev = new_node


    def prepend(self, data): 

        new_node = Node(data)   

        if self.is_empty():

            self.head = new_node
            self.head.next = self.head
            self.head.prev = self.head
            return

        current = self.head         

        while current.next is not self.head:
            current = current.next

        new_node.next, self.head.prev = self.head, new_node
        current.next, new_node.prev = new_node, current
        self.head = new_node
     

    def return_node(self, index):
        
        if self.is_empty():
            return

        ind = self._index_handler(index)

        current = self.head

        for i in range(ind):
            current = current.next
        
        return current


    def insert_after(self, data, prev_node): 
        
        if self.is_empty():
            return

        new_node = Node(data)

        current = self.return_node(self._get_nodes(prev_node))

        new_node.next, new_node.prev = current.next, current
        current.next.prev, current.next = new_node, new_node


    def search(self, data):

        if self.is_empty():
            return

        elems = self._list_items()

        occurrences = [str(x) for x in range(len(elems)) if elems[x].data == data] 

        if len(occurrences) != 0:

            return print(f"'{data}' appears in position(s): {', '.join(occurrences)}")
        
        else:

            return print(f"'{data}' was not found")
    

    def clear_list(self): 
        
        if self.is_empty():
            return
        
        else:            
            self.head = None


    def delete(self, data): 
        
        if self.is_empty():
            return
        
        if len(self._list_items()) == 1:
            self.clear_list()

        current = self.head
        node_position = self._get_nodes(data)

        for i in range(node_position):
            current = current.next

        current.next.prev, current.prev.next = current.prev, current.next

        if current is self.head:
            self.head = current.next

        current = None
     

    def reverse(self): 
        
        if self.is_empty():
            return
        
        first_head = self.head
        new_head = self.head.next

        current = self.head

        tail = self.head.prev
        
        while first_head.next is not tail:

            tail.next = new_head
            first_head.next, current.prev = new_head.next, new_head
            new_head.next, new_head.prev = current, tail

            current = new_head
            new_head = first_head.next


        self.head = tail
        self.head.prev = first_head                                                            


    def extend(self, linked_list): 
        
        if self.is_empty():

            if linked_list.is_empty():
                return

            self.head = linked_list.head
            return
        
        if linked_list.is_empty():
            return
        
        current = self.head
        tail = current.prev
        other_head = linked_list.head
        other_tail = other_head.prev

        current.prev, other_tail.next = other_tail, current
        tail.next, other_head.prev = other_head, tail
    

    def pop(self, index = -1): 
        
        if self.is_empty():
            return

        ind = self._index_handler(index)
        node = self.return_node(ind)

        if self.len() == 1:
            self.head = None
            return node
        
        node.prev.next, node.next.prev = node.next, node.prev

        if node is self.head:
            self.head = node.next

        return node
      

    def bubble_sort(self): 
        
        if self.is_empty():
            return
                
        swapped = True

        while swapped is not False:

            swapped = False
            current = self.head
            prev_node = current.prev

            while True:

                next_node = current.next

                if current.next == self.head:
                    break

                if current.data > current.next.data:

                    swapped = True
                    
                    if current is self.head:
                        self.head = next_node

                    prev_node.next = next_node  
                    next_node.prev = current.prev
                    current.next = next_node.next
                    current.prev = next_node
                    next_node.next.prev = current
                    next_node.next = current                    

                    current, next_node = next_node, current
                
                prev_node = current
                current = current.next

                


                    


    
















































