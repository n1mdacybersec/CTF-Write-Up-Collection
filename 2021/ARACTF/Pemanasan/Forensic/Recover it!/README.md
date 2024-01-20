# Recover it!

## Deskripsi
Pada suatu hari PT. Telkom mendapat kiriman sebuah gambar dengan pesan "Gambar ini sudah dirusak dengan kunci kosong". Bantulah PT. Telkom untuk memecahkan misteri ini.

## Solusi
Dari gambar tersebut dicoba beberapa langkah seperti mengamati strings, metadata dari file gambar menggunakan exiftool namun masih tidak menunjukkan adanya informasi yang penting.
Terdapat sebuah file yang dimasukkan ke dalam file gambar tersebut dan bisa diekstrak menggunakan steghide
``` shell
$ steghide extract -sf sunset.jpg
Enter passphrase: 
wrote extracted data to "steganopayload835646.txt".
$ cat steganopayload835646.txt
Mau cari apa??
2nkerk3malsandmkll

https://drive.google.com/file/d/18g9-KKUeOh_OQoVp8bUanwTGUuJQzuod/view?usp=sh
aring
```

Link tersebut merupakan link untuk mendownload file yang lain, yaitu fin.gif. Setelah didownload file tidak bisa dibuka. Ketika dicek menggunakan exiftool muncul file format error.
``` shell
$ exiftool fin.gif
ExifTool Version Number         : 12.55
File Name                       : fin.gif
Directory                       : .
File Size                       : 29 kB
File Modification Date/Time     : 2023:02:08 22:28:34+07:00
File Access Date/Time           : 2023:02:08 22:33:49+07:00
File Inode Change Date/Time     : 2023:02:08 22:28:36+07:00
File Permissions                : -rw-r--r--
Error                           : File format error
```
Karena terdapat file format error kemungkinan terdapat kerusakan pada file gif tersebut. Cara yang bisa dilakukan adalah dengan mengecek menggunakan perintah xxd
``` shell
$ xxd fin.gif
00000000: 3961 f401 3961 d002 d002 f700 00fb fbfb  9a..9a..........
00000010: 0303 03f2 f2f2 d3d3 d3ea eaea 7b7b 7ba3  ............{{{.
-- output truncated --
```
Pada byte 0 hingga 3 yaitu 39 61 F4 01 terdapat kerusakan yang menyebabkan file gif tidak dikenali. Pada [Wikipedia](https://en.wikipedia.org/wiki/GIF) dan link [berikut](https://www.file-recovery.com/gif-signature-format.htm) dijelaskan nilai apa saja yang harus sesuai untuk byte penting agar gif bisa dikenali.

Karena kerusakan sudah cukup jelas, tinggal diedit menggunakan vim atau xxd sehingga nilai byte 0 hingga 3 seperti berikut ini.
![Recovered GIF format](./recovered_gif.png)

Saat file gif dibuka terdapat pesan yang ditulis menggunakan base64. Decoding menggunakan perintah berikut
``` shell
echo "YXJhMjAyMXtzdDNnNG5vXzFzX3YzcnlfZnVufQ==" | base64 -d
```
Setelah di-decode didapatkan flag yang dicari

## Flag
### ara2021{st3g4no_1s_v3ry_fun}