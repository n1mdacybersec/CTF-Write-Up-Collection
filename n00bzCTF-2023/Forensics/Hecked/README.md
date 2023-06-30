# Hecked

## Deskripsi
Someone hacked my server :( Can you please find out how? Note: Flag is `n00bz{md5sum(vulnerableService_serviceVersion_attackersFirstBashCommandOnTheHackedServer)}`
Replace the md5sum(...) with the ACTUAL MD5SUM of the above when you find it, like so: `echo -n vulnerableService_serviceVersion_attackersFirstBashCommandOnHackedServer | md5sum`
Also, case and underscores are important! Author: NoobHacker

## Attachment
[dump.pcap](./Challenge/dump.pcap)

## Solusi
Kita diberikan file pcap lalu dibuka menggunakan wireshark. Lalu kita menggunakan fitur follow untuk melihat seluruh percakapan. Dari follow kita dapat mengetahui bahwa `vulnerableService` merupakan `FTP` yang mana bernama `vsFTPd` dengan versi 2.3.4. Lalu command pertama yang dilakukan pada server yang sudah tereksploitasi adalah `id`. Lalu satukan semuanya sesuai dengan format, menjadi `vsFTPd_2.3.4_id`.

Lalu kita lakukan encode dengan `MD5` dengan perintah berikut:
```shell
echo -n vsFTPd_2.3.4_id | md5sum # a806fef72a92508b7a64776bb83ad4cb
```

## Flag
### n00bz{a806fef72a92508b7a64776bb83ad4cb}