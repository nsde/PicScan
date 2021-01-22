import os
import random
cwd = os.getcwd()

output_filename = str(random.randint(1000,9999))

pic_path = "C:\\Users\\xitzf\\Pictures\\"
prefix = ""
suffix = ".png"

name = ""
names = []
while name != "0":
    name = input("")
    name = prefix + name + suffix
    names.append(name)

    os.system('"C:\\Program Files\\paint.net\\PaintDotNet.exe" '+  pic_path + name)

    with open (cwd + "\\output\\" + output_filename + ".txt", "w") as f:
        names_str = ""
        for n in names:
            names_str += n + "\n"
        f.write(names_str)
