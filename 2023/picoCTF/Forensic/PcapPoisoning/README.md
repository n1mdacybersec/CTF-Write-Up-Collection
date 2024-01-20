# PcapPoisoning

## Deskripsi
How about some hide and seek heh?
Download this [file](https://artifacts.picoctf.net/c/375/trace.pcap) and find the flag.

## Solusi
Diberikan suatu file [pcap](Challenge/trace.pcap), ketika dibuka menggunakan `Wireshark` sekilas hanya tampak data TCP dan juga FTP. Tetapi jika diperhatikan dengan seksama di packet nomor 4 terdapat `FTP Request` yang berisikan `username root password toor`, yang mana terjadi akses kredensial di dalamnya dari `IP Source: 172.16.0.2` menuju `IP Destination: 10.253.0.6`. Kamipun melakukan follow pada packet tersebut dan ternyata terdapat lagi packet nomor 507 yang juga mempunyai `IP Source` dan `IP Destination` yang sama. 

Ketika kami melihat tampilan `Packet Bytes` untuk packet nomor 507 tersebut ternyata terdapat flag di dalamnya.
```shell
0000   45 00 00 52 00 01 00 00 40 06 c3 90 ac 10 00 02   E..R....@.......
0010   0a fd 00 06 00 14 00 15 00 00 00 00 00 00 00 00   ................
0020   50 02 20 00 8b 73 00 00 70 69 63 6f 43 54 46 7b   P. ..s..picoCTF{
0030   50 36 34 50 5f 34 4e 34 4c 37 53 31 53 5f 53 55   P64P_4N4L7S1S_SU
0040   35 35 33 35 35 46 55 4c 5f 35 62 36 61 36 30 36   55355FUL_5b6a606
0050   31 7d                                             1}
```

## Flag
### picoCTF{P64P_4N4L7S1S_SU55355FUL_5b6a6061}
