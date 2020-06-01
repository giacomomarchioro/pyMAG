from MAG import MAGFile
metadata = MAGFile()
metadata.gen.set_access_rights('uso pubblico')
metadata.gen.set_agency('IT:VR0056')
metadata.gen.add_img_group('master')
mastergrp = metadata.gen.img_groups['master']
mastergrp.image_metrics.set_bitpersample('16,16,16')
mastergrp.image_metrics.set_photometricinterpretation('RGB')
mastergrp.format.set_name('TIF')
mastergrp.format.set_mime('image/tiff')

metadata.add_stru()
stru0 = metadata.structs[0]