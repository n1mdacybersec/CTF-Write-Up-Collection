# Flag Shop

## Deskripsi
Come and buy yourself a flag! Author: NoobMaster

`nc challs.n00bzunit3d.xyz 50267`

## Solusi
Pada challenge ini diberikan suatu `netcat connection` yang mana merupakan suatu toko untuk membeli flag. Diketahui kita hanya mempunyai `$100`, sedangkan harga `real_flag` adalah sebesar `$1337`. Di sini kita berpikir bahwa vulnerability terdapat di `fake_flag`, kami berpikir bahwa `real_flag` tersebut merupakan unsigned int. Maka kita mencoba membeli `fake_flag` dengan angka negatif. Dan ternyata saldo bertambah menjadi lebih besar daripada harga `real_flag` dan kita membeli flagnya.

## Flag
### n00bz{5h0p_g0t_h3ck3d_4nd_fl4g_g0t_570l3n!}