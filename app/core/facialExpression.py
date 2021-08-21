from fer import FER
import cv2

class FacialExpression:
    def __init__(self):
        self.detector = FER()

    def compute(self, fileName: str):
        img = cv2.imread(fileName)
        result = self.detector.detect_emotions(img)[0]["emotions"]
        return result