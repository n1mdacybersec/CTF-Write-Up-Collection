# Painfully Deep Flag

## Deskripsi
This one is a bit deep in the stack.

## Attachment
[flag.pdf](./Challenge/flag.pdf)

## Solusi
Pada challenge ini diberikan sebuah file pdf. Pada PDF forensic biasanya kita akan mencari tahu mengenai struktur dari PDF itu sendiri, dimana kita bisa menemukan informasi tambahan seperti kemungkinan adanya embedded object atau gambar yang secara kasat mata tidak terlihat. Link [berikut ini](https://resources.infosecinstitute.com/topics/hacking/pdf-file-format-basic-structure/) memberikan informasi mengenai struktur PDF.

Langkah pertama adalah dengan menggunakan command `strings` untuk melihat struktur dari flag.pdf

```
strings flag.pdf
```

Pada gambar di bawah ini menunjukkan terdapat beberapa gambar yang ada pada file pdf tersebut, namun yang dapat kita lihat hanya satu.

![Multiple images inside PDF](./1.png)

Untuk mengekstrak seluruh gambar yang di dalam pdf, bisa menggunakan command `pdfimages`.

```
pdfimages flag.pdf extract/
```

Command tersebut akan mengekstrak seluruh gambar yang ada pada flag.pdf dan hasil ekstraknya akan diletakkan pada direktori extract. Untuk hasil gambar yang diekstrak masih berupa format .ppm, perlu diubah lagi menjadi format .png atau .jpeg, karena beberapa aplikasi gallery tidak bisa membuka file .ppm.

![Flag](./flag.png)

## Flag
### amateursCTF{0ut_0f_b0unds}