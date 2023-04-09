# useless

## Deskripsi
There's an interesting script in the user's home directory.

The work computer is running SSH. We've been given a script which performs some basic calculations, explore the script and find a flag.

## Points
100

## Solusi
Pada deskripsi terdapat sebuah script yang harus dianalisa untuk mendapatkan flag. Script tersebut bernama `useless` dan berada pada current directory.

```bash
#!/bin/bash
# Basic mathematical operations via command-line arguments

if [ $# != 3 ]
then
  echo "Read the code first"
else
        if [[ "$1" == "add" ]]
        then 
          sum=$(( $2 + $3 ))
          echo "The Sum is: $sum"  

        elif [[ "$1" == "sub" ]]
        then 
          sub=$(( $2 - $3 ))
          echo "The Substract is: $sub" 

        elif [[ "$1" == "div" ]]
        then 
          div=$(( $2 / $3 ))
          echo "The quotient is: $div" 

        elif [[ "$1" == "mul" ]]
        then
          mul=$(( $2 * $3 ))
          echo "The product is: $mul" 

        else
          echo "Read the manual"
         
        fi
fi
```

Flag ditemukan dengan membaca manual dari program tersebut
```
man useless
```

![Flag](./man.png)

## Flag
### picoCTF{us3l3ss_ch4ll3ng3_3xpl0it3d_6173}
