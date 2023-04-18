# Safe Opener 2

## Deskripsi
What can you do with this file?
I forgot the key to my safe but this [file](https://artifacts.picoctf.net/c/289/SafeOpener.class) is supposed to help me with retrieving the lost key. Can you help me unlock my safe?

## Hint
1. Download and try to decompile the file.

## Solusi
Diberikan suatu file [class](Challenge/SafeOpener.class) dan kita diberikan instruksi untuk meretrieve key yang terdapat di dalam file `class` tersebut. Pada hint sudah diberikan bantuan bahwa cobalah untuk melakukan decompile pada file tersebut.

Kita melakukan decompile menggunakan `jd-gui`, dikarenakan tools tersebut mempermudah kami dan file yang diberikan juga dalam ekstensi `.class` yang mana merupakan ekstensi dari file `Java`.

Ketika kita membukanya menggunakan `jd-gui` dan melihat isi dari source file, langsung terlihat flagnya di dalam fungsi `openSafe()`.
```java
public static boolean openSafe(String password) {
    String encodedkey = "picoCTF{SAf3_0p3n3rr_y0u_solv3d_it_de45efd6}";
    if (password.equals(encodedkey)) {
      System.out.println("Sesame open");
      return true;
    } 
    System.out.println("Password is incorrect\n");
    return false;
  }
```

Berikut merupakan screenshot dari keseluruhan source codenya.
[Result](result.png)

## Flag
### picoCTF{SAf3_0p3n3rr_y0u_solv3d_it_de45efd6}
