import sys
from PyQt6 import QtWidgets
from captcha2text_window import Ui_Form
import ddddocr
import requests
import io
from PyQt6.QtGui import QPixmap


class MyPyQT_Form(QtWidgets.QWidget, Ui_Form):
    def __init__(self):
        super(MyPyQT_Form, self).__init__()
        self.setupUi(self)

    def identifyButton_click(self):
        print(self.urlEdit.text())
        code, img_stream = identify(self.urlEdit.text())
        self.textEdit.append(code)
        try:
            pixmap = QPixmap()
            pixmap.loadFromData(img_stream.getvalue())
            self.imgLable.setPixmap(pixmap)
        except:
            pass


def identify(url):
    try:
        header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
        }
        s = requests.Session()
        r = s.get(url, headers=header)
        img = r.content
        img_stream = io.BytesIO(img)
        ocr = ddddocr.DdddOcr()
        res = ocr.classification(img_stream.getvalue())
        return res, img_stream
    except:
        return "ERROR", None


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    my_pyqt_form = MyPyQT_Form()
    my_pyqt_form.show()
    sys.exit(app.exec())