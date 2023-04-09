# Help

## Deskripsi
Bob is receiving a message from their clients, to put this text on the display in the office. Bob is confused because he didn't know what it is, can you help him?

Format: ARA2023{lowercase_flag}

[Attachment](./Challenge/help.txt)

## Solusi
Diberikan file teks yang isinya seperti bilangan biner, namun jika dihitung kembali hanya terdapat 7 bit. Ternyata bilangan 0 dan 1 tersebut merepresentasikan 7-segment display (terlihat dari deskripsi soal yang menyebutkan display). Untuk mendecode pesan tersebut digunakan [dCode](https://www.dcode.fr/7-segment-display), namun didapatkan hasil seperti di bawah ini.

![Not readable 7-segment display](./1.png)

Terlihat bahwa karakter yang ditampilkan menggunakan 7-segment display terbalik. Untuk itu isi dari file `help.txt` direverse dan di decode kembali.

![Final result](./result.png)

Sudah terlihat huruf yang ditampilkan pada 7-segment display, yaitu supertranscendentess_it_is_hehe. Sehingga flagnya menjadi ARA2023{supertranscendentess_it_is_hehe}.

## Flag
### ARA2023{supertranscendentess_it_is_hehe}