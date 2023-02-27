# The Lady Sound

## Deskripsi
Pada suatu hari PT. Pama mendapatkan sebuah voice note yang sudah dirusak. Bantulah PT. Pama untuk memperbaiki file audio yang telah dirusak ini

## Solusi
Seperti yang telah dijelaskan pada deskripsi dari soal, bahwa terdapat file audio (.m4a) yang telah rusak dan harus diperbaiki. Untuk memperbaikinya gunakan hex editor.
Pada hex editor hapus byte 0-35 seperti pada gambar.

![Delete first 36 byte from file](./1.png)

Langkah selanjutnya adalah menggunakan tool faad, yaitu tool yang digunakan untuk mendecode audio dengan AAC codec. Digunakan perintah berikut untuk mendecode file menjadi WAV.
``` shell
faad flag.m4a
```

File WAV tersebut jika diputar akan mengeluarkan audio `Here is your flag th15_15_34sy`

## Flag
### ara2021{th15_15_34sy}

