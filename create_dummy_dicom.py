import pydicom
from pydicom.dataset import Dataset, FileDataset
import datetime
import numpy as np
import os

filename = "sample.dcm"

# Create a dataset
file_meta = pydicom.Dataset()
ds = FileDataset(filename, {}, file_meta=file_meta, preamble=b"\0" * 128)

# Add patient and study data
ds.PatientName = "John Doe"
ds.PatientID = "123456"
ds.StudyDate = datetime.date.today().strftime('%Y%m%d')
ds.Modality = "OT"  # Other
ds.StudyDescription = "Dummy DICOM File"
ds.SeriesDescription = "Sample"

# Add image data (dummy 64x64 image)
rows, cols = 64, 64
image = np.zeros((rows, cols), dtype=np.uint16)
ds.Rows = rows
ds.Columns = cols
ds.PixelData = image.tobytes()
ds.PhotometricInterpretation = "MONOCHROME2"
ds.BitsAllocated = 16
ds.BitsStored = 16
ds.HighBit = 15
ds.SamplesPerPixel = 1

# Save file
ds.save_as(filename)
print(f"Dummy DICOM file created: {os.path.abspath(filename)}")
