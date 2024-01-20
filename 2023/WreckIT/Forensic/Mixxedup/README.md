# Mixxedup

## Deskripsi
Tidak hanya minuman keras yang membuat mabuk, pict el ini juga membuat saya mabuk

## Solusi
Diberikan sebuah file [c.jpg](./Challenge/c.jpg) yang memiliki file lagi di dalamnya. Digunakan binwalk untuk mengekstrak file yang ada di dalamnya.

``` bash
binwalk -e c.jpg
```

Hasil ekstrak menghasilkan beberapa file berikut ini.
```
.
├── 13FDC.zip
├── dobleh.txt
└── flag.png

0 directories, 3 files
```

Isi dari file `dobleh.txt` seperti berikut ini
```
saya aslinya 400, sekarang 2000
```
Kemudian `flag.png` jika dibuka seperti ini

![Not a flag](https://user-images.githubusercontent.com/88087942/235346729-7d239577-8aff-4c59-a19b-7274e77ae747.png)

File `flag.png` ini memiliki ukuran dimensi 2000x400 dan dari keterangan file `dobleh.txt` diketahui bahwa ukuran asli gambar adalah 400, mungkin memiliki dimensi asli 400x400.
Gambar tersebut memiliki beberapa tulisan yang saling tumpah tindih, kita bisa menggunakan program Python untuk mencari flag yang kita inginkan. Namun permasalahannya adalah terletak pada nilai pixel yang pas untuk diambil datanya.
Melalui beberapa kali error berikut adalah program Python yang digunakan untuk menghasilkan dua buah gambar yang merupakan flag.

```python
from PIL import Image

im = Image.open("flag.png")

im1 = Image.new(mode="RGB", size=(400, 400))

def image_new(name, pixel, step):
	for x in range(400):
		for y in range(400):
			# Get the RGB color value for each step in pixel
			r, g, b = im.getpixel((pixel, y))
			# Modify image by putting the RGB color value from previous step
			im1.putpixel((x, y), (r, g, b))
		pixel += step

	im1.save(str(name)+".png")

image_new("image_new1", 0, 5)
image_new("image_new2", 1, 5)
```

Akan dihasilkan dua gambar yang telah diencode menggunakan base64. Hasil decodenya seperti berikut ini
![flag](https://user-images.githubusercontent.com/88087942/235347120-fda9bd1b-2fd0-4305-9239-feb2d6e6999e.png)

## Flag
### WRECKIT40{p1x3Ls_M4k3_M3_C0nfu53d_40D}
