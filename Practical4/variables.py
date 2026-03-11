a = 5.08
b = 5.33
c = 5.55

# claculate the difference between b and a, and c and b
d = b - a
e = c - b

print(d, e)

# compare d and e, and print which one is larger
if d > e:
    print("d is larger than e, the population growth is decelerating")
elif d < e:
    print("e is larger than d, the population growth is accelerating")
else:
    print("d and e are equal, the population growth is constant")

# the population growth is decelerating 

X = True
Y = False

W = X or Y
print(f"W is {W}")

# Truth table for X or Y

# Or
# | X | Y | X or Y |
# |---|---|--------|
# | True | True | True |
# | True | False | True |
# | False | True | True |
# | False | False | False |