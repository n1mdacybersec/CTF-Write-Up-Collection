# Jack Sparrow

## Deskripsi
Not all treasure is silver and gold mate! let the ship flow from left to right

## Solusi
Diberikan sebuah file gambar dan untuk menemukan flag dari tantangan ini diperlukan tool atau aplikasi color picker yang bisa memberikan nilai hex dari warna tersebut.

![Hex value from color](./jack_sparrow_1.png)

Setelah diketahui seluruh nilainya, kita bisa membuat program Python sederhana untuk mengubah hex menjadi ASCII
``` python
string = "617261323032317b337a5f507a5f6c7a5f6c336d306e5f53515a7d"
decoded = bytes.fromhex(string)
decoded = decoded.decode("ascii")
print(decoded)
```

## Flag
### ara2021{3z_Pz_lz_l3m0n_SQZ}
