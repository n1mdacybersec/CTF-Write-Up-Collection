# PDF-Mess

## Deskripsi
This file seems to be a simple copy and paste from wikipedia. It would be necessary to dig a little deeper...

Good luck!

Format : `Hero{}`

## Attachment
[strange.pdf](./Challenge/strange.pdf)

## Solusi
Diberikan sebuah file PDF yang ketika dilihat isinya menggunakan command `strings` terdapat embedded object `script.js` seperti berikut ini.

```
$ strings strange.pdf
-- output truncated --
110 0 obj
<< /Length 179
/Type /EmbeddedFile
/Filter /FlateDecode
/Params << /Size 199
/Checksum <083542c62e17ca3367bd590c1ab38578> >>
/Subtype /application#2Fjs >>
stream
/lf{H
mf"{
endstream
endobj
111 0 obj
<< /F (script.js)
/Type /Filespec
/EF << /F 110 0 R >> >>
endobj
-- output truncated --
```

Ketika dicoba untuk mengekstrak seluruh objek yang ada pada PDF tersebut menggunakan `binwalk` tidak terdapat `script.js` yang dicari. Selanjutnya digunakan `pdfdetach` yang merupakan tool yang digunakan untuk menampilkan atau mengekstrak seluruh embedded file atau object yang ada pada PDF.

``` bash
$ pdfdetach -list strange.pdf
Syntax Error (227426): Illegal character <2f> in hex string
Syntax Error (227427): Illegal character <72> in hex string
Syntax Error (227430): Illegal character <3a> in hex string
Syntax Error (227431): Illegal character <52> in hex string
Syntax Error (227436): Illegal character <2f> in hex string
Syntax Error (227437): Illegal character <78> in hex string
Syntax Error (227438): Illegal character <3a> in hex string
Syntax Error (227439): Illegal character <78> in hex string
Syntax Error (227440): Illegal character <6d> in hex string
Syntax Error (227441): Illegal character <70> in hex string
Syntax Error (227442): Illegal character <6d> in hex string
Syntax Error (227444): Illegal character <74> in hex string
Syntax Error (227448): Illegal character <3f> in hex string
Syntax Error (227449): Illegal character <78> in hex string
Syntax Error (227450): Illegal character <70> in hex string
Syntax Error (227453): Illegal character <6b> in hex string
Syntax Error (227455): Illegal character <74> in hex string
Syntax Error (227458): Illegal character <6e> in hex string
Syntax Error (227460): Illegal character <3d> in hex string
Syntax Error (227461): Illegal character <22> in hex string
Syntax Error (227462): Illegal character <77> in hex string
Syntax Error (227463): Illegal character <22> in hex string
Syntax Error (227464): Illegal character <3f> in hex string
1 embedded files
1: script.js
```

Terlihat ketika embedded object dilist menggunakan `pdfdetach` terdapat file `script.js`. Untuk mengekstrak file tersebut menggunakan `pdfdetach` menggunakan perintah berikut.

``` bash
pdfdetach -save 1 strange.pdf
```

Isi dari `script.js` seperti berikut ini

```js
const CryptoJS=require('crypto-js'),key='3d3067e197cf4d0a',ciphertext=CryptoJS['AES']['encrypt'](message,key)['toString'](),cipher='U2FsdGVkX1+2k+cHVHn/CMkXGGDmb0DpmShxtTfwNnMr9dU1I6/GQI/iYWEexsod';
```

Program tersebut akan mengenkripsi pesan menggunakan metode enkripsi AES. Untuk mendapatkan pesan yang belum dienkripsi kita bisa mengubah sedikit program di atas.

```js
const CryptoJS=require('crypto-js');

const key = '3d3067e197cf4d0a';
const ciphertext = 'U2FsdGVkX1+2k+cHVHn/CMkXGGDmb0DpmShxtTfwNnMr9dU1I6/GQI/iYWEexsod';

var bytes = CryptoJS.AES.decrypt(ciphertext, key);
var message = bytes.toString(CryptoJS.enc.Utf8);

console.log(message);
```

Hasil dari program tersebut adalah
![flag](./flag.png)

## Flag
### Hero{M4L1C10U5_C0D3_1N_PDF}
