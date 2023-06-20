import cv2
import imutils
import numpy as np
import pandas as pd
from list_ports import cameraUtils
from ocr_engine import  load_OCR_engine
from imutils.video import VideoStream


def main(port_index):

	reader = load_OCR_engine()

	# Defining the video strem on capture card index 0 by default
	print("[STATUS] Starting video stream ...")
	vs = VideoStream(src=port_index).start()

	# Scale for downscaling the image when processing
	new_w, new_h = 320, 230

	print("[INFO] Press q in the video feed to exit ...")
	while True:

		# Getting the current frame, standardizing it and saving a copy
		frame = vs.read()
		frame = imutils.resize(frame, width=1000)
		orig = frame.copy()

		# Downsizing the image and defining a ratio to the original size
		h, w = frame.shape[:2]
		ratio_w = w / float(new_w)
		ratio_h = h / float(new_h)
		frame = cv2.resize(frame, (new_w, new_h))

		# Parsing the frame through the text recognition and saving the results in a DataFrame
		results = reader.readtext(np.array(frame))
		df = pd.DataFrame(results, columns=['bbox','text','conf'])

		# Looping over the results from the current frame and displaying it in a box overlay
		for _, row in df.iterrows():
			box_tuples = [(int(x * ratio_w), int(y * ratio_h)) for x, y in row['bbox']]
			cv2.rectangle(orig, box_tuples[0], box_tuples[2], (0, 255, 0), 1)
			text = f"{row['text']} - {round(row['conf'], 2)}"
			cv2.putText(orig, text, (box_tuples[3][0], box_tuples[3][1] + 18), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1)
		
		# Show the original image with the added boxes
		cv2.imshow("Live text recognition", orig)
		
		# Check for 'q' keypress to stop the program
		key = cv2.waitKey(1) & 0xFF
		if key == ord('q'):
			break

	# Stop the resources and closing all windows
	vs.stop()
	cv2.destroyAllWindows()


if __name__ == "__main__":
	print("[STATUS] Listing all available video ports ...")

	# Function to print all available video indexes and return them as a list
	avail_ports = cameraUtils.list_ports()

	# Get the valid selected port index from the user 
	port_index = cameraUtils.get_valid_input(avail_ports)

	main(port_index)