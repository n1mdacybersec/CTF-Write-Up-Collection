# L0v32x0r

## Deskripsi
Vonny and Zee were having a treasure hunt game until they realized that one of the clues was a not alike the other clues as it has a random text written on the clue.

The clue was "001300737173723a70321e3971331e352975351e247574387e3c".

Help them to find what the hidden clue means!

## Solusi
Clue yang diberikan berupa karakter hex yang kemungkinan sudah di xor dengan ukuran 1 byte. Seperti yang kita tahu bahwa 1 hex bernilai 4 bit, sehingga 2 hex akan bernilai 8 bit atau 1 byte. Jika dilihat clue yang diberikan memiliki panjang 52 bit, itu artinya jika kita bagi panjangnya dengan 2 akan ada 26 karakter dengan panjang 2 bit. Solusi dari permasalahan ini adalah dengan program Python berikut.

```python
def xor(hex_a, hex_b):
	return hex(int(hex_a, 16) ^ int(hex_b, 16))[2:]

def xor_count(cipher, key):
	hex_key = ''
	result = ''
	for i in range(0, round(len(cipher)/2), 1):
    	hex_key += hex(ord(key[i % len(key)]))[2:]
	cipher_xor = xor(cipher, hex_key)
	for j in range(0, len(cipher_xor)-1, 2):
    	result += chr(int(cipher_xor[j]+cipher_xor[j+1], 16))
	return result

def main():
	cipher = '001300737173723a70321e3971331e352975351e247574387e3c'
	key = 'A'
	print(xor_count(cipher, key))

if __name__ == '__main__':
	main()
```

### Solusi Alternatif
Selain dengan menggunakan program Python di atas, dapat juga digunakan program Python berikut ini untuk melakukan bruteforce flag terhadap 1 byte XOR.

``` python
cipher = '001300737173723a70321e3971331e352975351e247574387e3c'
cipher = bytes.fromhex(cipher).decode('utf-8')

for i in range(0x00,0xff):
    result = ''
    for j in cipher:
        result += chr(i^ord(j))
    if 'ARA2023{' in result:
        print('flag :', result)
```

## Flag
### ARA2023{1s_x0r_th4t_e45y?}
