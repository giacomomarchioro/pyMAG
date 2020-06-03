# !pip install xmlschema
import os
import xmlschema
import requests
import time
# gli schemi originali possono essere trovati al seguente indirizzo:
# https://www.iccu.sbn.it/export/sites/iccu/documenti/mag2-2006.html
# però attenzione il file dc.xsd deve essere rinominato simpledc20020312.xsd
# possiamo scaricarli 
# baseurl = 'https://www.iccu.sbn.it/export/sites/iccu/documenti/'
# g = ['metadigit.xsd','metatype.xsd','audio-mag.xsd','video-mag.xsd','dc.xsd','xlink.xsd','niso-mag.xsd']
# for s in g:
#     content = 0
#     r = requests.get("".join([baseurl,s]))
#     content = r.content
#     filepath = os.path.join(os.getcwd(),'MAGXSD',s)
#     with open(filepath,'wb') as f:
#         f.write(content)


mainschema = os.path.join(os.getcwd(),'MAGXSD','metadigit.xsd')
folderwithschemas = os.path.join(os.getcwd(),'MAGXSD')
schema = xmlschema.XMLSchema(mainschema, base_url=folderwithschemas)
schema.validate('MagExporteample.xml')
schema.validate('testw.xml') 
