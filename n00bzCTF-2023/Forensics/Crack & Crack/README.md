# Crack & Crack

## Deskripsi
Just Crack & Crack! Author: NoobMaster

## Attachment
[flag.avi](./Challenge/flag.zip)

## Solusi
Pada challenge ini terdapat sebuah file zip yang terkunci. Kita gunakan tools bernama `fcrackzip` untuk melakukan bruteforce terhadap file zip tersebut dengan menggunakan wordlist `rockyou.txt`.

![Fcrack Zip](fcrackzip.png)

Setelah dilakukan bruteforce, kita mendapatkan passwordnya yaitu `1337h4x0r`. Ternyata di dalam file zip tersebut juga terdapat file pdf yang juga dalam kondisi terprotected oleh password. Maka kita menggunakan tools `pdfcrack` untuk melakukan bruteforce terhadap file pdf tersebut.

![PDF Crack](pdfcrack.png)

Bruteforce juga tetap dilakukan menggunakan wordlist `rockyou.txt` dan kita mendapatkan password dari pdf tersebut, yaitu `noobmaster`. Setelah dibuka file pdf tersebut, langsung kita diberikan flagnya.

## Flag
### n00bz{CR4CK3D_4ND_CR4CK3D_1a4d2e5f}