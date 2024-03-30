# Super SSH

## Description
Using a Secure Shell (SSH) is going to be pretty important. 
Can you `ssh` as `ctf-player` to `titan.picoctf.net` at port `60572` to get the flag? You'll also need the password `1ad5be0d`. 
If asked, accept the fingerprint with `yes`. <br>
If your device doesn't have a shell, you can use: https://webshell.picoctf.org <br>
If you're not sure what a shell is, check out our Primer: https://primer.picoctf.com/#_the_shell

## Hints
1. https://linux.die.net/man/1/ssh
2. You can try logging in 'as' someone with `<user>@titan.picoctf.net`
3. How could you specify the port?
4. Remember, passwords are hidden when typed into the shell

## Points
25

## Solution
In order to connect to the challenge machine using SSH to get the flag, we can use this command below

```sh
ssh ctf-player@titan.picoctf.net -p 60572
```

You need to accept the certificate by typing `yes`. Input the password to get the flag

## Flag
`picoCTF{s3cur3_c0nn3ct10n_8306c99d}`
