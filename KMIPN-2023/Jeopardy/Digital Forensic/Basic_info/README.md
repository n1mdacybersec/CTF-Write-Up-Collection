# Basic_info

## Deskripsi
Temukan Flag di dalam gambar ini..

`flag=KMIPN{flag2:md5 file}`

## Attachment
[KMIPN23.png](./Challenge/KMIPN23.png)

## Solusi
Langkah pertama adalah dengan mengecek gambar tersebut menggunakan exiftool

```bash
exiftool KMIPN23.png
```

Dari hasil tersebut didapatkan data setelah chunk IEND. 
Perlu diketahui bahwa setelah chunk IEND seharusnya tidak ada data, karena itu adalah tanda akhir dari file PNG. Penjelasan lengkap ada pada [Wikipedia](https://en.wikipedia.org/wiki/PNG).

![Trailer data after IEND chunk](./1.png)

Untuk mengetahui isi dari data setelah chunk IEND, dapat digunakan command strings. Hasil dari command strings didapatkan flag2 seperti pada gambar di bawah

```bash
strings KMIPN23.png | tail -n 5
```

![Data after IEND](./2.png)

Kemudian untuk mengecek md5 digunakan command md5sum

```bash
md5sum KMIPN23.png
```

## Flag
### KMIPN{cekstrings:4ecce6394798580638cfed50376149a7}

