import pyqrcode
import png
s="https://www.geo-fs.com/geofs.php?v=3.5"
url= pyqrcode.create(s)
url.svg('My QR.SVG',scale=8)
url.png('My QR.png',scale=6)