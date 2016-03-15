"""A small script for generating a markdown page from images.
Run from inside root folder of repo"""
import os
os.remove("images.md")
with open('images.md', 'w') as f:
<<<<<<< HEAD
    print("Generating markdown")
    for image in sorted(os.listdir("Images\\Thumbnails")):
        f.write("%s\n\n" % image)
=======
    for image in sorted(os.listdir("Images")):
        f.write("[{0}](Schematics/{0})\n\n".format(image.replace("png","schematic")))
>>>>>>> origin/master
        f.write("![{0}](Images/{0})\n\n".format(image))
