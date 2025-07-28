import pydicom
from pydicom.dataset import Dataset, FileDataset
import numpy as np
import datetime

filename = "fake_sample.dcm"
file_meta = Dataset()
file_meta.MediaStorageSOPClassUID = pydicom.uid.SecondaryCaptureImageStorage
file_meta.MediaStorageSOPInstanceUID = pydicom.uid.generate_uid()
file_meta.ImplementationClassUID = pydicom.uid.generate_uid()
file_meta.TransferSyntaxUID = pydicom.uid.ExplicitVRLittleEndian  # important!

ds = FileDataset(filename, {}, file_meta=file_meta, preamble=b"\0" * 128)

ds.Modality = "OT"
ds.ContentDate = str(datetime.date.today()).replace("-", "")
ds.ContentTime = str(datetime.datetime.now().time()).replace(":", "").split(".")[0]

pixel_array = (np.random.rand(256, 256) * 255).astype(np.uint8)
ds.Rows, ds.Columns = pixel_array.shape
ds.SamplesPerPixel = 1
ds.PhotometricInterpretation = "MONOCHROME2"
ds.BitsAllocated = 8
ds.BitsStored = 8
ds.HighBit = 7
ds.PixelRepresentation = 0
ds.PixelData = pixel_array.tobytes()

ds.save_as(filename)
print(f"Fake DICOM file saved as {filename}")

