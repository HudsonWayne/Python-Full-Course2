import qrcode

# Create a QR code for the URL
img = qrcode.make("https://github.com/HudsonWayne?tab=overview&from=2025-04-01&to=2025-04-11")

# Save the image
img.save("hudson_qr.png")