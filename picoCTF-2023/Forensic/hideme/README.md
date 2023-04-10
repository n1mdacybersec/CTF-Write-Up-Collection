# hideme

## Deskripsi
Every file gets a flag.
The SOC analyst saw one image been sent back and forth between two people. They decided to investigate and found out that there was more than what meets the eye [here](https://artifacts.picoctf.net/c/257/flag.png).

## Solusi
Diberikan suatu image [Flag](Challenge/flag.png), di deskripsi secara tersirat tertulis bahwa terdapat gambar lain di dalam gambar flag. Digunakanlah command `binwalk` sebagai berikut untuk mengekstrak gambar tersebut:
```shell
$binwalk -e flag.png 

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             PNG image, 512 x 504, 8-bit/color RGBA, non-interlaced
41            0x29            Zlib compressed data, compressed
39739         0x9B3B          Zip archive data, at least v1.0 to extract, name: secret/
39804         0x9B7C          Zip archive data, at least v2.0 to extract, compressed size: 2959, uncompressed size: 3108, name: secret/flag.png
42998         0xA7F6          End of Zip archive, footer length: 22
```
Ternyata benar bahwa di dalam file gambar asli terdapat directory rahasia dengan file flag lagi di dalamnya, yaitu `secret/flag.png`. Lalu tinggal kita masuk ke direktori `secret` dan melihat isi dari file [Flag](flag.png). Di gambar tersebut telah bertuliskan flag yang kita cari.

## Flag
### picoCTF{Hiddinng_An_imag3_within_@n_ima9e_dc2ab58f}
