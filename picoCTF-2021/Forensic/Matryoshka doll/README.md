# Matryoshka doll

## Deskripsi
Matryoshka dolls are a set of wooden dolls of decreasing size placed one inside another. What's the final one? Image: [this](./Challenge/dolls.jpg)

## Hints
- Wait, you can hide files inside files? But how do you find them?
- Make sure to submit the flag as picoCTF{XXXXX}

## Solusi
Diberikan sebuah file jpg dan jika dicermati dari deskripsi soal terdapat data yang ada pada file jpg tersebut.

Langkah penyelesaiannya adalah dengan menggunakan binwalk.
```shell
binwalk -e dolls.jpg
```

Sesuai dengan deskripsi soal terdapat gambar lainnya di dalam file `dolls.jpg`. Gambar tersebut seperti pada matryoshka doll dimana terdapat boneka paling kecil di dalam isi dari boneka-boneka yang lebih besar. Jadi seharusnya hasil akhirnya adalah flag yang akan dicari.

Gambar diekstrak terus menerus menggunakan binwalk hingga struktur direktori menjadi seperti berikut ini
```shell
$ tree _dolls.jpg.extracted
_dolls.jpg.extracted
├── 4286C.zip
└── base_images
    ├── 2_c.jpg
    └── _2_c.jpg.extracted
        ├── 2DD3B.zip
        └── base_images
            ├── 3_c.jpg
            └── _3_c.jpg.extracted
                ├── 1E2D6.zip
                └── base_images
                    ├── 4_c.jpg
                    └── _4_c.jpg.extracted
                        ├── 136DA.zip
                        └── flag.txt

6 directories, 8 files
```

Flag terdapat pada file flag.txt

## Flag
### picoCTF{336cf6d51c9d9774fd37196c1d7320ff}
