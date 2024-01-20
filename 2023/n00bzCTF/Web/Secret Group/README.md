# Secret Group

## Deskripsi
To get the flag, you must be a member of the secret group! Author: NoobMaster

http://challs.n00bzunit3d.xyz:31401/ 

## Solusi
Saat mengakses web dari challenge ini diberikan sebuah response yang menyatakan bahwa browser yang digunakan bukan merupakan `n00bz-4dm1n`.

```
$ curl http://challs.n00bzunit3d.xyz:31401/
<p>Not an agent of the <b>n00bz-4dm1n</b> secure browser!</p>
```

Setelah mengatur browser yang digunakan menjadi `n00bz-4dm1n` dengan mengatur header `User-Agent` didapatkan response sebagai berikut.

```
curl -H "User-Agent: n00bz-4dm1n" http://challs.n00bzunit3d.xyz:31401/
<p>Does not Accept <b>fl4g</b></p>
```

Dari response tersebut, tidak jelas maksud dari tidak menerima `fl4g`. Hingga akhirnya ditemukan response yang lain dengan menggunakan request header `Accept: fl4g`.

```
curl -H "User-Agent: n00bz-4dm1n" -H "Accept: fl4g" http://challs.n00bzunit3d.xyz:31401/
<p>Connection not <b>s3cur3</b></p>
```

Dari response di atas, awalnya aku mengira bahwa koneksi ke website harus secure. Oleh karena itu digunakan header `Strict-Transport-Security` atau sering disebut dengan HSTS untuk meminta koneksi secara secure ke HTTPS server, namun ternyata salah. 
Disini hanya perlu mengatur header `Connection: s3cur3` sehingga mendapatkan response yang baru

```
curl -H "User-Agent: n00bz-4dm1n" -H "Accept: fl4g" -H "Connection: s3cur3" http://challs.n00bzunit3d.xyz:31401/
<p>Not refered by <b>s3cr3t.n00bz-4dm1n.xyz</b></p>
```

Dari response di atas, kita perlu untuk membuat request header `Referer: s3cr3t.n00bz-4dm1n.xyz`.

```
curl -H "User-Agent: n00bz-4dm1n" -H "Accept: fl4g" -H "Connection: s3cur3" -H "Referer: s3cr3t.n00bz-4dm1n.xyz" http://challs.n00bzunit3d.xyz:31401/
<b>Give-Flag</b> is not <b>7ru3</b>
```

Request header yang terakhir adalah dengan mengirimkan header `Give-Flag: 7ru3`
```
curl -H "User-Agent: n00bz-4dm1n" -H "Accept: fl4g" -H "Connection: s3cur3" -H "Referer: s3cr3t.n00bz-4dm1n.xyz" -H "Give-Flag: 7ru3" http://challs.n00bzunit3d.xyz:31401/
```

![Flag](./flag.png)

## Flag
### n00bz{y0u_4r3_n0w_4_v4l1d_m3mb3r_0f_th3_s3cr3t_gr0up!}