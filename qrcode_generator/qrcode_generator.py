import qrcode
from MyQR import myqr
from PIL import Image,ImageDraw,ImageFont

def QR_With_Central_Img(link="https://github.com/MM-DCT/JiMaJiang", central_picture="img/LOGO_green.jpg", outputput_file="qrcode_with_border.png", outputput_file_="qrcode_without_border.png"):
    #link: url
    #central_picture: central picture filename
    #outputput_file: output filename

    bordercolor = (123,150,111)
    width = 40
    if link=="https://github.com/MM-DCT/JiMaJiang" :
        btext = "~ 来芝麻酱的Github页面看看吧 ~" 
    else : btext = "~ 扫一扫前往芝麻酱页面 ~" 
    

    qr = qrcode.QRCode(
    version=5, error_correction=qrcode.constants.ERROR_CORRECT_H, box_size=8, border=4)
    qr.add_data(link)
    qr.make(fit=True)
    img = qr.make_image(fill_color=bordercolor)
    img = img.convert("RGBA")
    icon = Image.open(central_picture)

    img_w, img_h = img.size
    factor = 4
    size_w = int(img_w / factor)
    size_h = int(img_h / factor)

    icon_w, icon_h = icon.size
    if icon_w > size_w: icon_w = size_w
    if icon_h > size_h: icon_h = size_h
    icon = icon.resize((icon_w, icon_h), Image.ANTIALIAS)

    w = int((img_w - icon_w) / 2)
    h = int((img_h - icon_h) / 2)
    icon = icon.convert("RGBA")
    img.paste(icon, (w, h), icon)

    bw = 2*width + img_w
    bh = 2*width + img_w
    
    img_new = Image.new('RGB', (bw, bh), bordercolor)
    img_new.paste(img, (width, width))

    draw = ImageDraw.Draw(img_new)
    font = ImageFont.truetype(font='menmiao.ttf', size=20, encoding="utf-8")
    draw.text((100,10),btext,font=font,direction=None)
    img.save(outputput_file_)
    img_new.save(outputput_file)


# if __name__ == '__main__':
#     QR_With_Central_Img(link="https://github.com/MM-DCT")