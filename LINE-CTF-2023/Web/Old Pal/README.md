# Old Pal

## Deskripsi
How about an Old Pal for your aperitif?
http://104.198.120.186:11006/cgi-bin/main.pl?password= 

## Solusi
Pada challenge ini untuk mendapatkan flag harus memasukkan nilai password yang benar.
Source code diberikan berupa program yang dibuat menggunakan Perl.

```perl
#!/usr/bin/perl
use strict;
use warnings;

use CGI;
use URI::Escape;


$SIG{__WARN__} = \&warn;
sub warn {
    print("Hacker? :(");
    exit(1);
}


my $q = CGI->new;
print "Content-Type: text/html\n\n";


my $pw = uri_unescape(scalar $q->param("password"));
if ($pw eq '') {
    print "Hello :)";
    exit();
}
if (length($pw) >= 20) {
    print "Too long :(";
    die();
}
if ($pw =~ /[^0-9a-zA-Z_-]/) {
    print "Illegal character :(";
    die();
}
if ($pw !~ /[0-9]/ || $pw !~ /[a-zA-Z]/ || $pw !~ /[_-]/) {
    print "Weak password :(";
    die();
}
if ($pw =~ /[0-9_-][boxe]/i) {
    print "Do not punch me :(";
    die();
}
if ($pw =~ /AUTOLOAD|BEGIN|CHECK|DESTROY|END|INIT|UNITCHECK|abs|accept|alarm|atan2|bind|binmode|bless|break|caller|chdir|chmod|chomp|chop|chown|chr|chroot|close|closedir|connect|cos|crypt|dbmclose|dbmopen|defined|delete|die|dump|each|endgrent|endhostent|endnetent|endprotoent|endpwent|endservent|eof|eval|exec|exists|exit|fcntl|fileno|flock|fork|format|formline|getc|getgrent|getgrgid|getgrnam|gethostbyaddr|gethostbyname|gethostent|getlogin|getnetbyaddr|getnetbyname|getnetent|getpeername|getpgrp|getppid|getpriority|getprotobyname|getprotobynumber|getprotoent|getpwent|getpwnam|getpwuid|getservbyname|getservbyport|getservent|getsockname|getsockopt|glob|gmtime|goto|grep|hex|index|int|ioctl|join|keys|kill|last|lc|lcfirst|length|link|listen|local|localtime|log|lstat|map|mkdir|msgctl|msgget|msgrcv|msgsnd|my|next|not|oct|open|opendir|ord|our|pack|pipe|pop|pos|print|printf|prototype|push|quotemeta|rand|read|readdir|readline|readlink|readpipe|recv|redo|ref|rename|require|reset|return|reverse|rewinddir|rindex|rmdir|say|scalar|seek|seekdir|select|semctl|semget|semop|send|setgrent|sethostent|setnetent|setpgrp|setpriority|setprotoent|setpwent|setservent|setsockopt|shift|shmctl|shmget|shmread|shmwrite|shutdown|sin|sleep|socket|socketpair|sort|splice|split|sprintf|sqrt|srand|stat|state|study|substr|symlink|syscall|sysopen|sysread|sysseek|system|syswrite|tell|telldir|tie|tied|time|times|truncate|uc|ucfirst|umask|undef|unlink|unpack|unshift|untie|use|utime|values|vec|wait|waitpid|wantarray|warn|write/) {
    print "I know eval injection :(";
    die();
}
if ($pw =~ /[Mx. squ1ffy]/i) {
    print "You may have had one too many Old Pal :(";
    die();
}


if (eval("$pw == 20230325")) {
    print "Congrats! Flag is LINECTF{redacted}"
} else {
    print "wrong password :(";
    die();
};
```

Dari program tersebut kita tidak bisa menggunakan evaluation injection atau semacamnya karena terdapat blacklist yang mencegah untuk mengeksploitasi metode tersebut.
Jika dilihat, program tersebut sudah terdapat password yang diketahui, yaitu `20230325`. Namun tidak bisa hanya memasukkan password berupa angka saja karena pada program terdapat beberapa pengecekan untuk password yang dimasukkan supaya valid, seperti di bawah ini:
- Password tidak boleh kosong
- Password tidak boleh lebih dari 20 karakter
- Password harus terdiri atas angka `0-9`, huruf `a-z` atau `A-Z`, dan harus terdiri dari spesial karakter `_` atau `-`.

Salah satu hal menarik yang bisa dilakukan adalah dengan menggunakan v-string pada Perl untuk tetap memenuhi kriteria di atas namun juga nilai password yang dimasukkan tetap sama, yaitu `20230325`. V-string adalah nilai desimal dari ASCII yang dapat dibaca oleh Perl sebagai karakter dari ASCII. Referensinya ada pada link berikut [ini](https://www.tutorialspoint.com/v-strings-in-perl).

Password yang akan digunakan adalah nilai 20230325 dikurangi dengan v-string dari bilangan 0. 
Sehingga nilai dari 20230325 masih tetap sama, karena nilai yang pengecekan kondisi dari `20230325` bertipe integer. 
Password yang digunakan untuk mendapatkan flag adalah seperti berikut ini.

![Using v-string to make the if condition true](./solved.png)

Penjelasan dari password yang digunakan di atas seperti berikut ini. Nilai dari v-string `v48` adalah bilangan 0, merujuk pada tabel ASCII. Jika nilai `20230325-v48` maka hasil akhirnya adalah tetap `20230325` karena bilangan integer apapun dikurangi dengan 0 nilainya pasti sama.

``` perl
$pw = 20230325;
$zeroChar = v48; # represent 0 in ASCII
$pw2 = $pw-$zeroChar;

print "The value of pw = $pw\n";
print "The value of pw2 = $pw2\n";

if(eval("$pw == $pw2")){
    print "True";
}

# Output
# The value of pw = 20230325
# The value of pw2 = 20230325
# True
```

## Flag
### LINECTF{3e05d493c941cfe0dd81b70dbf2d972b}