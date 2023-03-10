# @B4SH

## Deskripsi

Ailee had just moved out to a boarding house in the countryside to escape the fast-paced and hectic city life. She was very excited to start her life with a new environment, she was very happy before she found out that the room she rented was very dark. Suddenly she found out 2 strange papers on the wall behind the door that says:

"5A495A323032337B346D62793077625F677330663973675F677334675F2167355F345F733468733F7D".

Help Ailee to find what's behind the text written on the paper.

## Solusi
Pesan yang ada di deskripsi soal dikonversi dari hex ke ASCII dan didapatkan hasil seperti berikut.

``` shell
$ echo 5A495A323032337B346D62793077625F677330663973675F677334675F2167355F345F733468733F7D | xxd -r -p
ZIZ2023{4mby0wb_gs0f9sg_gs4g_!g5_4_s4hs?}
```

Terdapat teks yang masih belum sesuai dengan format flag. Pada awalnya chiper yang digunakan adalah Caesar cipher, ternyata cipher yang digunakan adalah Affine cipher. Digunakan [dCode](https://www.dcode.fr/affine-cipher) untuk mendapatkan flag.

![Decoding result](./result.png)

## Flag
### ARA2023{4nyb0dy_th0u9ht_th4t_!t5_4_h4sh?}