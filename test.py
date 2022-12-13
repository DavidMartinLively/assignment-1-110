from config import me

print(me)

#read
print(me["first"])
print(me["first"] + " " + me["last"])


#modify values

me["first"] = "David L"
print(me["first"])

# add new keys

me["preferred_color"] = "Purple"
print(me)


#print the full address
# format: num street, city

address = me["address"]
print(str(address["number"]) + " " + address["street"] + " " + address["city"])



