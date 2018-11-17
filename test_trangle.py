#!/usr/bin/env python3.5

n=5

# North East Arrow
#for i in range(0,n):
#	for j in range(0,n):
#		if (i+j == n-1) :
#			print("*", end=" ")
#		elif (((j == n-2) and (i == 0)) or ((j == n-1) and (i == 1))):
#			print("*", end=" ")
#		else:
#			print("  ", end="")
#	print("")
#
## South West Arrow
#for i in range(0,n):
#	for j in range(0,n):
#		if (i+j == n-1) :
#			print("*", end=" ")
#		elif (((i == n-2) and (j == 0)) or ((i == n-1) and (j == 1))):
#			print("*", end=" ")
#		else:
#			print("  ", end="")
#	print("")
#
#
## North West Arrow
#for i in range(0,n):
#	for j in range(0,n):
#		if (i == j) :
#			print("*", end=" ")
#		elif (((i == 1) and (j == 0)) or ((i == 0) and (j == 1))):
#			print("*", end=" ")
#		else:
#			print("  ", end="")
#	print("")
#
## South East Arrow
#for i in range(0,n):
#	for j in range(0,n):
#		if (i == j) :
#			print("*", end=" ")
#		elif (((i == n-1) and (j == n-2)) or ((i == n-2) and (j == n-1))):
#			print("*", end=" ")
#		else:
#			print("  ", end="")
#	print("")

# South North Arrow
for i in range(0,n):
       for j in range(0,n):
		print("j is",int(j/2))
#               if (int(j / 2) == 2) :
#                       print("*", end=" ")
#               elif (((i == n-1) and (j == n-2)) or ((i == n-2) and (j == n-1))):
#                       print("*", end=" ")
               else:
                       print("  ", end="")
       print("")

