res = lambda x,y:x+y
print(res(9,8))
res = lambda x,y,z:(x*y)/z
print(res(6,7,2))
list = [1, 2, 3, 4]
iter_var = iter(list)
print(iter_var)
type(iter_var)
for i in iter_var:
    print(i)

list1 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
iter_var1 = iter(list1)
for j in iter_var1:
    if j % 2 == 0:
        print(j)

listx = [1,2,3,4]
for i in listx:
    if i % 2 == 0:
        print(i)

#check the blow list and display the
# string where the string contain 'a' letter with iteratoe
#list = ["aaa", "wer", "aer", "ggt"]
listy = ["aaa", "wer", "aer", "ggt"]
iter_vary = iter(listy)
for i in iter_vary:
    print(i)

#without generatoe
def square(k):
    for k in range (k):
        k = k**2
    return i
res = square(i)
print(res)