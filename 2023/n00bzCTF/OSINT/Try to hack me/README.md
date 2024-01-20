# Try to hack me

## Deskripsi
My friend `brayannoob` gave me a ctf challenge and told me `Try to hack me`. Author: noob_abhinav

## Solusi
Pada challenge ini diberikan sebuah username yang harus dicari untuk mencari flag. Kita bisa menggunakan OSINT tool [sherlock](https://github.com/sherlock-project/sherlock) untuk mencari akun atau username yang ada.
Langkah-langkah untuk mencari flag seperti berikut ini:
1. Gunakan sherlock untuk mencari akun dengan nama `brayannoob`.
```
python3 sherlock --timeout 5 brayannoob
```
2. Hasil pencarian menggunakan sherlock akan menunjukkan bahwa `brayannoob` mempunyai akun Github.
3. Kita akan berfokus pada repository `BrayanResearch` karena repository tersebut baru diupdate 7 jam terakhir pada saat CTF berlangsung.
4. Pada file `README.md` pada repository tersebut terdapat informasi seperti berikut ini.
```
<!-- hi -->
<!-- my secret -->
<!-- username : brayan234 -->
```
5. Pencarian dengan sherlock dilanjutkan dengan username `brayan234`.
```
python3 sherlock --timeout 5 brayan234
```
6. Dari hasil pencarian username `brayan234` memiliki akun Try Hack Me. 
7. Saat mengakses link username [brayan234](https://tryhackme.com/p/brayan234) terdapat flag berikut

![Flag](./flag.png)

## Flag
### n00bz{y0u_p4ss3d_th3_ch4ll3ng3_c0ngr4tul4t10ns_7c48179d2b7547938409152641cf8e}