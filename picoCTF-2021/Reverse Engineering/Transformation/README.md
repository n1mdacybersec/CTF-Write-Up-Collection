# Transformation

## Deskripsi
I wonder what this really is... [enc](https://mercury.picoctf.net/static/0d3145dafdc4fbcf01891912eb6c0968/enc)
```
''.join([chr((ord(flag[i]) << 8) + ord(flag[i + 1])) for i in range(0, len(flag), 2)])
```

## Hint
You may find some decoders online

## Solusi
Sebuah file binary atau executable yang jika dijalankan akan menghasilkan `灩捯䍔䙻ㄶ形楴獟楮獴㌴摟潦弸弲㘶㠴挲ぽ`. Begitu pula jika menggunakan `cat enc`.
Jika dilihat berdasarkan source code yang diberikan pada soal, maka program akan:
- Menggeser 8 bit ke kiri dari tiap elemen dari list flag
- Kemudian tiap elemen flag ditambahkan dengan nilai flag + 1
- Operasi tersebut dilakukan berulang sampai sebanyak panjangnya flag dengan nilai iterasi 2
- Hasil operasi tersebut akan menghasilkan sebuah string baru

Dari penjelasan di atas, bisa dilakukan reverse untuk proses dari program tersebut dengan program Python berikut
``` python
file = open("enc").read()

flag = ""
for i in range(0, len(file)):
    c1 = chr((ord(file[i]) >> 8))
    c2 = chr(file[i].encode('utf-16be')[-1])
    flag += c1+c2

print(flag)
```
Program di atas akan melakukan perulangan yang menjalankan proses:
- Menggeser 8 bit (1 byte) ke kanan untuk pasangan karakter pertama
- Mengkonversi karakter ke byte kemudian byte terakhir di encode menggunakan UTF-16BE untuk mendapatkan pasangan karakter kedua
- Menambahkan nilai c1 dan c2 ke flag

## Flag
### picoCTF{16_bits_inst34d_of_8_26684c20}
