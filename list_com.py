list = {1,2,3,4,5}
res = [i for i in list if i > 5]
print(res)
res = [i for i in list if i % 2 == 0]
print(res)
keys = ["name","age","city"]
values = ["banglore", 25, "Hyderabad"]
dictionary = {k:v for k,v in zip {keys,values}}
print(dictionary)