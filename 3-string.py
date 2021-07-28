import os

filename = os.listdir('/home/shiva/Documents/admin-them/ElaAdmin-master/images/')

print(filename)

pngFile = [ f for f in filename if f.endswith('.png')]

print(pngFile)