# Soft Glow Image Filter 🖼✨

This Python project applies a **soft glow effect** to images using the Pillow (PIL) library. Originally built in Google Colab, it allows users to upload images, process them with a glow effect, and download the enhanced results.

## 🔍 Overview

The soft glow effect creates a dreamy aesthetic by:
- Slightly increasing brightness
- Applying a Gaussian blur
- Enhancing color saturation
- Blending the blurred image with the original

This project is ideal for simple image enhancement or artistic photo edits.

## 📂 File

- `dip_cec.py` – Main Python script that processes uploaded images and applies the glow effect.

## 🚀 How It Works

1. Upload an image (JPG/PNG).
2. The script:
   - Converts the image to RGBA format.
   - Enhances brightness and color.
   - Applies a Gaussian blur.
   - Blends the blurred image with the original.
3. Displays the original and processed images.
4. Saves and downloads the new image.

## 🛠 Requirements

- Python 3.x
- [Pillow](https://pillow.readthedocs.io/en/stable/) (`pip install pillow`)
- [matplotlib](https://matplotlib.org/) (`pip install matplotlib`)
- Google Colab or a Jupyter-compatible environment (for upload/download functionality)

## 🔧 How to Use

1. Open the script in Google Colab or a Python environment.
2. Run all cells.
3. Upload your image when prompted.
4. View and save the output image.

## 📷 Example

| Original | Soft Glow |
|----------|-----------|
| ![original](example_original.png) | ![glow](example_glow.png) |

*Replace the above images with your own before uploading.*

## 📄 License

MIT License – feel free to use, modify, and share!

---

Feel free to fork the project, star it, or contribute with new effects and features!
