import qrcode
import image

qr = qrcode.QRCode(
    version=15,  # bigger the number bigger the complexity of the image
    box_size=10,  # size of qr code
    border=4,  # border white part of te qr code
)

data = "https://github.com/Deepan-mn"

qr.add_data(data)
qr.make(fit=True)
img = qr.make_image(fill="black", back_color="white")
img.save("myqrcode.png")

