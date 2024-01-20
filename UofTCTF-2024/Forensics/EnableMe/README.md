# EnableMe

## Description
You've received a confidential document! Follow the instructions to unlock it.

Note: This is not malware

Author: SteakEnthusiast

## Attachment
[invoice.docm](./Challenge/invoice.docm)

## Solution
Another challenge involving documents from Microsoft Office files.
In this challenge we were provided with a Word macro document. For macro-enabled document, Microsoft Office always create a separate file extensions for it, in this case .docm file extension for Word macro-enabled document.
When we open the file, there's image in the document and that image have been blurred and the macro of the document will display a message in a pop-up window.

To complete this challenge, the first step is to extract the contents of the file. 
For additional information, Microsoft Office document is actually a zip file, so we can extract the file.
To extract the file we can use `binwalk` command or change the file extension to .zip and extract the archived using 7-zip or similar applications.

```shell
binwalk -e invoice.docm
```

After the file was successfully extracted, I tried to find files that might contain flags by searching based on the pattern of the flag format, i.e. uoftctf but found no results.
Then, I became curious about the macros of this document. 
The macro of this document can be found in the `word` directory and there will be a file with the name `vbaProject.bin` which is the macro of the document.

The `vbaProject.bin` file is a binary file, so we cannot open the file to find out its contents.
Then I found out about [oletools](https://github.com/decalage2/oletools) which is a tools to analyze binary file inside Microsoft Office documents.
Run this command to analyze `vbaProject.bin`.

```shell
olevba vbaProject.bin
```

After executing that command, the tool will return a VBA script.

```VBA
Sub AutoOpen()
    Dim v6 As Variant, v7 As Variant
    v6 = Array(98, 120, 113, 99, 116, 99, 113, 108, 115, 39, 116, 111, 72, 113, 38, 123, 36, 34, 72, 116, 35, 121, 72, 101, 98, 121, 72, 116, 39, 115, 114, 72, 99, 39, 39, 39, 106)
    v7 = Array(44, 32, 51, 84, 43, 53, 48, 62, 68, 114, 38, 61, 17, 70, 121, 45, 112, 126, 26, 39, 21, 78, 21, 7, 6, 26, 127, 8, 89, 0, 1, 54, 26, 87, 16, 10, 84)
    
    Dim v8 As Integer: v8 = 23

    Dim v9 As String, v10 As String, v4 As String, i As Integer
    v9 = ""
    For i = 0 To UBound(v6)
        v9 = v9 & Chr(v6(i) Xor Asc(Mid(Chr(v8), (i Mod Len(Chr(v8))) + 1, 1)))
    Next i

    v10 = ""
    For i = 0 To UBound(v7)
        v10 = v10 & Chr(v7(i) Xor Asc(Mid(v9, (i Mod Len(v9)) + 1, 1)))
    Next i

    MsgBox v10
End Sub
```

Honestly, I know nothing about VBA or VBscript. 
With the help of ChatGPT, I create a python program of that VBA script and show the flag.

```py
def transform(k, key):
    result = ""
    for i in range(len(k)):
        result += chr(k[i] ^ ord(key[i % len(key)]))
    return result

def main():
    v6 = [98, 120, 113, 99, 116, 99, 113, 108, 115, 39, 116, 111, 72, 113, 38, 123, 36, 34, 72, 116, 35, 121, 72, 101, 98, 121, 72, 116, 39, 115, 114, 72, 99, 39, 39, 39, 106]
    v7 = [44, 32, 51, 84, 43, 53, 48, 62, 68, 114, 38, 61, 17, 70, 121, 45, 112, 126, 26, 39, 21, 78, 21, 7, 6, 26, 127, 8, 89, 0, 1, 54, 26, 87, 16, 10, 84]

    v8 = 23

    v9 = transform(v6, chr(v8))
    v10 = transform(v7, v9)

    print(v9)
    print(v10)

if __name__ == "__main__":
    main()
```

## Flag
`uoftctf{d0cx_f1l35_c4n_run_c0de_t000}`
