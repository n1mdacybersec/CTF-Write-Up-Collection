# Exam Answer

## Description
Budi ingin mengetahui jawaban yang pernah diujikan pada saat UAS kepada Caesar. Tetapi Caesar hanya memberikan sebuah gambar. Bisakah anda membantu Budi untuk mengetahui apa yang sebenarnya Caesar berikan?

In English translation the description of the challenge will be look like this

> Budi wanted to know the answer of final exam from Caesar. But Caesar only gave a picture. Can you help Budi find out what Caesar really gave?

## Attachment
[logo_politbatam.png](./Challenge/logo_polibatam.png)

## Solution
Given the following image [file](./Challenge/logo_polibatam.png) which is a png file. First, check the string value which may contain a flag. 
``` shell
strings logo_polibatam.png
```
From the results of checking the string from the image, there is information that can be obtained, which is the presence of text after the IEND chunk.

![Strings for given image](./IEND_chunk.png)

According to information from [Wikipedia](https://en.wikipedia.org/wiki/Portable_Network_Graphics), IEND chunk is the last part of png or it could be said that it's to marked the end of png file.

If there is inserted text after the IEND chunk it is likely the flag that we're being searched for. The text after the chunk looks like it has been encoded using base64.
**WFpWQ0E5e0NieXZncnhhdnhPbmduenF2cXZldnhuYWNucW5nbmF0dG55ODVacnY3NTU1fQ==**

Decode the base64 encoding with this following command
``` shell
echo "WFpWQ0E5e0NieXZncnhhdnhPbmduenF2cXZldnhuYWNucW5nbmF0dG55ODVacnY3NTU1fQ==" | base64 -d
```
We will get this result `XZVCA9{CbyvgrxavxOngnzqvqvevxnacnqngnattny85Zrv7555}`

However, the result that has been decoded does not match the flag format, namely `KMIPN4{flag}`. For this reason, we tried to use ROT13 because the challenge description still includes Caesar's name.

The result became `KMIPN9{PoliteknikBatamdidirikanpadatanggal85Mei7555}`.

This result is close to the flag that we're looking for, but from Google search results show that Politeknik Negeri Batam was founded on May 30, 2000. So the correct flag is `KMIPN4{PoliteknikBatamdidirikanpadatanggal30Mei2000}`

## Flag
`KMIPN4{PoliteknikBatamdidirikanpadatanggal30Mei2000}`
