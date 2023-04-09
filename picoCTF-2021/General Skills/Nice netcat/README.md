# Nice netcat...

## Deskripsi
There is a nice program that you can talk to by using this command in a shell: `$ nc mercury.picoctf.net 22902`, but it doesn't speak English...

## Hint
- You can practice using netcat with this picoGym problem: [what's a netcat](https://play.picoctf.org/practice/challenge/34)
- You can practice reading and writing ASCII with this picoGym problem: [Let's Warm Up](https://play.picoctf.org/practice/challenge/22)

## Solusi
Saat terhubung menggunakan netcat terdapat beberapa angka yang ditampilkan. Angka tersebut terlihat seperti nilai desimal dari ASCII.
Kita bisa menyalin nilainya dan menggunakan [CyberChef](https://gchq.github.io/CyberChef/) untuk mengkonversi nilai desimal ke ACII.

![Converted decimal to ASCII](./flag.png)

## Flag
### picoCTF{g00d_k1tty!_n1c3_k1tty!_d3dfd6df}
