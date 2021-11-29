#1

#2
a=5**9
print(a)

a=3//2
print(a)

a=7//3
print(a)

a=7/3
print(a)

a=6==6
print(a)

a=20
a+=30
a%=3
print(a)

print(True*False)

print(True & False)

print(True and False)

print(((6>3) and (7<4) or (18==3)) and (9>3))

print(True is False)

print(False in 'False')

print(((True == False) or (False > True)) and (False <= True))

#3 
s1="Nice to have it"
s2="here"
print(s1,s2)

#4
a = [1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]
print(a[3][1][2][0])

#5
a.insert(0,s1)
a.append(s2)
print(a)

#6
no = [386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 
953, 345, 399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 
687, 217, 815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 
742, 717, 958,743, 527]
for i in no:
    if(i%2==0):
     print(i) 
    elif i<700:
     break

#7
color_list_1 = set(["White", "Black", "Red"]) 
color_list_2 = set(["Red", "Green"])
print(color_list_1-color_list_2)

#8 
def pangram(str):
    alpha = 'abcdefghijklmopqrstuvwxyz'
    for i in alpha:
        if i not in str:
            return False
    return True
    
a= "the quick brown fox jumps over a lazy dog"
if(pangram(a)==True):
    print("yes")
else:
    print("no")
  
#9
n=(input('enter the no.:'))
n1=n*2
n2=n*3
n3=n
print(int(n3)+int(n1)+int(n2))

#10
string1=eval(input("Enter string in the given fashion"))     # 23 54 12#98 3 17
string1=string1.strip()
string1+=" "
num=""
x=[]
y=[]
flag=0
for i in string1:
    if(i!=" "):
        if(i!="#"):
            num+=i
        else:
            flag=1
            x.append(int(num))
            num=""
    
    else:
        if(flag==0):
            x.append(int(num))
            num=""
        else:
            y.append(int(num))
            num=""
print(x)
print(y)

#11
string2=(input("enter the words"))
string2=string2.strip()
string2+=","
word=""
l=[]
for i in string2:
    if(i!=","):
        word+=i
    else:
        l.append(word)
        word=""
l.sort()
print(l)

#12
d={'Student' : ['Rahul','Kishore','Vidhya','Raakhi'],'Marks' : [57,87,67,79]}
max=0
k=-1
for i in d['Marks']:
    k+=1
    if(max<i):
        max=i
        p=k
print(d['Student'][p])

#13
string = input("Enter the string")
string = list(string)
alpha = list('abcdefghijklmnopqrstuvwxyz')
num = list('0123456789')
i=0
j=0
for word in string:
    if(word in alpha):
        i+=1
    elif(word in num):
        j+=1
print(f'LETTERS {i}')
print(f'DIGITS {j}')

#14
d={'Name':['Akash','Soniya','Vishakha','Akshay','Rahul','Vikas'],
   'Subject':['Python','Java','Python','C','Python','Java'],
   'Ratings':[8.4,7.8,8,9,8.2,5.6]}
inp=input("enter subject name")
idx=-1
pos=[]
for i in d['Subject']:
    idx+=1
    if(inp==i):
        pos.append(idx)
newData={'Name':[],'Subject':[],'Ratings':[]}
for i in pos:
    newData['Name'].append(d['Name'][i])
    newData['Subject'].append(d['Subject'][i])
    newData['Ratings'].append(d['Ratings'][i])
    
print(newData)

#15
                              
#16
x=0
y=0
while(True):
    string4=(input("enter the instructions"))
    if (string4 == ""):
        break
    else:
        string4=string4.split(' ')
        if string4[0]=="UP":
            y+=int(string4[1])
        elif string4[0]=="DOWN":
            y-=int(string4[1])
        elif string4[0]=="RIGHT":
            x+=int(string4[1])
        elif string4[0]=="LEFT":
            x-=int(string4[1])
dist=(((x**2)+(y**2))**(1/2))
print('DISTANCE:',int(dist))

