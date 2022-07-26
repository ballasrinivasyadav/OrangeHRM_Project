greeting = "Good Morning"
a = 4
if a>2:
    print("Condition Matches")
    print("Second Line")
else:
    print("If else condition code is completed")

    ### For Loop

obj = [1,2,5,7,9]
for i in obj:
    print(i*2)

####Sum of first natural numbers 1+2+3+4+5 = 15
# range(i,j) >> i to j-1
print("***********************************")
sum = 1
for j in range(1,6):  #2+3+4+5+6
    sum = sum+j
print(sum)

print("***********************************")
for k in range(1,10,2):
    print(k)
    print("********************SKIPPINNG FIRST INDEX*******")

for m in range(10):
    print(m)