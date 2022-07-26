i = 10
while i > 2:
    if i == 5:
         continue
    if i == 3:
        break
    print(i)
    i = i-1
print("While loop execution is done")


i = 11
while i > 4:
    i = i-1
    if i == 3:
        continue
    print(i)