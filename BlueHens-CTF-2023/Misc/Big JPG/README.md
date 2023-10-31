# Big JPG

## Description
There's more data to this image than what meets the eye.

-azroberts

## Attachment
[big-image.jpg](./Challenge/big-image.jpg)

## Solution
I got a jpg image for this challenge, and the description of the challenge said there's more data in this image.
For this challenge I will use https://www.aperisolve.com/ to extract any other informations from this image. The tool at Aperi'Solve combining all tool that we need for Steganography for image file.

Using this website there's xz compressed data.
![xz compressed data](./binwalk.png)

After extracting the xz compressed data, there was a `605EA` file.
Check using `file` command and the result show that the file was tar compressed data, so we can extract it again.

![Check the type of file](./file_command.png)

After extracting file `605EA` we got 2 images, `key.png` and `flag.jpg`.
Let's check the `key.png` first using Aperi'Solve.

From `key.png` file, we know there's password from `zsteg` tool.
Probably this password was used for hide secret information using `zsteg` or `steghide` for `flag.jpg`.

![Password found from key.png](./password.png)

Then, let's try to check the last image `flag.jpg` using Aperi'Solve. 
But before we submit the image as is, let's change a bit parameter first because we got a password in the previous step.
Before submitting the image, make sure you click enabled on `I've got a password !` and insert the password there. After you done with inserting the password, click submit.

![Insert password](./insert_password.png)

From `steghide` tool we got a `flag.txt` file. It should be the flag for this challenge.

![steghide successfully recover a flag](./steghide.png)

## Flag
`UDCTF{lay3r5_0n_lay3r5}`



