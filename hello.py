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




# class student:
#     def __init__(self,value):
#         self.value=value
#     def __add__(self, other):
#         return self.value+other.value
# n=student(10)
# n1=student(20)
# print(n+n1)


# try:
#     num=int(input("enter value:"))
#     print(100/num)
# except:
#     print("something wrong")



# class student:
#     def __init__(self):
#         self.__name="shifa"
#     def get_name(self):
#         return self.__name
#     def set_name(self,name):
#         self.__name=name
# obj=student()
# print(obj.get_name())
# obj.set_name("safa")
# print(obj.get_name())



# from abc import ABC,abstractmethod
# class student(ABC):
#     @abstractmethod
#     def __init__(self):
#         pass
# class Hello(student):
#     def __init__(self):
#         print("shifa yasmin")
#     def him(self):
#         print("safayas")
# obj=Hello()
# obj.him()

# a = 10        # int
# b = 5.5       # float
# result = a + b
# print(result)
# print(type(result))




# arr=[11,22,335,55]
# print(frozenset(arr))


# for i in range(1,4):
#     print("for:",i)

#     j=1
#     while j<3:
#         print(j)
#         j+=1



# def num(a,b):
#       res=list(zip(a,b))
#       print(res)
# num([0,22,233],["shifa","safa","shahma","sachu"])



# def val(n):
#   vowels="aeiou"
#   count=0
#   for i in n:
#     if i in vowels:
#       count+=1
      
#   print("count is:",count)

# val("ssshhshhhhhiiiiiiii")




# a={1,2,3,3}
# b={4,5,6}
# a.update(b)
# print(a)




# def val(n):
#     for key,i in n.items():
#         print(key,":",i)
# val({"name":"shifa","age":10,"place":"malapputam"})
    



# def val(n):
#     sqrt=["even" if i%2==0 else "odd" for i in n]
#     print(sqrt)

# val([1,2,3,4,5,6,7])




# def val(n):
#      count=0
#      for i in range(2,n+1):
#           if n%i==0:
#                count+=1

#      if count==1:
#           print("prime")
#      else:
#           print("not prime")
# val(7)


# def val(m):
#     res=str(m)
#     print(res)
#     if res=="".join(reversed(res)):
#         print("pallindom")
#     else:
#         print("not pallindrom") 
# val(123)




# def arr(n):
#     print(max(n))
# arr([11,22,12,66,44])



# def val(n):
#     for i in n:
#         print(i,"*",end="")
# val("shifa yasmin")


# def decorator(func):
#     def name():
#         print("shifa")
#         func()
#         print("safa")
#     return name
# @decorator
# def him():
#     print("shahma")
# him()
\

# def decorator1(fun):
#     def val(num):
#         if num>0:
#             fun(num)
#         else:
#             print("only possitive number")
#     return val
# @decorator1
# def name(num1):
#     print(num1*num1)
# name(5)
# name(-2)


# def values(func):
#     def val(age):
#         if age>18:
#             func("eligble for vote")
#         else:
#             print("not eligible")
#     return val
# @values
# def name(n):
#     print(n)
# name(19)
# name(18)



# def arr(n):
#     n.sort()
#     for i in n[::-1]:
#         print(i)
#     print(n[-2])
    
# arr([11,22,12,8,55])




# class Solution(object):
#     def lengthOfLastWord(self, s):
#         res=s.strip(" ")
#         res1=res.split(" ")
#         print(len(res1[-1]))
# obj=Solution()
# obj.lengthOfLastWord("Hello World")
# obj.lengthOfLastWord("   fly me   to   the moon  ")
# obj.lengthOfLastWord("luffy is still joyboy")






# class hello:
#     @classmethod
#     def val(cls):
#         cls.name="shifa"
#         return cls.name
# obj=hello()
# print(obj.val())


# class hello:
#     @staticmethod
#     def val():
#         print("shifa yasmin p")
# hello.val()



# class hello:
#     def val(self):
#         print("shifa yasmin")
# class sample(hello):
#     def num(self,name):
#         self.name=name
#         return self.name
# obj=sample()
# obj.val()
# print(obj.num("shifa"))




# class hello:
#     def __init__(self):
#         super().__init__()
#         print("Shifa yasmin")
# class hay:
#     def __init__(self):
#         super().__init__()
#         print("safa yasmin")
# class sample(hello,hay):
#       def __init__(self):
#           super().__init__()
#           print("shahma fath")
# obj=sample()




# def val(n,b):
#     n.update(b)
#     print(n)
# val({1,2,3,4},{5,6,7})



# def val(n):
#     res=list(filter(lambda x:x%2==0,n))
#     print(res)
# val([11,22,33,44,55,77])


# def arr(val):
#     res=[x for x in val if x%2==0]
#     print(res)
# arr([1,2,3,4])



# def arr(n):
#     res=n.split()
#     res1=max(res,key=len)
#     print(res1)
# arr("shifa yasmin pp")




# def arr(n):
#     n.sort()
#     # print(n[::-1])
#     print(n[-2])
# arr([11,33,22,55,34])




# class hello:
#     def __init__(self):
#         self._name="shifa"
#     def get_method(self):
#         return self._name
#     def set_method(self,name):
#         self._name=name
# obj=hello()
# print(obj.get_method())
# obj.set_method("safa")
# print(obj.get_method())



# def val(n):
#     largest=n[0]
#     second=n[0]
#     for i in n:
#         if i>largest:
#             second=largest
#             largest=i
#         elif i>second and i!=largest:
#             i=second
#     print("sec :",second)
# val([11,33,22,55,88,88])



# def decorator(func):
#     def val():
#         print("shiifa")
#         func()
#         print("safa")
#     return val
# @decorator
# def name():
#     print("safa yasmin")
# name()




# def val(n):
#     res=[x%2==0 for x in n]
#     print(res)
# val([11,22,34,55])

# class Solution(object):
#     def searchInsert(self, nums, target):
#         if target in nums:
#             return nums.index(target)
# obj=Solution()
# print(obj.searchInsert([1,3,5,6],5))
# print(obj.searchInsert([1,3,5,6],2))
# print(obj.searchInsert([1,3,5,6],4))



# class Solution(object):
#     def merge(self, nums1, m, nums2, n):
#         for i in nums1:
#             if len(m):
#                return i
# obj=Solution()
# print(obj.merge([1,2,3,0,0,0],3,[2,5,6],3))
# print(obj.merge([1],1,[],0))
# print(obj.merge([0],0,[1],1))


# class Solution(object):
#     def sortedSquares(self, nums):
#         a=[int(i**2) for i in nums]
#         a.sort()
#         print(a)
            
# obj=Solution()
# obj.sortedSquares([-4,-1,0,3,10])
# obj.sortedSquares([-7,-3,2,3,11])


# class Solution(object):
#     def sortedSquares(self, nums):
#         a=[int(i**2) for i in nums]
#         print(a.sort())
            
# obj=Solution()
# obj.sortedSquares([-4,-1,0,3,10])
# obj.sortedSquares([-7,-3,2,3,11])
        

# class Solution(object):
#     def isValid(self, s):
#         for i in s:
#             if "()[]{}" in s:
#                  return True
#             else:
#                 return False
# obj=Solution()
# print(obj.isValid("()"))
# print(obj.isValid("()[]{}"))
# print(obj.isValid("(]"))


# class Solution(object):
#     def romanToInt(self, s):
#         obj1 = {
#             "I": 1,
#             "V": 5,
#             "X": 10,
#             "L": 50,
#             "C": 100,
#             "D": 500,
#             "M": 1000
#         }
#         res=0
#         for i in s:
#             res+=obj1[i]
#         return res
# obj=Solution()
# print(obj.romanToInt("III"))
# print(obj.romanToInt("LVIII"))
# print(obj.romanToInt("MCMXCIV"))
        
# arr=[11,33,22,55,23]
# max=arr[0]
# for i in arr:
#     if i>max:
#         max=i
# print(max)


# import bisect

# nums = [5, 12, 18, 25, 40, 55, 70, 99]

# index = bisect.bisect_left(nums, 99)
# bisect.insort(nums,44)

# print(index)
# print(nums)
# print(index)



# a=[1,2,3,4,5]
# b=21,31,54
# a.append(b)
# print(a)



# stack=[10,20,30]
# stack.pop()
# print(stack)

# stack=[]
# stack.append(40)
# stack.append(30)
# stack.append(20)
# stack.append(10)
# print(stack)




# class Solution(object):
#     def isAnagram(self, s, t):
#         if sorted(s)==sorted(t):
#            return True
#         else:
#             return False
# obj=Solution()
# print(obj.isAnagram("anagram","nagaram"))
# print(obj.isAnagram("rat","car"))



# class Solution(object):
#     def addStrings(self, num1, num2):
#         return int(num1)+int(num2)
# obj=Solution()
# print(obj.addStrings("11","123"))
# print(obj.addStrings("456","77"))
# print(obj.addStrings("0","0"))



# class Solution(object):
#     def addStrings(self, num1, num2):
#          res=str(int(num1)+int(num2))
#          return res
# obj=Solution()
# print(obj.addStrings("11","123"))
# print(obj.addStrings("456","77"))
# print(obj.addStrings("0","0"))



# def val(arr,target):
#     for i in range(len(arr)):
#         if arr[i]==target:
#             return i
#     return -1
# print(val([11,33,22,44,66],96))

        
        # dsa







# def val(arr,target):
#     low=0
#     high=len(arr)-1
#     while low<=high:
#           mid=(low+high)//2
#           if arr[mid]==target:
#             return mid
#           elif arr[mid]<target:
#             low=mid+1
#           else:
#             high=mid-1
#     return -1
# arr=[10,20,30,40,50]
# target=40
# result=val(arr,target)
# print(result)



# def val(n):
#     max=n[0]
#     for x in n:
#         if x>max:
#            max=x
#     return max
# print(val([11,22,44,33,12]))



# def arr(val):
#     if len(val)<=1:
#         return val
#     mid=len(val)//2
#     left=arr(val[:mid])
#     right=arr(val[mid:])
#     return sorted(left+right)
# print(arr([2,4,3,7,6,5]))

# class Solution(object):
#     def isPalindrome(self, s):
#         res=""
#         for ch in s:
#             if ch.isalpha():
#                res+=ch
#         if res.lower()==res[::-1].lower():
#             return True
#         else:
#             return False

# obj=Solution()   
# print(obj.isPalindrome("A man, a plan, a canal: Panama")) 
# print(obj.isPalindrome("race a car")) 
# print(obj.isPalindrome(" ")) 





# class Solution(object):
#     def validPalindrome(self, s):
#         for i in s:
#             if i in s:
#                 return True
            
#         return False
# obj=Solution()
# print(obj.validPalindrome("aba"))
# print(obj.validPalindrome("abca"))
# print(obj.validPalindrome("abc"))




# def val(n,m):
#     if m==0:
#         return 1
#     return n*val(n,m-1)
# print(val(2,5))



# def val(n):
#     arr=[]
#     for i in range(n):
#         arr.append(i)
#     return arr
# print(val(5))



# def val(n):
#     for i in str(n)[::-1]:
#         print(i,end="")
# val(123)



# numbers = [1, 2, 3, ..., 1000000]

# print(500000 in numbers)
# numbers = {1, 2, 3, ..., 1000000}

# print(500000 in numbers)



# arr=[11,22,33,44]
# new={}
# for i in arr:
#     new[i]=new.get(i,0)+1
# print(new)


# class Solution(object):
#     def detectCapitalUse(self, word):
#         for i in word:
#             if i.upper():
#                 return True
#             else:
#                 return False
# obj=Solution()
# print(obj.detectCapitalUse("USA"))
# print(obj.detectCapitalUse("FlaG"))

# class Solution(object):
#     def detectCapitalUse(self, word):
#         for i in word:
#             if i.upper():
#                 return True
#             else:
#                 return False
# obj=Solution()
# print(obj.detectCapitalUse("USA"))
# print(obj.detectCapitalUse("FlaG"))



# class Solution(object):
#     def detectCapitalUse(self, word):
#         # for i in word:
#             if word.isupper():
#                 return True
#             else:
#                 return False
# obj=Solution()
# print(obj.detectCapitalUse("USA"))
# print(obj.detectCapitalUse("FlaG"))



# class Solution(object):
#     def detectCapitalUse(self, word):
#         for i in word:
#             if  word.isupper() or word.islower() or word[0].isupper() and word[1:].islower():
#                 return True
#             else:
#                 return False
# obj=Solution()
# print(obj.detectCapitalUse("USA"))
# print(obj.detectCapitalUse("FlaG"))


# class Solution(object):
#     def capitalizeTitle(self, title):
#         return title.split()
# obj=Solution()
# print(obj.capitalizeTitle("capiTalIze tHe titLe"))
# print(obj.capitalizeTitle("First leTTeR of EACH Word"))
# print(obj.capitalizeTitle("i lOve leetcode"))




# class Solution(object):
#     def capitalizeTitle(self, title):
#         res=title.split()
#         for i in res:
#             if len(i)>=3:
#                 return title.title()
#             else:
#                 return title.lower()
# obj=Solution()
# print(obj.capitalizeTitle("capiTalIze tHe titLe"))
# print(obj.capitalizeTitle("First leTTeR of EACH Word"))
# print(obj.capitalizeTitle("i lOve leetcode"))


# class Solution(object):
#     def capitalizeTitle(self, title):
#         res=title.split()
#         for i in res:
#             if len(i)==1 and len(i)==2:
#                 return title.lower()
#             else:
#                 return title.title()
# obj=Solution()
# print(obj.capitalizeTitle("capiTalIze tHe titLe"))
# print(obj.capitalizeTitle("First leTTeR of EACH Word"))
# print(obj.capitalizeTitle("i lOve leetcode"))




# class Solution(object):
#     def capitalizeTitle(self, title):
#         res=title.split()
#         ans=[]
#         for i in res:
#             if len(i)<=2:
#                 ans.append(i.lower())
#             else:
#                 ans.append(i.capitalize())
#         return " ".join(ans)
# obj=Solution()
# print(obj.capitalizeTitle("capiTalIze tHe titLe"))
# print(obj.capitalizeTitle("First leTTeR of EACH Word"))
# print(obj.capitalizeTitle("i lOve leetcode"))




# def arr(val,target):
#     seen={}
#     for i,num in enumerate(val):
#         needed=target-num
#         if needed in seen:
#             return [seen[needed],i]
#         seen[num]=i
# print(arr([2,7,3,2,4,8],9))




# arr=[1,2,3,4,5,6,7,1,2,3,4]
# freq={}
# for num in arr:
#     freq[num]=freq.get(num,0)+1
# print(freq)



# class Solution(object):
#     def getLeastFrequentDigit(self, n):
#         freq={}
        
#         for i in str(n):
#             freq[i]=freq.get(i,0)+1
#         return min(freq,key=lambda x:(freq[x],x))
# obj=Solution()
# print(obj.getLeastFrequentDigit(1553322))
# print(obj.getLeastFrequentDigit(723344511))




# class Solution(object):
#     def getLeastFrequentDigit(self, n):
#         freq={}
#         for i in str(n):
#             freq[i]=freq.get(i,0)+1
#         res= min(freq,key=lambda x:(freq[x],x))
#         return int(res)
# obj=Solution()
# print(obj.getLeastFrequentDigit(1553322))
# print(obj.getLeastFrequentDigit(723344511))



# class Solution(object):
#     def maxFrequencyElements(self, nums):
#         freq={}
#         for i in nums:
#             freq[i]=freq.get(i,0)+1
#         res=max(freq,key=lambda x:(freq(x),x))
#         return res
# obj=Solution()
# print(obj.maxFrequencyElements([1,2,2,3,1,4]))
# print(obj.maxFrequencyElements([1,2,3,4,5]))



# class Solution(object):
#     def maxFrequencyElements(self, nums):
#         freq={}
#         for i in nums:
#             freq[i]=freq.get(i,0)+1
#         return max(freq)
        
# obj=Solution()
# print(obj.maxFrequencyElements([1,2,2,3,1,4]))
# print(obj.maxFrequencyElements([1,2,3,4,5]))


# class Solution(object):
#     def frequencySort(self, nums):
#         freq={}
#         res=[]
#         for i in nums:
#             freq[i]=freq.get(i,0)+1
#             res=freq[i]
#         return sort(res)
# obj=Solution()
# print(obj.frequencySort([1,1,2,2,2,3]))
# print(obj.frequencySort([2,3,1,3,2]))
# print(obj.frequencySort([-1,1,-6,4,5,-6,1,4,1]))


# class Solution(object):
#     def frequencySort(self, nums):
#         freq={}
#         for i in nums:
#             freq[i]=freq.get(i,0)+1
#         return list(sorted(freq))[::-1]
# obj=Solution()
# print(obj.frequencySort([1,1,2,2,2,3]))
# print(obj.frequencySort([2,3,1,3,2]))
# print(obj.frequencySort([-1,1,-6,4,5,-6,1,4,1]))
        


# class Solution(object):
#     def frequencySort(self, nums):
#         freq = {}

#         for i in nums:
#             freq[i] = freq.get(i, 0) + 1

#         result = []

#         for i in freq:
#             result += [i] * freq[i]

#         return result
# obj=Solution()
# print(obj.frequencySort([1,1,2,2,2,3]))
# print(obj.frequencySort([2,3,1,3,2]))
# print(obj.frequencySort([-1,1,-6,4,5,-6,1,4,1]))




# class Solution(object):
#     def mostFrequentEven(self, nums):
#         freq={}
#         for i in nums:
#             freq[i]=freq.get(i,0)+1
#         even=[i for i in freq if i%2==0]
#         if not even:
#             return -1
#         else:
#             return max(freq)
# obj=Solution()
# print(obj.mostFrequentEven([0,1,2,2,4,4,1]))
# print(obj.mostFrequentEven([4,4,4,9,2,4]))
# print(obj.mostFrequentEven([29,47,21,41,13,37,25,7]))




# def val(arr,index,value):
#     arr.append(None)
#     for i in range(len(arr)-1,index,-1):
#         arr[i]=arr[i-1]
#     arr[index]=value
#     return arr
# print(val([10,20,30,40,50],2,24))
        


# def val(arr,index):
#     for i in range(index,len(arr)-1):
#         arr[i]=arr[i+1]
#     arr.pop()
#     return arr     
# print(val([10,20,30,40,50],2))



# def val(arr,value):
#     for i in range(len(arr)-1):
#         return i
# print(val([10,20,30,40,50]))



# arr=[1,2,3,4,5,6,7]
# print(arr[2:4:2])



# def val(a):
#     return name+age
# print(name="Shifa",age=10)



# import copy
# arr=[[10,20,30],[1,2,3,4],[9,8,7]]
# new=copy.deepcopy(arr)
# new[2][1]=100
# print(arr)
# print(new)



# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
# n1 = Node(10)
# n2 = Node(20)
# n3 = Node(30)
# n1.next = n2
# n2.next = n3
# head = n1

# current = head

# while current:
#     print(current.data, end=" → ")
#     current = current.next

# print("None")



# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None
# n1=Node(10)
# n2=Node(20)
# n3=Node(30)
# n1.next=n2
# n2.next=n3
# head=n1
# current=head
# while current:
#     print(current.data,end="=>")
#     current=cur
# rent.next
# print("none")



# class node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None
# head=node(20)
# new=node(10)
# new.next=head
# head=new
# current=head
# while current:
#     print(current.data,end="=>")
#     current=current.next
# print("none")



# class node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None
# head=node(10)
# head.next=node(20)
# head.next.next=node(30)
# new=node(40)
# current=head
# while current.next:
#     current=current.next
# current.next=new
# current=head
# while current:
#     print(current.data,end="=>")
#     current=current.next
# print("null")



# class node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None
# head=node(10)
# head.next=node(20)
# head.next.next=node(30)
# head.next.next.next=node(40)
# new=node(25)
# current=head
# while current.data!=20:
#     current=current.next
# new.next=current.next
# current.next=new
# current=head
# while current:
#     print(current.data,end="=>")
#     current=current.next
# print("null")


# class node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None
#         self.prev=None
# n1=node(10)
# n2=node(20)
# n3=node(30)
# n4=node(40)
# n1.next=n2
# n2.prev=n1

# n2.next=n3
# n3.prev=n2

# n3.next=n4
# n4.prev=n3
# head=n1
# current=head
# while current:
#       print(current.data,end="=>")
#       current=current.next
# print("none")
# tail=n4
# current=tail
# while current:
#      print(current.data,end="<=")
#      current=current.prev
# print("none")



# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.prev = None
#         self.next = None


# class DoublyLinkedList:
#     def __init__(self):
#         self.head = None

#     def insert_beginning(self, data):
#         new_node = Node(data)

#         # If list is not empty
#         if self.head is not None:
#             new_node.next = self.head
#             self.head.prev = new_node

#         # New node becomes head
#         self.head = new_node

#     def display(self):
#         current = self.head

#         while current:
#             print(current.data, end=" ⇄ ")
#             current = current.next

#         print("None")


# dll = DoublyLinkedList()
# dll.insert_beginning(40)
# dll.insert_beginning(30)
# dll.insert_beginning(20)
# dll.insert_beginning(10)
# dll.display()



# stack=[]
# if len(stack)==0:
#    print("empty")


# arr="shifa"
# for i in arr[::-1]:
#     print(i,end="")


# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None


# class Stack:
#     def __init__(self):
#         self.top = None

#     def push(self, data):
#         new_node = Node(data)
#         new_node.next = self.top
#         self.top = new_node

#     def pop(self):
#         if self.top is None:
#             return "Stack is empty"

#         value = self.top.data
#         self.top = self.top.next
#         return value

#     def peek(self):
#         if self.top is None:
#             return "Stack is empty"

#         return self.top.data

#     def is_empty(self):
#         return self.top is None


# stack = Stack()

# stack.push(10)
# stack.push(20)
# stack.push(30)

# print("Top:", stack.peek())
# print("Pop:", stack.pop())
# print("Top:", stack.peek())
# print("Empty:", stack.is_empty())



# class node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None
# class stack:
#     def __init__(self):
#         self.top=None
#     def push(self,data):
#         new=node(data)
#         new.next=self.top
#         self.top=new
# stack=stack()
# stack.push(10)
# stack.push(20)
# stack.push(30)
# print(stack.top.data)




# class node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None
# class stack:
#     def __init__(self):
#         self.top=None
#     def push(self,data):
#         new_node=node(data)
#         new_node.next=self.top
#         self.top=new_node
#     def pop(self):
#         if self.top is None:
#             return "empty data"
#         data=self.top.data
#         self.top=self.top.next
#         return data

# stack=stack()
# stack.push(10)
# stack.push(20)
# stack.push(30)
# print(stack.pop())
# print(stack.top.data)\


# class node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None
# class stack:
#     def __init__(self):
#         self.top=None
#     def push(self,data):
#         new_node=node(data)
#         new_node.next=self.top
#         self.top=new_node
#     def pop(self):
#         if self.top is None:
#             return "empty data"
#         data=self.top.data
#         self.top=self.top.next
#         return data
    
#     def peek(self):
#         if self.top is None:
#             return "empty"
#         return self.top.data
#     def is_empty(self):
#         return self.top is None
# stack=stack()
# stack.push(10)
# stack.push(20)
# stack.push(30)
# print(stack.pop())
# print(stack.top.data)
# print("Top:", stack.peek())
# print("Empty:", stack.is_empty())


# def val(name):
#     stack=[]
#     for i in name:
#         stack.append(i)
#     result=""
#     while stack:
#         result+=stack.pop()
#     return result
# print(val("shifa"))


# def val(name):
#     stack=[]
#     for i in name:
#         stack.append(i)
#     result="" 
#     while stack:
#         result+=stack.pop()
#     return result
# print(val("shifa"))


# def val(s):
#     stack=[]
#     pairs={")":"(","]":"[","}":"{"}
#     for i in s:
#         if i in "({[":
#             stack.append(i)
#         else :
#             if not stack or stack.pop()!=pairs[i]:
#                 return False
#     return len(stack)==0
        
# print(val("[{()}]"))



# from collections import deque

# queue = deque()
# queue.append(10)
# queue.append(20)
# queue.append(30)

# print(queue)






# from collections import deque

# queue = deque()

# queue.append(10)  # Enqueue
# queue.append(20)  # Enqueue
# queue.append(30)  # Enqueue

# print(queue)



# from collections import deque
# queue=deque()
# queue.append(10)
# queue.append(20)
# queue.append(30)
# queue.pop()
# print(queue)


# queue=[]
# queue.append(10)
# queue.append(20)
# queue.append(30)
# print(queue)
# x=queue.pop(0)
# print("remove:",x)
# print(queue)



# def val(n,target):
#     num=[]
#     for i in range(len(n)):
#         if n[i]==target:
#             return i
#     return -1

# print(val([11,33,22,44,56,66],66))


# arr=[11,2,33,4,5,6]
# res=sorted(arr,reverse=True)
# arr.sort(reverse=True)
# print(res)
# print(arr)


# name=["shifa","safa","yasmin"]
# name.sort(key=len)
# print(name)


# address={
#     "name":"shifa",
#     "age":10,
#     "place":"koramkode"
# }
# print(address["name"])
# print(address["age"])


# print(hash("apple"))

# num=[1,2,3,4,5,2,5]
# for i in range(len(num)):
#     for j in range(i+1,len(num)):
#         if num[i]==num[j]:
#            print("dublicate",num[i])



def val(n):
    seen=set()
    for i in n:
        if i in seen:
            return True
        seen.add(i)
    return False
        
print(val([1,2,3,4,5]))