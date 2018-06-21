# http://img95.699pic.com/photo/50066/1239.jpg_wh300.jpg
import urllib.request  
import re 

imgList=[]

for i in range(int(1239),int(1250)):
 	imgUrl='http://img95.699pic.com/photo/50066/'+str(i)+'.jpg_wh300.jpg'
 	imgList.append(imgUrl)
print(imgList)
imgList = re.findall(imgre,imgUrl) 

for imgUrl in imgList:  # 列表循环  
        print('正在下载：%s'%imgUrl[0])  
        # urlretrieve(url,local)方法根据图片的url将图片保存到本机  
        urllib.request.urlretrieve(imgUrl[0],'E:/pythonSpiderFile/img/%d.jpg'%x)  
        x+=1
        
