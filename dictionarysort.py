keys=input("Enter the keys: ").split()
dict1={}
for key in keys:
    value=input(f"Enter the value for {key}: ")
    dict1[key]=value
print("Original Dictionary")
print(dict1)
keys.sort()
dict_sort_asc={key:dict1[key] for key in keys}
print("Ascending order: ")
print(dict_sort_asc)
keys.sort(reverse=True)
dict_sort_dsc={key:dict1[key] for key in keys}
print("Descending order")
print(dict_sort_dsc)
