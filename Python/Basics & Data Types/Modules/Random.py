import random
from unittest.util import strclass

l = ['apple', 'orange', 'pineapple']

# print(random.choice(l))

# print(random.choices(l, cum_weights=None, k=10))

# print(random.choices(l, cum_weights=[20, 50, 90], k=10))


# #Uniformly picked
# res = random.choices(l, cum_weights=None, k=100)

# print(f'apple: {res.count(l[0])}\norenage: {res.count(l[1])}\npineapple: {res.count(l[2])}')



# #with relative probability
# res = random.choices(l, cum_weights=[15, 25, 60], k=100)

# print(f'apple: {res.count(l[0])}\norenage: {res.count(l[1])}\npineapple: {res.count(l[2])}')



#with cumulative probability
# res = random.choices(l, cum_weights=[15, 40, 100], k=100)

# print(f'apple: {res.count(l[0])}\norenage: {res.count(l[1])}\npineapple: {res.count(l[2])}')


deck = list(range (1,52+1))

# print(deck) 

# random.shuffle(deck)

# print(deck)


# print(random.sample(deck, k=5))



