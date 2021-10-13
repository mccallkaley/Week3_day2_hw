# CLASS - 
# squared_nums = list(map(lambda x: x**2 if x<10 else x,numbers))
# print(squared_nums)

#Convert the list below from Celsius to Farhenheit, using the map function with a lambda...

#Output: [('Nashua', 89.6), ('Boston', 53.6), ('Los Angelos', 111.2), ('Miami', 84.2)]

# F = (9/5)*C + 32

places = [('Nashua',32),("Boston",12),("Los Angelos",44),("Miami",29)]

faren_places = list(map(lambda x: (x[0], x[1] * (9/5) + 32), places))

print(faren_places)