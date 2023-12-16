import requests
import os
from PIL import Image

url="https://www.ibm.com/"
r=requests.get(url)

header = r.request.headers


url='https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/IDSNlogo.png'
r = requests.get(url)

path = os.path.join(os.getcwd(), 'image.png')

with open(path, 'wb') as f:
    f.write(r.content)

Image.open(path)
