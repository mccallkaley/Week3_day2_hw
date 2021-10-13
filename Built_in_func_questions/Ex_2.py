#Write an anonymous function that sorts this list by the last name...
#Hint: Use the ".sort()" method and access the key"

#Output: ['Victor aNisimov', 'Gary A.J. Bernstein', 'Joel Carter', 'Andrew P. Garfield', 'David hassELHOFF']

#capital matters
# print(sorted(people, key = lambda person_dict: person_dict["age"],reverse=True)) ex used in class kind of similar

author = ["Joel Carter", "Victor aNisimov", "Andrew P. Garfield","David hassELHOFF","Gary A.J. Bernstein"]

author.sort(key = lambda name: name.split(" ")[-1].upper())

print(author)


