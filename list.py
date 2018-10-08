items = []
while True:
    a = input('wanna add item to your list : yes/no ')
    if a == ('yes'):
        b = input('enter item ')
        if b in items :
            print('the item is already in your list')
        else:
            items.append(b)
    else:
        break
print(items)
