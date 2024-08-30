# Steps:
# Install all the libraries needed
# create a function that collects a text and cinverts it to a qrcode
# Save the qrcode as an image
# run the functions

import qrcode # pip install qrcode Image (both are different packages)

def generate_qrcode(text):
          qr = qrcode.QRCode(
                    version = 1,
                    error_correction = qrcode.constants.ERROR_CORRECT_L,
                    box_size = 10,
                    border = 4,
          )

          qr.add_data(text)
          qr.make(fit=True)
          img = qr.make_image(fill_color="black", back_color="white")
          img.save("qrimg.png")

generate_qrcode("https://moonmanas.blogspot.com/")