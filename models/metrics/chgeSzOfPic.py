from PIL import  Image
import os
#可以考虑循环处理

path="30"  #图片所在的文件夹路径
for maindir, subdir,file_name_list in os.walk(path):
    print(file_name_list)
    for file_name in file_name_list:
        image=os.path.join(maindir,file_name) #获取每张图片的路径
        file=Image.open(image)
        out=file.resize((224,224),Image.ANTIALIAS)  #以高质量修改图片尺寸为 nonono（400，48）
        out.save(image)                            #以同名保存到原路径