# Waktunya Peng_dekriptor_an

## Deskripsi
diberikan file flag.txt berisi kode morse berikut:

```
--... ..... / --... --... / --... ...-- / ---.. ----- / --... ---.. / .---- ..--- ...-- / --... --... / ----. --... / .----
.---- ....- / .---- ----- ..... / ...-- ..--- / -.... ---.. / ----. --... / .---- ----- ....- / .---- .---- --... / .----
----- ---.. / .---- .---- --... / .---- ----- --... / ----. --... / .---- .---- ----- / ...-- ..--- / -.... ..... / .----
----- ----- / ----. --... / ----. ---.. / ...-- ..--- / ---.. ...-- / .---- ----- .---- / ----. ---.. / .---- ----- .---- /
.---- ----- ---.. / .---- .---- --... / .---- ----- ----. / ...-- ..--- / --... ...-- / .---- ----- ---.. / .---- -----
----. / .---- .---- --... / .---- ..--- .....
```

## Solusi
Dilakukan dekripsi kode morse menggunakan [Morse Code Translator | Morse Code World](https://morsecode.world/international/translator.html) didapatkan list integer berikut:

![Translate morse code](./1.png)

Selanjutnya integer tersebut yang merupakan bilangan desimal dikonversi ke ASCII untuk mendapatkan flag. Digunakan [CyberChef](https://gchq.github.io/CyberChef/) untuk melakukan konversi tersebut.

![Convert decimal to ASCII](./2.png)

## Flag
### KMIPN{Mari Dahulukan Adab Sebelum Ilmu}