# FindAndOpen

## Deskripsi
Someone might have hidden the password in the trace file. <br>
Find the key to unlock this [file](./Challenge/flag.zip). [This tracefile](./Challenge/dump.pcap) might be good to analyze.

## Points
200

## Hints
- Download the pcap and look for the password or flag.
- Don't try to use a password cracking tool, there are easier ways here.

## Solusi
Dari kedua file yang diberikan, sebuah file zip di dalamnya terdapat sebuah file flag yang terkunci dengan password. Di dalam hint yang diberikan disebutkan bahwa percuma untuk menggunakan password cracking tool atau bruteforce password karena di dalam file pcap terdapat password yang dicari.

File pcap tersebut memiliki paket yang menarik, yaitu paket yang informasinya berasal dari Ethernet II. Jika ditelusuri, paket dengan informasi tersebut memberitahukan bahwa flag telah dipisah dan pada packet ke-48 terlihat seperti ada paket yang dikirimkan menggunakan base64.

![Information send using base64](./1.png)

Hasil dari decoding base64 tersebut adalah seperti ini

![Part of flag from pcap](./2.png)

Karena pada file pcap tersebut ketika dicari lagi tidak ada informasi mengenai password yang digunakan untuk membuka file flag yang terkunci, maka asumsinya adalah part dari flag itu juga adalah password dari file flag tersebut. Ternyata memang benar part dari flag adalah passwordnya

![Final flag](./3.png)

## Flag
### picoCTF{R34DING_LOKd_fil56_succ3ss_5ed3a878}

