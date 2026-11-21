# 🎨 Color Detection from Image

A Python application that detects and identifies colors from any image in real time. Simply double-click on any pixel in the image, and the app instantly displays the **color name** along with its **RGB values** — matched from a dataset of **865 colors**.

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)
![OpenCV](https://img.shields.io/badge/OpenCV-4.x-green?logo=opencv&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-2.x-purple?logo=pandas&logoColor=white)
![Platform](https://img.shields.io/badge/Platform-Windows-lightgrey?logo=windows&logoColor=white)

---

## 📌 About

Ever looked at a color in an image and wondered what it's called? This project solves that. It uses **OpenCV** to load and display an image, captures mouse click events, reads the pixel's BGR values, and matches them to the closest color name from a comprehensive CSV dataset using **Manhattan distance**.

The color name and RGB values are displayed as an overlay on the image — with automatic text color adjustment (white on dark backgrounds, black on light backgrounds) for readability.

---

## ✨ Features

- 🖱️ **Interactive Detection** — Double-click anywhere on the image to identify the color
- 🏷️ **865 Named Colors** — Matches against a comprehensive color database
- 📊 **RGB Display** — Shows the exact R, G, B values alongside the color name
- 🎯 **Closest Match Algorithm** — Uses Manhattan distance for accurate color matching
- 🔄 **Adaptive Text** — Automatically switches text color for readability on light/dark backgrounds
- 💻 **Standalone Executable** — Pre-built `.exe` available (no Python installation needed)
- 📂 **File Picker GUI** — The executable version opens a file dialog to select images (no command line required)

---

## 🗂️ Project Structure

```
Color_Detection_Project/
├── color_detection.py          # Main script (CLI version)
├── color_detection_exe.py      # Executable version (GUI file picker)
├── colors.csv                  # Dataset with 865 color names and RGB values
├── Sample Image.jpg            # Sample image for testing
├── dist/
│   └── Color Detection.exe     # Standalone Windows executable
├── requirements.txt            # Python dependencies
└── README.md
```

---

## 🚀 Getting Started

### Option 1: Run the Executable (Easiest)

> No Python installation required!

1. Download `Color Detection.exe` from the [`dist/`](dist/) folder
2. **Double-click** the `.exe` file
3. A file picker dialog opens — **select any image**
4. Double-click on the image to detect colors
5. Press **ESC** to quit

### Option 2: Run with Python

#### Prerequisites

- Python 3.x
- pip

#### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/<your-username>/Color-Detection-Project.git
   cd Color-Detection-Project
   ```

2. **Install dependencies**
   ```bash
   pip install opencv-python pandas numpy
   ```

3. **Run the application**
   ```bash
   python color_detection.py -i "Sample Image.jpg"
   ```
   Replace `"Sample Image.jpg"` with the path to any image of your choice.

---

## 🖼️ How to Use

1. Run the application with an image (see above)
2. An OpenCV window opens displaying your image
3. **Double-click** on any spot in the image
4. A colored rectangle appears at the top showing:
   - The **color name** (e.g., "Tomato")
   - The **RGB values** (e.g., R=255 G=99 B=71)
5. Keep clicking on different areas to detect more colors
6. Press **ESC** to close the window

---

## 🔧 How It Works

1. **Image Loading** — The image is loaded using OpenCV's `imread()`
2. **Mouse Event Capture** — A callback function listens for double-click events and captures the pixel's BGR values at that coordinate
3. **Color Matching** — The RGB values are compared against all 865 entries in `colors.csv` using **Manhattan distance**:

   $$d = |R_1 - R_2| + |G_1 - G_2| + |B_1 - B_2|$$

   The color with the smallest distance is selected as the match.
4. **Display** — A rectangle filled with the detected color is drawn on the image, with the color name and RGB values overlaid as text

---

## 📦 Dependencies

| Package | Purpose |
|---------|---------|
| `opencv-python` | Image loading, display, and mouse event handling |
| `pandas` | Reading and querying the color dataset (CSV) |
| `numpy` | Pixel array operations |

---

## 🛠️ Build Executable Yourself

To build the standalone `.exe` from source:

```bash
pip install pyinstaller
pyinstaller --onefile --windowed --name "Color Detection" --add-data "colors.csv;." color_detection_exe.py
```

The executable will be generated in the `dist/` folder.

---

## 👤 Author

**Amish Kaushik Dutta**
Roll No: 24EA4CS05

---

## 📄 License

This project is open source and available for educational purposes.
