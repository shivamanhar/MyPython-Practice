import os

filename = os.listdir('/home/shiva/Documents/admin-them/ElaAdmin-master/images/')

print(filename)

result = any(f.endswith('psd') for f in filename)

print(result)