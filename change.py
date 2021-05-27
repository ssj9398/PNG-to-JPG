from PIL import Image
import os.path
import glob

targerdir = r"E:\test" #해당 폴더 설정

files = os.listdir(targerdir)

format = [".jpg",".png",".jpeg","bmp",".JPG",".PNG","JPEG","BMP"] #지원하는 파일 형태의 확장자들
for (path,dirs,files) in os.walk(targerdir):
    for file in files:
         if file.endswith(tuple(format)):
             file = glob.glob("*.png")
             for x in file:
                if not os.path.isdir(x): filename = os.path.splitext(x)
                try:
                 os.rename(x, file[0] + '.jpg')



                 image = Image.open(path+"\\"+file)


                 print(image.filename)
                 print(image.size)

                 image.save(path+"\\"+file)
                 print(image.size)
                except:
                    print()