from MAG import MAGFile
import datetime

# la data è espressa in UTC
d = datetime.datetime.utcnow()
data = d.strftime('%Y-%m-%dT%H:%M:%SZ')
# la data è espressa con il fuso orario corrente
d = datetime.datetime.now()
data = d.strftime('%Y-%m-%dT%H:%M:%S')
a = MAGFile()
a.gen.set_access_rights("uso pubblico")
a.gen.set_agency("Università di Verona")
a.gen.set_collection("http://bibliotecacapitolare.org/catalogo-dei-manoscritti/")
a.gen.set_stprog("https://sites.hss.univr.it/laboratori_integrati/laboratorio-lamedan/") #cambiare
a.gen.set_completeness(0)
a.gen.set_creation(data)
a.gen.add_img_group('RAW-nef')
a.gen.img_groups['RAW-nef'].scanning.set_capture_software('digiCamControl (digiCamControlsetup_2.1.2.exe)')
a.gen.img_groups['RAW-nef'].scanning.set_scanner_manufacturer('Nikon Corporation') 
a.gen.img_groups['RAW-nef'].scanning.set_scanner_model('D810')
a.write('testw.xml')

