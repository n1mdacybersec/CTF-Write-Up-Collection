# PUZZLE

## Deskripsi
Kamu disuruh untuk mencari tahu file file yang berhasil diambil oleh Hacker dimana file-file tersebut jika disusun akan membentuk sebuah gambar yang berisikan flag rahasia. Temukan dan kamu berkesempatan untuk terpilih menjadi Blue Team di Telkom Indonesia

## Solusi
Soal yang diberikan berupa sebuah file PCAP. Dalam deskripsi soal disebutkan bahwa terdapat file-file yang telah diambil oleh Hacker dan kita harus menyusun file tersebut untuk mendapatkan flag.
Karena packet yang di-capture berupa beberapa packet TCP dan FTP, maka lebih mudah untuk melihat packet-packet tersebut dengan Follow TCP Stream.

Dari stream pertama terlihat bahwa terdapat operasi untuk menyimpan file 1, 5, 3, 2, dan 4.
