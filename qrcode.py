# basic_qrcode.py

import segno

qrcode = segno.make_qr("https://www.youtube.com/watch?v=i4VMxFuboEE")
qrcode.save("Te_la_dedico_bby.png")