'Nice Teams'

'Source: https://github.com/kilian-hu/hackerrank-solutions/blob/master/certificates/problem-solving-intermediate/nice-teams/solution.py'

# Input

# Case1
# rating = [1,1,1,1]
# minDiff = 1 # Expected Output: 0

# Case2
# rating = [3,4,5,2,1,1]
# minDiff = 3 # Expected Output: 2

# Custom case
# rating = [3,4,5,2,1,1,1,1,1]
# minDiff = 0 # Expected Output: _


# My Approach
# def maxPairs(skillLevel, minDiff):

#     skillLevel = sorted(skillLevel)
#     pairs = []
#     idx = 0
#     n = len(skillLevel)

#     for i in range(n//2):

#         while idx < n and skillLevel[idx] - skillLevel[i] < minDiff:
#             idx += 1

#         if idx >= n:
#             break
    
#         pairs.append(idx)

#     pairs = pairs[:(n//2)]

#     res = 0
#     idx2 = n-1

#     for j in reversed(pairs):

#         if j <= idx2:

#             res += 1
#             idx2 -= 1

#     return res

# print(maxPairs(rating, minDiff))



'Largest Area'
'Source: https://github.com/kilian-hu/hackerrank-solutions/blob/master/certificates/problem-solving-intermediate/largest-area/solution.py'

# input

# Case 1
# w = 2
# h = 2
# isVertical = [0,1]
# distance = [1,1]

# Case 2
w = 4
h = 3
isVertical = [1,1]
distance = [1,3]


#My Approach 

class Node:

    def __init__(self, parent, l, r, op=max):
        self.parent = parent
        self.l = l
        self.r = r
        self.lc = None
        self.rc = None
        self.val = r - l
        self.op = op
    
    def split(self, x):
       
        assert self.l <= x <= self.r

        if x == self.l or x == self.r:
            # Split lies on borders.
            return
        
        if self.lc:

            if x == self.lc.r:
                # Split lies on mid split.
                return
            
            if x < self.lc.r:
                self.lc.split(x)

            else:
                self.rc.split(x)

            self.val = self.op(self.lc.val, self.rc.val)

        else:

            self.lc = Node(parent=self, l=self.l, r=x)            
            self.rc = Node(parent=self, l=x, r=self.r)
            self.val = self.op(x - self.l, self.r - x)

 
def getMaxArea(w, h, isVertical, distance):

    w_root = Node(parent=None, l=0, r=w)
    h_root = Node(parent=None, l=0, r=h)
    result = []

    for iv, d in zip(isVertical, distance):

        if iv:
            w_root.split(d)

        else:
            h_root.split(d)

        result.append(w_root.val * h_root.val)

    return result



print(getMaxArea(w, h, isVertical, distance))


