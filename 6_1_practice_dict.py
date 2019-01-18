# Python 3.7.2/win10 64bit/IDE:Pycharm 2018.3.3
# practice with dictionary and set
# clear()	Removes all the elements from the dictionary
# copy()	Returns a copy of the dictionary
# fromkeys()	Returns a dictionary with the specified keys and values
# get()	Returns the value of the specified key
# items()	Returns a list containing the a tuple for each key value pair
# keys()	Returns a list containing the dictionary's keys
# pop()	Removes the element with the specified key
# popitem()	Removes the last inserted key-value pair
# setdefault()	Returns the value of the specified key.
#               If the key does not exist: insert the key, with the specified value
# update()	Updates the dictionary with the specified key-value pairs
# values()	Returns a list of all the values in the dictionary

# initialization
country_info1=dict()
country_info1["swiss"]=[41, "Bern"]
country_info1["uk"]=[34, "London"]

country_info2={"korea":[81, "Seoul"], "usa":[1, "DC"], "spain":[34, "Madrid"]}

# iteration
for key, values in country_info1.items():
    print("country_info1 iteration: ", key, values)
print("\n")
for key, values in country_info2.items():
    print("country_info2 iteration: ", key, values)
print("\n")
for key in country_info1.keys():
    print("country_info1 key iteration: ", key)

# Access the item
print("\n")
print("Access the item: ", country_info1["swiss"])
print("Access the item: ", country_info2.get("usa"))

# copy all of dictionary
print("\n")
dict_test=country_info1.copy()
print("copy all of country_info1", dict_test)

print("\n")
# print(country_info1.fromkeys([41, "Bern"]))
print(country_info1.items())

country_info2_india={"india":[41, "New Delhi"]}
country_info2.update(country_info2_india)
for key, values in country_info2.items():
    print(key, values)
print("\n")
country_info2_usa={"usa":[1, "New York"]}
country_info2.update(country_info2_usa)
for key, values in country_info2.items():
    print(key, values)


print("\n")
# Access the values
for values in country_info2.values():
    print("Access all values: ", values)

# pop test
# RuntimeError: dictionary changed size during iteration
# This error occurs because of modifying dict when iterating.
# for key in country_info2.keys(): => for key in country_info2.copy().keys():
# for key in country_info2.keys(): => runtime error occurs
for key in country_info2.copy().keys():
    if(key=="spain"):
        del country_info2["spain"]

# sort return list
sorted_country_info2=sorted(country_info2.items(), key=lambda x:x[0])
print(type(sorted_country_info2))
sorted_country_info2=dict(sorted_country_info2)
print("sorted country info2: ", sorted_country_info2)
print(type(sorted_country_info2))
print("\n")

# remove all dictionary
country_info1.clear()
country_info2.clear()
print("removes all of country_info1 items", country_info1)
print("removes all of country_info2 items", country_info2)