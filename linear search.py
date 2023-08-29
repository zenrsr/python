def locate_card(cards,query):
    position = 0
    while position < len(cards):
        if cards[position] == query:
            return position
        position += 1
    return -1
cards = list(map(int,input("Enter the array: ").split(',')))
query = int(input())
print(locate_card(cards,query))