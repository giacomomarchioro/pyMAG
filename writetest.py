from MAG import MAGFile
a = MAGFile('MagExportEample.xml')
a.gen.img_groups['jpeg150'].scanning.set_capture_software('micio 1.2')
a.gen.img_groups['jpeg150'].scanning.set_scanner_manufacturer('zico') 
a.gen.img_groups['jpeg150'].scanning.set_scanner_model('zicomaioplus') 
a.gen.img_groups['master'].scanning.set_capture_software('micio 1.2')
a.gen.img_groups['master'].scanning.set_scanner_manufacturer('zico') 
a.gen.img_groups['master'].scanning.set_scanner_model('zicomaioplus') 
a.write('testw.xml')

