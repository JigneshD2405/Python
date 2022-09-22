'''
files1=open('python.txt','r')
ans=files1.readlines()
print(ans)
files1.close()


with open('python.txt','r') as file1:
    ans = file1.read()
    print(ans)


file=open('python.txt','w')
ans=file.write('Hey')
print(ans)
file.close()

file=open('python.txt','r')
result=file.read()
print(result)
file.close()


with open('python.txt','w') as file:
    ans=file.write('Hello')
    print(ans)
    file.close()


with open('python.txt','a') as file:
    ans=file.write(' I am learning Python')
    print(ans)
    file.close()

with open('python.txt','r') as file:
    ans=file.read()
    print(ans)
    file.close()


file=open('python.txt','r+')
write=file.write('welcome')
print(write)
file.close()

file=open('python.txt','r+')
read=file.read()
print(read)
file.close()
'''

