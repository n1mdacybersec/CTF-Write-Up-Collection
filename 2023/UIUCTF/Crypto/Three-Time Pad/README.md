# Three-Time Pad

## Deskripsi
We've been monitoring our adversaries' communication channels, but they encrypt their data with XOR one-time pads! However, we hear rumors that they're reusing the pads...

Enclosed are three encrypted messages. Our mole overheard the plaintext of message 2. Given this information, can you break the enemy's encryption and get the plaintext of the other messages?

## Attachments
[c1](./Challenge/c1) [c2](./Challenge/c2) [c3](./Challenge/c3) [p2](./Challenge/p2)

## Solusi
Challenge kali ini merupakan penerapan dari one-time pads encryption, dimana enkripsi menggunakan one-time pads akan menggunakan operasi XOR untuk mengenkripsi plain text dengan key.
Yang perlu diketahui dari one-time pads sendiri adalah plain text yang telah dienkripsi tidak akan bisa dikembalikan ke plain text jika tidak mengetahui key yang digunakan untuk mengenkripsi. Namun key ini hanya bisa digunakan sekali, oleh karena itu dinamakan dengan one-time pads.

Pada challenge ini kita diberikan 4 buah file, yaitu file c1, c2, dan c3 yang merupakan teks yang telah dienkripsi dan p2 adalah plain text dari c2.
Seperti yang disebutkan sebelumnya bahwa one-time pads sangat aman selama key hanya digunakan sekali, namun pada challenge ini kita tidak memiliki key yang digunakan untuk mengenkripsi pesan.
Untuk mendapatkan key yang digunakan untuk mengenkripsi c2 kita bisa melakukan XOR c2 dengan p2, karena hal ini berkaitan dengan salah satu sifat dari operasi XOR itu sendiri.

```
(A ^ B) ^ A = (A ^ A) ^ B
            = 0 ^ B
            = B
```

Dari contoh persamaan di atas, anggaplah A adalah plain text dan B adalah key. Operasi XOR sendiri mempunyai sifat yang mirip dengan sifat asosiatif pada aritmatika. Kemudian jika A di XOR dengan A maka hasilnya adalah 0, sehingga kita bisa mendapatkan key yang digunakan untuk mengenkripsi plain text A.

Source code yang digunakan untuk menyelesaikan challenge ini seperti berikut.

```python
import binascii

def xor(s1,s2):
	key = bytes([a ^ b for a, b in zip(s1,s2)])
	return key

if __name__=="__main__":
	c1 = "14f5f95b4a252948a8aef177d6c92d82e3016362bd7463f41f40a00ad9e0ccad911b959ef8dfad5f1cc4481ecb64"
	c2 = "06e2f65a4c256d0ba8ada164cecd329cae436069f83476e91757e91bd4a4cce2c60a8f9aac8cb14210d55253cd787c0f6a"
	c3 = "03f9ea574c267249b2b1ef5d91cd3c99904a3f75873871e94157df0fcbb5d1eab94f9386"
	p2 = "printed on flammable material so that spies could"
	
	c1 = binascii.unhexlify(c1)
	c2 = binascii.unhexlify(c2)
	c3 = binascii.unhexlify(c3)
	p2 = p2.encode('utf-8')
	
	# Obtain the key of c2 by XOR-ing c2 with p2
	key = xor(c2,p2)
	print("Key value: ", key)
	
	# Try to decrypt c1 and c3 using the key
	p1 = xor(c1,key)
	p3 = xor(c3,key)
	
	p1 = p1.decode('utf-8')
	p3 = p3.decode('utf-8')
	print("Decrypted p1: ", p1)
	print("Decrypted p3: ", p3)
```

## Flag
### uiuctf{burn_3ach_k3y_aft3r_us1ng_1t}