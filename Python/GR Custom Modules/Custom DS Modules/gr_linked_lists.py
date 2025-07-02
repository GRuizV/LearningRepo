
class Node:

    def __init__(self, data=None):

        self.data = data
        self.next = None
        self.prev = None




class SinglyLinkedList:


    def __init__(self):

        self.head = None




    def is_empty(self):
        return self.head is None

    def append(self, data):

        new_node = Node(data)

        if self.head == None: 

            self.head = new_node
        
        else:

            current = self.head

            while current.next is not None:

                current = current.next

            current.next = new_node

    def prepend(self, data):

        new_node = Node(data)

        current = self.head

        self.head = new_node

        self.head.next = current

        del current     # This is made to not leave memory used on a buffer node.
 
    def insert_after(self, data, prev_node): 
        
        new_node = Node(data)

        prev_node_positions = self._get_nodes(prev_node)

        new_node_position = int()


        if len(prev_node_positions) == 0:

            return print(f"'{prev_node}' was not found in the list")
        

        elif len(prev_node_positions) == 1:

            new_node_position = prev_node_positions[0]

        else:
                    
            occurrences_positions = [str(x) for x in prev_node_positions]

            print(f"'{prev_node}' appears in positions: {', '.join(occurrences_positions)} ")

            new_node_position = int(input('After which position would you like to insert the new node: '))

            while new_node_position not in [int(x) for x in occurrences_positions]:

                print(f'\n{new_node_position} is an invalid position\nPlease select a valid position')

                print(f"'{prev_node}' appears in positions: {', '.join(occurrences_positions)}\n ")

                new_node_position = int(input('After which position would you like to insert the new node: '))

       

        current = self.head

        for i in range(new_node_position):      # Traversing until the disered position

            current = current.next

            
        succeeding_node = current.next

        current.next = new_node

        new_node.next = succeeding_node

    def search(self, data):
        
        finding = self._get_nodes(data)


        if len(finding) == 0:

            return print(f"'{data}' was not found")

        else:

            occurrences_positions = [str(x) for x in finding]

            return print(f"'{data}' appears in position(s): {', '.join(occurrences_positions)}")

    def len(self):

        if self.is_empty():
            return
        
        return len(self._list_items())

    def print_list(self):

        return print(self._list_items())
    
    def delete(self, data):

        if data not in self._list_items():
            return print(f"'{data}' is not in the list")
        
        
        delete_positions = self._get_nodes(data)

        if len(delete_positions) > 1:

            delete_positions = [str(x) for x in delete_positions]

            print(f"'{data}' appears in positions: {', '.join(delete_positions)} ")

            deleted_node_position = int(input('Which position would you like to delete: '))

            while deleted_node_position not in [int(x) for x in delete_positions]:

                print(f'\n{deleted_node_position} is an invalid position\nPlease select a valid position')

                print(f"'{data}' appears in positions: {', '.join(delete_positions)} ")

                deleted_node_position = int(input('After which position would you like to insert the new node: '))          

        else: 

            deleted_node_position = delete_positions[0]


        current = self.head


        if deleted_node_position == 0:

            self.head = current.next
            return
        
        else:       

            for i in range(deleted_node_position-1):

                current = current.next

            current.next = current.next.next

            return
    
    def bubble_sort(self):

        if self.is_empty():
            return
           
        swapped = True

        while swapped is not False:

            swapped = False
            current = self.head

            while True:

                if current.next == None:
                    break

                if current.data > current.next.data:
                    
                    current.data, current.next.data = current.next.data, current.data
                    swapped = True

                current = current.next

    def reverse_list(self):

        if self.is_empty():
            return
            
        current = self.head
        prev = None

        while current is not None:

            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        
        self.head = prev
  
    def extend_list(self, new_list):

        if self.is_empty():
            return
        
        current = self.head

        while current.next is not None:
            current = current.next

        current.next = new_list.head

    def pop_node(self, index = -1):

        if self.is_empty():
            return
        

        ind = self._access_index(index)
        
        current = self.head

        # if is the head of the list
        if ind == 0:

            self.head = self.head.next
            current.next = None
            
            return current

        # Any other case
        else: 
            
            for i in range(ind-1):
                current = current.next
        
            prev = current
            current = current.next

            if current is None:
                prev.next = None
            
            else:
                prev.next = current.next

            current.next = None

            return current

    def data_in_index(self, index):

        if self.is_empty():
            return
        
        ind = self._access_index(index)

        current = self.head

        for i in range(ind):

            current = current.next

        return current.data





    def _get_nodes(self, data):

        current = self.head

        occurrences = list()

        _get_position = 0


        while current is not None:

            if current.data == data:
                    
                occurrences.append(_get_position)
                
            current = current.next

            _get_position += 1


        return occurrences

    def _access_index(self, index):

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

        if self.head is not None:       

            current = self.head

            ret_list = list()


            while current is not None:

                    ret_list.append(current.data)

                    current = current.next

            return ret_list




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

    def len(self):
        return len(self._list_items())

    def print_list(self):

        if self.is_empty():
            print('Empty list')
        
        return print(self._list_items())

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




class CircularSinglyLinkedList:

    def __init__(self):

        self.head = None




    def is_empty(self):

        return self.head is None

    def append(self, data):
      
        new_node = Node(data)
        

        if self.is_empty():

            self.head = new_node
            self.head.next = self.head
               
        else:

            current = self.head

            while current.next is not self.head:

                current = current.next
                     

            current.next = new_node
            new_node.next = self.head

    def prepend(self, data): 

        new_node = Node(data)

        if self.is_empty():
            self.head = new_node
            self.head.next = self.head
            return


        current = self.head
        
        while current.next is not self.head:
            current = current.next
        
        new_node.next = self.head
        current.next = new_node
        self.head = new_node

    def print_list(self):
        
        if self.is_empty():
            return print('Empty List')

        print([x.data for x in self._list_items()])

    def print_nodes(self):

        if self.is_empty():
            return print('Empty List')

        nodes_list = self._list_items()

        for node in nodes_list:

            if node is self.head:
                print(f"Head: '{node.data}'\nNext: '{node.next.data}'", end='\n')
                print()
                continue

            print(f"Node: '{node.data}'\nNext: '{node.next.data}'", end='\n')
            print()

    def len(self):
        
        return len(self._list_items())

    def insert_after(self, data, prev_node):

        if self.is_empty():
            return

        current = self.head
        new_node = Node(data)
         
        new_node_position = self._get_nodes(prev_node)        

        if new_node_position is None:
            return

        for i in range(new_node_position):
            
            current = current.next

        new_node.next = current.next
        current.next = new_node
  
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

        occurrences = [str(x) for x in range(len(items_list)) if items_list[x].data == data]

        if len(occurrences) != 0:
            return print(f"'{data}' appears in position(s): {', '.join(occurrences)}")
        
        else:
            return print(f"'{data}' was not found")

    def delete(self, data):

        if self.is_empty():
            return
        

        if len(self._list_items()) == 1:
            self.clear()
            return

        delete_position = self._get_nodes(data)

        current = self.head


        if delete_position is None:
            return        


        # If the deleted node is the head
        if delete_position == 0:

            while current.next is not self.head:
                current = current.next
            
            current.next = self.head.next
            self.head = self.head.next
            
            return
        


        # Otherwise
        for i in range(delete_position-1):

            current = current.next


        if current.next.next is self.head:

            current.next = self.head
        
        else:
            
            current.next = current.next.next

    def reverse(self):

        if self.is_empty():
            return
    
        first_head = self.head
        current = self.head
        tail = self.return_node(-1)
        new_head = self.head.next

        while first_head.next is not tail:

            tail.next = new_head
            first_head.next = new_head.next
            new_head.next = current

            current = new_head
            new_head = first_head.next

        self.head = tail

    def extend(self, ext_list):
        
        if self.is_empty() and ext_list.is_empty():
            return 

        if not self.is_empty() and ext_list.is_empty():
            return 

        if self.is_empty() and not ext_list.is_empty():
            self.head = ext_list.head
            return
        

        tail = self.return_node(-1)
        new_list_tail = ext_list.return_node(-1)

        tail.next = ext_list.head
        new_list_tail.next = self.head

    def copy_list(self, list):

        self.head = list.head

    def pop(self, index = -1):

        if self.is_empty():
            return
        

        ind = self._index_handler(index)

        popped_node = self.return_node(ind)

        current = self.head

        # if is the head
        if popped_node is self.head:

            tail = self.return_node(-1)
            tail.next = self.head.next
            self.head = self.head.next

            return popped_node


        # Otherwise
        for i in range(ind-1):
            current = current.next

        current.next = current.next.next

        return popped_node

    def clear(self):

        if self.is_empty():
            return
        
        self.head = None

    def bubble_sort(self):

        if self.is_empty():
            return
           
        swapped = True

        while swapped is not False:

            swapped = False
            current = self.head

            while True:

                if current.next == self.head:
                    break

                if current.data > current.next.data:
                    
                    current.data, current.next.data = current.next.data, current.data
                    swapped = True

                current = current.next




    def _list_items(self):

        if self.is_empty():
            return
        
        current = self.head
        _list = list()
        _list.append(current)

        while current.next is not self.head:
                        
            current = current.next
            _list.append(current)
        
        return _list

    def _get_nodes(self, data):
        
        if self.is_empty():
            return
        
        occurrences = list()
        _get_position = 0
    

        current = self.head

        # Checking the head of the list

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





class DoublyCircularLinkedList:

    def __init__(self):

        self.head = None



    
    def is_empty(self):
        
        return self.head is None

    def print_list(self):

        if self.is_empty():
            return print('Empty list')

        print([x.data for x in self._list_items()])

    def print_nodes(self):

        if self.is_empty():
            return
    
        items_list = self._list_items()

        for i in items_list:

            if i is self.head:

                print(f'Head: {i.data}\nNext: {i.next.data}\nPrev: {i.prev.data}\n')
            
            else:
                print(f'Node: {i.data}\nNext: {i.next.data}\nPrev: {i.prev.data}\n')

    def len(self):
        
        if self.is_empty():
            return 0
        
        return len(self._list_items())

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































































