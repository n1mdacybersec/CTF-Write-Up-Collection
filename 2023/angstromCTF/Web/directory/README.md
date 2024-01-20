# directory

## Deskripsi
[This](https://directory.web.actf.co/) is one of the directories of all time, and I would definitely rate it out of 10.

## Points
40

## Solusi
Challenge yang diberikan berupa web yang memiliki banyak link. Link yang tersedia ada 5000 dan flag terdapat pada salah satu link tersebut.

```html
<html>
<body><a href="0.html">page 0</a><br />
<a href="1.html">page 1</a><br />
<a href="2.html">page 2</a><br />
<a href="3.html">page 3</a><br />
<a href="4.html">page 4</a><br />
...
<a href="4999.html">page 4999</a><br />
```

Disini digunakan tools [httrack](https://www.httrack.com/) untuk membuat salinan dari website asli dari challenge tersebut.
Setelah selesai menyalin seluruh isi dari website asli, kita cari flag tersebut. Dari hasil pencarian, flag terdapat pada link ke-3054.

![flag](./flag.png)

## Flag
### actf{y0u_f0und_me_b51d0cde76739fa3}
