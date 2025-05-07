#Task 1 - Working with Lists
fruit_list = ["apple", "banana", "cherry", "date", "elderberry"]
print("Original list:", fruit_list)
fruit_list.append("fig")
print("After adding a fruit:", fruit_list)
fruit_list.remove("fig")
print("After removing a fruit:", fruit_list)
fruit_list = fruit_list[::-1]
print("Reversed list:", fruit_list)
print()

#Task 2 - Exploring Dictionaries
my_dictionary = {"name": "Arash", "age": 23, "city": "Fairfax"}
my_dictionary["favorite color"] = "Blue"
my_dictionary["city"] = "New York"
print("Keys:", ", ".join(my_dictionary.keys()))
print("Values:", ", ".join(str(value) for value in my_dictionary.values()))
print()

#Task 3 - Using Tuples
favorite_things = ("Inception", "Bohemian Rhapsody", "1984")
print("Favorite things:", favorite_things)
try:
    favorite_things[1] = "Imagine"
except TypeError:
    print("Oops! Tuples cannot be changed.")
print("Length of tuple:", len(favorite_things))