import qrcode
from PIL import Image
import qrcode.constants

qr = qrcode.QRCode(version=1,
                   error_correction=qrcode.constants.ERROR_CORRECT_H,
                   box_size=10, border=10)
qr.add_data("Hello world!")
qr.make(fit = True)
img = qr.make_image()
img.save("qr_adv.png")