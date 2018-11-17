#!/usr/bin/python3.5

print ("Let Triangle")
for i in range(0, 5):
    for j in range(0, i+1):
        print("* ",end="")
    print()

print ("Ulta Left Triangle")
for i in range(5,0,-1):
    for j in range(0,i):
            print ("* ", end="")
    print (" ")

print ("Right Trangle approch 1")
k = 8
for i in range(0, 5):
    for j in range(0, k):
        print(end=" ")
    k = k - 2
    for j in range(0, i+1):
        print("* ", end="")
    print()

print ("Right Trangle approch 2")
n=6
for i in range(0,n-1):
        for j in range(1,n):
                if i+j >= n-1:
                        print("*", end=" ")
                else:
                        print("  ", end="")
        print("")


print ("Ulta Right Trangle approch 2")
for i in range(0,n-1):
        for j in range(n-1,0,-1):
                if i+j <= n-1:
                        print("*", end=" ")
                else:
                        print("  ", end="")
        print(" ")

