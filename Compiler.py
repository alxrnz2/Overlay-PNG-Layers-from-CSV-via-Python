import csv
from PIL import Image
with open('Compiler.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count >= 0:
            line_count += 1
        
            name = row[0]
            backgroundimg = row[1]
            hobbyimg = row[2]
            bodyimg = row[3]
            eyesimg = row[4]
            specialimg = row[5]

            background = Image.open(backgroundimg+".png")
            hobby = Image.open(hobbyimg+".png")
            body = Image.open(bodyimg+".png")
            eyes = Image.open(eyesimg+".png")
            special = Image.open(specialimg+".png")

            background.paste(hobby,(0,0),hobby)
            background.paste(body,(0,0),body)
            background.paste(eyes,(0,0),eyes)
            background.paste(special,(0,0),special)

            background.save(name+".png", "PNG")
        else:
            line_count += 1
    print(f'Processed {line_count} lines.')