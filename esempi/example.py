from MAG import MAGFile
from datetime import datetime
datetime.now().replace(microsecond=0).isoformat()
fileMAG = MAGFile()
fileMAG.gen.set_creation(datetime.now().replace(microsecond=0).isoformat())
fileMAG.gen.set_last_update(datetime.now().replace(microsecond=0).isoformat())
fileMAG.gen.set_completeness("digitalizzazione completa") # tradotto in 1
fileMAG.gen.set_access_rights("uso pubblico") # tradotto in 1
#fileMAG.gen.set_agency('IT:VR0056') # Anagrafe biblioteche
fileMAG.gen.set_agency("https://n2t.net/ark:/40016") # ARK identifier
fileMAG.gen.set_stprog("https://www.dcuci.univr.it/") # od una pagina dedicata
fileMAG.gen.set_collection("http://bibliotecacapitolare.org/catalogo-dei-manoscritti/")

fileMAG.gen.add_img_group(ID="raw")
rawgrp = fileMAG.gen.img_groups["raw"]
rawgrp.image_metrics.set_bitpersample('14,14,14') # questo bit per sample non sarebbe valido
rawgrp.image_metrics.set_photometricinterpretation('RGB')
rawgrp.image_metrics.set_samplingfrequencyunit('inch, pollice')
rawgrp.image_metrics.set_samplingfrequencyplane('object plane')
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


fileMAG.bib.set_level("m")
fileMAG.bib.add_identifier("XXV_A")
fileMAG.bib.add_title("Vita nuova")
fileMAG.bib.add_creator("Alighieri Dante")
fileMAG.bib.add_subject("Poesie")
fileMAG.bib.add_date("1234")
fileMAG.bib.add_type("Text")
fileMAG.bib.add_contributor("")
fileMAG.bib.add_language("IT")
fileMAG.bib.add_format("membranaceo, 334 x 312 cm")
fileMAG.bib.add_rights("CCBY")
fileMAG.bib.add_coverage("Not known")
fileMAG.bib.add_description("This is a test decription")
fileMAG.bib.add_coverage("not know")
fileMAG.bib.create_holdingsID("BibliotecaCapitolare")
bibcap = fileMAG.bib.holdings['BibliotecaCapitolare']
bibcap.set_library("Biblioteca Capitolare di Verona")
bibcap.set_inventory_number("MXCV (234)")
bibcap.add_shelfmark("[VII 3 4]", collocation_type="modern")
#fileMAG.bib.local_bib.add_geo_coord("")
#fileMAG.bib.local_bib.add_not_date(1445)
intro = fileMAG.add_stru()
intro.set_nomenclature("Introduzione") 
intro.add_element(2,10,"img")
subintro = intro.add_stru()
subintro.set_nomenclature("Paragrafo del'introduzione")
subintro.add_element(3,4,"img")


images = [{'nomenclature':'1v'}]
for i in images:
    img = fileMAG.add_img(imggroupID='raw',holdingsID='BibliotecaCapitolare')
    img.set_datetimecreated("2020")
    img.set_nomenclature(i['nomenclature'])
    img.image_dimensions.set_imagelengthandwidth(length=1000,width=1000)
    img.set_file("hhtps.myfile",Location="URL")
    img.set_md5("asdvsdv")
    img.set_scale(0)
    img.set_side("left")
    img.add_usage(uso="alta risoluzione",copyright="il repository ha il copyright dell'oggetto digitale")
    target2 = img.add_target()
    target2.set_targetID("X-RiteColorCheckerSG")
    target2.set_targetType(0)

fileMAG.write('test.xml')



