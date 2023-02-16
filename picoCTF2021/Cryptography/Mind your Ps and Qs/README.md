# Mind your Ps and Qs

## Deskripsi
In RSA, a small e value can be problematic, but what about N? Can you decrypt this? [values](https://mercury.picoctf.net/static/38f30029ab93478310e906d3d084a4c1/values)

## Hint
Bits are expensive, I used only a little bit over 100 to save money

## Solusi
File values berisi seperti berikut ini
```
Decrypt my super sick RSA:
c: 240986837130071017759137533082982207147971245672412893755780400885108149004760496
n: 831416828080417866340504968188990032810316193533653516022175784399720141076262857
e: 65537
```
Pada algoritma RSA nilai `c` adalah teks yang telah di enkripsi, nilai `n` adalah perkalian antara dua bilangan prima, yaitu `n = p*q`. 
Nilai `e` adalah bilangan yang lebih besar dari 1 dan lebih kecil dari `phi` dan bilangan tersebut koprima dengan `phi`.
Nilai `d` digunakan sebagai private key dan didapatkan dari perkalian invers `e` dengan `mod(phi)`. Variable `m` adalah pesan yang telah didekripsi, dengan persamaan `c^d mod n

Untuk lebih jelasnya ada pada operasi berikut
```
c = ciphertext
n = p * q ; dimana p dan q bilangan prima
phi = (p-1)*(q-1)
e = bilangan antara 2 < e < phi dan memenuhi syarat FPB(e,phi) == 1
d = e^(-1) mod(phi)
m = c^d mod (n)
```

Pada [Wikipedia](https://en.wikipedia.org/wiki/RSA_(cryptosystem)) dijelaskan lebih detail mengenai algoritma RSA.
Untuk mendapatkan nilai `p` dan `q` dapat menggunakan [Factordb](http://factordb.com/index.php) karena Factordb memiliki database untuk bilangan faktorisasi.
Dari hasil Factordb didapatkan nilai
```
p = 1593021310640923782355996681284584012117
q = 521911930824021492581321351826927897005221
```

Karena nilai `p` dan `q` kita bisa mendapatkan pesan yang didekripsi dengan program Python berikut
``` python
from Crypto.Util.number import inverse, long_to_bytes

c = 240986837130071017759137533082982207147971245672412893755780400885108149004760496
n = 831416828080417866340504968188990032810316193533653516022175784399720141076262857
p = 1593021310640923782355996681284584012117
q = 521911930824021492581321351826927897005221
e = 65537

phi = (p-1)*(q-1)

d = inverse(e, phi)
m = pow(c,d,n)

print(long_to_bytes(m))
```

## Flag
picoCTF{sma11_N_n0_g0od_23540368}



