#1
# lst=["a","b","c"]
# for x in lst:
#     print(x)

#2
# lst=["a","b","c"]
# x=0
# while x < len(lst):
#     print(lst[x])
#     x +=1

#3
# dct={
#     "a":1,
#     "b":2
# }
# lst1=["c","d"]
# lst2=[3,4]
# lst3=dct
# for i in lst1:
#     for x in lst2:
#         dct.update(i=x)
#         lst3.update(dct)
# print(lst3)

#4
# dct={
#     "a":1,
#     "b":2,
#     "c":3
# }
# a=dct.values()
# for x in a:
#     print(x)

#5
# a=[
#     [11,12,13,14,15],
#     [21,22,23,24,25],
#     [31,32,33,34,35],
#     [41,42,43,44,45],
#     [51,52,53,54,55],
# ]
# b=[]
# for x in range(len(a[0])):
#     c=[]
#     for i in a:
#         c.append(i[x])
#     b.append(c)
# for i in b:
#     print(i)

#6
# a=[
#     [11,12,13],
#     [21,22,23],
#     [31,32,33],
# ]
#
# b=[
#     14,24,34
# ]
#
# for x in range(len(a)):
#     a[x].append(b[x])
# print("\n",a[0],"\n",a[1],"\n",a[2])

#7
# a=[
#     [1,2,3,4,5],
#     [1,2,3,4,5],
#     [1,2,3,4,5],
#     [1,2,3,4,5],
#     [1,2,3,4,5],
# ]
#
# b=[sum(x[i] for x in a) for i in range(len(a[0]))]
# print(b)