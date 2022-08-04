import pyqrcode
from pyqrcode import QRCode

link = "https://youtube.com/channel/abc"

#Generate the QRCode
url = pyqrcode.create(link)

#create and save the file using myqr.png
url.svg("myt.svg", scale = 8)


