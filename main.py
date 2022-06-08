# 1.loop through the list
# 2. swap the first and last name
# 3. sort the list alphabetically

def sorted_names(list1):
    reversed_list = []
    for name in list1:
        first_name = name.split()[0]
        last_name = name.split()[1]
        name = last_name + " " + first_name
        reversed_list.append(name)
    return sorted(reversed_list)

# names = ["Beyonce Knowles", "Alicia Keys", "Katie Perry", "Chris Brown", "Tom Cruise"]
# print(sorted_names(names)) ----> ['Brown Chris', 'Cruise Tom', 'Keys Alicia', 'Knowles Beyonce', 'Perry Katie']

