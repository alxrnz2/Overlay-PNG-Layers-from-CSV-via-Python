# Overlay-PNG-Layers-from-CSV-via-Python
Overlay PNG layers according to a CSV file using a Python script and the Pillow library.

## Overview

Our `Compiler.py` python script overlays PNG layers to create a new PNG, based on instructions in a CSV file. Before modifying and running this script, you'll need PNG layers to combine and a CSV file containing the filenames of those layers in the order you'd like them to be overlaid.

The script imports the `csv` module to read your CSV file and the `PIL` (or [Pillow](https://pillow.readthedocs.io/en/stable/)) library to manipulate image files.

## Steps to update `Compiler.py`

First, adjust `Compiler.csv` to match the filename of your CSV roster.

Then, adjust the layer objects for the layers in your project. For the [Yellowstone Firepit Crew](https://firepitcrew.org/), each image consisted of five layers (background, hobby, body, eyes and a special object). And each image was named per the first column of the CSV.

For debugging purposes, we use descriptive labels for each variable.

```
name = row[0]
backgroundimg = row[1]
hobbyimg = row[2]
bodyimg = row[3]
eyesimg = row[4]
specialimg = row[5]
```

Sync any changes above to the below commands: opening each layer and then pasting each layer on the background. Replace the `background` prefix for the `paste` and `save` commands with your first layer.

```
background = Image.open(backgroundimg+".png")
hobby = Image.open(hobbyimg+".png")
body = Image.open(bodyimg+".png")
eyes = Image.open(eyesimg+".png")
special = Image.open(specialimg+".png")
...
background.paste(hobby,(0,0),hobby)
background.paste(body,(0,0),body)
background.paste(eyes,(0,0),eyes)
background.paste(special,(0,0),special)
...
background.save(name+".png", "PNG")
```

## Create your new PNGs

Run the `Compiler.py` script in your IDE/CLI of choice. If you're new to Python scripts, check out this [Python tutorial](https://code.visualstudio.com/docs/python/python-tutorial) from [VS Code](https://code.visualstudio.com/).
