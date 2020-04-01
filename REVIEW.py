'''


def fact(n):
    if n==1:
        return 1
    return n*fact(n-1)
print(fact(3))

def power(x,n=2):
    s=1
    while n>0:
        s=s*x
        n = n - 1  # n只起到决定决定循环次数的作用
    return s   #why the result will be different if the place if return change
print(power(5))

def greet(name='world'):
    print('hello',name)
print(greet())
print(greet('bob'))

def fn(*args):
    print(args)
print('b')
print('a', 'b', 'd')
print()



def average(*args):
    if len(args)!=0:
        return sum(args)*1.0/len(args)  #为了显示出小数，需要乘以一个浮点数
    else:
        return 0.0

print (average(1))
print(average(1,2))
print(average(1,1))    #DIFFERENT FROM I PRESUME


L=(1,4,5)
SUM=0
for x in L:
    SUM=SUM+x
print(SUM)

L=['ada','lisa','bart','paul']
print(L[::2])

M=list(range(0,101))
print(M)
print(M[1:10])
print(M[::3])
print(M[:50:5])
print(M[-10:])
print(M[-46::5])

'abc'.upper()

#def firstcharupper(s):
   # 's'.upper('s'[:1])
   # return 's'
#print(firstcharupper('hello'))# 待修改

L=list(range(1,101))
for i in L:
  if  i % 7==0:
        print(i)

d={'a','b','c'}
for key in d:
    print(key)
for i, key in enumerate(['a','b','c']):
    print(i,key)

L=['a','b','c','d']
M=[1,2,3,4]
print(zip(M,L))

def format_name(s):

    return s.capitalize()

list (map(format_name, ['adam', 'LISA', 'barT']))

sum=0
n=1
while n<100:
    sum=sum+n
    n=n+2
print(sum)


#a=input("a=")
#b=input("b=")
#print("before excahnge:",a,b)
#c=b
#b=a
#a=c
#print("after excahnge:",a,b)

print("560MINS=",560//60,"H", 560%60,"min")
print(560//60,560%60)


for x in range(1,10):
 for y in range(1,10):
    print("%d*%d=%d" %(x,y,x*y))




i = int(raw_input('净利润:'))
arr = [100,60,40,20,10,0]
rat = [0.01,0.015,0.03,0.05,0.075,0.1]
r = 0
for idx in range(0,6):
    if i > arr[idx]:
        r += (i - arr[idx]) * rat[idx]
        print((i - arr[idx]) * rat[idx])
        i = arr[idx]

print(r)


M = []
for i in range(2, 101):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
          M.append(i)

print(M)

from pip._vendor.distlib.compat import raw_input

L=[]
a=int(raw_input("please enter a number:"))
if a==1:
    print(a)
else:
    for i in M[:]:
        if a%i==0:
            L.append(i)
            a/=i
print(L)


import time

from pip._vendor.distlib.compat import raw_input

T=time.time()
print(T)

I=time.localtime()
print(I)

A=time.strftime("%Y-%m-%d,%H:%M:%S",time.localtime())
print(A)


import datetime
print(datetime.date.today())
print(datetime.date(1978,4,5))


import re


#正则式
zero=raw_input("Please enter your sentence:")
dig=0
char=0
space=0
other=0
for i in range(len(zero)):
    if re.match('\d',zero[i]):
        dig+=1
    elif  re.match('[a-zA-Z]',zero[i]):
        char+=1
    elif re.match('\s',zero[i]):
        space+=1
    else:
        other+=1


print("dig is%d,char is%d,space is%d,other is%d" %(dig,char,space,other))




a=input("name=")
b= input("state=")
print("Dont play with %s, he is %s" %(a,b))




my_name='Z MOI'
print(f"Let's talk to {my_name}.")


age=18
weight=90
height=160
total=age+weight+height
print(f"If add yulu's {age},{weight},{height}, you can get her little'{total}'")

a="no"
b="Isn't that joke so funny!"
print(b+a)

print("!"*10)

print("Jan\nFed\nMar\nApr\nMay")

age=input('How old are you:')
weight=input('How much do you weight:')
height=input('How tall are you:')

print(f"So you are {age} old,{height}cm tall and {weight}kg heavy")


weeklist={'M':'Monday','T':{'u':'Tuesday','h':'Thursday'},'W':'Wednesday','F':'Friday','S':{'a':'Saturday','u':'Sunday'}}
letter1=input("Please enter the first letter:")
letter1=letter1.upper()
if letter1 in ['T','S']:
    letter2=input('Please enter the second letter:')
    print(weeklist[letter1][letter2])
else:
    print(weeklist[letter1])

print(weeklist['M'])


a=['1','2','3']
a.reverse()
print(a)


l=[1,2,3,4,5]
print(l)

str='-'
seq=('I','will','love','you')
print(str.join(seq))

b=('I','am','angry')
c="!"
f=c.join(b)
print(f)


import time
def greet():
    print('Good morning,motherfucker')
    time.sleep(2)

def three_greet():
    for i in range(3):
          greet()

three_greet()

from pip._vendor.distlib.compat import raw_input

lower=int(raw_input('Please enter:'))
upper=int(raw_input('Please enter'))
for num in range(lower,upper+1):
    if num>1:

        for i in range(2,num):
            if num%i==0:
                break
        else:print(num)

from pip._vendor.distlib.compat import raw_input


a=[]
for n in range(10):
    a.append(int(raw_input('Please enter 10 numbers:')))
    a.sort()
print(a)


matrix=[[1,2,3],[4,5,6],[7,8,9]]
print(matrix)
sum=0
for i in range(0,3):
    sum=sum+matrix[i][i]
print(sum)

from pip._vendor.distlib.compat import raw_input

x=[1,3,5,6,88,121]
y=int(raw_input('Please enter a number:'))
x.append(y)
x.sort()
print(x)
print(x[::-1])



def auto():
    num=2
    print('internal block num=%d'%num)

    for i in range(3):
     print('The num=%d'%num)
     num=num+2
auto()




import numpy as np
from pip._vendor.distlib.compat import raw_input

x=np.array([[12,7,3],
           [4,5,6],
           [7,8,9] ])
y=np.array([[5,8,1],
           [6,7,3],
           [4,5,9] ])
z=x+y
print(z)

sum=0
for i in range(1,101):
    sum=sum+i
print('the total is %d'%sum)

a=int(raw_input('please enter a number:'))
b=a**2
if b<50:
    quit
else:
    print(b)



script=argv
print('1st',script)


from sys import argv
scrpit,user_name=argv
promot='>'
print(f'I am the {scrpit}script')



def exchange(a,b):
    a,b=b,a
    return(a,b)
if __name__ == '__main__':
    x=10
    y=20
    print('x=%d,y=%d' % (x, y))
    x,y=exchange(x,y)
    print('x=%d,y=%d' % (x, y))


i=10
j=20
if i>j:
    print('a')
elif i==j:
    print('b')
elif i<j:
    print('c')
else:
    print('un')


def compare(num1, num2):
  if num1 > num2:
            print("%s大于%s" % (num1, num2))
  elif num2 > num1:
            print("%s大于%s" % (num2, num1))
  else:
            print("%s等于%s" % (num1, num2))



numOne = input("请输入第一个数字:")
numTwo = input("请输入第二个数字:")
compare(numOne, numTwo)


MAXIMUM = lambda x, y: (x > y) * x + (x < y) * y
MINIMUM = lambda x, y: (x > y) * y + (x < y) * x

if __name__ == '__main__':
    a = 10
    b = 20
    print('The largar one is %d' % MAXIMUM(a, b))
    print('The lower one is %d' % MINIMUM(a, b))



x=5
y=4
print((x > y) * x + (x < y) * y)


S=lambda x,y:x+y
print(S(4,6))


import random
print(random.random())  #0--1

print(random.uniform(10,20))#10--20
print(random.randint(10,20))#intergar 10-20
print(random.choice([x for x in range(1,50)]))






k = 1
j = 1
for i in range(0, 26):
    canvas.create_oval(310 - k, 250 - k, 310 + k, 250 + k, width=100)
    k += j
    j += 0.3

    mainloop()



if __name__ == '__main__':
 from tkinter import*
root=Tk()
root.title('HELOO')#设置标题

a=Canvas(root,width=700,height=900,bg="blue")
a.pack(expand=YES,fill=BOTH)
k = 1
j = 1
for i in range(0, 26):
  a.create_oval(310 - k, 250 - k, 310 + k, 250 + k, width=100)
  k =k+j
  j =j+0.3

mainloop()


from tkinter import*
a=Tk()
a.title('Harder')
b=Canvas(a,width=300,height=300,bg='green')
b.pack(expand=YES,fill=BOTH)
x0=263
y0=263
y1=275
x1=275
for i in range(19):
    b.create_line(x0,y0,x0,y1,width=1,fill='red')
    x0=x0-5
    y0=y0-5
    x1=x1+5
    y1=y1+5

mainloop()


a=input('enter a word:')
print(f'the length of the word is',len(a))


num=10
list1=[]
for i in range(1,num+1):
    list2=[]
    print()
    for j in range(1,i+1):
        if j==1:
            list2.append(1)
        elif i==j:
            list2.insert(j-1,1)
        else :
            list2.insert(j-1,list1[j-2]+list1[j-1])
        for k in range(0,len(list2)):
            print(list2[k])
            list1=list2



num = 10
list2 = []
for i in range(1,num+1):
    for j in range(1,i+1):
        if j == 1:
            list2.append(i)
        elif i == j:
            list2.insert(j - 1, 1)
        else:
            list2.append(10)
print(list2)


num = 10
list1 = []
for i in range(1,num+1):
    list2 = []
    print()
    for j in range(1,i+1):
        if j == 1:
            list2.append(1)
        elif i == j:
            list2.insert(j - 1, 1)
        else:
            list2.insert(j - 1, list1[j - 2] + list1[j - 1])
    for k in range(0,len(list2)):
        print(list2[k])
    list1 = list2


a=s=[1]
for i in range(0,10):
    for j in range(i+1):
        if j==0 or i==j:
            s.append(1)
            break
        else:
            s.append(10)
            a,s=s,[]

print(a)

'''


import numpy as np
a=np.array([1,2,3,4,5,6])
print(a)
x=np.random.randint(1,100,10)
print(x)
x = x.reshape((len(x),1))

print(x)

b=np.random.randn(2,3)
print(b)


import copy
m=[1,2,3,4,['a','b']]
print(m)
n=m
print(n)
w=copy.copy(m)
print(w)
d=copy.deepcopy(m)
print(d)
m.append(5)
print(d)

name = 'Lizz'
print(name[0:2])

import time
d={1:'Matt',2:'is',3:'useless'}
for value in dict.items(d):
    print(value)
    time.sleep(2)



import calendar
cal=calendar.month(2019,11)
print(cal)

import time
time=time.time()
print(time) #时间戳

import time
now=time.localtime(time.time())
print(now)

import time
print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime()))

time.sleep(1)
print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime()))





L= []
for x in range(101,201):
    for y in range(2,x):
        if x%y==0:
          break
    else:    #为什么变化后影响这么大呢

                 L.append(x)


print(L)
print('Total amount is: %d' %len(L))


for x in range(1,10):
    for y in range(0,10):
        for z in range(0,10):
            m=100*x+10*y+z
            n=x**3+y**3+z**3
            if m==n:
              print(n)


from pip._vendor.distlib.compat import raw_input

a=int(raw_input('Please enter the number:'))
b=int(raw_input('Please enter the time:'))
c=1
sum=0
while b>=1:
    num=a*b*c
    c=c*10
    b=b-1
    sum=sum+num

print(sum)



L=[]
for i in range(1,1001):
    sum=0
    for j in range(1,i):
      if i%j==0:
            sum=sum+j
            L.append(j)
    if sum==i:
              print(i,L)



a=100
b=10
sum=0
while b>=0:
    sum = sum + a
    a=0.5*a
    sum= sum+a
    b=b-1

print(sum,a)


a=1
b=10
while b>1:
    a=(a+1)*2
    b=b-1
print(a)


n=['a','b','c']
m=[]
for i in range(3):
    if n[i]!='a' and n[i]!='c':
        m.insert(i,'x')  #第二位insert（第二位插X）
    elif n[i]!='c':
        m.insert(i,'z')
    else:
        m.insert(i,'y')

        print(m)

        print('a--%s,b--%s,c--%s'%(m[0],m[1],m[2]))


L= []
for x in range(101,201):
    for y in range(2,x):
        if x%y==0:
          break

    else:
                 L.append(x)
print(L)



for i in range(1,5):
    print(' '*(4-i),end="")
    for j in range(1,2*i):
        print('*',end="") #line 132,133没怎么看懂 print里也没用到J啊
    print()
for i in range(3,0,-1):
    print(' '*(4-i),end="")
    for j in range(1,2*i):
        print('*',end="")
    print()


a=2
b=1
s=0
for n in range(1,21):
    s=s+a/b
    t=a
    a=a+b
    b=t
print(s)


def fact(n):
    if n==1:
        return 1
    else:
        return n*fact(n-1)
s=0
for n in range(1,21):
    s=s+fact(n)

print(s)


for i in range(1,5):
    print(' '*(4-i),end="")
    print('*'*(2*i-1),end="") #line 132,133没怎么看懂 print里也没用到J啊
    print()
for i in range(3,0,-1):
    print(' '*(4-i),end="")
    for j in range(1,2*i):
        print('*',end="")
    print()









a=10
b=2
for i in range(1,5):
    a=a+b
print(a)

from pip._vendor.distlib.compat import raw_input


S=input('Input a string:')
L=list(S)
L.reverse()
for i in range(len(L)):
    print(L[i])


num=list(input('Plaese enter a number:'))
print(len(num))
num.reverse()
for i in range(len(num)):
    print(num[i])


a=list(input('Please enter a number:'))
b=a[::-1]
if a==b:
    print('%s is round'%a)
else:
    print('%s is not round'%a)





new=[]
number=[1,2,3,4,5]
for i in number:
    print(f'Addling {i} to the list:')
    new.append(i)
print(new)
for r in new:
    print(f'this {r} is in the new list')




from tkinter import*
new=Tk()
new.title('NIKI LOL')
a=Canvas(new,width=400,height=400,bg='blue')
x0=200
y0=100
x1=100
y1=100

a.create_rectangle(x0,y0,x1,y1)

a.pack()
mainloop()



from tkinter import*
new=Tk()
new.title('NIKI LOL')
a=Canvas(new,width=400,height=400,bg='blue')
x0=100
y0=100
x1=100
y1=100
for i in range(19):
    a.create_rectangle(x0,y0,x1,y1)
    x0-=5
    y0-=5
    x1+=5
    y1+=5
a.pack()
new.mainloop()


import pandas as pd
import numpy as np

df=pd.DataFrame([[1.4,np.nan],[7.1,-4.5],[np.nan,np.nan],[0.75,-1.3]],
                index=list('abcd'),
                columns=['one','two'])
print(df)

print(df.sum())

print(df.sum(axis=1))

print(df.iloc[0][1])

print(df.mean(axis=1,skipna=False))

print(df.idxmax())

print(df.cumsum())

print(df.describe())

obj=pd.Series(['a','a','b','c']*4)
print(obj.describe())

print(obj.unique())

print(obj.value_counts())

mask=obj.isin(['b','c'])
print(mask)

print(obj[mask])


data=pd.Series([1,np.nan,3.5,np.nan,7])

print(data)


print(data.dropna())

data=pd.DataFrame([[1.,6.5,3.],[1.,np.nan,np.nan],
               [np.nan,np.nan,np.nan],[np.nan,6.5,3.]])

print(data)

clean=data.dropna()
print(clean)

print(data.dropna(how='all'))

data[4]=np.nan
print(data)

print(data.dropna(axis=1,how='all'))

df=pd.DataFrame(np.random.randn(7,3))
df.loc[:4,1]=np.nan
df.loc[:2,2]=np.nan
print(df)

print(df.dropna())

print(df.dropna(thresh=2))

print(df.fillna(0))

df.fillna({1:0.5,2:0},inplace=True)
print(df)


df=pd.DataFrame(np.random.randn(6,3))

df.iloc[2:,1]=np.nan
df.iloc[4:,2]=np.nan

print(df)

print(df.fillna(method='ffill'))



df.fillna(method='ffill',limit=2,inplace=True)

print(df)

data=pd.Series([1.,np.nan,3.5,np.nan,7])
data.fillna(data.mean(),inplace=True)
print(data)

data=pd.DataFrame({'k1':['one','two']*3+['two'],
                   'k2':[1,1,2,3,3,4,4]})

print(data)

print(data.duplicated())

print(data.drop_duplicates())

data['v1']=np.arange(7)
print(data)

print(data.drop_duplicates(['k1']))

data=pd.DataFrame({'food':['bacon','pulled pork','bacon','Pastrami','corned beef','Bacon','Pastrami','honey ham','nova lox'],
                   'ounces':[4,3,12,6,7.5,8,3,5,6]})

meat_to_animal={
    'bacon':"pig",
'pulled pork': 'pig',
'pastrami':'cow',
'corned beef':'cow',
'honey ham':'pig',
'nova lox':'salmon'}

lowercased=data['food'].str.lower()
print(lowercased)
data['animal']=lowercased.map(meat_to_animal)

print(data)

data=pd.Series([1,-999,2,-999,-1000,3])
data.replace(-999,np.nan,inplace=True)

print(data)

data.replace([-999,-1000],[np.nan,0],inplace=True)

print(data)

data=pd.DataFrame(np.arange(12).reshape((3,4)),
                  index=['Ohio','Colorado','New York'],
                  columns=['one','two','three','four'])

transform=lambda x: x[:4].upper()
data.index=data.index.map(transform)

print(data)

data.rename(index=str.title,columns=str.upper,inplace=True)
print(data)

data.rename(index={'Ohio':'ID'},
            columns={'THREE':'peekaboo'},inplace=True)

print(data)

ages=[20,22,25,27,21,23,37,31,61,45,41,32]
bins=[18,25,35,60,100]
group_names=['Youth','YoungAdult','MiddleAged','Senior']
cats=pd.cut(ages,bins,labels=group_names)
f=pd.value_counts(cats)
print(f)

data=np.random.randn(1000)
cats=pd.qcut(data,4)
print(cats)

f=pd.value_counts(cats)
print(f)


data=pd.DataFrame(np.random.randn(1000,4))

print(data.describe())

cal=data[2]

print(cal[np.abs(cal)>3])

print(data[(np.abs(data)>3).any(1)])

print(np.sign(data).head())

data[np.abs(data)>3]=np.sign(data)*3

print(data.describe())

df=pd.DataFrame(np.arange(5*4).reshape((5,4)))

sampler=np.random.permutation(5)

print(sampler)

print(df.take(sampler))

print(df.sample(3))

choices=pd.Series([5,7,-1,6,4])

draws=choices.sample(n=10,replace=True)

print(draws)

import pandas as pd
df=pd.DataFrame([
    ['green','A'],
    ['red','B'],
    ['blue','A']],
    columns=['color','class']
)

print(df)

df=pd.get_dummies(df)

print(df)

df=pd.DataFrame({'key':['b','b','a','c','a','b'],
                 'data1':range(6)})
print(df)


df=pd.get_dummies(df['key'],prefix='key')

print(df)

mnames=['movie_id','title','genres']

moives=pd.read_table('datasets/movielens/movies.dat',sep="::",header=None,names=mnames)


import re

lst=re.findall('\d','123qwe456asd')
print(lst)
ist=re.findall('\D','123qwe456a@@sd')
print(ist)

lst=re.findall('\w',"d&*()qh321>wi")
print(lst)
ist=re.findall('\W',"d&*()qh321>wi")
print(ist)

a=re.match(r'[Hh][eE]llo','HEllo world').group()
print(a)

a=re.match(r'speed\d','speed9').group()
print(a)

a=re.match(r'speed[1-37-9]','speed8').group()
print(a)

a=re.match(r'speed[1-8a-dA-D]','speedA').group()
print(a)

a=re.match(r"\d{8}","12345678901").group()  #只匹配8位
print(a)

a=re.match(r"021-?\d{5}","021-12345678901").group()  #? 字符前面的东西，可有1个可没有
print(a)


names = ['name1', 'name2', 'name3_', '_name4', '2_name5', '_name!']

for name in names:
    ret = re.match(r"[a-zA-Z_]+[\w]", name)  # 如果不用+号，就成了匹配前2位字符
    # 或者 ret = re.match(r"[a-zA-Z_][\w]*" , name) #与上面是等价的
    if ret:  # 当ret有值得时候，就执行if
        print("变量名 %s 符合要求，正则表达式匹配出来的数据是：%s " % (name, ret.group()))
    else:  # 当ret没有值得时候，就执行else
        print("变量名 %s 非法。" % name)


names=['name1','name2','name3_','_name4','2_name5','_name!']

for name in names:
    ret=re.match(r'[a-zA-Z_][\w]*$',name)  # 在后面加一个 $ 符号，就代表着前面的正则匹配结束的时候，列表中的字符串也要同时匹配完，如果不加$这个符号
    if ret:
        print('yes %s'%name)
    else:
        print('no %s'%name)

#字符 {m,n}  匹配前一个字符出现从m到n位，如果{1,12}，只出现1次至12位，即至少1位，至多12次  邮箱地址至少M位 至多N位

'''
a=input('please enter your address:')
ret=re.match(r"([a-zA-Z0-9_]{4,20})@(163|139|qq).com$",a)
if ret:
    print('yes %s' %(ret.group(1)))
else:
    print('no%s' %a)
'''

ret = re.match(r"([a-zA-Z0-9_]{4,20})@(163|139|QQ)\.com$", "1654653@QQ.com").group(1)
print(ret)
#如果想提取 @ 前面的数据，只要加上()圆括号就可以了，圆括号里面的参数代表坐标，1个坐标就是第一个圆括号的数据，2就是第二个圆括号的数据，坐标如果超出了范围，就会报错


#匹配一行文字的所有开头字母内容

s="i love you not because !!!! of who you are, but because of who i am when i am with you"
content=re.findall(r"\b\w",s)
print(content)


s="i love you not because 12sd 34er 56df e4 54434"
number=re.findall(r"\b\d",s)
print(number)

s="'bat', 'bit', 'but', 'hat', 'hit', 'hut"
content=re.findall(r'[a-z][a-z]t',s)
print(content)

#a.*?b匹配最短的，以a开始，以b结束的字符串。如果把它应用于aabab的话，它会匹配aab和ab。 惰性匹配
#表达式 .* 的意思很好理解，就是单个字符匹配任意次，即贪婪匹配。
#表达式 .*? 是满足条件的情况只匹配一次，即懒惰匹配\

#提取完整的年月日和时间
s="""se234 1987-02-09 07:30:00

    1987-02-10 07:25:00"""

content=re.findall(r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}",s,re.M)
print(content)


s="""693152032@qq.com, werksdf@163.com, sdf@sina.com

    sfjsdf@139.com, soifsdfj@134.com

    pwoeir423@123.com"""

content=re.sub(r"\w+@\w+.com","yulupi@163.com ",s,re.M)
print(s)
print(content)
