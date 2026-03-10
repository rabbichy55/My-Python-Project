import qrcode

# link convert to qr code
data = input("Please paste your link")

# Create a QR code
qr = qrcode.QRCode(
    version=1, # Size if the QR code (1 is the smallest)
    error_correction=qrcode.constants.ERROR_CORRECT_H,  # Error correction level
    box_size=10,  # Size of each box in QR cose
    border=4,  # Border size around the QR code

)

# Add data to QR code
qr.add_data(data)
qr.make(fit=True)

# Create an image from the QR code
img = qr.make_image(fill_color="black", back_color="white")

# Save the img
img.save("Scan the QR Code please!.png")
