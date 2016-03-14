"""A small script for generating a markdown page from images.
Run from inside root folder of repo"""
import os
with open('images.md', 'w') as f:
    for image in sorted(os.listdir("Images")):
        f.write("%s\n\n" % image)
        f.write("![{0}](Images/{0})\n\n".format(image))
