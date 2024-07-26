#Program to print Patterns 
for i in range(0, 5):
    for j in range(0, i):
        print("*", end = "")
    print("")
n = 5
for i in range(0, 5):
    for j in range(0, n):
        print("*", end = "")
    print("")
    n-=1

