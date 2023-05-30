# Subliminal#2

## Deskripsi
An image has been hidden in this video. Don't fall into madness.

Little squares size : 20x20 pixels

Format : `Hero{}`

## Attachment
[subliminal_hide](./Challenge/subliminal_hide.mp4)

## Solusi
File yang diberikan memiliki sebuah gambar seperti bagian dari flag yang melintasi seluruh video, seperti berikut ini.
![1.png](./1.png)

Dari deskripsi challenge, bagian flag dibagi menjadi gambar-gambar kecil berukuran 20x20. 
Program Python berikut akan mendapatkan gambar-gambar kecil berukuran 20x20 dan menggabungkannya.

```python
import cv2
import numpy as np
import argparse

def extractor(video_path, output_path):
    video = cv2.VideoCapture(video_path)
    width = int(video.get(3))
    height = int(video.get(4))

    # Black image at the beginning
    image = np.zeros((height, width, 3), np.uint8)

    i = 0
    while True:
        # Read a video frame
        ret, frame = video.read()
        if not ret:
            break

        # Get the square and add it to the flag file
        x = i % (width // 20) * 20
        y = i // (width // 20) * 20
        image[y:y+20, x:x+20] = frame[y:y+20, x:x+20]
        i += 1
    
    cv2.imwrite(output_path, image)
    video.release()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--path", help="Path of the video")
    parser.add_argument("-o", "--output", help="Output path of the video")

    args = parser.parse_args()
    video_path = args.path
    output_path = args.output

    if video_path and output_path is not None:
        extractor(video_path, output_path)
    else:
        print("Video not found")
```

Untuk menjalankan program seperti berikut ini

```
python3 program.py -p subliminal_hide.mp4 -o flag.png
```

Flagnya seperti berikut ini

![flag](./flag.png)

## Flag
### Hero{Not_So_Subliminal}