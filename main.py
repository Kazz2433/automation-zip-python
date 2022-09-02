import shutil
import os
import zipfile
from zipfile import ZipFile

names = []
refined= 0
for root, dirs, files in os.walk(".", topdown=False):
   for name in files:
      if name.endswith('.zip'):
            names = list(name.split('.'))
            refined = names[0]
            names.append(refined)
            os.makedirs(refined)
            shutil.move(os.path.join(root,name),os.path.join(root,refined))


for root, dirs, files in os.walk(".", topdown=False):
   for name in files:
      if name.endswith('.zip'):
         with zipfile.ZipFile(os.path.join(root, name),"r") as zip_ref:
            zip_ref.extractall(name)

for root, dirs, files in os.walk(".", topdown=False):
   for name in files:
      if name.endswith('.zip'):
         names = list(name.split('.'))
         refined = names[0]
         names.append(refined)
         shutil.rmtree(refined)

