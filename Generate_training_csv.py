# This generates the training data .csv file containing name of colors,
# hex code, R G B values for all the colors
import csv
from PIL import Image
import matplotlib

#Input of the path where the training images are stored
path = r"C:\Users\shubh\Downloads\colorpic.jpg"
im = Image.open(path)
pixels = list(im.getdata())

# Generation of the csv file containing the B G R values as indices
with open("training_data_1.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(pixels)
with open('training_data_1.csv', newline='') as csvfile:
    pixels = csv.reader(csvfile, delimiter=' ')

col_hex = matplotlib.colors.cnames["black"]

# Prepend of the color tag in the generated csv file
x11 = open(r'C:\Users\shubh\PycharmProjects\Color_detection_task_SubhasankarDwibedi\training_data_1.csv')
y11 = csv.reader(x11)
z11 = []
# Generatig the list of  RGB values
for row in y11:
    z11.append(['black'] + ['Black_Color'] + ['col_hex'] + row)
#Converting the list type to csv file columns appended for generating training csv file
with open("training_data_1.csv", "w", newline="") as f1:
    writer = csv.writer(f1)
    writer.writerows(z11)
with open('training_data_1.csv', newline='') as csvfile:
    z11 = csv.reader(csvfile, delimiter=' ')

# The traing file "training_data_1.csv" is created and ready for training
# This generated file is to be used in the "Detect_color.py" file

