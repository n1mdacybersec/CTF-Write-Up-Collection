# Scan Surprise

## Description

I've gotten bored of handing out flags as text. Wouldn't it be cool if they were an image instead? <br>
You can download the challenge files here: <br>
[challenge.zip](./Challenge/challenge.zip)

Additional details will be available after launching your challenge instance.

**NOTE: This is an instance challenge, start the instance to get more information**

## Hints
1. QR codes are a way of encoding data. While they're most known for storing URLs, they can store other things too.
2. Mobile phones have included native QR code scanners in their cameras since version 8 (Oreo) and iOS 11
3. If you don't have access to a phone, you can also use zbar-tools to convert an image to text

## Points
50

## Solution

After unzipping the file, there's `flag.png` that appeared as QR code.
To get the flag in this challenge is pretty easy, you just need to scan the QR code.
In this case I used [cyberchef](https://gchq.github.io/CyberChef/).

## Flag
`picoCTF{p33k_@_b00_b5ce2572}`
