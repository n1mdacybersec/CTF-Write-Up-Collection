# PNG-G

## Deskripsi
Don't let appearances fool you.

Good luck!

Format : `Hero{}`

## Attachment
[pngg.png](./Challenge/pngg.png)

## Solusi
Diberikan sebuah file png dan ketika dicek menggunakan perintah `file` menunjukkan bahwa file tersebut merupakan file png.

```bash
$ file pngg.png
pngg.png: PNG image data, 500 x 500, 8-bit/color RGB, non-interlaced
```

Kemudian dicoba menggunakan `exiftool` untuk mengambil informasi mengenai metadata yang ada file tersebut.

```bash
$ exiftool pngg.png
ExifTool Version Number         : 12.57
File Name                       : pngg.png
Directory                       : .
File Size                       : 512 kB
File Modification Date/Time     : 2023:05:21 15:15:28+07:00
File Access Date/Time           : 2023:05:21 15:16:43+07:00
File Inode Change Date/Time     : 2023:05:21 15:16:43+07:00
File Permissions                : -rw-r--r--
File Type                       : APNG
File Type Extension             : png
MIME Type                       : image/apng
Image Width                     : 500
Image Height                    : 500
Bit Depth                       : 8
Color Type                      : RGB
Compression                     : Deflate/Inflate
Filter                          : Adaptive
Interlace                       : Noninterlaced
Animation Frames                : 2
Animation Plays                 : inf
Transparency                    : 0 0 16
Image Size                      : 500x500
Megapixels                      : 0.250
```

Dari hasil command `exiftool` menunjukkan bahwa tipe filenya adalah apng dan bukan png. 
Jika kita cari menggunakan google, file apng merupakan file animasi png, yang mirip dengan gif.
Informasinya bisa dilihat pada link [berikut](https://docs.fileformat.com/image/apng/)

Digunakan link [berikut](https://products.groupdocs.app/viewer/apng) untuk membuka file apng, namun sebelum itu kita harus mengubah ekstensi file dari yang sebelumnya png menjadi apng.
Hasilnya adalah seperti berikut

![flag](./flag.png)

## Flag
### Hero{Not_Just_A_PNG}
