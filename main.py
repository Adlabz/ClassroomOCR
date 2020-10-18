import numpy as np
import cv2


def detect_text(path):
    from google.cloud import vision
    import io
    client = vision.ImageAnnotatorClient()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.Image(content=content)

    response = client.text_detection(image=image)
    texts = response.text_annotations
    writing = ''

    for text in texts:
        writing+=' ' + text.description
    return  writing

def start_video():
    count = 0
    texts = []
    while count <= 3:
        page_in_frame = False
        video_capture = cv2.VideoCapture(0)
        ret, frame = video_capture.read()
        cv2.imwrite('stack.jpg', frame)
        image = cv2.imread('stack.jpg',-1)
        paper = cv2.resize(image,(500,500))
        ret, thresh_gray = cv2.threshold(cv2.cvtColor(paper, cv2.COLOR_BGR2GRAY),
                                200, 255, cv2.THRESH_BINARY)
        contours, hier = cv2.findContours(thresh_gray, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
        if len(contours) < 10:
            page_in_frame = True #probably
            curr_state = page_in_frame
            for c in contours:
                rect = cv2.minAreaRect(c)
                box = cv2.boxPoints(rect)
                # convert all coordinates floating point values to int
                box = np.int0(box)
                # draw a green 'nghien' rectangle
                # cv2.drawContours(paper, [box], 0, (0, 255, 0),1)

        if (page_in_frame):
            text = detect_text('stack.jpg')
            res = text.rsplit('\n', 1)
            string = res[1]
            texts.append(string)
            # print(string)
            count += 1


        cv2.imshow('paper', frame)
        #cv2.imwrite('paper.jpg',paper)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # print(texts)
    ans = max(set(texts), key=texts.count)
    print(ans)
    video_capture.release()

def main():
    while True:
        print("Press \'s\' to start a reading!")
        video_capture = cv2.VideoCapture(0)
        while True:
            ret, frame = video_capture.read()
            cv2.imshow('paper', frame)
            if cv2.waitKey(1) & 0xFF == ord('s'):
                break
        start_video()

main()
