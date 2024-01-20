# ReadMyCert

## Deskripsi
How about we take you on an adventure on exploring certificate signing requests
<br>
Take a look at this CSR file [here](./Challenge/readmycert.csr).

## Points
100

## Hints
Download the certificate signing request and try to read it.

## Solusi
Untuk membaca file CSR dengan menggunakan command di Linux digunakan perintah `openssl` seperti berikut ini.

```bash
openssl req -text -noout -verify -in readmycert.csr
```

![Flag at the CommonName information](./flag.png)

## Flag
### picoCTF{read_mycert_57f58832}
