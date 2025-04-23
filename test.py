import cv2
from func_timeout import func_set_timeout, FunctionTimedOut
from paddleocr import PaddleOCR

ocr = PaddleOCR(use_angle_cls=True, lang="ch", show_log=False)

@func_set_timeout(1)
def f():
    while True:
        img = cv2.imread("cn_example.jpg")
        result = ocr.ocr(img)
        print(result)

while True:
    try:
        f()
    except FunctionTimedOut:
        print("timeout")
