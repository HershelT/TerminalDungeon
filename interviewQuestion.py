strings = "69tyry"
newInt = 0 
for num in strings:
    for x in range(0, 10):
        if str(x) == num:
            newInt = newInt*10 + x
print(type(newInt))
print(newInt)


