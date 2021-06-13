from pyzbar.pyzbar import decode 
from PIL import Image 

img = Image.open("my_qrcode10.png")

decoding_qr = decode(img) # 불러온 이미지를 디코딩 

print("QR 코드에 담겨진 내용은 : ")
print(decoding_qr[0].data.decode()) ## 리스트로 받아오고 내가 쳤던 메세지를 받아온다.