# Flag Checker

## Deskripsi
Periksa apakah flag mu benar atau tidak!

## Solusi
Challenge yang diberikan memberikan sebuah file executable untuk Windows. Langkah pertama yang dilakukan adalah mengecek strings dari file tersebut.
``` shell
strings FlagChecker.exe
```
Tidak ada hasil yang begitu bisa digali informasinya

Langkah berikutnya adalah mencoba perintah objdump untuk menampilkan semua konten dari file executable beserta isinya pada masing-masing memory.
``` shell
$ objdump -s FlagChecker.exe
-- output truncated --
 402fe0 65787400 7365745f 54657874 00666c61  ext.set_Text.fla
 402ff0 67546578 74005368 6f770073 65745f54  gText.Show.set_T
 403000 6162496e 64657800 4d657373 61676542  abIndex.MessageB
 403010 6f780054 65787442 6f780067 65745f41  ox.TextBox.get_A
 403020 7373656d 626c7900 49734e75 6c6c4f72  ssembly.IsNullOr
 403030 456d7074 79000000 00395000 6c006500  Empty....9P.l.e.
 403040 61007300 65002000 46006900 6c006c00  a.s.e. .F.i.l.l.
 403050 20007400 68006500 20004600 6c006100   .t.h.e. .F.l.a.
 403060 67002000 53007400 72006900 6e006700  g. .S.t.r.i.n.g.
 403070 2100000d 45007200 72006f00 72002100  !...E.r.r.o.r.!.
 403080 004b4b00 4d004900 50004e00 34007b00  .KK.M.I.P.N.4.{.
 403090 68003400 72006400 63003000 64003300  h.4.r.d.c.0.d.3.
 4030a0 64005f00 76003400 6c007500 33005f00  d._.v.4.l.u.3._.
 4030b0 31007300 5f003300 7a005f00 74003000  1.s._.3.z._.t.0.
 4030c0 5f007200 33003400 64007d00 002b5900  _.r.3.4.d.}..+Y.
 4030d0 6f007500 72002000 46006c00 61006700  o.u.r. .F.l.a.g.
 4030e0 20004900 73002000 43006f00 72007200   .I.s. .C.o.r.r.
 4030f0 65006300 74002100 00114300 6f007200  e.c.t.!...C.o.r.
 403100 72006500 63007400 21000021 54007200  r.e.c.t.!..!T.r.
 403110 79002000 41006700 61006900 6e002000  y. .A.g.a.i.n. .
-- output truncated --
```
Terlihat terdapat string berupa flag yang ditulis secara hardcoded di file executable tersebut.

## Flag
### KMIPN4{h4rdc0d3d_v4lu3_1s_3z_t0_r34d}