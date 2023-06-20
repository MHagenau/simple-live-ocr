# OCR on live video stream

Application for performing live OCR on video stream in Python using the easyocr library.

## Live demo
![live-demo](https://github.com/MHagenau/simple-live-ocr/assets/9133193/6ce9b039-16d6-4124-961b-9247354c4ac5)

## Running the program

In order to run the program use the following commands to setup the enviroment and install the dependencies. The program will ask which capture card you would like to use. By default the program does not use GPU, this can be enabled in the code and will increase performance significantly.

Creating the enviroment
```
python -m venv .venv
```
Activating the enviroment
```
.\.venv\Scripts\Activate.ps1
```
Installing the dependencies
```
pip install -r .\requirements.txt
```
Running the program
```
python .\ocr\main.py
```
