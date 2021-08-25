import cv2
import pandas as pd
import argparse

# exception handling for wrong image path input by the user
try:
# Reading the image with opencv
# please insert the path containg the image you want to train here
 img = cv2.imread(r"C:\Users\shubh\Downloads\testimage.jpg")

#Global variables declaration to be used later on
 mouseclick = False
 r = g = b = xposition = yposition = 0

#Read through the generated csv file using pandas and assigning names to each of the columns
 index=["color","Name_of_color","hex","R","G","B"]
 csv = pd.read_csv('training_data_1.csv', names=index, header=None)

#This function calculates the distance from all colors and calculates distance
# to get the most fitting colors
 def NametheColor(R,G,B):
     minimum = 10000
     for i in range(len(csv)):
         d = abs(R- int(csv.loc[i,"R"])) + abs(G- int(csv.loc[i,"G"]))+ abs(B- int(csv.loc[i,"B"]))
         if(d<=minimum):
             minimum = d
             colname = csv.loc[i,"Name_of_color"]
     return colname

#Function to get the xposition and yposition ahen mouse clicked at a certain location
 def getnbox_function(event, x,y,flags,param):
     if event == cv2.EVENT_LBUTTONDBLCLK:
         global b,g,r,xposition,yposition, mouseclick
         mouseclick = True
         xposition = x
         yposition = y
         b,g,r = img[y,x]
         b = int(b)
         g = int(g)
         r = int(r)
       
 cv2.namedWindow('image')
 cv2.setMouseCallback('image',getnbox_function)

 while(1):

     cv2.imshow("image",img)
     if (mouseclick):
   
        #cv2.rectangle arguments:imagefile, startingpoint, endingpoint, color name, thickness
        # -1 to fill it completely
         cv2.rectangle(img,(20,20), (750,60), (b,g,r), -1)

        #Forming the string of text for displaying detected color name
        # and their corresponding R G B values
         text = NametheColor(r,g,b) + ' R='+ str(r) +  ' G='+ str(g) +  ' B='+ str(b)
        
        #cv2.putText arguments: image name, text, start, font size, display color,
        # thickness and Linetype
         cv2.putText(img, text,(50,50),2,0.8,(255,255,255),2,cv2.LINE_AA)

        #Information Text in black color when detected is light in nature
         if(r+g+b>=600):
             cv2.putText(img, text,(50,50),2,0.8,(0,0,0),2,cv2.LINE_AA)
            
         mouseclick=False

    #After detection we can sue the "Esc" key to break out of the loop and end execution
     if cv2.waitKey(20) & 0xFF ==27:
         break
    
 cv2.destroyAllWindows()
except:
    print("Please the correct path containing the test image")
