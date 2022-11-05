# 1) Write a 'split_name' function that returns a string and returns a dictionary with first_name and Last_name
def split_name(name):
    first_name, last_name = name.split(maxsplit=1)
    return {
        'first_name': first_name,
        'last_name': last_name,
    }

assert split_name("Kevin Bacon") == {
    "first_name" : "Kevin",
    "last_name" : "Bacon",
}, print(f"Expected {{'first_name': 'Kevin', 'last_name': 'Bacon'}} but received {split_name('Kevin Bacon')}")

def is_palindrome(item):
    item = str(item)
    return item == item[::-1]

assert is_palindrome("radar") == True, print(f"Expected True but got {is_palindrome('radar')}")

def build_list(item, count):
    items []
    for_ in range(count):
        items.append(item)
    return items
    
