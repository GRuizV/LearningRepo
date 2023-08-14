from math import log
import heapq

# source: https://gist.github.com/ydm/4f0c948bc0d151631621


first = lambda h: 2**h - 1      # H stands for level height
last = lambda h: first(h + 1)
level = lambda heap, h: heap[first(h):last(h)]
prepare = lambda e, field: str(e).center(field)


def hprint(heap, width=None):

    if width is None:
        width = max(len(str(e)) for e in heap)

    height = int(log(len(heap), 2)) + 1    
    gap = ' ' * width

    for h in range(height):
        below = 2 ** (height - h - 1)
        field = (2 * below - 1) * width
        print(gap.join(prepare(e, field) for e in level(heap, h)))


def main():
    h = []
    for x in reversed(range(31)):
        # e = chr(ord('A') + x)
        e = x
        heapq.heappush(h, e)
        print('Adding {}:'.format(e))
        hprint(h)
        print()


if __name__ == '__main__':
    main()