L=[]
n=int(input("Enter No. of numbers:"''))
print('Enter',n,'numbers into the list:-')
i=0
while i<n:
    x=int(input())
    L.append(x)
    i=i+1
    for j in range(n+1):
        if j%2!=0:
            print(j)
