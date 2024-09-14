# Gitint 5e

## Description
One of the repos in the les-amateurs organization is kind of suspicious. Can you find all the real flags in that repository and report back? There are 3 flags total, one of which is worth 0 points. For this challenge, submit the flag with the sha256 hash 
```
5e60b82a7b0860b53b6f100f599a5e04d52faf1a556ea78578e594af2e2ccf7c
```

## Solution
Following the title and description of  this challenge, this might be related to Github repository. Let's try to search on Google with the keyword `les-amateurs`, maybe we can find the Github account or organization. I found the Github account of [les-amateurs](https://github.com/les-amateurs/more-CTFd-mods/branches).
After I found the Github account, now I need to narrowed down the interesting repositories on this Github account that hold the flag for this challenge. I'm looking at the commit date that are close to the time when this CTF was held. Following this method, I found this [repository](https://github.com/les-amateurs/more-CTFd-mods/branches). This repository have 2 branches and one of them is `flag` branch. Hmm, interesting, now let's take a look at this branch. In this branch, I found the flag in the commits with the message Initial Commit and Update README.md.

![Flag on commits](./flag.png)

Now, let's check the flag by using the SHA256 hash that are provided to the description of this challenge. If the result is same, then this is a real flag for this challenge.

```
$ echo -n 'amateursCTF{y0u-fOunD_m3;bu7:d1D U r34L!y?}' | sha256sum
5e60b82a7b0860b53b6f100f599a5e04d52faf1a556ea78578e594af2e2ccf7c  -
```

## Flag
`amateursCTF{y0u-fOunD_m3;bu7:d1D U r34L!y?}`
