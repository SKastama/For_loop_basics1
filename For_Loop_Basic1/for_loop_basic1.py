print("Question 1")
for i in range(0, 150):
    print(i)


print("")
print("Question 2")
for i in range(5, 1000, 5):
    print(i)


print("")
print("Question 3")
for i in range(1, 100):
    if i%10 == 0:
        print("Coding Dojo")
    elif i%5 == 0:
        print("Coding")
    else:
        print(i)

print("")
print("Question 4")
sum = 0
for i in range(0, 500000):
    if i%2 != 0:
        sum+= i
print(sum)

print("")
print("Question 5")
sum= 0
for i in range(2018, 0, -4):
    print(i)

print("")
print("Question 6")
def flexible_counter(lowNum, highNum, mult):
    for i in range(lowNum, highNum + 1):
        if i%mult == 0:
            print(i)
print(flexible_counter(2, 9, 3))
