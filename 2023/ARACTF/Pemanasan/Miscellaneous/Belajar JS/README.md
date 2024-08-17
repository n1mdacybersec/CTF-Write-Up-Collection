# Belajar JS

## Description

Aku ingin menjadi Dewa JS!
http://103.152.242.116:8419/

English translation version:
> I want to be a JS God!
> http://103.152.242.116:8419/

## Solution
If we observed the website source code using inspect element there's an unreadable code in tag `<script>` that only written by using symbols at it's [index.html](./index.html). This symbols might be an obfuscated Javascript code. After digging some information on the internet, this Javascript code is obfuscated using JSFuck.

To deobfuscate the JSFuck obfuscated code, we can use this link https://enkhee-osiris.github.io/Decoder-JSFuck/
The result after deobfuscation is like this.

```js
alert('Hello'); //ARA2023{j4vaScr1pt_iS_v3rY_w3irD}
```

## Flag
`ARA2023{j4vaScr1pt_iS_v3rY_w3irD}`
