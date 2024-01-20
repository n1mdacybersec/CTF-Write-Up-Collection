# catch me if you can

## Deskripsi
Somebody [help](https://catch-me-if-you-can.web.actf.co/)!

## Points
10

## Solusi
Pada challenge ini terdapat animasi teks yang berputar menggunakan tag `marquee` yang ada pada HTML.
Tag `marquee` sendiri digunakan untuk membuat animasi teks atau objek bergerak pada HTML tanpa menggunakan CSS. Penjelesan dari `marquee` ada pada link [berikut](https://www.tutorialspoint.com/html/html_marquees.htm)

Untuk mendapatkan flag, hanya perlu menginspect element dari web challenge tersebut. 
```html
<html><head>
<meta http-equiv="content-type" content="text/html; charset=windows-1252">
        <style>
            body {
                font-family: "Comic Sans MS", "Comic Sans", cursive;
            }
            #flag {
                border: 2px solid red;
                position: absolute;
                top: 50%;
                left: 0;
                -moz-user-select: -moz-none;
                -khtml-user-select: none;
                -webkit-user-select: none;
                -ms-user-select: none;
                user-select: none;

                animation-name: spin;
                animation-duration: 3000ms;
                animation-iteration-count: infinite;
                animation-timing-function: linear; 
            }

            @keyframes spin {
                from {
                    transform:rotate(0deg);
                }
                to {
                    transform:rotate(360deg);
                }
            }
        </style>
    </head>
    <body>
        <h1>catch me if you can!</h1>
        <marquee scrollamount="50" id="flag">actf{y0u_caught_m3!_0101ff9abc2a724814dfd1c85c766afc7fbd88d2cdf747d8d9ddbf12d68ff874}</marquee>
    
</body></html>
```

## Flag
### actf{y0u_caught_m3!_0101ff9abc2a724814dfd1c85c766afc7fbd88d2cdf747d8d9ddbf12d68ff874}