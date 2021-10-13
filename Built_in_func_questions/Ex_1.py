#Filter out all of the empty strings from the list below

#Output: ['Argentina', 'San Diego', 'Boston', 'New York']

places = [" ","Argentina", " ", "San Diego","","  ","","Boston","New York"]


# def filter_places(place):
#     if len(place) > 2:
#         return True
#     else:
#         return False

list_new = list(filter(lambda place: True if len(place) > 2 else False, places))
print(list_new)