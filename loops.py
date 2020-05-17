# if statements
greeting1 = "good morning"
greeting2 = "good MORNINg"
greeting2 = greeting2.lower()
if greeting1 == greeting2:
    print("Condition matches")
    print("second line")
else:
    print("condition does not match")
print("if else condition code is complete")
print("************************************************")
print("test")

# for loop
obj = [2, 3, 16, 7, 56]
for element in obj:
    if element%2 == 0:
        print(element)
print("************************************************")
print("test")

# sum of First Natural numbers 1+2+3+4+5
# range(i, j) -> i to j-1
count = 0
for value in range(1, 6):
    count = count + value
print(count)
print("************************************************")
print("test")

# this means start from 1 and go up to, but not including, 10 and increment by 3
for k in range(1, 10, 3):
    print(k)
print("************************************************")
print("test")

# this means to start from 0 and go up to, but not including, 10
for m in range(10):
    print(m)
print("test")