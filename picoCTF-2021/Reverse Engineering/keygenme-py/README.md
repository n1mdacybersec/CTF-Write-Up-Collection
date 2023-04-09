# keygenme-py

## Deskripsi
[keygenme-trial.py](https://mercury.picoctf.net/static/b016c61bd2cc0be05a59da1dde67a2ac/keygenme-trial.py)

## Solusi
Saat melihat source code dari program terdapat hal yang menarik
``` python
username_trial = "GOUGH"
bUsername_trial = b"GOUGH"

key_part_static1_trial = "picoCTF{1n_7h3_|<3y_of_"
key_part_dynamic1_trial = "xxxxxxxx"
key_part_static2_trial = "}"
key_full_template_trial = key_part_static1_trial + key_part_dynamic1_trial + key_part_static2_trial
```
Terdapat username `GOUGH` kemudian cara pembuatan kunci yang merupakan flag. Flag berasal dari static key pertama ditambah dengan dynamic dan ditambah lagi dengan static key kedua.

``` python
def enter_license():
    user_key = input("\nEnter your license key: ")
    user_key = user_key.strip()

    global bUsername_trial
    
    if check_key(user_key, bUsername_trial):
        decrypt_full_version(user_key)
    else:
        print("\nKey is NOT VALID. Check your data entry.\n\n")
```
Pada fungsi `enter_license()` dilakukan pengecekan key dengan menggunakan key yang dimasukkan oleh user dan username.

``` python
def check_key(key, username_trial):

    global key_full_template_trial

    if len(key) != len(key_full_template_trial):
        return False
    else:
        # Check static base key part --v
        i = 0
        for c in key_part_static1_trial:
            if key[i] != c:
                return False

            i += 1
 ```
 Pada fungsi `check_key()` terdapat pengecekan agar panjang key yang dimasukkan oleh user sama dengan panjang `key_full_template_trial`.
 Selanjutnya pengecekan untuk bagian static key pertama. Karena nilai static key pertama sudah pasti benar hasilnya maka mengisi bagian static key pertama dan lanjut untuk mengecek bagian dynamic key
 
 ``` python
        # TODO : test performance on toolbox container
        # Check dynamic part --v
        if key[i] != hashlib.sha256(username_trial).hexdigest()[4]:
            return False
        else:
            i += 1

        if key[i] != hashlib.sha256(username_trial).hexdigest()[5]:
            return False
        else:
            i += 1

        if key[i] != hashlib.sha256(username_trial).hexdigest()[3]:
            return False
        else:
            i += 1

        if key[i] != hashlib.sha256(username_trial).hexdigest()[6]:
            return False
        else:
            i += 1

        if key[i] != hashlib.sha256(username_trial).hexdigest()[2]:
            return False
        else:
            i += 1

        if key[i] != hashlib.sha256(username_trial).hexdigest()[7]:
            return False
        else:
            i += 1

        if key[i] != hashlib.sha256(username_trial).hexdigest()[1]:
            return False
        else:
            i += 1

        if key[i] != hashlib.sha256(username_trial).hexdigest()[8]:
            return False
 ```
 Pada pengecekan dynamic key terlihat bahwa kunci dicocokkan dengan hexdigest dari sha256 untuk bagian tertentu dari string `username_trial`. Diketahui bahwa nilai dari `username_trial` adalah `GOUGH` dan akan diambil hexdigest sha256 dengan posisi `4,5,3,6,2,7,1,8`. 

Solusi dari permasalahan tersebut sebenarnya cukup sederhana, yaitu dengan:
- Memasukkan bagian key static pertama sebagai bagian pertama flag
- Mendapatkan dynamic key dengan cara mencari hexdigest sha256 dari username `GOUGH` dengan urutan posisi `4,5,3,6,2,7,1,8` sebagai bagian flag kedua
- Memasukkan bagian key static kedua sebagai bagian terakhir dari flag

Dari logika di atas dapat dibuat sebuah program Python berikut
``` python
import hashlib

'''
how key generated
key_part_static1_trial = "picoCTF{1n_7h3_|<3y_of_"
key_part_dynamic1_trial = "xxxxxxxx"
key_part_static2_trial = "}"
key_full_template_trial = key_part_static1_trial + key_part_dynamic1_trial + key_part_static2_trial
'''

username_trial = b"GOUGH"

key_part_static1_trial = "picoCTF{1n_7h3_|<3y_of_"
key_part_static2_trial = "}"

positions = [4,5,3,6,2,7,1,8]

dynamic_key = "".join([hashlib.sha256(username_trial).hexdigest()[i] for i in positions])

flag = key_part_static1_trial + dynamic_key + key_part_static2_trial
print(flag)
```

## Flag
### picoCTF{1n_7h3_|<3y_of_f911a486}
