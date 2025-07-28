import sys
import pydicom
import numpy as np
import matplotlib.pyplot as plt
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QFileDialog
from annotation_handler import save_annotations, load_annotations

class DicomApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Medical Annotation Tool")
        self.setGeometry(100, 100, 600, 400)

        # Buttons
        self.open_button = QPushButton("Open DICOM", self)
        self.open_button.setGeometry(50, 50, 200, 50)
        self.open_button.clicked.connect(self.open_dicom)

        self.save_button = QPushButton("Save Annotations", self)
        self.save_button.setGeometry(50, 120, 200, 50)
        self.save_button.clicked.connect(self.save_annotations)

        self.load_button = QPushButton("Load Annotations", self)
        self.load_button.setGeometry(50, 190, 200, 50)
        self.load_button.clicked.connect(self.load_annotations)

        # Data
        self.annotations = []

    def open_dicom(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Open DICOM File", "", "DICOM files (*.dcm)")
        if file_path:
            ds = pydicom.dcmread(file_path)
            image = ds.pixel_array
            plt.imshow(image, cmap=plt.cm.gray)
            plt.show()

            # Add dummy annotation (rectangle at fixed position)
            self.annotations.append({"type": "rectangle", "x": 50, "y": 50, "width": 100, "height": 50})
            print("Dummy annotation added")

    def save_annotations(self):
        save_annotations(self.annotations)

    def load_annotations(self):
        self.annotations = load_annotations()
        print("Current Annotations:", self.annotations)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = DicomApp()
    window.show()
    sys.exit(app.exec_())
