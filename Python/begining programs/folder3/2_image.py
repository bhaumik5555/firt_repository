from PIL import Image
import os

print(os.getcwd())
os.chdir(r'F:\Python\Pictures')
print(os.getcwd())

# img1 = Image.open('mic_image_1.jpg')
# img1.save("img1.png")
# img1.show()

for item in os.listdir():
    print(item)
    print(os.path.splitexe(item))
    if item.endswith('.jpg'):
        img1 = Image.open(item)
        print(os.path.splitexe(item))
        img_name,img_exe = os.path.splitexe(img1)
        img1.save(f'{img_name}.png')

