# Rabbithole

## Deskripsi

Anda tau Matryoshka Doll? kali ini aku gembok dengan sandi yang sangat secure!

## Solusi
Diberikan sebuah file [zip](./Challenge/1000.zip) yang isinya berupa file zip yang di-password dan ketika di ekstrak akan ada lagi file zip yang di-password.
File zip tersebut memiliki karakteristik seperti ini
- File dengan nama `999_password.zip` adalah file zip yang di-password
- File `pw999.txt` adalah password yang digunakan untuk mengekstrak file `999_password.zip`
- Hasil dari proses ekstrak adalah `999.zip` (zip tanpa password)
- File `999.zip` jika diekstrak menghasilkan file `998_password.zip` dan `pw998.txt`.
- Proses di atas terus berulang.

Dari karakteristik itu bisa dibuat sebuah program Python sederhana untuk mengekstrak seluruh file zip dan hanya menyisakan file zip yang terakhir yang kemungkinan ada flag di dalamnya.

```python
import zipfile

filezip = ""
filepw = ""
newzip = ""

x = range(999, 0, -1)

for i in x:
    filezip = str(i)+"_password.zip"
    filepw = "pw"+(str(i))+".txt"
    
    with open(filepw, "r") as f:
        with zipfile.ZipFile(filezip, 'r') as file:
            file.extractall(pwd = bytes(f.read(), 'utf-8'))
            newzip = str(i)+".zip"
            with zipfile.ZipFile(newzip, 'r') as child:
                child.extractall()
                print("Extracting...", newzip) 
    f.close()
```

Program tersebut dijalankan di directory atau folder yang sama dengan file `999_password.zip` dan `pw999.txt`.
Hasil akhirnya adalah file `1.zip` yang di dalamnya terdapat file `flag.txt`. Jika dibuka file `flag.txt` terdapat pesan yang di-encode menggunakan hexadecimal.
Digunakan [CyberChef](https://gchq.github.io/CyberChef/) untuk decode pesan dan didapatkan flag yang dicari.

![Flag](./flag.png)

## Flag
### WRECKIT40{!_H0p3_u_d1dn'7_d0_i7_m4Nu411y_40D}
