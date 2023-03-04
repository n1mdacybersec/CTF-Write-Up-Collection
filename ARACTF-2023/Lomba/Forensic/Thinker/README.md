# Thinker

## Deskripsi
I always overthink about finding other part of myself, can you help me?

## Solusi
Waduh soal OSINT tapi sekarang disuruh untuk menstalker akun sosial media orang. Tapi karena yang dicari ini adalah akun cosplayer jadinya bersemangat hehe.

Dari deskripsi soal cukup sulit untuk mencari akun dengan deskripsi yang telah disebutkan. Percobaan pertama adalah dengan melakukan pencarian di search engine menggunakan wajah cosplayer yang ada pada [video](./Challenge/Sheiscute.mp4).

Pencarian menggunakan gambar pada search engine seperti Google, Bing, dan Yandex masih tidak menemukan hasil yang bisa mengarah kepada akun sosial media cosplayer yang dicari. Sampai akhirnya didapatkan sedikit petunjuk menggunakan pencarian wajah pada [Pimeyes](https://pimeyes.com) yaitu terdapat gambar wajah yang mirip. Namun sayangnya pencarian gratis pada Pimeyes tidak bisa menemukan sumber dari gambar yang sudah muncul. Hasil pencarian di Pimeyes di download gambarnya untuk selanjutnya dilakukan pencarian lagi menggunakan gambar tambahan.

![Face search using Pimeyes](./pimeyes_search_result.jpeg)

Gambar-gambar yang telah didapat melalui Pimeyes ketika dicari lagi menggunakan pencarian gambar di search engine lain masih tidak menemukan clue untuk mengarah ke akun cosplayer itu. Masih stuck tidak menemukan petunjuk, akhirnya dicoba clue terakhir yaitu cosplayer itu pernah berfoto dengan cosplayer dengan nama `Sakura` yang berasal dari China.

Pencarian menggunakan keyword sakura dilakukan di Instagram dan ditemukan akun dengan username `sakura.gun` yang merupakan cosplayer asal China dan memiliki nama Sakura. Nah karena sudah ditemukan sedikit titik terang, maka hanya perlu menggunakan skill untuk stalking orang :). Dari hasil pencarian di akun Instagram `sakura.gun` ditemukan seorang cosplayer yang pernah berfoto dengan `sakura.gun` dan memiliki wajah yang mirip dengan yang ada di video, akun dengan username `yanzikenko`.

Oke ternyata memang benar akun tersebut adalah orang yang sama dengan yang ada di video soal.

![Proof if yanzikenko is the same person in the video](./yanzikenko.jpeg)

Lanjut dengan stalking akun `yanzikenko` namun tidak ada foto-foto yang sesuai pada deskripsi soal. Pencarian dilanjutkan pada akun Facebook dari `yanzikenko` yaitu `yanzikenko.hii`. Foto pertama yang sesuai dengan deskripsi soal, yaitu tempat yanzikenko berkuliah. Dia pernah berkuliah di Beijing Normal University (BNU)

![Yanzikenko graduated from BNU](./yanzikenko_graduated_from_her_university.jpg)

Gambar yang kedua adalah saat dia berfoto dengan maskot, maskotnya bernama Molly.

![Photo with mascot](./photo_with_molly.jpg)

Gambar yang ketiga adalah foto di toko buku. Pada instruksi soal disebutkan untuk mengetahui jam dan tanggal foto itu di-upload.

![Photo at bookstore](./photo_at_bookstore.png)

Yang terakhir adalah mencari fotonya saat berfoto dengan sakura.gun. Di dalam postingan tersebut ada komentar yang berisi bagian terakhir dari flag yang dicari. Akhirnya ditemukan bagian terakhir dari flag `Y0u4r3ThE0s1nTm45t3R`

![Comment contained the part of the flag](./comment_with_flag_inside.png)

Langkah terakhir adalah menggabungkan seluruh flag yang ditemukan sesuai dengan format yang ada file [instruction.txt](./Challenge/instruction.txt). Karena yang dicari adalah ID bukan username dari cosplayer yang dimaksud, maka digunakan link [berikut](https://commentpicker.com/instagram-user-id.php) untuk mencari user ID Instagram yanzikenko. ID nya adalah 44793134117.

![Search Instagram ID](./search_insta_id.png)

Akhirnya telah ditemukan semua bagian flag, hanya tinggal menggabungkannya sesuai instruksi.
Dengan didapatkannya flag pada soal ini, saya berfikir ini soal mengajarkan buat jadi stalker atau petinju vtu-

![Yo WTF](./MoonaYoWTF.png)

## Flag
### ARA2023{44793134117_BNU_Molly_3Juni2019-10:25_Y0u4r3ThE0s1nTm45t3R}

