from MAG import MAGFile
from datetime import datetime
datetime.now().replace(microsecond=0).isoformat()
fileMAG = MAGFile()
fileMAG.gen.set_creation = datetime.now().replace(microsecond=0).isoformat()
fileMAG.gen.set_last_update = datetime.now().replace(microsecond=0).isoformat()
fileMAG.gen.set_completeness("digitalizzazione completa") # tradotto in 1
fileMAG.gen.set_access_rights("uso pubblico") # tradotto in 1
#fileMAG.gen.set_agency('IT:VR0056') # Anagrafe biblioteche
fileMAG.gen.set_agency("https://n2t.net/ark:/40016") # ARK identifier
fileMAG.gen.set_stprog("https://www.dcuci.univr.it/") # od una pagina dedicata
fileMAG.gen.set_collection("http://bibliotecacapitolare.org/catalogo-dei-manoscritti/")
fileMAG.gen.add_img_group(ID="raw")
rawgrp = fileMAG.gen.img_groups["raw"]
# questo bit per sample non sarebbe valido
rawgrp.image_metrics.set_bitpersample('14,14,14')
rawgrp.image_metrics.set_photometricinterpretation('RGB')
rawgrp.image_metrics.set_samplingfrequencyunit('inch, pollice')
rawgrp.image_metrics.set_samplingfrequencyplanetype('object plane')
rawgrp.image_metrics.set_xsamplingfrequency(600) # da calcolare
rawgrp.image_metrics.set_ysamplingfrequency(600)
rawgrp.format.set_name('NEF')
rawgrp.format.set_compression('Uncompressed')
rawgrp.format.set_mime('image/x-nikon-nef')
rawgrp.scanning.set_scanningagency("Dr. Andrea Brugnoli - Università di Verona")
rawgrp.scanning.set_capture_software("digiCamControl - digiCamControlsetup_2.1.2.exe")
rawgrp.scanning.set_scanner_manufacturer("")
rawgrp.scanning.set_scanner_model("")

# 7360 × 4912
fileMAG.gen.add_img_group("master")
mastergrp = fileMAG.gen.img_groups["master"]
mastergrp.image_metrics.set_bitpersample('16,16,16')
mastergrp.image_metrics.set_photometricinterpretation('RGB')
mastergrp.format.set_name('TIF')
mastergrp.format.set_mime('image/tiff')
fileMAG.add_stru()
stru0 = fileMAG.structs[0]

import numpy as np
np.argmin()
