#!/usr/bin/python3
################################################################################
# for iteration
################################################################################
# dictionary of countries and capitals
d = {
    "Beglium":"Brussels",
    "Great-Brittain":"London",
    "France":"Paris",
    "Spain":"Madrid"
}

print("List of capitals:")
print("="*30)
for v in d.values():
   print(v)

################################################################################
# triangle pattern
n = 5

for i in range(n):
   #print(i,end=" ")
   print(" ")
   for j in range(i):
      print("*", end=" ")
for i in range(n,0,-1):
   print(" ")
   for j in range(i):
      print("*", end=" ")
print("\n")


    
