# rsa

## Deskripsi
I think I did my RSA right...

## Attachments
[flag.enc](./Challenge/flag.enc) [public.pem](./Challenge/public.pem) [private.pem](./Challenge/private.pem)

## Solusi
Pada challenge ini merupakan challenge cryptography menggunakan RSA. Seperti yang kita tahu bahwa RSA merupakan jenis asymmetric encryption, yang artinya terdapat public key yang digunakan untuk mengenkripsi pesan dan private key untuk mendekripsi pesan yang sudah terenkripsi.

Karena pada challenge ini kita sudah mendapatkan private key yang digunakan untuk mendekripsi flag, maka kita hanya perlu membaca nilai `n` dan `d` dari private key. Berdasarkan [Wikipedia](https://en.wikipedia.org/wiki/RSA_(cryptosystem)) untuk mendekripsi pesan kita bisa menggunakan persamaan berikut.

```
m = c ** d mod (n)
```
Berdasarkan persamaan tersebut `m` adalah plaintext dari pesan yang telah dienkripsi, `c` adalah ciphertext atau pesan yang telah dienkripsi, `d` adalah private key exponent dan `n` adalah bilangan dari hasil perkalian bilangan prima `p` dan `q` dan `n` adalah public key exponent yang digunakan untuk mengenkripsi pesan.

Digunakan program Python berikut ini untuk mendekripsi flag.enc.

```py
from Crypto.PublicKey import RSA
from Crypto.Util.number import long_to_bytes, bytes_to_long, inverse

k = open("private.pem", "rb").read()
private_key = RSA.importKey(k)
n = private_key.n
d = private_key.d

c = open("flag.enc", "rb").read()
c = bytes_to_long(c)

m = pow(c,d,n)
m = long_to_bytes(m)

print("Flag: ", m.decode('utf-8'))
```

## Flag
### ictf{keep_your_private_keys_private}