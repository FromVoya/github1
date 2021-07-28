def x():
    t="""Генератор - это иттератор, элементы которго можно перебирать только один раз."""
    for i in t:
        yield i

k=[]
b=[]
e=[]
for i in x():
    for j in i:
        if j==" ": continue
        if j.isalnum() == True:k.append(j)
    if i==" ":
        b="".join(k)
        e.append(b)
        k=[]
for i in e:
    if i!="":
        print(i)




    # if i == " ":
    #     b.append(k)
    #     k=[]
    #     continue
    # k.append(i)
# for c in b:
#     for i in c:
#         if i == "\n" or i==" ": break
#         print(i,end="")
#     print(end=" ")

# num=["as","aea","asc"]
# print(" ".join(num))
