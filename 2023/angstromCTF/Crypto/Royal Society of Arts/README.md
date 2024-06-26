# Royal Society of Arts

## Deskripsi
RSA strikes strikes strikes strikes again again again again!

[rsa.py](./Challenge/rsa.py) [output](./Challenge/output.txt)

## Points
70

## Solusi
Program yang diberikan seperti berikut ini

```python
from Crypto.Util.number import getStrongPrime, bytes_to_long
f = open("flag.txt").read()
m = bytes_to_long(f.encode())
p = getStrongPrime(512)
q = getStrongPrime(512)
n = p*q
e = 65537
c = pow(m,e,n)
print("n =",n)
print("e =",e)
print("c =",c)
print("(p-2)*(q-1) =", (p-2)*(q-1))
print("(p-1)*(q-2) =", (p-1)*(q-2))
```

Dari hasil program tersebut diketahui nilai `c` (teks terenkripsi), `n` (perkalian 2 bilangan prima besar p dan q), dan `e` sebagai bagian dari public key. Selain itu juga diketahui nilai `(p-2)*(q-1)` dan `(p-1)*(q-2)`.

Mungkin langkah ini sedikit unintended, tetapi ketika nilai `n` dicari nilai faktorisasinya, yaitu `p` dan `q` menggunakan [factordb](http://factordb.com/) didapatkan faktorisasinya. 
Sehingga dibuat program python berikut ini untuk langsung melakukan decrypt pesan yang telah dienkripsi

```python
from Crypto.Util.number import inverse, long_to_bytes

n = 125152237161980107859596658891851084232065907177682165993300073587653109353529564397637482758441209445085460664497151026134819384539887509146955251284230158509195522123739130077725744091649212709410268449632822394998403777113982287135909401792915941770405800840172214125677106752311001755849804716850482011237
c = 40544832072726879770661606103417010618988078158535064967318135325645800905492733782556836821807067038917156891878646364780739241157067824416245546374568847937204678288252116089080688173934638564031950544806463980467254757125934359394683198190255474629179266277601987023393543376811412693043039558487983367289
e = 65537
p = 10066608627787074136474825702134891213485892488338118768309318431767076602486802139831042195689782446036335353380696670398366251621025771896701757102780451
q = 12432413118408092556922180864578909882548688341838757808040464238372914542545091804094841981170595006563808958609560634333378522509950041851974318809712087

phi = (p-1)*(q-1)

d = inverse(e, phi)
m = pow(c,d,n)

print(long_to_bytes(m))
```

## Flag
### actf{tw0_equ4ti0ns_in_tw0_unkn0wns_d62507431b7e7087}