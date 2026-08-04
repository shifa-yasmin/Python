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


# import random
# name=["shifa","safa","shahma"]
# random.shuffle(name)
# print(name)


# import math
# print(math.sin(8))


# import math
# print(math.lcm(2,4))

# import math
# print(math.gcd(4,6))




# def arr(num):
#        print(min(num)) 

# arr([1,44,22,33,77])

# import math
# a=[11,44,22,55,33]
# print(math.max)



# def num(num1):
#     print(set(num1))
# num({11,22,33,22})



# def num(num1):
#     print(set(num1))
# num([11,22,33,22])


# def num(num1):
#   num1.sort(reverse=True) 
#   print(num1[1])
# num([11,99,66,77,33])


# def arr(num):
#    num.reverse()
#    print(num)

# arr({"name":"shifa","age":10})



# def arr(num):
#     for i in num:
#         if(i%2==0):
#             print(i ,end=",")
# arr([11,22,1,2,3,4])



# def arr(num,n):
#    for i in range(1,n+1):
#       if i not in num:
#          print(i)
# arr([1,2,3,5],5)


# num=[x for x in range(1,10) if x%2==0]
# print(num)



# def arr(num):
#    count=0
#    for i in range(1,num+1):
#       if num%i==0:
#          count+=1
#    if count==2:
#       print("prime number")
#    else:
#      print("not prime") 
# arr(4)



# name="shifa"
# print(name[::-1])


# def arr(name):
#     for i in name[::-1]:
#         print(i,end="")
# arr("shifa")



# def num(a):
#     count=0
#     vowels="aeiou"
#     for i in a:
#         if i in vowels:
#             count+=1
#     print(count)
# num("shifa yasminii") 




# def arr(name):
#     res=name[::-1]
#     if res in name:
#         print("pallindrom")
#     else:
#         print("not pallindrom")
# arr("shhs")



# def arr(name):
#     print(name.replace("shifa","i love java"))
# arr("shifa")




# def arr(name):
#     print(len(name))
# arr("shifa yasmin")




# def arr(name):
#     print(name.split())
# arr("shifa yasmin")




# def arr(name):
#     print("_ " .join(name))
# arr(["shifa","safa"])


# def arr(name):
#     print(name.strip())
# arr(" shifag ")



# def arr(name):
#     print(name.capitalize())
# arr("i love you")




# def arr(name):
#    name.count(33)
#    print(name)
# arr((11,22,44,33,33))



# def arr(num):
#     print(tuple(num))
# arr([1,2,3,4,5])


# def arr(a,b):
#     print(a.difference(b))
# arr({1,2,3},{2,4,5})



# def arr(**data):
#     for i,a in data.items():
#         print(i ,":", a)
# arr(name="shifa",age=10,place="koramkod")


# sqrt={x:x*x for x in range(1,6)}
# print(sqrt)



# def arr(name):
#     for i in name:
#      if name.count(i)>1:
#         print(i ,end="")
#         name=name.replace(i," ")
# arr("shiifaa")



# def arr(num):
#     num.sort(reverse=True)
#     print(num[1])
# arr([11,33,22,44,99])


# name="shiifa"
# name1={x for x in name if x in name}
# print(name1)



# def arr(num):
#     d={}
#     for i in num:
#         if i in d:
#             d[i]+=1
#         else:
#             d[i]=1
#     print(d)
# arr("shifa")




# class student:
#     def name():
#         print("shifa yasmin")
# s1=student
# s1.name()


# class add:
#     def name(self,a,b):
#         print(a+b)
# h1=add()
# h1.name(10,20)




# class add:
#     def name(self):
#         print("shifayasmin")
# h1=add()
# h1.name()



# class student:
#     def __init__(self):
#         print("shifa yasmin")
# h1=student()



# class studant:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
# s1=studant("shifa",19)
# print(s1.name)
# print(s1.age)


# class sudents:
#     def __init__(self,name):
#            self.name=name
#     def arr(self):
#                  print(self.name,"my name")
# h1=sudents("shifa")
# h1.arr()
           


# class arr:
#     def __init__(self,name,salary):
#         self.name=name
#         self.salary=salary
#     def val(self):
#         print("name is :", self.name)
#         print("salary is:",self.salary)
# h1=arr("shifa",100000)
# h1.val()




# class arr:
#     def __init__(self,length,width):
#         self.length=length
#         self.width=width
#     def triangle(self):
#         print(self.length*self.width)
        
# h1=arr(4,3)
# h1.triangle()



# class arr:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#         print(self.name)
#         print(self.age)
# h1=arr("shifa",19)
# h2=arr("safa",19)




# class arr:
#     school="duhss thotha"
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
# h1=arr("shifa",19)
# h2=arr("safa",29)
# print(h1.name ,"-",arr.school)
# print(h2.name ,"-",arr.school)


# class arr:
#     def __init__(self):
#         name="shifa"
#         print(name)
# h1=arr()
# # h1.person()




# class students:
#     def __init__(self,name):
#         self.name=name
#     def arr(self):
#         print(self.name)
# h1=students("shifa")
# h1.arr()


# class students:
#     school="duhss thootha"
#     @staticmethod
#     def num():
#         print(students.school)
# students.num()



# class student:
#     def __init__(self,name):
#         self.name=name
#     def val(self):
#         print("name is:",self.name)
# class child(student):
#     def val2(self):
#         print("my name is :",self.name)
# h1=child("shifa")
# h1.val2()
# h1.val()




# class parent:
#     def val(self):
#         print("shifa yasmin p")
# class child(parent):
#     def num(self):
#         print("safa yasmin")
# h1=child()
# h1.val()
# h1.num()



# class parent:
#     def val(self):
#         print("parent mother")
# class father:
#     def num(self):
#         print("mother")
# class child(parent,father):
#     def number(self):
#         print("shahma fathima")
# h1=child()
# h1.val()
# h1.num()
# h1.number()



# class father:
#     def val(self):
#         print("shifa yasmin")
# class mother(father):
#     def num(self):
#         print("shahma fathima")
# class child(mother):
#     def hwllo(self):
#         print("safa yasmin")
# h1=child()
# h1.val()
# h1.num()
# h1.hwllo()




# class parent:
#     def val(self):
#         print("shifa yasmin")
# class child(parent):
#     def num(self):
#         print("shahma fathima")
# class Hello(parent):
#     def hum(self):
#         print("sachu")
# h1=Hello()
# h1.hum()
# h1.val()
# h2=child()
# h2.num()
# h2.val()



# class parent:
#     def __init__(self,name=None):
#         self.name=name
# class child(parent):
#     def num(self,name,age):
#          super().__init__(name)
#          self.age=age
       
# h1=child()
# h1.num("shifa",19)
# print(h1.name)
# print(h1.age)


# class parent:
#     def __init__(self,name):
#         self.name=name
# class child(parent):
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
# h1=child("shifa",18)
# print(h1.name)
# print(h1.age)





# class calculator:
#     def num(self,*val):
#         return sum(val)

# c=calculator()
# print(c.num(111,22,334))




# class calculator:
#     def val(self,a,b=0,c=0):
#         print(a+b+c)
# c=calculator
# c.val(10,20)
# c.val(1,2,3)



# class calculator:
#     def val(self,*num):
#         print(sum(num))
# c=calculator
# c.val(10,20,30)
# c.val(30,348,156)




# from abc import ABC ,abstractmethod
# class Animal(ABC):
#     @abstractmethod
#     def sound(self):
#         pass
# class Shifa(Animal):
#     def sound(self):
#         print("shifa yasmin p")
# c=Shifa()
# c.sound()



# arr="shifa"
# print(arr.encode())





# def num1(num):
#      for i in num[::-1]:
#        print(i,end="")    
# num1("shifa")



# arr="shifa"
# print(arr[::-1])



# def arr(num):  
#     res=str(num)[::-1]
#     if str(num)==res:
#         print("pallindrom")
#     else:
#         print("not pallindrom")
# arr(121)



# def arr(name):
#     vowels="aeiou"
#     for i in name:
#         if i in vowels:
#             print("vowels")  
#             return
#     print("not vowels")
# arr("shifa")



# numb=[11,22,33,45]
# it=iter(numb)
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))




# arr="shifa"
# it=iter(arr)
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))


# name="shifa"
# it=iter(name)
# for i in it:
#     print(i)


# def arr(name):
#     vowels="aeiou"
#     count=0
#     for i in name:
#         if i in vowels:
#            count+=1

#     print(count) 
# arr("shifaaaa") 


# def arr(name):
#  res="" 
#  for i in name:
#   if i not in res:
#    res+=i
#  print(res)
# arr("shiiffa")



# def arr(val):
#     freq={}
#     for i in val:
#         if i in freq:
#             freq[i]+=1
#         else:
#             freq[i]=1
#     print(freq)
# arr([1,2,1,3,4,3])



# def arr(name):
#     val={}
#     for i in name:
#         if i in val:
#             val[i]+=1
#         else:
#             val[i]=1
#     print(val)
# arr("shifa")



# def val(name):
#  for i in name:
#   if name.count(i)==1:
#    print(i)
#    return
            
# val("aabbbcccdg")



# def val(num):
#    num.sort()
#    for i in reversed(num):
#       print(i)     
# val([11,22,33,44,11,44])


# def num():
#     yield 1
#     yield 2
#     yield 3
# gen=num()
# print(next(gen))
# print(next(gen))
# print(next(gen))


# def num():
#     yield 1
#     yield 2
# gen=num()
# print(next(gen))
# print(next(gen))



# class student:
#     def __iter__(self):
#         self.num=1
#         return self
#     def __next__(self):
#         if self.num<=3:
#             x=self.num
#             self.num+=1
#             return x
#         else:
#             raise StopIteration
# a=student()
# for i in a:
#     print(i)


# num=[10,20,33,44]
# a=iter(num)
# print(next(a))
# print(next(a))
# print(next(a))


# num=[1]
# id=iter(num)
# print(next(id))
# print(next(id))

# names = ["Ali", "John", "Sara"]
# for i in names:
#     print(i)



# def count():
#     for i in range(1,7):
#         yield i
# a=count()
# for i in a:
#     print(i)




# def val():
#     yield 10
#     yield 20
#     yield 30
# a=val()
# for i in a:
#     print(i)



# def val():
#     for i in range(1,8):
#         yield i
# a=val()
# for i in a:
#     print(i)



# def val():
#     for i in range(1,8):
#         yield i
# a=val()
# for i in a:
#     print(i*i)




# def val():
#     for i in range(1,10):
#         if i%2==0:
#          yield i
# a=val()
# for i in a:
#     print(i)




# def val():
#     for i in range(1,10):
#         if i%2!=0:
#             yield i
# a=val()
# for i in a:
#     print(i)



# file=open("student.txt","w")
# file.write("hello world")
# file.close()

# file=open("student.txt","a")
# file.write("\nshifa")
# file.close()

# file=open("student.txt","r")
# print(file.read())
# file.close()



# with open("sample.txt","r") as file:
#     print(file.read(5))
#     file.seek(0)
#     print(file.read(5))


# with open("sample.txt","r") as file:
#     file.read(5)
#     print(file.tell())


# try:
#     with open("sample.txt","r") as file:
#         print(file.read())
# except FileNotFoundError:
#     print("error")


# file=open("student.txt","r")
# print(file.readlines())
# file.close()


# file=open("student.txt","r")
# for i in file:
#     print(i.strip())
# file.close()
# file = open("newfile.txt", "x")

# file.close()




# import os
# if os.path.exists("student.txt"):
#     print("Exist")
# else:
#     print("not exist")



# import os
# print(os.remove("newfile.txt"))



# file=open("student.txt","r")
# print(file.flush())
# file.close()



# def main(num):
#     res=list(map(lambda x:x*x, num))
#     print(res)
# main([2,4,5,6,7])


# def main(x):
#     return x * x
# def main2(num):
#     res=list(map(main,num))
#     print(res)
# main2([2,3,4,5])



# def arr(name):
#     res=list(map(str.upper,name))
#     print(res)
# arr(["shifa","safa"])



# def arr(name):
#     res=list(map(str.lower,name))
#     print(res)
# arr(["SHIFA","SAFA"])
    


# def val(num):
#     res=max(num,key=len)
#     print(res)
# val(["shifa","safa","shahma","fathimaa"])


# from functools import reduce
# def val(num):
#     res=reduce(lambda x,y:x if x<y else y,num)
#     print(res)
# val([10,202,1,303,303])


# name=["shifa","safa","shahma"]
# age=[10,20,30]
# res=list(zip(name,age))
# print(res)


# def outer():
#     name="shifa"
#     def inner():
#         print(name)
#     return inner
# a=outer()
# a()



# def outer():
#     name="safa"
#     def inner():
#         print(name)
#     return inner
# a=outer()
# a()



# def outer():
#     count=0
#     def inner():
#         nonlocal count
#         count+=1
#         return count
#     return inner
# h1=outer()
# print(h1())


# def val():
#     return "hello"
# print(val)
# print(val())



# def outer():
#    def inner():
#        print("shifa yasmin ")
#    inner()

# outer()



# def decorator(fun):
#     def inner():
#         print("shifa yasmin p")
#         fun()
#         print("safa yasmin p")
#     return inner
# # @decorator
# def outer():
#     print("shahma")
# outer=decorator(outer)
# outer()


# i=1
# while i<=5:
#     print(i)
#     i+=1


# for i in range(1,10):
#     if i==5:
#         break
#     print(i)



# for i  in range(1,9):
#     if i==5:
#         continue
#     print(i)


# for i in range(7):
#     pass
# print("shifa")




# def num(val):
#   res=sorted(val)[::-1]
#   print(res[1])
# num([11,1,22,55,44])



# def num(a,b):
#       res=list(zip(a,b))
#       print(res)
# num([0,22,233],["shifa","safa","shahma"])

# def num(val):
#     val.discard(20)
#     print(val)
# num({10,20,30,40})




# num=[11,22,33]
# print(12 not in num)


# def fun(a):
#     a.add(1999)
#     print(a)
# fun({11,22,33,44})




# students={"name":"shifa","age":10,"place":"koramkode"}
# for index,value in enumerate(students):
#     print(index,":",value)



# name="shifa YASasmin safa"
# print(name.find("Y"))



# def arr(a,b):
#     return a+b
# res=arr(10,20)
# print(res)



# def total(*numbers):
#     print(sum(numbers))

# total(10, 20, 30, 40)

# def details(**data):
#     print(data)

# details(name="Ali", age=20)



# def arr(**val):
#     print(val)
# arr(name="shifa",age=10)



# def ar(**val):
#     for key,value in val.items():
#         print(key,":",value)
# ar(name="safa",age=12,place="koramkode")



# def val(n):
#     if n<=0:
#      return
#     val(n-1)
#     print(n)
# val(9)


# def arr(n):
#     if n==1:
#         return 1
#     else:
#         return n*arr(n-1)
# print(arr(5))



# def val(n):
#     res=lambda x:x*x
#     print(res(n))
# val(5)



# def val(a):
#     res=lambda a: "even"  if a%2==0 else "odd"
#     print(res(a))
# val(10)


# def val(val):
#     res=list(map(lambda x:x*2,val))
#     print(res)
# val([11,2,3,4,5])


# from functools import reduce
# def arr(n):
#     res=reduce(lambda x,y:x+y,n)
#     print(res)
# arr([11,22,30,40])



# from math import sqrt
# def arr(val):
#     res=list(map(sqrt,val))
#     print(res)
# arr([11,22,33,45])



# from math import pow
# def arr(n,m):
#     print(pow(n,m))
# arr(2,5)



# import math
# print(math.factorial(5))

# import random
# def arr(a):
#       random.shuffle(a)
#       print(a)
# arr([11,22,33,44])

# a=100
# print(type(a))
# del a
# print(a)



# def arr(val):
#     print(frozenset(val))
# arr([11,22,33,44])

# a=10
# b=19
# largest=a if a>b else b
# print(largest)




# for i in range(3):
#     print("for",i)
#     j=1
#     while j<3:
#         print("while",j)
#         j+=1



# def arr(val):
#     res={x:x*x for x in val}
#     print(res)
# arr([1,2,3,4,5])


# arr=[1,2,3,4,5]
# res=[x*2 for x in arr]
# print(res)



# def arr(val):
#     res=list(map(x%2==0 for x in val))
#     print(res)
# arr([11,22,33,44])



# def arr(val):
#     res=set(x for x in val)
#     print(res)
# arr([1,2,3,4,6,4,1])




# def arr(**val):
#      print(val)
# arr(name="shiafa",age=20)


# class arr:
#     def val(self):
#         print("shifa yasmin p")
# h1=arr()
# h1.val()



# class val:
#     def __init__(self,name):
#         self.name=name
# h1=val("shifa yasmin")
# print(h1.name)



# class val:
#     @classmethod
#     def name(cls,name):
#         cls.name=name

# val.name("shifa yasmin")
# print(val.name)



# class val:
#     # @staticmethod
#     def name(name):
#         return name
# print(val.name("shifa"))



# class hello:
#     def __init__(self,name):
#         self.name=name
# class sample(hello):
#     def simple(self, age):
#         # super().__init__(name)
#         self.age=age
# h1=sample("shifa")
# h1.simple(19)
# print(h1.name)
# print(h1.age)



# class hello():
#     def __init__(self,age):
#         self.age=age
# class hay(hello):
#     def __init__(self, age,name):
#         super().__init__(age)
#         self.name=name
# h1=hay(13,"shifa")
# print(h1.name)
# print(h1.age)




# class hello():
#     def __init__(self):
#         print("shifa yasmin")
#         super().__init__()
# class hay():
#     def __init__(self):
#         print("safa yasmin p")
#         super().__init__()
# class Him(hello,hay):
#     def __init__(self):
#         super().__init__()
# h1=Him()



# class hello():
#     def __init__(self):
#         print("shifa yasmin")
# class hay(hello):
#     def __init__(self):
#         super().__init__()
#         print("safa yasmin")
# class him(hay):
#     def __init__(self):
#         super().__init__()
#         print("shahma fathima")
# h1=him()


# class hello():
#     def __init__(self):
#        print("shifa yasmin")
# class hay(hello):
#     def __init__(self):
#         super().__init__()
#         print("safa yasmin p")
# class him(hello):
#     def __init__(self):
#         super().__init__()
#         print("shahma")
# h1=him()
# h1=hay()
    

# class hello():
#     def __init__(self,name=None):
#         self.name=name
# class him(hello):
#     def val(self,age,name):
#         self.age=age
#         super().__init__(name)
# h1=him()
# h1.val(19,"shifa")
# print(h1.name)
# print(h1.age)
    

# class hello():
#     def sount(self):
#         print("shifa")
# class hay(hello):
#     def sount(self):
#         print("safa")
#         return super().sount()
# class him(hay):
#     def sount(self):
#         print("shahma")
#         return super().sount()
# h1=him()
# h1.sount()
# h2=hay()
# h2.sount()



# class hello:
#     def sum(self,a,b=0,c=0):
#         return a+b+c
# s=hello()
# print(s.sum(10,20,30))
       



# from abc import ABC,abstractmethod
# class vehicle(ABC):
#     @abstractmethod
#     def hell(self):
#         pass
# class sample(vehicle):
#     def hell(self):
#         print("safa yasmin")
# class simple(sample):
#     def hy(self):
#         print("shahma")
# h1=simple()
# h1.hy()
# h1.hell()
    

    
# class hello():
#     def arr(self,name):
#      self.__name=name
# h1=hello()
# h1.arr("shifa")
# print(h1.__name)

# x="safa yasmin"
# x.split()
# for i in x:
#     print(i, end="")



# class Solution(object):
#     def reverseString(self, s):
#         """
#         :type s: List[str]
#         :rtype: None Do not return anything, modify s in-place instead.
#         """
#         for i in s.reverse():
#             print(i)
    
# reverseString(["h","e","l","l","o"])   
# reverseString(["H","a","n","n","a","h"])  



# def name(s):
#     for i in s[::-1]:
#         print(i,end="")
# name(["s","h","i","f","a"])



# class Solution(object):
#     def gcdOfOddEvenSums(self, n):
        
        
# obj=Solution()
# obj.gcdOfOddEvenSums(4)
# obj.gcdOfOddEvenSums(5)



# class Solution(object):
#     def gcdOfOddEvenSums(self, n):
#         for i in range(1,n+1):
#             if i%2==0:
#              print(i)
        
        
# obj=Solution()
# obj.gcdOfOddEvenSums(4)
# obj.gcdOfOddEvenSums(5)

# class Solution(object):
#     def mergeTwoLists(self, list1, list2):
#         list1.extend(list2)
#         list1.sort()
#         print(list1)
        
# obj=Solution()
# obj.mergeTwoLists([1,2,4],[1,3,4])
# obj.mergeTwoLists([],[])
# obj.mergeTwoLists([],[0])




# number=(10,20,30)
# id=iter(number)
# print(id.__next__())
# print(next(id))
# print(next(id))




# def num(n):
#     n.sort()
#     for i in n[::-1]:
#         res=i
#         print(res,end="-")

#     print("sec is:",res[1])
# num([11,22,55,44,99])


# from functools import reduce
# def num(n,m):
#     res=list(zip(n,m))
#     print(res)
# num([11,22],["shifa","saga"])




# class value:
#     def __init__(self,name):
#         self.name=name
#     def __str__(self):
#         return f"name is:{self.name}"
# obj=value("shifa")
# print(obj)




class student:
    def __init__(self,value):
        self.value=value
    def __add__(self, other):
        return self.value+other.value
n=student(10)
n1=student(20)
print(n+n1)
