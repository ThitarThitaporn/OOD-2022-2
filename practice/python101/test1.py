a = 10
b = 10.5
c = 'a'

#print(type(a))
#print(a.__doc__)
'''print(type(b))
print(type(c))
print(ord(c)) #Ascii of charecter
print(f'var c {c} = ascii {ord(c)}') '''

'''
if a is b :
    print('a')
elif b > c :
    print('b')
else :
    print('c')

while True:
    print()
'''
ls = "kmitl 2566"

'''
for i in ls:
    print(i)
'''

'''
n = len(ls)
i = 0
while i< n :
    print(ls[i])
    i+=1

i = 0
while i < len(ls):
    print(ls[i])
    i+=1


for i in reversed(ls) :
    print(i)
'''
'''
n = len(ls)
i = n-1
while i >= 0:
    print(ls[i])
    i -= 1

# out of range คือ การเรียกนอกเหนือจากlist เลยทำให้เกิด error
print(ls[-1])
print(len(ls))

'''
#หาตำแหน่งของข้อมูลที่ต้องการ ว่าอยู่ตำแหน่งไหน

'''

count = 0
for i in ls:
    if i == target:
        print(count)
    count += 1
'''
i =0
target = '5'
while i < len(ls) :
    if ls[i] == target:
        print("while = ",i)
    i += 1