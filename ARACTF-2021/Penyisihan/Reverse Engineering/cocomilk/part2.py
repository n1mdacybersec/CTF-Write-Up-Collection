a = input("Input: ")
b = ""
c = ""

for x, y in enumerate(a):
    if x % 2 == 0:
    	b += y
    else :
        c += y

c = c[::-1]
d = ""

for y,z in enumerate(c):
    d += chr(ord(z)^y^ord(b[y]))

print(":".join("{:02x}".format(ord(c)) for c in d))
