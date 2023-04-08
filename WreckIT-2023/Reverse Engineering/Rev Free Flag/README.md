# Rev Free Flag

## Deskripsi
anggep aja flag gratis bang. kasian banyak yang blom pernah nyentuh ctfd keknya.

## Solusi
Diberikan file [Challenge](challenge/chall.c) yang di dalamnya terdapat array. Dapat dilihat bahwa setiap elemen pada array `c` dilakukan proses XOR, yaitu jika indeks karakter adalah bilangan ganjil dan hasil XOR antara nilai integer dengan nilai 24/32 tidak sama dengan nilai ASCII dari karakter pada setiap indeks. 

Karena kita sudah mempunyai setiap karakter di dalam array `c`, maka kita dapat membalikkan prosesnya. Kami membuat script python [Solve](solve.py) seperti berikut:
```
c = [119, 74, 101, 91, 107, 81, 116, 44, 16, 99, 20, 107, 76, 41, 127, 122, 20, 118, 71, 71, 80, 125, 82, 117, 17, 118,
     84, 44, 20, 118, 127, 44, 84, 44, 83, 44, 78, 71, 78, 43, 87, 122, 73, 43, 127, 126, 82, 113, 69, 118, 68, 116, 89, 101]
data = [0] * 54
for i in range(len(c)):
    if i % 2 == 0:
        data[i] = c[i] ^ 32
    else:
        data[i] = c[i] ^ 24
flag = "".join([chr(x) for x in data])
print(flag)
```
Setelah dirun, maka VOILA! Ketemu flagnya.

## Flag
### WRECKIT40{4sl1_b4ng_perm1nt44n_4t4s4n_n3wbi3_friendly}



