import qrcode
while True:
    Text = input("請輸入內容：")
    img = qrcode.make(Text)
    img.save(Text+".jpg")