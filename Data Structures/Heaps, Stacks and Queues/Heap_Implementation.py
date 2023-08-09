
class MaxHeap:

    def __init__(self):
        self.heap = []

    def insert(self, value):
        self.heap.append(value)
        self._heapify_up(len(self.heap) - 1)

    def _heapify_up(self, index):
        parent_index = (index - 1) // 2
        while parent_index >= 0 and self.heap[index] > self.heap[parent_index]:
            self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
            index = parent_index
            parent_index = (index - 1) // 2

    def extract_max(self):
        if len(self.heap) == 0:
            return None

        max_value = self.heap[0]
        last_value = self.heap.pop()
        
        if len(self.heap) > 0:
            self.heap[0] = last_value
            self._heapify_down(0)
        
        return max_value

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


    def heap_len(self):
        return len(self.heap)


    def display(self):
        print(self.heap)


    def display_heap(self):

        heap = self.heap

        def get_level(index):
            return (index.bit_length() - 1) if index > 0 else 0

        def print_spaces(count):
            print(" " * count, end="")

        def print_branches(levels, current_level, index):
            if current_level >= levels:
                return

            elements_in_level = 2 ** current_level
            spaces_between_elements = 2 ** (levels - current_level) - 1

            print_spaces(spaces_between_elements)

            for i in range(elements_in_level):
                current_index = (2 ** current_level - 1) + i
                if current_index < len(heap):
                    print(f"{heap[current_index]:>4}", end="")
                else:
                    break

                if i < elements_in_level - 1:
                    print_spaces(spaces_between_elements * 2)

            print()

            for i in range(elements_in_level):
                current_index = (2 ** current_level - 1) + i
                if current_index < len(heap):
                    left_child_level = get_level(current_index * 2 + 1)
                    right_child_level = get_level(current_index * 2 + 2)

                    if left_child_level > current_level:
                        print_spaces(spaces_between_elements)
                    else:
                        print_branches(levels, current_level + 1, current_index * 2)

                    if right_child_level > current_level:
                        print_spaces(spaces_between_elements)
                    else:
                        print_branches(levels, current_level + 1, current_index * 2 + 1)

                    break

        height = get_level(len(heap) - 1) + 1
        print_branches(height, 0, 0)