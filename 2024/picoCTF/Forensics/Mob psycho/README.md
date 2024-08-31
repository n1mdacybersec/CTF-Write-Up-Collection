# Mob psycho

## Description
Can you handle APKs?
Download the android apk [here](./Challenge/mobpsycho.apk).

## Hints
1. Did you know you can `unzip` APK files?
2. Now you have the whole host of shell tools for searching these files.

## Points
200

## Solution
We got an APK files as attachment for this challenge. APK files is a file format for mobile application for Android-based operating system. For this challenge we got an interesting hint, which said that you can decompress an APK file. This is true, because the package content of APK file is in ZIP archive format, you can read about this information from [Wikipedia](https://en.wikipedia.org/wiki/Apk_(file_format)).

Based on this information, it should be easier to decompile or in this case decompress an APK file, because any tool that could extract or decompress ZIP archive are able to do the job. But, using tools like `unzip` to decompile an APK file will make the content of XML files is hardly readable. Because of this, we can use this [site](https://www.decompiler.com/) to decompile the APK file. After decompiling the APK file, we can download it as a ZIP file.

After decompiling the file, you'll found many files inside the ZIP file. To save time, we can focus on `AndroidManifest.xml` and all of the XML files. You can now open `AndroidManifest.xml` or all the XML files by using text editor because the content is now fully readable. 

However, after spending some time searching for any clue or flag from all the XML files, I couldn't found one. Searching using the format of flag `pico` also reach a dead end. Maybe the flag is not directly written using human readable format, it could be written using base64 encoding or simply that the flag is an image file or files that are not normally in APK package. Then I tried to search all txt files that are available inside the directory. My assumption earlier was right, there's a file called `flag.txt` inside the directory of `res/color`. The content of this `flag.txt` is written using hex encoding.

```
7069636f4354467b6178386d433052553676655f4e5838356c346178386d436c5f35653637656135657d
```

To decode the hex encoding, we can use this command

```bash
echo 7069636f4354467b6178386d433052553676655f4e5838356c346178386d436c5f35653637656135657d | xxd -r -p
```

## Flag
`picoCTF{ax8mC0RU6ve_NX85l4ax8mCl_5e67ea5e}`

