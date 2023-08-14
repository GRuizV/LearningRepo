
class MaxHeap:

    def __init__(self):

        self.heap = []


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
        
        heap = self.heap
        if not heap:
            return

        def get_level(index):
            return (index.bit_length() - 1) if index > 0 else 0

        def get_children_indices(parent_index):
            left_child_index = 2 * parent_index + 1
            right_child_index = 2 * parent_index + 2
            return left_child_index, right_child_index

        def print_spaces(count):
            print(" " * count, end="")

        height = get_level(len(heap) - 1) + 1
        max_width = 2 ** height - 1

        # Initialize queue with the root node
        queue = [(0, 0)]  # (index, level)

        current_level = 0
        current_line_index = 0

        while queue:
            index, level = queue.pop(0)

            if level > current_level:
                # Move to the next line
                print()
                current_line_index = 0
                current_level = level

            if index < len(heap):
                # Print the value
                print_spaces(max_width // (2 ** (level + 1)))
                print(f"{heap[index]:>4}", end="")
            else:
                # Print spaces for missing elements
                print_spaces(max_width // (2 ** (level + 1) + 1))

            current_line_index += 1

            # Add children to the queue
            left_child_index, right_child_index = get_children_indices(index)
            if left_child_index < len(heap):
                queue.append((left_child_index, level + 1))
            if right_child_index < len(heap):
                queue.append((right_child_index, level + 1))

        print()  # Print a newline at the end



class MinHeap: 

    def __init__(self):

        self.heap = []


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
        
        heap = self.heap
        if not heap:
            return

        def get_level(index):
            return (index.bit_length() - 1) if index > 0 else 0

        def get_children_indices(parent_index):
            left_child_index = 2 * parent_index + 1
            right_child_index = 2 * parent_index + 2
            return left_child_index, right_child_index

        def print_spaces(count):
            print(" " * count, end="")

        height = get_level(len(heap) - 1) + 1
        max_width = 2 ** height - 1

        # Initialize queue with the root node
        queue = [(0, 0)]  # (index, level)

        current_level = 0
        current_line_index = 0

        while queue:
            index, level = queue.pop(0)

            if level > current_level:
                # Move to the next line
                print()
                current_line_index = 0
                current_level = level

            if index < len(heap):
                # Print the value
                print_spaces(max_width // (2 ** (level + 1)))
                print(f"{heap[index]:>4}", end="")
            else:
                # Print spaces for missing elements
                print_spaces(max_width // (2 ** (level + 1) + 1))

            current_line_index += 1

            # Add children to the queue
            left_child_index, right_child_index = get_children_indices(index)
            if left_child_index < len(heap):
                queue.append((left_child_index, level + 1))
            if right_child_index < len(heap):
                queue.append((right_child_index, level + 1))

        print()  # Print a newline at the end






