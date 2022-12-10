#Import csv module to intepret CSV roster and Pillow library to manipulate image files
import csv
from PIL import Image

#Update file name of CSV if needed
with open('Compiler.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    
    #Change to a higher line to redo specific combinations if desired
    line_count = 0
    
    #Loops through each line in the CSV
    for row in csv_reader:
        if line_count >= 0:
            line_count += 1
        
            #Customize for your project; for the Firepit Crew (see firepitcrew.org), each animal portrait consisted of 5 layers
            name = row[0]
            backgroundimg = row[1]
            hobbyimg = row[2]
            bodyimg = row[3]
            eyesimg = row[4]
            specialimg = row[5]

            #Layer filenames must match the CSV exactly to open the correct layer
            background = Image.open(backgroundimg+".png")
            hobby = Image.open(hobbyimg+".png")
            body = Image.open(bodyimg+".png")
            eyes = Image.open(eyesimg+".png")
            special = Image.open(specialimg+".png")

            #Pastes each open layer on the first background layer (hobby, body, eyes, and finally, special)
            background.paste(hobby,(0,0),hobby)
            background.paste(body,(0,0),body)
            background.paste(eyes,(0,0),eyes)
            background.paste(special,(0,0),special)

            #Saves the overlayed layers as a new PNG, named per the first column in the CSV
            background.save(name+".png", "PNG")
        else:
            line_count += 1
    print(f'Processed {line_count} lines.')
