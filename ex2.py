import random
a = input()
length = len(a)
b = random.randint(1, length)
new_a = ''
new_aa = ''
for i in range(b):
    new_a += random.choice(a)
print(new_a)
for i in range(2, length, 3):
    new_aa += a[i]
print(new_aa)
