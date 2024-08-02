
class Node:

    def __init__(self, data = None):

        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:

    def __init__(self):

        self.head = None

    
    def is_empty(self):
        return self.head is None
    

    def append(self, data):

        node_to_add = Node(data)

        if self.is_empty():
            
            self.head = node_to_add
            return

        
        current = self.head
        
        while current.next is not None:

            current = current.next

        node_to_add.next = None
        node_to_add.prev = current
        current.next = node_to_add
    

    def prepend(self, data):

        node_to_add = Node(data)

        current = self.head

        node_to_add.prev = None
        node_to_add.next = current
        self.head = node_to_add

        if current is None:
            return
        
        current.prev = node_to_add


    def _get_nodes(self, data):

        occurrences = list()
        _get_position = 0
    

        current = self.head

        # Traverse all the list collection occurrences of the data searched
        while current is not None:

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


    def _list_items(self):

        if self.is_empty():
            return
        
        current = self.head
        _items = list()

        while current is not None:

            _items.append(current.data)
            current = current.next          
       
        return _items


    def len(self):
        return len(self._list_items())


    def print_list(self):

        if self.is_empty():
            print('Empty list')

        items_data = self._list_items()
        
        return print(', '.join(items_data))


    def insert_after(self, data, prev_node):

        if self.is_empty():
            return

        current = self.head
        new_node = Node(data)
         
        new_node_position = self._get_nodes(prev_node)        

        if new_node_position == None:
            return

        for i in range(new_node_position):
            
            current = current.next

        new_node.next = current.next
        
        if current.next is not None:
            current.next.prev = new_node

        current.next = new_node
        new_node.prev = current


    def return_node(self, index):

        if self.is_empty():
            return

        current = self.head

        ind = self._index_handler(index)

        for i in range(ind):

            current = current.next
        
        return current


    def search(self, data):

        if self.is_empty():
            return
        
        items_list = self._list_items()

        occurrences = [str(x) for x in range(len(items_list)) if items_list[x] == data]

        if len(occurrences) != 0:
            return print(f"'{data}' appears in position(s): {', '.join(occurrences)}")
        
        else:
            return print(f"'{data}' was not found")


    def delete(self, data):

        if self.is_empty():
            return
        
        delete_position = self._get_nodes(data)

        current = self.return_node(delete_position)

        # If the deleted node is the head
        if current is self.head:

            current.next.prev = None
            self.head = current.next
            return
        
        # If the deleted node is the tail
        if current.next == None:

            current.prev.next = None
            return

        # Otherwise
        current.prev.next = current.next
        current.next.prev = current.prev

        del current


    def reverse(self):
        
        if self.is_empty():
            return
        
        current = self.head
        prev_node = None

        while current is not None:
            
            next_node = current.next

            if current.next is not None:
                next_node.prev = current.next.next

            current.next = prev_node
            current.prev = next_node
           
            prev_node = current
            current = next_node

        self.head = prev_node


    def extend(self, linked_list):
        
        current = self.head

        while current.next is not None:
            current = current.next

        ext_head = linked_list.head

        current.next = ext_head
        ext_head.prev = current


    def pop(self, index = -1): 
        
        if self.is_empty():
            return

        index = self._index_handler(index)

        popped_node = self.return_node(index)

        prev_node = popped_node.prev
        next_node = popped_node.next

        if next_node is not None:
            next_node.prev = prev_node
        
        if prev_node is not None:
            prev_node.next = next_node

        if popped_node is self.head:
            self.head = next_node

        return popped_node

 
    def bubble_sort(self):

        if self.is_empty():
            return
        
        swapped = True

        while swapped is not False:

            swapped = False
            prev_node = None
            current = self.head

            while True:

                next_node = current.next

                if current.next is None:
                    break
                
                if current.data > current.next.data:

                    swapped = True

                    if current is self.head:
                        self.head = next_node
                    
                    else:
                        prev_node.next = next_node

                    next_node.prev = current.prev
                    current.next = next_node.next
                    current.prev = next_node
                    
                    if next_node.next is not None:
                        next_node.next.prev = current

                    next_node.next = current

                    current, next_node = next_node, current                

                prev_node = current
                current = current.next


    def print_nodes(self):

        if self.is_empty():
            return
        
        current = self.head
        _nodes = list()
        
        while current is not None:

            _nodes.append(current)
            current = current.next          
       
       
        for i in _nodes:
            
            if i == self.head and self.head.next is not None:
                print(f"Head: '{i.data}'\nPrev: '{i.prev}'\nNext: '{i.next.data}'")
                print()

            elif i == self.head and self.head.next is None:
                print(f"Head: '{i.data}'\nPrev: '{i.prev}'\nNext: '{i.next}'")

            elif i.next is None:
                print(f"Node: '{i.data}'\nPrev: '{i.prev.data}'\nNext: '{i.next}'")
            
            else:
                print(f"Node: '{i.data}'\nPrev: '{i.prev.data}'\nNext: '{i.next.data}'", end='\n')
                print()


    def clear_list(self):
        
        if self.is_empty():
            return
        
        self.head = None
            













































































































