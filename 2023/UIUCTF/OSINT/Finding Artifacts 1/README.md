# Finding Artifacts 1

## Deskripsi
David is on a trip to collect and document some of the world’s greatest artifacts. He is looking for a coveted bronze statue of the “Excellent One” in New York City. What museum is this located at? The flag format is the location name in lowercase, separated by underscores. <br>
For example: `uiuctf{statue_of_liberty}`

## Hints
- The first two characters of the statue begin with "ma"
- It is very prevalent in southern Asia

## Solusi
Pada challenge ini kita mencari sebuah patung yang terbuat dari perunggu di museum-museum yang ada di kota New York. Dari hint yang pertama kita tahu bahwa patung tersebut berawalan dengan `ma`.

Hasil pencarian google menunjukkan bahwa patung perunggu yang dimaksud adalah `mahakala`. Pencarian dilakukan dengan mencari patung mahakala pada museum yang ada di kota New York. 
Patung tersebut ditemukan pada koleksi dari [Rubin Museum of Art](https://rubinmuseum.org/collection/artwork/six-armed-mahakala)

## Flag
### uiuctf{rubin_museum_of_art}