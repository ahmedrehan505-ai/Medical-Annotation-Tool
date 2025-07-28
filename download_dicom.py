import requests

url = "https://github.com/IMTDePonte/MedicalData/raw/master/sample.dcm"
response = requests.get(url)

if response.status_code == 200:
    with open("sample.dcm", "wb") as f:
        f.write(response.content)
    print("DICOM file downloaded successfully as sample.dcm")
else:
    print("Failed to download file:", response.status_code)
