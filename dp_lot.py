import os 
from urllib.request import urlretrieve 

#创建下载的文件本地存放目录
downpath = '/home/pi/Desktop/108python'
os.makedirs(downpath, exist_ok=True)

#待下载的图片地址列表
pictures = [
    'https://img-cdn.xue.cn/book_32333_cover.jpg',
    'https://img-cdn.xue.cn/book_34757_cover.jpg',
    'https://img-cdn.xue.cn/book_34238_cover.jpg']

for pic_url in pictures:
    #根据url构造图片本地文件名
    pic_file = downpath + pic_url.split('/')[-1]
    #下载一张图片并以制定的文件名存放到指定路径
    urlretrieve(pic_url, pic_file)
    print(pic_file, 'done...')

print('All is done.')