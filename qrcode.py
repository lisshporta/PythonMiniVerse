# pip install pyqrcode
# pip install pyzbar
# pip install Pillow
# pip install pypng

import pyqrcode
from pyzbar.pyzbar import decode
from PIL import Image

qr = pyqrcode.create('https://github.com/')
qr.png('qrcode.png', scale = 8)
print('QRcode successfully generated!')
