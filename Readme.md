<h1 align="center">BING Images Scraper and Downloader</h1>
<p align="center">
    <img alt="Version" src="https://img.shields.io/badge/Version-0.1.0-blue?style=for-the-badge&color=blue">
    <img alt="Stars" src="https://img.shields.io/github/stars/Gabi-Zar/bing_images_scraper?style=for-the-badge&color=magenta">
    <img alt="Forks" src="https://img.shields.io/github/forks/Gabi-Zar/bing_images_scraper?color=cyan&style=for-the-badge&color=purple">
    <img alt="License" src="https://img.shields.io/github/license/Gabi-Zar/bing_images_scraper?style=for-the-badge&color=blue">
    <br>
    <a href="https://github.com/Gabi-Zar"><img title="Developer" src="https://img.shields.io/badge/Developer-GabiZar-red?style=flat-square"></a>
    <img alt="Maintained" src="https://img.shields.io/badge/Maintained-No-blue?style=flat-square">
    <img alt="Written In" src="https://img.shields.io/badge/Written%20In-Python-yellow?style=flat-square">
</p>


This repository contains a Python script designed to search a content on bing and download every images

> [!CAUTION]
> Use this script responsibly. Please respect copyright and usage right of downloaed images.

## 🌟 Highlights

- Download image with axel for faster download
- Contains a version optimized for termux on android and a universal version

## 🔗 Requirements

- [Python 3](https://www.python.org/) or higher
- [Axel](https://github.com/axel-download-accelerator/axel) ```pkg install axel``` for termux or ```apt install axel``` for any debian based os
- pip dependencies in requirements.txt ```pip install -r requirements.txt```

## 🚀 Usage

1. Clone this repository or download it manually:
    ```bash
    git clone https://github.com/Gabi-Zar/bing_images_scraper.git
    cd bing_images_scraper
    ```

2. Run the script:
    - Universal
        ```bash
        python bing_images_scraper.py input.png 
        ```
    - Termux
        ```bash
        python bing_images_scraper_termux.py input.png 
        ```

## ⚙️ How does it work

1. The script is looking for what you have chosen on bing
2. It extract all the images url
3. It download every images with axel

## ❓ FAQ

- If you have any questions please open an issue

## 📜 License

This project is licensed under the [MIT License](LICENSE).