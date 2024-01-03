n = int(input())
members = []

for i in range(n):
    age, name = input().split()
    members.append((int(age), name, i))
    
members.sort(key=lambda x: (x[0], x[2]))

for i in range(n):
    print(f"{members[i][0]} {members[i][1]}")