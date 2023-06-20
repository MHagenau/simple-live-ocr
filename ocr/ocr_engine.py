import easyocr
import torch

def load_OCR_engine():
    gpu_available = torch.cuda.is_available()
    use_gpu = False

    if gpu_available:
        choice = input("GPU is available. Do you want to use it? (y/n): ")
        if choice.lower() == "y":
            use_gpu = True

    reader = easyocr.Reader(['en'], gpu=use_gpu)
    print("[STATUS] Loading the OCR model ...")
    return reader