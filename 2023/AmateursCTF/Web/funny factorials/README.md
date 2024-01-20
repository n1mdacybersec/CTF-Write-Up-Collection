# funny factorials

## Deskripsi
I made a factorials app! It's so fancy and shmancy. However factorials don't seem to properly compute at big numbers! Can you help me fix it?

[funny-factorials.amt.rs](https://funny-factorials.amt.rs)

## Attachments
[app.py](./Challenge/app.py) [Dockerfile](./Challenge/Dockerfile)

## Solusi
Mari kita lihat `Dockerfile` yang diberikan pada challenge ini.

```dockerfile
FROM python:3.10-slim-buster

RUN pip3 install flask
COPY flag.txt /

WORKDIR /app
COPY app/* /app/
copy app/templates/* /app/templates/
copy app/themes/* /app/themes/

EXPOSE 5000

ENTRYPOINT ["python3", "app.py"]
```

Dari informasi `Dockerfile` tersebut, diketahui bahwa file `flag.txt` dicopy ke direktori `/`.
Selanjutnya dilihat source code dari `app.py`, ditemukan hal menarik seperti berikut ini.

```python
def filter_path(path):
    # print(path)
    path = path.replace("../", "")
    try:
        return filter_path(path)
    except RecursionError:
        # remove root / from path if it exists
        if path[0] == "/":
            path = path[1:]
        print(path)
        return path

@app.route('/')
def index():
    safe_theme = filter_path(request.args.get("theme", "themes/theme1.css"))
    f = open(safe_theme, "r")
    theme = f.read()
    f.close()
    return render_template('index.html', css=theme)
```

Pada potongan source code tersebut, diketahui bahwa terdapat fungsi untuk melakukan pengecekan path yang dimasukkan, disini terlihat bahwa path `../` akan dihapus dan jika terdapat `/` juga akan dihapus.
Kemudian diketahui juga kita bisa memanggil css yang berbeda dengan menggunakan methode GET `theme` dan secara default css yang ditampilkan adalah `theme=themes/theme1.css`.

Untuk mendapatkan flag yang dianggap sebagai css yang ditampilkan di website tersebut, kita perlu melihat kembali pengecekan path yang ada pada website ini. Dimana setiap terdapat `/` atau `../` akan dihapus.
Jika kita memasukkan `/` pada `theme=/` maka hasilnya adalah `theme=`, namun jika kita memasukkan `//` tidak akan terhapus karena tidak memenuhi satupun kondisi pada fungsi filter_path(). 
Flag didapatkan dengan memasukkan URL berikut ini.

```
https://funny-factorials.amt.rs/?theme=//flag.txt
```

![Flag](./flag.png)

## Flag
### amateursCTF{h1tt1ng_th3_r3curs10n_l1mt_1s_1mp0ssibl3}