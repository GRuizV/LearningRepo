from math import log


class MaxHeap:

    def __init__(self):

        self.heap = []


    

    def insert(self, value):

        self.heap.append(value)
        self._heapify_up(len(self.heap) - 1)

    def extract_max(self):

        if len(self.heap) == 0:
            return None

        max_value = self.heap[0]
        last_value = self.heap.pop()
        
        if len(self.heap) > 0:
            self.heap[0] = last_value
            self._heapify_down(0)
        
        return max_value

    def find_min(self):

        """
        I know is an overkill to look up for minimums like this but is a halfway between actually calling a min() to the list on which the heap is built
        and to iterate over each parent-child groups, just for sake of learning and coding.
        
        everything within a while loop that is going to break when the comparison pass the last leaf node
        1. Make ranges to pull up the first group of childs and find the minium and store it.
        2. Refresh the range for the next level of childs, up to the total amount of childs or the end of the heap.
        """

        if len(self.heap) == 0:
            return None

        if len(self.heap) == 1:
            return self.heap[0]             
       
        childs_range = [1,2]
        min_val = min([self.heap[i] for i in range(childs_range[0], childs_range[1]+1)])
        index = int()

        while index < len(self.heap):

            # Taking all the child nodes from the next level
            childs_range = [childs_range[0]*2+1, childs_range[1]*2+2]   

            # If the new upper bound is greater than the heap, take the last index of the heap instead
            if childs_range[1] > len(self.heap)-1:  
                childs_range[1] = len(self.heap)-1

            childs_min = min([self.heap[i] for i in range(childs_range[0], childs_range[1]+1)])

            if childs_min < min_val:
                min_val = childs_min

            index = childs_range[-1] + 1

        return min_val

    def heap_len(self):
        return len(self.heap)

    def display(self):
        print(self.heap)

    def delete(self, index):

        """
        This method will handle there cases:
        1. if the deletion is in the last leaf
        2. if the deletion is in the root
        3. if the deletion is anywhere else
        """

        ind = self._index_handler(index)

        # Deletion at the last leaf
        if ind == self.heap_len() - 1: 
            self.pop()
            return        

        self.heap[ind] = self.heap[-1]
        self.heap = self.heap[:-1]
        
        # Deletion at the root
        if ind == 0:
            self._heapify_down(0)
            return
        

        # If the deletion is in between, after the replacement the heap need to validate up and down to maintain the MaxHeap
        parent = ( ind - 1) // 2

        if self.heap[ind] > self.heap[parent]:
            self._heapify_up(ind)

        else:
            self._heapify_down(ind)
    
    def pop(self):
        
        if not self.heap:
            return
        
        popped = self.heap[-1]
        self.heap = self.heap[:-1]

        return popped

    def display_heap(self):
        
        #This stands for the index of the first node of each level
        first = lambda h: 2**h - 1      # H stands for level height

        #This stands for the index of the last node of each level
        last = lambda h: first(h + 1)

        level = lambda heap, h: heap[first(h):last(h)]
        prepare = lambda e, field: str(e).center(field)

        width = max(len(str(e)) for e in self.heap)

        height = int(log(len(self.heap), 2)) + 1    
        gap = ' ' * width

        for h in range(height):

            #This below calculation brought me confusion, but my conclusion is that it represents the number of nodes
            #at the end of the heap if the curren level where the lvl 0, i.e. each node in the level act as the root
            #from there, that the in lvl 0: is 8, in lvl 1: is 4, ... lvl 4: is 1
            below = 2 ** (height - h - 1)
            field = (2 * below - 1) * width
            print(gap.join(prepare(e, field) for e in level(self.heap, h)))




    def _index_handler(self, index):

            if index > (self.heap_len()-1) or index < -self.heap_len():
                raise IndexError('Index out of range')
            
            # converting the index into a positive index
            if index < 0: 

                norm_index = range(self.heap_len())
                inv_index = range(-len(norm_index),0)
                dict_index = {k:v for k,v in zip(inv_index, norm_index)}

                return dict_index[index]

            else:

                return index   

    def _heapify_up(self, index):

        parent_index = (index - 1) // 2

        while parent_index >= 0 and self.heap[index] > self.heap[parent_index]:

            self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]

            index = parent_index
            parent_index = (index - 1) // 2

    def _heapify_down(self, index):

        left_child_index = 2 * index + 1
        right_child_index = 2 * index + 2
        largest = index

        if left_child_index < len(self.heap) and self.heap[left_child_index] > self.heap[largest]:
            largest = left_child_index

        if right_child_index < len(self.heap) and self.heap[right_child_index] > self.heap[largest]:
            largest = right_child_index

        if largest != index:
            self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
            self._heapify_down(largest)





class MinHeap: 

    def __init__(self):

        self.heap = []




    def insert(self, value):

        self.heap.append(value)
        self._heapify_up(len(self.heap) - 1)

    def extract_min(self):

        if len(self.heap) == 0:
            return None

        min_value = self.heap[0]
        last_value = self.heap.pop()
        
        if len(self.heap) > 0:
            self.heap[0] = last_value
            self._heapify_down(0)
        
        return min_value

    def find_max(self):

        """
        I know is an overkill to look up for maximums like this but is a halfway between actually calling a max() to the list on which the heap is built
        and to iterate over each parent-child groups, just for sake of learning and coding.
        
        everything within a while loop that is going to break when the comparison pass the last leaf node
        1. Make ranges to pull up the first group of childs and find the minium and store it.
        2. Refresh the range for the next level of childs, up to the total amount of childs or the end of the heap.
        """

        if len(self.heap) == 0:
            return None

        if len(self.heap) == 1:
            return self.heap[0]             
       
        childs_range = [1,2]
        max_val = max([self.heap[i] for i in range(childs_range[0], childs_range[1]+1)])
        index = int()

        while index < len(self.heap):

            # Taking all the child nodes from the next level
            childs_range = [childs_range[0]*2+1, childs_range[1]*2+2]   

            # If the new upper bound is greater than the heap, take the last index of the heap instead
            if childs_range[1] > len(self.heap)-1:  
                childs_range[1] = len(self.heap)-1

            childs_max = max([self.heap[i] for i in range(childs_range[0], childs_range[1]+1)])

            if childs_max > max_val:
                max_val = childs_max

            index = childs_range[-1] + 1

        return max_val

    def heap_len(self):
        return len(self.heap)

    def display(self):
        print(self.heap)

    def delete(self, index):

        """
        This method will handle there cases:
        1. if the deletion is in the last leaf
        2. if the deletion is in the root
        3. if the deletion is anywhere else
        """

        ind = self._index_handler(index)

        # Deletion at the last leaf
        if ind == self.heap_len() - 1: 
            self.pop()
            return        

        self.heap[ind] = self.heap[-1]
        self.heap = self.heap[:-1]
        
        # Deletion at the root
        if ind == 0:
            self._heapify_down(0)
            return
        

        # If the deletion is in between, after the replacement the heap need to validate up and down to maintain the MaxHeap
        parent = ( ind - 1) // 2

        if self.heap[ind] < self.heap[parent]:
            self._heapify_up(ind)

        else:
            self._heapify_down(ind)
    
    def pop(self):
        
        if not self.heap:
            return
        
        popped = self.heap[-1]
        self.heap = self.heap[:-1]

        return popped

    def display_heap(self):
        
        #This stands for the index of the first node of each level
        first = lambda h: 2**h - 1      # H stands for level height

        #This stands for the index of the last node of each level
        last = lambda h: first(h + 1)

        level = lambda heap, h: heap[first(h):last(h)]
        prepare = lambda e, field: str(e).center(field)

        width = max(len(str(e)) for e in self.heap)

        height = int(log(len(self.heap), 2)) + 1    
        gap = ' ' * width

        for h in range(height):

            #This below calculation brought me confusion, byt my conclusion is that it represents the number of nodes
            #at the end of the heap if the curren level where the lvl 0, i.e. each node in the level act as the root
            #from there, that the in lvl 0: is 8, in lvl 1: is 4, ... lvl 4: is 1
            below = 2 ** (height - h - 1)
            field = (2 * below - 1) * width
            print(gap.join(prepare(e, field) for e in level(self.heap, h)))




    def _index_handler(self, index):

        if index > (self.heap_len()-1) or index < -self.heap_len():
            raise IndexError('Index out of range')
        
        # converting the index into a positive index
        if index < 0: 

            norm_index = range(self.heap_len())
            inv_index = range(-len(norm_index),0)
            dict_index = {k:v for k,v in zip(inv_index, norm_index)}

            return dict_index[index]

        else:

            return index   

    def _heapify_up(self, index):

        parent_index = (index - 1) // 2

        while parent_index >= 0 and self.heap[index] < self.heap[parent_index]:

            self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]

            index = parent_index
            parent_index = (index - 1) // 2

    def _heapify_down(self, index):

        left_child_index = 2 * index + 1
        right_child_index = 2 * index + 2
        smallest = index

        if left_child_index < len(self.heap) and self.heap[left_child_index] < self.heap[smallest]:
            smallest = left_child_index

        if right_child_index < len(self.heap) and self.heap[right_child_index] < self.heap[smallest]:
            smallest = right_child_index

        if smallest != index:
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            self._heapify_down(smallest)






