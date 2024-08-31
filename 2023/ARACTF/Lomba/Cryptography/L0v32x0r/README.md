# L0v32x0r

## Description
Vonny and Zee were having a treasure hunt game until they realized that one of the clues was a not alike the other clues as it has a random text written on the clue.

The clue was "001300737173723a70321e3971331e352975351e247574387e3c".

Help them to find what the hidden clue means!

## Solution
The `clue` is a hex character that has probably been XOR with a size of 1 byte. As we know that 1 hex character is worth 4 bits, so 2 hex characters will be worth 8 bits or 1 byte. If you look at the `clue`, it has a length of 52 bits, that means if we divide the length by 2 there will be 26 characters with a length of 2 bits. The solution to this problem is in this Python program.

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

### Alternate
In addition to using the Python program above, you can also use the following Python program to bruteforce the flag against 1 byte XOR.

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
`ARA2023{1s_x0r_th4t_e45y?}`
