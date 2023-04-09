# cocomilk

## Deskripsi
Qiqi adalah seorang zombie yang sering pelupa. Suatu hari ia membuat kodingan dalam bahasa C++ untuk membuat kode rahasia lokasi cocomilk. Namun beberapa saat kemudian dia lupa menulis kodingan tersebut dalam bahasa C++ dan menuliskannya dalam bahasa Python. Qiqi yang kebingungan mencoba menginputkan lokasi cocomilk tersebut dengan menjalankan kodingannya dalam bahasa C++ dan Python. Anehnya, kodingannya dapat berjalan dan menghasilkan Output 1 pada bahasa C++ dan Output 2 pada bahasa Python. Beberapa saat kemudian, Qiqi melupakan lokasi rahasia cocomilk yang barusan diinputkan. Bantu Qiqi untuk mendapatkan lokasi rahasia cocomilk miliknya!

## Solusi
Diberikan sebuah file zip yang berisi 2 file output berupa txt dan satu program dalam bahasa C++. Pada deskripsi soal telah disebutkan bahwa terdapat program yang ditulis menggunakan C++ dan Python dalam satu program. Program tersebut dituliskan dalam bahasa C++ namun pada bagian yang di comment terdapat program yang dituliskan menggunakan bahasa Python.

![Program terdiri bahasa C++ dan Python](./1.png)

Program yang ditulis menggunakan bahasa C++ seperti berikut ini
``` cpp
#include <iostream>
#include <string>
#include <bits/stdc++.h> 
using namespace std;
string z(string a);
string y(string b);

string z(string a) {
	string b = "";
	for (int i = 0; i < a.length(); i+=2) {
		b += a[i];
	}
	return y(b);
}

string y(string b) {
	string a = "";
	for (int i = 0;i < b.length(); i++) {
		a+=b[i]^i;
	}
	reverse(a.begin(), a.end());
	return a;
}

int main() {
	string a;
	cout<<"Input: ";
	cin>>a;
	cout << z(a) << endl;
	return 0;
}
```
Program tersebut akan membaca input dari user sebagai string (a). Kemudian mengambil index genap dari string (a) dan disimpan sebagai string (b) yang kemudian akan di XOR menggunakan integer mulai dari 0 sampai panjangnya (b).

Lalu untuk program yang ditulis menggunakan Python
``` python
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
```
Untuk program Python sendiri akan membaca input dari user sebagai string (a). Dari string tersebut diambil index ganjil dan direverse disimpan sebagai string (c) dan index genap yang disimpan sebagai string (b). Setiap index dari (c) akan di XOR dengan index mulai dari 0 sampai panjangnya (c) yang kemudian di XOR lagi dengan tiap index dari (b). Hasil akhirnya akan diformat menjadi hex

Langkah penyelesaiannya adalah:
1. Membaca file `Output 1.txt` 
2. Kemudian di XOR dan mereverse setiap karakter.
3. Membaca file `Output 2.txt`
4. Mengubah karakter hex menjadi ASCII
5. XOR setiap karakter dari `Output 1.txt` dengan index mulai dari 0 sampai panjangnya seluruh karakter dari hasil XOR dan reverse `Output 1.txt`. Kemudian XOR lagi dengan seluruh index dari karakter ASCII `Output 2.txt`
6. Reverse karakter dari hasil step 5.
7. Menggabungkan seluruh string

Penyelesaian menggunakan program Python berikut
``` python
part1 = open("Output 1.txt").read()
part1 = part1[::-1]

message1 = "".join([chr(ord(part1[i])^i) for i in range(len(part1))])

part2 = open("Output 2.txt").read().split(":")

output2 = "".join([chr(int(i, 16)) for i in part2])

message2 = ""
b = message1

for y, z in enumerate(b):
        message2 += chr(ord(z)^y^ord(output2[y]))
message2 = message2[::-1]

flag = ""

for x in range(len(message1)):
        flag += message1[x]
        flag += message2[x]

print(flag)
```

## Flag
### ara2021{C0com1lk_IS_Coc0g04t_M!lK}