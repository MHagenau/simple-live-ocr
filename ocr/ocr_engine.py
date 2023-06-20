import easyocr


def load_OCR_engine():
	# Defining the OCR engine - several options are available here
	reader = easyocr.Reader(['en'], gpu = False)
	print("[STATUS] Loading the OCR model ...")
	return reader