# num=-1
# if num>0:
#    print("possitive")
# else:
#    print("negative")


# num=5
# if num%2==0:
#     print("even")
# else:
#     print("odd")


# age=3
# if age>=18:
#     print("eligible for vote")
# else:
#     print("not eligible")


# a=10000
# b=200
# c=100
# if a>b and a>c:
#     print("a large")
# elif b>a and b>c:
#     print("b is large")
# else:
#     print("c is large")


# mark=18
# if mark<18:
#     print("fail")
# else:
#     print("pass")


# mark=39
# if mark>30:
#     print("A grade")
# elif mark>20:
#     print("B grade")
# else:
#     print("D grade")


# admin="admin"
# password="admin1234"
# if admin=="admin" and password=="admin1234":
#     print("succuss")
# else:
#     print("fail")

# ch ="a"
# if ch=="a" or"e" or"i" or"o" or "u":
#     print("vowels")
# else:
#     print("not vowels")


# day=3
# match day:
#  case 1:
#   print("sunday")
#  case 2:
#   print("monday")
#  case 3:
#    print("tuesday")
#  case 4:
#    print("wednesday")
#  case 5:
#    print("thursday")



# arr=["apple","banana","mango"]
# arr.insert(0,"graps")
# arr.append("shifa")
# # arr[1]="graps"
# print(arr)



# arr=["shifa","safa","shahma"]
# print(arr[1])

# arr=(1,2,3,4)
# print(arr)


# students={
#        "name":"shifa",
#         "age":10,
#         "place":"koramkod"
# }
# print(students["name"])


# arr={1,1,2,2,3,4,5}
# print(arr)


# arr=[11,12,44,66,10]
# arr.reverse()
# print(arr)



# arr=[1,2,3,4,5,5]
# num=arr[::-1]
# print(num)



# numbers = [10, 20, 20, 30, 40, 40]
# print(numbers.index(20))



# a=[1,2,3]
# b=[3,4,5,6]
# print(a.union(b))



# arr=["mango","banana"]
# arr.extend(["orange","bnana"])
# print(arr)


# arr = [10, 20, 20, 30, 40, 40]
# print(count(arr))

# arr = ("apple", "banana", "orange", "apple", "grape")
# print(arr.index("orange"))\



# arr={11,22,33,44}
# arr1={1,22,33}
# print(arr.difference(arr1))


# a = {1, 2, 3}
# b = {4, 5, 6,7,3}

# a.update(b)

# print(a)


# arr=(1,2,3,4,5,6)
# for n in arr:
#     print(n)


# stydents={
#     "name":"sgifa",
#     "age":10
# }
# stydents["place"]="koramkode"
# print(stydents)


# stydents={
#     "name":"sgifa",
#     "age":10
# }
# for n in stydents:
#    print(n)




# stydents={
#     "name":"sgifa",
#     "age":10
# }
# for n in stydents.values():
#    print(n)


# stydents={
#     "name":"sgifa",
#     "age":10
# }
# for n in stydents:
#     # print(n)
#     #  name
#     #           age

# for n in stydents.values():
#    print(n)    //sgifa
#                  10

# for key , n in stydents.items():
#     print(key ,":", n) //name : sgifa
#                         age : 10



# stydents={
#     "name":"sgifa",
#     "age":10
# }

# print(stydents.keys())
# print(stydents.values())
# print(stydents.items())


# stydents={
#     "name":"sgifa",
#     "age":10
# }
# # stydents.update({"name":"safa","age":10})
# stydents.clear()
# print(stydents)




# stydents={
#     "name":"sgifa",
#     "age":10
# }
# stydents.pop("age")
# print(stydents)





# i=1
# while i<6:
#     print(i)
#     i+=1



# for n in range(1,6):
#     if n==4:
#         break
#     print(n)



# sqr={x:x*x for x in range(1,6)}
# print(sqr)


# name=" SHIFA "
# print(name.strip())

# name="shifa"
# print(name.replace("shifa","i love you"))



# name="python"
# print(name[2:])

# words = ["Python", "is", "Easy"]
# print(" ".join(words))



# name="SHIhifa yasmin p"
# print(name.swapcase())


# def name():
#     print("shifa yasmin")

# name()



# def sum(a,b):
#     print(a+b)

# sum(10,20)


# def sqrt(num):
#     return num*num
# result=sqrt(5)
# print(result)


# def name(name="shifa"):
#     print("hello" +name)

# name()
# name("john")



# arr=[11,22,34,55]
# arr.remove(10)
# print(arr)


# def val(**data):
#     for key , n in data.items():
#         print(key, ":", n)

# val(name="shifa" , age=10, place="koramkode")



# def num(*n):
#    for i in n:
#       print(i)

# num(11,22,33,44)



# def name(*name1):
#     for i in name1:
#         print(i)

# name("shifa","safa","shahama")




# def arr(**name):
#     for i,val in name.items():
#         print(i ,":" ,val)
# arr(name="shifa",age=10)


# def arr(*num):
#     print(num)
# arr(11,22,33,44)



# def arr(num):
#     if num==0:
#         return 
#     print(num)
#     arr(num-1)

# arr(5)



# def arr(num):
#     if num==1:
#         return 1
#     return num*arr(num-1)
# print(arr(6))



# def arr(num):
#     if(num<=1):
#         return num
#     return arr(num-1)+arr(num-2)
# for i in range(8):
#    print(arr(i))



# def arr(name):
#     for i in name[::-1]:
#         print(i,end="")
# arr("shifa")



# def arr(name):
#     for i in name[::-1]:
#         print(i ,end=" ")

# arr(["shifa","safa","shahma"])




# def arr(num):
#     reverse=int(str(num)[::-1])
#     print(reverse)
#     if num==reverse:
#         print("pallindrom")
#     else:
#         print("not pallindrom")
# arr(1221)



# def arr(name):
#     # if "a" in name or"e" in name or "i" in name or "o" in name or "u" in name:
#     if "aeiou" in name:
#         print("vowel number")
#     else:
#         print("not vowels")
# arr("shfwi")


# def arr(name):
#     vowels="aeiou"
#     for i in name:
#         if i in vowels:
#             print("vovels includes")
#             return

#     print("not vowel")
# arr("shf")



# def arr(name):
#     vowels="aeiou"
#     for i in name:
#         if i in vowels:
#             print("vowels include")
#             return
#     print("not vowels")
# arr("shff")\



# def arr(name):
#     vowels="aeiou"
#     count=0
#     for i in name:
#         if i in vowels:
#             count+=1
#     print("count is",count)
# arr("shifa")



# a=[1,2,3]
# b=[4,5,6]
# print(a+b)



# sqr= lambda x:x*x
# print(sqr(8))


# sum= lambda a,b :a+b
# print(sum(10,20))


# import  math
# print(math.sqrt(5))
# print(math.factorial(5))
# print(math.pi)


# import random
# print(random.randint(1,10))


# import random
# num=[1,2,3,4,6]
# random.shuffle(num)
# print(num)\


import random
name=["shifa","safa","shahma"]
random.shuffle(name)
print(name)