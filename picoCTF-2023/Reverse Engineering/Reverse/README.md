# Reverse

## Deskripsi
Try reversing this file? Can ya?
I forgot the password to this [file](https://artifacts.picoctf.net/c/276/ret). Please find it for me?

## Solusi
Diberikan suatu file [exe](Challenge/ret) dan kita diberikan instruksi untuk melakukan reverse pada file ini. Kita bisa menggunakan command `strings` sebagai langkah awal untuk mengecek apakah terdapat `direct flag` yang terdapat pada file tersebut.

Ketika kita menggunakan command `strings`, ternyata benar kita dapat langsung menemukan flagnya.
![Result](result.png)

## Flag
### picoCTF{3lf_r3v3r5ing_succe55ful_9ae85289}
