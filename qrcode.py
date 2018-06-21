from PIL import Image

# codeLib = '''@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,"^`'.'''#生成字符画所需的字符集
codeLib = '''@$B%8&WM#ZO0QLCJUYX*oahkbdpqwmzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`.  '''
count = len(codeLib)

def transform1(image_file):
    image_file = image_file.convert("L")#转换为黑白图片，参数"L"表示黑白模式
    codePic = ''
    for h in range(0,image_file.size[1]):  #size属性表示图片的分辨率，'0'为横向大小，'1'为纵向
        for w in range(0,image_file.size[0]):
            gray = image_file.getpixel((w,h)) #返回指定位置的像素，如果所打开的图像是多层次的图片，那这个方法就返回一个元组
            codePic = codePic + codeLib[int(((count-1)*gray)/256)]#建立灰度与字符集的映射
        codePic = codePic+'\r\n'
    return codePic

# def transform2(image_file):
#     codePic = ''
#     for h in range(0,image_file.size[1]):
#         for w in range(0,image_file.size[0]):
#             g,r,b = image_file.getpixel((w,h))
#             gray = int(r* 0.299+g* 0.587+b* 0.114)
#             codePic = codePic + codeLib[int(((count-1)*gray)/256)]
#         codePic = codePic+'\r\n'
#     return codePic


fp = open(u'C:/Users/Administrator/Desktop/z.jpg','rb')
image_file = Image.open(fp)
image_file=image_file.resize((int(image_file.size[0]*0.225), int(image_file.size[1]*0.15)))#调整图片大小
print(u'Info:',image_file.size[0],' ',image_file.size[1],' ',count)

tmp = open('111.txt','w')
tmp.write(transform1(image_file))
tmp.close()

# a=open(r"C:/Users/Administrator/Desktop/111.txt","r")
# s=a.read()
# print(s)
# import qrcode
# qr = qrcode.QRCode(
#     version=2,
#     error_correction=qrcode.constants.ERROR_CORRECT_L,
#     box_size=10,
#     border=4,
# )
# qr.add_data('Some data')
# qr.make(fit=True)

# img = qr.make_image(fill_color="black", back_color="white")
# img.get_image().show()


