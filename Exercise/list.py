#---------------list--------------------------
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(thislist[2:6])
# for x in thislist:
#     print(x)
# if "apple" in thislist:
#     print("yes")
# else:
#     print("No")
# thislist.append("orange")
# thislist.insert(2,'orange')
# thislist.remove("banana")
# thislist.pop()
# print(thislist)

def remove_duplicate(arr):
    uniq_items = []
    for i in arr:
        if i not in uniq_items:
            uniq_items.append(i)
    return uniq_items

a = [10,20,30,20,10,50,60,40,80,50,40]
# print(remove_duplicate(a)

x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(a[::2])
def select_odd(arr):
    items = []
    for i in arr:
        if i%2==1:
            items.append(i)
    return items

# print(select_odd(x))

