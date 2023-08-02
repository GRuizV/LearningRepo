class Node:

    def __init__(self, data = None):

        self.data = data
        self.next = None


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


    def print_list(self):
        
        if self.is_empty():
            return print('Empty List')

        print_list = self._list_items()

        for i in range(len(print_list)-1):

            print(print_list[i].data, end=', ')
        
        print(print_list[-1].data)
        

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



        














