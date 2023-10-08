# plai_n_rsa

## Description
I've dropped the "n" ... where is my "n" :(

## Attachment
[dist.tar.gz](./Challenge/dist.tar.gz)

## Solution
First let's see the source code of this challenge

```python
import os

from Crypto.Util.number import bytes_to_long, getPrime

flag = os.getenvb(b"FLAG", b"SECCON{THIS_IS_FAKE}")
assert flag.startswith(b"SECCON{")
m = bytes_to_long(flag)
e = 0x10001
p = getPrime(1024)
q = getPrime(1024)
n = p * q
e = 65537
phi = (p-1)*(q-1)
d = pow(e, -1, phi)
hint = p+q
c = pow(m,e,n)

print(f"e={e}")
print(f"d={d}")
print(f"hint={hint}")
print(f"c={c}")
```

From the code, we know the value of `e`, `d`, `c`, and `p + q` or in this case the value is in variable `hint`.
How to decrypt the ciphertext if we don't know the value of `n`?
Because in RSA you can decrypt the ciphertext using $`c^d\bmod{n}`$ . 

From this [link](https://crypto.stackexchange.com/questions/91402/given-e-and-d-find-phin) we can proceed to find `phi(n)` because we already know the value of `e`, `d`, and `p + q`.
We can find the possible candidate of `phi(n)` by bruteforcing `k`, where $`1\leq{k}<{e}`$ .
Then from this [link](https://crypto.stackexchange.com/questions/5791/why-is-it-important-that-phin-is-kept-a-secret-in-rsa) we can find the possible `n` values from `phi(n)`.

This is the source to solve this challenge.

```python
from Crypto.Util.number import long_to_bytes

e = 65537
d = 15353693384417089838724462548624665131984541847837698089157240133474013117762978616666693401860905655963327632448623455383380954863892476195097282728814827543900228088193570410336161860174277615946002137912428944732371746227020712674976297289176836843640091584337495338101474604288961147324379580088173382908779460843227208627086880126290639711592345543346940221730622306467346257744243136122427524303881976859137700891744052274657401050973668524557242083584193692826433940069148960314888969312277717419260452255851900683129483765765679159138030020213831221144899328188412603141096814132194067023700444075607645059793
c = 8886475661097818039066941589615421186081120873494216719709365309402150643930242604194319283606485508450705024002429584410440203415990175581398430415621156767275792997271367757163480361466096219943197979148150607711332505026324163525477415452796059295609690271141521528116799770835194738989305897474856228866459232100638048610347607923061496926398910241473920007677045790186229028825033878826280815810993961703594770572708574523213733640930273501406675234173813473008872562157659306181281292203417508382016007143058555525203094236927290804729068748715105735023514403359232769760857994195163746288848235503985114734813
hint = 275283221549738046345918168846641811313380618998221352140350570432714307281165805636851656302966169945585002477544100664479545771828799856955454062819317543203364336967894150765237798162853443692451109345096413650403488959887587524671632723079836454946011490118632739774018505384238035279207770245283729785148 # p+q

# References from https://crypto.stackexchange.com/questions/91402/given-e-and-d-find-phin
# https://crypto.stackexchange.com/questions/5791/why-is-it-important-that-phin-is-kept-a-secret-in-rsa

for k in range(1, e):
    if (d*e - 1) % k != 0:
        continue
    canditate_phi = (d*e - 1) // k

    # phi(n) = (p-1)(q-1) = pq - (p+q) + 1 = (n+1) - (p+q)
    n = canditate_phi + hint - 1
    m = long_to_bytes(pow(c,d,n))
    if b'SECCON{' in m:
        print(f"k = {k}")
        print(m.decode('utf-8'))
        break
```

## Flag
`SECCON{thank_you_for_finding_my_n!!!_GOOD_LUCK_IN_SECCON_CTF}`


