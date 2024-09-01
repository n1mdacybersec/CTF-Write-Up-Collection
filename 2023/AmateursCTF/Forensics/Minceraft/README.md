# Minceraft

## Description
I found these suspicious files on my minecraft server and I think there's a flag in them. I'm not sure where though.

Note: you do not need minecraft to solve this challenge. Maybe reference the minecraft region file format wiki?

## Attachments
[r.1.135.mca](./Challenge/r.1.135.mca)
[r.1.136.mca](./Challenge/r.1.136.mca)
[r.2.135.mca](./Challenge/r.2.135.mca)
[r.2.136.mca](./Challenge/r.2.136.mca)

## Solution
A little disclaimer, honestly for this challenge is the first type of minecraft challenge that I have ever tried, so I apologize if there is some information that is lacking or wrong.
Knowledge about minecraft can increase the level of understanding to complete this challenge, but it does not rule out the possibility for someone who does not understand anything about minecraft to still be able to complete this challenge.

In this challenge there are 4 .mca files or minecraft [anvil file format](https://minecraft.fandom.com/wiki/Anvil_file_format) which is an improvement of previous version [region file format](https://minecraft.fandom.com/wiki/Region_file_format). This file stores [chunks](https://minecraft.fandom.com/wiki/Chunk_format) from minecraft Java edition. Inside this chunks is a structure of tags that stores data, which is called NBT (Named Binary Tag). Additional information about NBT can be found at this [link](https://minecraft.fandom.com/wiki/NBT_format).

To solve this challenge we don't need to install minecraft, because based on my search result on Google there's an application that could open, read, and edit data from .mca file, this application is called [NBTExplorer](https://www.minecraftforum.net/forums/mapping-and-modding-java-edition/minecraft-tools/1262665-nbtexplorer-nbt-editor-for-windows-and-mac).

The first step is to open all the .mca files in NBTExplorer. The interesting part about NBT is we can change the attributes of items in game by changing the tag and its value, such as changing attribute of weapons or armors that normally use an anvil, but instead we can use NBT to directly change its value (like some cheat). In this [video](https://www.youtube.com/watch?v=tb_G8lqNZQ4) there's an example how the attribute of item are changed by editing the value of the tag.
The next step is to search for the flag in all of .mca files. In this challenge I don't exactly know if the flag is written following the flag format, which is `amateursCTF{flag}`, that's why the search is done by looking at the value of the tag. To find a value on tag or any chunks in NBTExplorer, click Search menu > Find and insert the tag at the Name coloumn.
The search results show the flag is in the file `r.1.135.mca` at chunk `30, 18`.

![Flag in tallgrass block](./flag.png)

## Flag
`amateursCTF{cow_wear_thing_lmao_0f9183ca}`
