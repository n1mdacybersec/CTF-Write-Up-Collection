# Commitment Issues

## Description
I accidentally wrote the flag down. Good thing I deleted it!
<br>
You download the challenge files here: 
[challenge.zip](./Challenge/challenge.zip)

## Hints
1. Version control can help you recover files if you change or lose them!
2. Read the chapter on Git from the picoPrimer [here](https://primer.picoctf.org/#_git_version_control)
3. You can 'checkout' commits to see the files inside them

## Points
50

## Solution
After extracting the challenge file, there's only message.txt inside that directory.
But if you use `ls -la` it will show a hidden file, a .git file.

```sh
$ ls -la
drwxr-xr-x 3 picoctf picoctf   37 Mar 30 08:49 .
drwxr-xr-x 9 picoctf picoctf 4096 Mar 30 08:44 ..
drwxr-xr-x 8 picoctf picoctf  166 Mar 30 08:49 .git
-rw-r--r-- 1 picoctf picoctf   11 Mar  9 21:10 message.txt
```

As you know .git file is a version control from git.
To start tracking commits and branches, we can type:

```sh
git init
```

After initializing the directory, we can use check the log of commits.

```sh
git log
```

![git commit history](./1.png)

We could see there's commit with the message "remove sensitive info" and that's our last commit.
For retrieving the flag, we need to copy the commit id with commit message "create flag".

```sh
git checkout e720dc26a1a55405fbdf4d338d465335c439fb3e
```

Now we just need to check the content of `message.txt`

```sh
cat message.txt
```

## Flag
`picoCTF{s@n1t1z3_7246792d}`
