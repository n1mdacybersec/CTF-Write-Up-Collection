# funny factorials

## Description
I made a factorials app! It's so fancy and shmancy. However factorials don't seem to properly compute at big numbers! Can you help me fix it?

[funny-factorials.amt.rs](https://funny-factorials.amt.rs)

## Attachments
[app.py](./Challenge/app.py) [Dockerfile](./Challenge/Dockerfile)

## Solution
First, let's take a look at the `Dockerfile` for this challenge.

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

The information that I got from the `Dockerfile` is that the `flag.txt` file is copied to the `/` directory. Now, let's take a look at the source code of the `app.py`. This is the interesting part of the `app.py`.

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

From the snippet of the source code, we know that the `filter_path` method or function is a function to check the path entered by the user. This function will remove and replace the user input that contains `../` or `/`.
Then, for the `/` route there's an `index` function that called `filter_path` when the user choose the theme for the website. By default the value of this theme is `theme=themes/theme1.css`. Because this value can be controlled by the user it might be the vulnerability for this chalenge.

For retrieving the flag, we can bypass the `filter_path` function. As I said earlier, this function will remove `../` or `/` from the input.
For example, if we enter `theme=/` as an input the result will be like this `theme=`. But, it doesn't mean that we cannot read the flag that are located in `/flag.txt`. If we enter something like `//` it will not be removed by the function, because it doesn't satisfy any conditions in the `filter_path` function.
To get the flag, enter this URL:

```
https://funny-factorials.amt.rs/?theme=//flag.txt
```

![Flag](./flag.png)

## Flag
`amateursCTF{h1tt1ng_th3_r3curs10n_l1mt_1s_1mp0ssibl3}`