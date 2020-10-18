WINNER OF BEST USE OF GOOGLE CLOUD @ HACKGT 7

This project uses Google Vision OCR to enable educators to make their classes more interactive. Where older students can benefit from services like TurningPoint for real-time questions and answers in class, younger students may prefer a more tactile experience. Just a notebook, tablet, or whiteboard would enable students to write and hold up their answers to the camera as though they were showing the teacher themselves, and OCR would recognize the answer text and submit it once the teacher ended the question.

Unfortunately, we were not able to get access to any video chat APIs in time that sufficiently matched our needs (Zoom, Bluejeans, etc. that are already used in schools), so we decided to leave out the video chat integration. Right now, we have the student-side code as a proof of concept. In use of this example, you press 's' to start a question, which emulates the teacher starting a question session in class. Once the answer is detected, it is outputted to the console, where in the final product we envision it being sent directly to the teacher, along with the image capture from the frame used for OCR to cross-reference against the answer submitted in case the submitted answer is incorrect.


Requires (python3):
cv2
numpy
google-cloud-vision

Step 1: Create credential for Google Vision using these steps: https://cloud.google.com/vision/docs/before-you-begin

Step 2: Create a virtual environment
  ```
  virtualenv env
  source env/bin/activate
  ```
Step 3: Use pip to install the three necessary libraries
  ```
  pip install cv2 numpy google-cloud-vision
  ```
Step 4: Clone this repository  

Step 5: Run the program using: `python main.py`
