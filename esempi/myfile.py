# coding: utf-8
from MAG import MAGFile
myfile = MAGFile()
myfile.gen.set_access_rights('uso pubblico')
myfile.gen.set_agency('IT:VR0056')
myfile.gen.create_img_groupID('master')
myfile.gen.img_groups['master'].format.set_mime('image/jpeg')
myfile.gen.img_groups['master'].format.set_name('TIF')
myfile.gen.creation

