def test_location(cards, query, mid):
    if cards[mid] == query:
        if mid-1 >= 0 and cards[mid-1] == query:
            return 'left'
        else:
            return 'found'
    elif cards[mid] < query:
        return 'left'
    else:
        return 'right'

def locate_card(cards, query):
    low, high = 0, len(cards) - 1
    while low <= high:
        mid = (low + high) // 2
        result = test_location(cards, query, mid)
        print("low: {} , high: {} , middle: {}".format(cards[low],cards[high],cards[mid]))
        if result == 'found':
            return mid
        elif result == 'left':
            hi = mid - 1
        elif result == 'right':
            lo = mid + 1
    return -1
cards = list(map(int,input("Enter sorted list : ").split(",")))
query = int(input())
print(locate_card((cards,query)))