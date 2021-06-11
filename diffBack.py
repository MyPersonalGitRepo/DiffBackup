import glob
import os

search_dir = "/F:\INTESA/"
# remove anything from the list that is not a file (directories, symlinks)
# thanks to J.F. Sebastion for pointing out that the requirement was a list
# of files (presumably not including directories)
files = list(filter(os.path.isfile, glob.glob(search_dir + "*")))
#files.sort(key=lambda x: os.path.getmtime(x))
print(files)
