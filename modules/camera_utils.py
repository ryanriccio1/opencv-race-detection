import cv2


class Camera(object):
    def __init__(self):
        self._capture = None
        self.frame = None
        self._capture = cv2.VideoCapture(0)
        self._face_cascade = cv2.CascadeClassifier('modules/face.xml')

    def stop_camera(self):
        self._capture.release()
        cv2.destroyAllWindows()

    def show_camera(self, text=None):
        _, self.frame = self._capture.read()
        gray = cv2.cvtColor(self.frame, cv2.COLOR_BGR2GRAY)
        faces = self._face_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5)
        for x, y, w, h in faces:
            print(x, y, w, h)
            roi_gray = gray[y:y+h, x:x+w]
            roi_color = self.frame[y - 50:y + h + 50, x - 50:x + w + 50]

            img_item = "current_image.png"
            cv2.imwrite(img_item, roi_color)

            cv2.rectangle(self.frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

        font = cv2.FONT_HERSHEY_SIMPLEX
        self.frame = cv2.putText(self.frame, text, (10, 450), font, 1, (0, 255, 0), 2, cv2.LINE_AA)
        cv2.imshow('frame', self.frame)
        if cv2.waitKey(20) & 0xFF == ord('q'):
            return False
        return True



