import qrcode
from qrcode.image.pil import PilImage
from PIL import Image, ImageDraw

input_data = "http://naweedhpr.website3.me/"
qr = qrcode.QRCode(
        version=1,
        box_size=10,
        border=5)
qr.add_data(input_data)
qr.make(input_data)
img = qr.make_image(fill='black', back_color='white')
img.save('qrcode001.png')