import qrcode as qr;
img = qr.make("Hello world!")
img.save("qrcode.png")
