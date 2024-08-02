
# The first thing is to create the Node Class
class Node:

    def __init__(self, data=None):

        self.data = data
        self.next = None




# Second the actual linked list is created, with its attributes
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


    def _list_items(self):

        if self.head is not None:       

            current = self.head

            ret_list = list()


            while current is not None:

                    ret_list.append(current.data)

                    current = current.next

            return ret_list


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




