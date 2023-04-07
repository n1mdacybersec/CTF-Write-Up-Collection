# chrono

## Deskripsi
How to automate tasks to run at intervals on linux servers?

## Points
100

## Solusi
Challenge berupa sebuah instance yang dapat diakses setelah  menjalankan instance tersebut. 
Dari deskripsi soal diberikan petunjuk untuk menjalankan sebuah task secara otomatis pada interval waktu tertentu. 
Pada Linux digunakan [cron](https://en.wikipedia.org/wiki/Cron) untuk menjalankan task secara otomatis dengan interval waktu tertentu.

Penyelesaiannya cukup straightforward, yaitu membaca file crontab yang ada di sistem.

```shell
cat /etc/crontab
```

### Unintended solution
Ditemukan juga cara menemukan flag secara unintended, yaitu membaca metadata.json yang ada pada directory /challenge
```shell
$ cat /challenge/metadata.json
{"flag": "picoCTF{Sch3DUL7NG_T45K3_L1NUX_0bb95b71}", "username": "REDACTED", "password": "REDACTED"}
```

## Flag
### picoCTF{Sch3DUL7NG_T45K3_L1NUX_0bb95b71}
