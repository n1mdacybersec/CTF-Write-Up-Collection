# Celeste Tunneling Association

## Deskripsi
[Welcome to the tunnels!!](https://pioneer.tailec718.ts.net/) Have fun!

[Here's the source](./Challenge/server.py)

## Points
40

## Solusi

Jika dilihat dari source code yang diberikan, terlihat bahwa untuk mendapatkan source perlu untuk mengatur header `Host: flag.local`.

```python
SECRET_SITE = b"flag.local"
FLAG = os.environ['FLAG']
...

    if num_hosts == 1:
        for name, value in headers:
            if name == b"host" and value == SECRET_SITE:
                await send({
                    'type': 'http.response.body',
                    'body': FLAG.encode(),
                })
                return
```

Sehingga hanya perlu membuat request ke server dengan menggunakan header `Host: flag.local` seperti berikut ini
![Request to server](./request.png)

## Flag
### actf{reaching_the_core_chapter_8}