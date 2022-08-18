import numpy as num
from PIL import Image
#Creating and Loading required arrays
x = num.load('sample.npy');
sort_ar = num.empty([10])
k = num.empty([1])
print("Cost Function Array")
print(x)
print('\t')
print('\t')
sort = num.sort(x) #Cost Function array is being sorted
for i in range (10): #Top ten cost function values is being copied to new empty array
    sort_ar[i] = sort[i+1]
k = sort_ar[0] #Lowest Cost function value
pos_tup = num.where(x==k)
pos = int(pos_tup[0])
print("Lowest Cost function value in given .npy file is" , k) #Location of lowest cost function in Cost function array
print("Location of the above cost function is", pos)
color_img = Image.open(r"C:\Users\gowth\OneDrive\Desktop\ddd\color_badInitialization_torch.gif")
depth_img = Image.open(r"C:\Users\gowth\OneDrive\Desktop\ddd\depth_badInitialization_torch.gif")
color_img.seek(pos)
color_img.show()
depth_img.seek(pos)
depth_img.show()


'''
# depths - [PIL_0, ... ,PIL_299]
depth_array = np.asarray([np.asarray(d) for d in depths])    
longer version:
for d in depths:
    depth_array.append(np.asarray(d))
depth_array = np.asarray(depth_array)
'''



    

