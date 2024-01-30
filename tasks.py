z="aabc"
f=[]
for i in range(len(z) - 1):
    for j in range(i + 1, len(z) + 1):
        d= z[i:j]
        
        f.append(d)
print("f is :",f)
output=f is : ['a', 'aa', 'aab', 'aabc', 'a', 'ab', 'abc', 'b', 'bc']
2
class calculator:
    def __init__(self,a,b):
        self.firstnumber=a
        self.secondnumber=b
class four(calculator):
    def add(self):
        print("the adition of:",self.firstnumber+self.secondnumber)
        
    def sub(self):
        print("the subraction of:",self.firstnumber-self.secondnumber)

    def mul(self):
        print("the multiplication of:",self.firstnumber*self.secondnumber)

    def div(self):
        print("the division of:",self.firstnumber+self.secondnumber)
class two (four):
    def mod(self):
        print("the module of:",self.firstnumber%self.secondnumber)
    
    def sq(self):
        print("the squreroot of:",self.firstnumber**self.secondnumber)
x1=two(15,5)
x1.sub()
output=subraction of : 10
3
a=5
for i in range (a):
    for j in range(i):
        print("*",end=" ")
    print()
output=
* 
* * 
* * * 
* * * * 
4
n=[1,1,1,3,3,6,6,7,8,8,8,8]
g={}
for i in n:
    if i not in g:
        g[i]=1
    else:
        g[i]+=1
print(g)
output={1: 3, 3: 2, 6: 2, 7: 1, 8: 4}
5
a=[1,2,3,4,5]
b=[]
c=sum(a)

for i in a:
    if i%5==0:
        pass
    else:
        b.append(c-i)
print(b)
maxi=b[0]
mini=b[0]
for i in b:
    if i>maxi:
        maxi=i
    elif i<mini:
        mini=i
print('the maximum value is',maxi)
print('the minimum value is',mini)
output=[14, 13, 12, 11]
the maximum value is 14
the minimum value is 11

