fruts = ["apple","banana", "cherry"]

print(fruts)

words = ("spam", "eggs", "sausages")
print(words[1])

#creating a tuple with information about a person

person = ("Yll", 17, "devops")

name, age, proffesion = person

print(name,  "'s", "profession is", proffesion, "and he is", age, "years old")


#creating dictionary

my_dictionary = {
    "key1": "value1",
    "key2": "value2",
    "key3": "value3"

    #more keys more values pairs
}

contact_info = {
    "Yll": "444-333-454",
    "Driloni": "445-555-787"
}

kreative_phone = contact_info ["Yll"]

print(kreative_phone)
print(contact_info)

contact_info ["Driloni"] = "87468-47347"

print(contact_info)

contact_info["Eros"] = "456845-45735"

print(contact_info)

#delete a contact info

del contact_info ["Yll"]
print(contact_info)

keys = contact_info.keys()

print(keys)

values = contact_info.values()
print(values)

#print items

items = contact_info.items()
print(items)

















