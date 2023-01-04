#multi line
course = '''
SPK's Salary is USD "75,000"
He recently switched organization
'''
print(course)

#index
first_name = "Abcdefg"
last_name = "Pqrstuv"

print(first_name[6])
print(first_name[-1])

print(first_name[4])
print(first_name[-3])

print(first_name[0:5])
print(first_name[:5])

print(first_name[0:])
print(first_name[:])

print(first_name[3:])

print(first_name[1:-1])  # print | 1 index | -1 excludes position

# formatted string
message = f"{first_name} [{last_name}] is a Cloud DevOps"
print(message)

# methods
full_name = f"{first_name} {last_name}"
print(full_name)

print(len(full_name))

print(full_name.upper())
print(full_name.lower())
print(full_name.capitalize())
print(full_name.title())

print(full_name.find("A"))  # case sensitive
print(full_name.find("q"))  # case sensitive

print(full_name.replace("SPK","PSK"))  # case sensitive

print("S" in full_name)  # case sensitive
print("S" in full_name)  # case sensitive

print(full_name.count("a"))  # case sensitive
print(full_name.count("A"))  # case sensitive

print(full_name.isdigit())

print(full_name.startswith("Sp"))  # case sensitive
print(full_name.startswith("SP"))  # case sensitive

print(full_name)

