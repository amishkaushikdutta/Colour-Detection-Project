import sys
import os
import pandas as pd
import cv2
import numpy as np
from tkinter import Tk, filedialog

def resource_path(relative_path):
    """Get absolute path to resource, works for dev and for PyInstaller bundle."""
    if hasattr(sys, '_MEIPASS'):
        # PyInstaller extracts bundled files to a temp folder
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath('.'), relative_path)

# --- Select image via file dialog (no command line needed) ---
Tk().withdraw()  # Hide the root tkinter window
img_path = filedialog.askopenfilename(
    title="Select an Image for Color Detection",
    filetypes=[
        ("Image files", "*.jpg *.jpeg *.png *.bmp *.tiff *.webp"),
        ("All files", "*.*")
    ]
)

if not img_path:
    print("No image selected. Exiting.")
    sys.exit(0)

# Reading image with opencv
img = cv2.imread(img_path)
if img is None:
    print(f"Error: Could not read image at '{img_path}'")
    sys.exit(1)

clicked = False
r = g = b = xpos = ypos = 0

index = ["color", "color_name", "hex", "R", "G", "B"]
csv = pd.read_csv(resource_path('colors.csv'), names=index, header=None)

def getColorName(R, G, B):
    minimum = 10000
    cname = ""
    for i in range(len(csv)):
        d = abs(R - int(csv.loc[i, "R"])) + abs(G - int(csv.loc[i, "G"])) + abs(B - int(csv.loc[i, "B"]))
        if d <= minimum:
            minimum = d
            cname = csv.loc[i, "color_name"]
    return cname

def draw_function(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        global b, g, r, xpos, ypos, clicked
        clicked = True
        xpos = x
        ypos = y
        b, g, r = img[y, x]
        b = int(b)
        g = int(g)
        r = int(r)

cv2.namedWindow('Color Detection - Double-click to detect color (ESC to quit)')
cv2.setMouseCallback('Color Detection - Double-click to detect color (ESC to quit)', draw_function)

while(1):
    cv2.imshow("Color Detection - Double-click to detect color (ESC to quit)", img)
    if (clicked):

        cv2.rectangle(img, (20, 20), (750, 60), (b, g, r), -1)

        text = getColorName(r, g, b) + ' R=' + str(r) + ' G=' + str(g) + ' B=' + str(b)

        cv2.putText(img, text, (50, 50), 2, 0.8, (255, 255, 255), 2, cv2.LINE_AA)

        if(r + g + b >= 600):
            cv2.putText(img, text, (50, 50), 2, 0.8, (0, 0, 0), 2, cv2.LINE_AA)
        clicked = False

    if cv2.waitKey(20) & 0xFF == 27:
        break

cv2.destroyAllWindows()
