import glob
from PIL import Image
a = glob.glob(r"C:/ASU/Spring 2021/PARA Lab/rgb/*.png");
print(*a, sep="\n")
frame = []
c = len(a)
print(c)
for pics in a:
    framenew = Image.open(pics)
    frame.append(framenew)
    #Saving GIF
frame[0].save('C:/ASU/Spring 2021/PARA Lab/rgb/GIF.gif', save_all=True, append_images= frame[1:], optimize = False, duration=10, loop=0)


   
