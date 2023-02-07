# Koki Yang Handal

## Deskripsi
Spongebob adalah seorang koki yang setiap hari membalikkan daging diatas panggangan. Kemudian dari daging tersebut ia susun sebanyak 3 tumpukan didalam roti yaitu tumpukan ke-1 selada, selanjutnya daging, dan keju. Suatu ketika restoran tempat ia bekerja kekurangan ke tiga bahan tersebut. Bantu spongebob untuk mencari ketiga bahan kemudian susun sesuai tumpukan dan lakukan pemanggangan.

## Solusi
Jika melihat deskripsi soal terdapat 3 bagian (selada, daging, dan keju) untuk flag yang dicari. Karena file yang diberikan merupakan file png, dilakukan pengecekan menggunakan exiftool.
``` shell
$ exiftool Spongebob.png
ExifTool Version Number         : 12.55
File Name                       : Spongebob.png
Directory                       : .
File Size                       : 495 kB
File Modification Date/Time     : 2023:02:07 23:50:25+07:00
File Access Date/Time           : 2023:02:07 23:53:22+07:00
File Inode Change Date/Time     : 2023:02:07 23:50:35+07:00
File Permissions                : -rw-r--r--
File Type                       : PNG
File Type Extension             : png
MIME Type                       : image/png
Image Width                     : 1080
Image Height                    : 608
Bit Depth                       : 8
Color Type                      : RGB
Compression                     : Deflate/Inflate
Filter                          : Adaptive
Interlace                       : Noninterlaced
Comment                         : Keju: 0xzQl9CaVRTfQ==
Image Size                      : 1080x608
Megapixels                      : 0.657
```
Terdapat comment section yang menunjukkan bagian terakhir flag, yaitu `Keju: 0xzQl9CaVRTfQ==`

Langkah berikutnya adalah mencari bagian flag yang lain, dengan cara mencari file yang disembunyikan pada file png tersebut. Untuk itu digunakan tool stegosuite. Stegosuite meminta sebuah secret yang digunakan untuk mengekstrak file tersebut. Secret yang dimaksud bisa saja berasal dari 3 bagian/bahan dari, dimana secret yang dimaksud adalah `Daging`.
![Searching for embedded file using stegosuite](./stegosuite.png)

Hasilnya didapatkan sebuah file flag.
``` shell
$ cat flag
Daging: fRmxhZ19EYXJpX
```

Bagian terakhir dari flag didapatkan dengan memainkan beberapa filter yang biasanya digunakan untuk menyembunyikan suatu teks pada gambar dalam soal forensic atau steganography. Disini digunakan tool stegsolve. Hasilnya terdapat sebuah teks saat mengaplikasikan Green plane 1 pada stegsolve, yaitu `Selada: YXJhMjAyMXtJbml`.

<img alt="Applied Green plane 1 using stegsolve" src="./stegsolve.png" width="600">

Setelah mendapatkan seluruh bagian flag, flag disusun sesuai urutan, yaitu selada, daging, kemudian keju. Sehingga menjadi `YXJhMjAyMXtJbmlfRmxhZ19EYXJpX0xzQl9CaVRTfQ==`. Format flag masih di-encode menggunakan base64, decode menggunakan perintah berikut
``` shell
echo "YXJhMjAyMXtJbmlfRmxhZ19EYXJpX0xzQl9CaVRTfQ==" | base64 -d
```
## Flag
### ara2021{Ini_Flag_Dari_LsB_BiTS}