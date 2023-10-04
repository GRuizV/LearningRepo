from typing import NamedTuple, Any

class Pair(NamedTuple):
    key: Any
    value: Any

# BLANK = object()

class HashTable:

    def __init__(self, capacity=int()):

        if capacity < 1:
            raise ValueError('Capacity mush be a positive number')
                
        self._slots = capacity * [None]
    

    def __len__(self):

        return len(self.pairs)


    def __setitem__(self, key, value):
        
        self._slots[self._index(key)] = Pair(key, value)

    
    def __getitem__(self, key):
        
        pair = self._slots[self._index(key)]

        if pair is None:
            raise KeyError(key)

        return pair.value
    

    def __contains__(self,key):

        try:
            self[key]
        
        except KeyError:
            return False
        
        else:
            return True

        
    def __delitem__(self, key):
        
        # #Initially
        # self.pairs[self._index(key)] = None

        if key in self:

            #Refactored
            self._slots[self._index(key)] = None

        #This is possible because by assigning with ['key'] it
        #delegates the assignment to the __setitem__() directly

        else:

            raise KeyError(key)




    def get(self, key, default=None):

        try:
            return self[key]
        
        except KeyError:
            return default




    def _index(self, key):

        return hash(key) % self.capacity


    @property
    def pairs(self):
        return {pair for pair in self._slots if pair}
    

    @property
    def keys(self):
        return {pair.key for pair in self.pairs}


    @property
    def values(self):
        return [pair.value for pair in self.pairs]
    

    @property
    def capacity(self):
        return len(self._slots)






























