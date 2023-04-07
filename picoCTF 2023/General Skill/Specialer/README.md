# Specialer

## Deskripsi
Reception of Special has been cool to say the least. 
That's why we made an exclusive version of Special, called Secure Comprehensive Interface for Affecting Linux Empirically Rad, or just 'Specialer'.
With Specialer, we really tried to remove the distractions from using a shell.
Yes, we took out spell checker because of everybody's complaining.
But we think you will be excited about our new, reduced feature set for keeping you focused on what needs it the most.
Please start an instance to test your very own copy of Specialer.

## Points
400

## Hints
What programs do you have access to?

## Solusi
Challenge ini hampir mirip dengan challenge Special, namun shell restriction yang ada bukan auto-correction, namun banyak command yang tidak ada.

![Some available commands on the restricted shell](./1-Specialer.png)

Dari gambar tersebut beberapa command yang bisa dijalankan adalah `cd`, `pwd`, dan `echo`.
Dari link [berikut](https://ubunlog.com/en/alternativas-al-comando-ls/#Utilizar_el_comando_echo) kita bisa menjalankan fungsi yang mirip dengan command `ls` dengan menggunakan `echo`
```
echo *
```

Kemudian biasanya kita menggunakan command `cat` untuk melihat isi dari sebuah file, namun karena command ini tidak ada maka bisa menggunakan command `echo` seperti pada berikut [ini](https://jarv.org/posts/cat-without-cat/).
Flag ada pada file `ala/kazam.txt` dan berikut caranya untuk mendapatkan flag.
![Read flag](./2-Specialer.png)

## Flag
### picoCTF{y0u_d0n7_4ppr3c1473_wh47_w3r3_d01ng_h3r3_49193632}
