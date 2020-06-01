from __future__ import print_function
import xml.etree.ElementTree as ET
import numpy as np
from . import GEN_IMG_sections
from . import BIB_section
from . import STRU_section
from .MAGtools import obbligatorio 
import warnings
import logging
#logging.captureWarnings(True)
"""

"""
__all__ = ['MAGFile']

class MAGFile(object):
    """An object oriented representation of the MAG application schema."""
    def __init__(self, filepath=None):
        # obbligatori
        self.gen = GEN_IMG_sections.gen() 
        self.bib = BIB_section.bib()
        # opzionali
        self.structs = [] 
        self.imgs = []
        self.version = "2.0.1"
        # counters
        self.struct_counter = 0
        self.imgs_counter = 0
        self.holdings_counter = 0
        self.warnings = warnings
        if filepath is not None:
            self.load(filepath)
    
    def add_img(self,holdingsID=None,imggroupID=None):
        if imggroupID is not None:
            if imggroupID not in self.gen.img_groups:
                warnings.warn("Referenziazione ad un img_group ID non definito in gen.img_groups.")
        if holdingsID is not None:
            if holdingsID not in self.bib.holdings:
                warnings.warn("Referenziazione ad un holdings ID non definito in bib.holdings.")
        self.imgs_counter += 1
        self.imgs.append(GEN_IMG_sections.img(self.imgs_counter,imggroupID,holdingsID))
    
    def add_stru(self):
        self.struct_counter += 1
        self.structs.append(STRU_section.stru(self.struct_counter))

    def check(self):
        # image metrics
        for img in self.imgs:
            sn = img.sequence_number
            fields = vars(img)
            for i in fields:
                if fields[i] is obbligatorio:
                    warnings.warn("Il campo %s dell'immagine %s è obbligatorio." %(i,sn),stacklevel=2)
            i_d = vars(img.image_dimensions)
            for i in i_d:
                    if i_d[i] is obbligatorio and i_dg[i] is obbligatorio:
                        warnings.warn("Il campo %s dell'immagine %s è obbligatorio." %(i,sn),stacklevel=2)
            i_m = vars(img.image_metrics)
            i_f = vars(img.format)
            i_s = vars(img.scanning)
            # il campo potrebbe essere definito all'interno di un image-group
            if fields['imggroupID'] is not None:
                imggrp = self.gen.img_groups[fields['imggroupID']]
                i_dg = vars(imggrp.image_dimensions)
                i_mg = vars(imggrp.image_metrics)
                i_fg = vars(imggrp.format)
                i_sg = vars(imggrp.scanning)
                for i in i_m:
                    if i_m[i] is obbligatorio and i_mg[i] is obbligatorio:
                        warnings.warn("Il campo %s dell'immagine %s è obbligatorio." %(i,sn),stacklevel=2)
                for i in i_f:
                    if i_f[i] is obbligatorio and i_fg[i] is obbligatorio:
                        warnings.warn("Il campo %s dell'immagine %s è obbligatorio." %(i,sn),stacklevel=2)
                if img.scanning.status == 'Used':
                    for i in i_s:
                        if i_s[i] is obbligatorio and i_sg[i] is obbligatorio:
                            warnings.warn("Il campo %s dell'immagine %s è obbligatorio." %(i,sn),stacklevel=2)
            else:
                for i in i_m:
                    if i_m[i] is obbligatorio:
                        warnings.warn("Il campo %s dell'immagine %s è obbligatorio." %(i,sn),stacklevel=2)
                for i in i_f:
                    if i_f[i] is obbligatorio:
                        warnings.warn("Il campo %s dell'immagine %s è obbligatorio." %(i,sn),stacklevel=2)
                if img.scanning.status == 'Used':
                    for i in i_s:
                        if i_s[i] is obbligatorio:
                            warnings.warn("Il campo %s dell'immagine %s è obbligatorio." %(i,sn),stacklevel=2)



                
            



    def load(self, filepath):
        tree = ET.parse(filepath)
        root = tree.getroot()
        def add_newstruct(elem):
            for se in elem:
                if se.tag.endswith('sequence_number'):
                    mystru = STRU_section.stru(se.text)
                elif se.tag.endswith('element'):
                    for sse in se:
                        pass
                    #TODO:Element
                    #mystru.add_element()
                elif se.tag.endswith('stru'):
                    mystru.add_stru(add_newstruct(se))
                else:
                    print("Non convertito%s" %se)


            if 'start' in elem.attrib:
                mystru.set_start(elem.attrib['start'])
            if 'stop' in elem.attrib:
                mystru.set_stop(elem.attrib['stop'])
            if 'descr' in elem.attrib:
                mystru.set_descr(elem.attrib['descr'])
            return mystru
            
        def load_scanning(elem,root):
            if se.tag.endswith('capture_software'):
                root.set_capture_software(se.text)
            elif se.tag.endswith('devicesource'):
                root.set_devicesource(se.text)
            elif se.tag.endswith('scanner_manufacturer'):
                root.set_scanner_manufacturer(se.text)
            elif se.tag.endswith('scanner_model'):
                root.set_scanner_model(se.text)
            elif se.tag.endswith('scanningagency'):
                root.set_scanningagency(se.text)
            elif se.tag.endswith('sourcetype'):
                root.set_sourcetype(se.text)
            else:
                print("Non convertito%s" %se)


        def load_format(elem,root):
            for se in elem:
                if se.tag.endswith('compression'):
                    root.set_compression(se.text)
                elif se.tag.endswith('mime'):
                    root.set_mime(se.text)
                elif se.tag.endswith('name'):
                    root.set_name(se.text)
                else:
                    print("Non convertito%s" %se)


        def load_image_metrics(elem,root):
            for se in elem:
                if se.tag.endswith('bitpersample'):
                    root.set_bitpersample(se.text)
                elif se.tag.endswith('photometricinterpretation'):
                    root.set_photometricinterpretation(se.text)
                elif se.tag.endswith('samplingfrequencyplane'):
                    root.set_samplingfrequencyplane(se.text)
                elif se.tag.endswith('samplingfrequencyunit'):
                    root.set_samplingfrequencyunit(se.text)
                elif se.tag.endswith('xsamplingfrequency'):
                    root.set_xsamplingfrequency(se.text)
                elif se.tag.endswith('ysamplingfrequency'):
                    root.set_ysamplingfrequency(se.text)
                else:
                    print("Non convertito%s" %se)


        def load_image_dimension(elem,root):
            imglengt, imagelength = None, None
            source_xdimension, source_ydimension = None, None

            for se in elem:
                if se.tag.endswith('imagewidth'):
                    imagewidth = se.text
                elif se.tag.endswith('imagelength'):
                    imagelength = se.text
                elif se.tag.endswith('source_xdimension'):
                    source_xdimension = se.text
                elif se.tag.endswith('source_ydimension'):
                    source_ydimension = se.text
                else:
                    print("Non convertito%s" %se)

            if imagewidth is not None and imagelength is not None:
                root.set_imagelengthandwidth(imagelength,imagewidth)
            if source_xdimension is not None and source_ydimension is not None:
                root.set_xydimensions(source_xdimension,source_ydimension)
            
        

        def load_img_group(elem):
            ID = elem.attrib['ID']
            self.gen.add_img_group(ID)
            for se in elem:
                if se.tag.endswith('dpi'):
                    self.gen.img_groups[ID].set_dpi(se.text)
                elif se.tag.endswith('ppi'):
                    self.gen.img_groups[ID].set_ppi(se.text)
                elif se.tag.endswith('image_metrics'):
                    root = self.gen.img_groups[ID].image_metrics
                    load_image_metrics(se,root)
                elif se.tag.endswith('format'):
                    root = self.gen.img_groups[ID].format
                    load_format(se,root)
                elif se.tag.endswith('scanning'):
                    root = self.gen.img_groups[ID].scanning
                    load_format(se,root)
                else:
                    print("Non convertito%s" %se)

        def load_holdings(elem):
            self.holdings_counter +=1
            # if there is no ID we use a progressive count as ID
            if 'ID' in elem.attrib:
                ID = elem.attrib['ID']
            else:
                ID = self.holdings_counter
            myholding = BIB_section.holdings(ID)
            for se in elem:
                if se.tag.endswith('shelfmark'):
                    myholding.add_shelfmark(se.text)
                elif se.tag.endswith('inventory_number'):
                    myholding.set_inventory_number(se.text)
                elif se.tag.endswith('library'):
                    myholding.set_library(se.text)
                else:
                    print('Non convertito: %s' %se)
            self.bib.holdings[ID] = myholding


        # Main part
        for elem in root:
            if elem.tag.endswith('gen'):
                # attributi
                self.gen.set_creation(elem.attrib['creation'])
                self.gen.set_last_update(elem.attrib['last_update'])
                # elementi
                for se in elem:
                    if se.tag.endswith('access_rights'):
                        self.gen.set_access_rights(se.text)
                    elif se.tag.endswith('agency'):
                        self.gen.set_agency(se.text)
                    elif se.tag.endswith('collection'):
                        self.gen.set_collection(se.text)
                    elif se.tag.endswith('completeness'):
                        self.gen.set_completeness(se.text)
                    elif se.tag.endswith('stprog'):
                        self.gen.set_stprog(se.text)
                    elif se.tag.endswith('img_group'):
                        load_img_group(se)
                    else:
                        print("Non convertito%s" %se)
            elif elem.tag.endswith('bib'):
                self.bib.set_level(elem.attrib['level'])
                for se in elem:
                    if se.tag.endswith('contributor'):
                        self.bib.add_contributor(se.text)
                    elif se.tag.endswith('coverage'):
                        self.bib.add_coverage(se.text)
                    elif se.tag.endswith('identifier'):
                        self.bib.add_coverage(se.text)
                    elif se.tag.endswith('creator'):
                        self.bib.add_creator(se.text)
                    elif se.tag.endswith('date'):
                        self.bib.add_date(se.text)
                    elif se.tag.endswith('description'):
                        self.bib.add_description(se.text)
                    elif se.tag.endswith('format'):
                        self.bib.add_format(se.text)
                    elif se.tag.endswith('language'):
                        self.bib.add_language(se.text)
                    elif se.tag.endswith('publisher'):
                        self.bib.add_publisher(se.text)
                    elif se.tag.endswith('relation'):
                        self.bib.add_relation(se.text)
                    elif se.tag.endswith('rights'):
                        self.bib.add_rights(se.text)
                    elif se.tag.endswith('source'):
                        self.bib.add_source(se.text)
                    elif se.tag.endswith('subject'):
                        self.bib.add_subject(se.text)
                    elif se.tag.endswith('title'):
                        self.bib.add_title(se.text)
                    elif se.tag.endswith('type'):
                        self.bib.add_type(se.text)
                    elif se.tag.endswith('holdings'):
                        load_holdings(se)
                    else:
                        print("Non convertito: %s" %se)
                
                
            elif elem.tag.endswith('stru'):
                # aggiungiamo ricorsivamente le strutture
                self.structs.append(add_newstruct(elem))

            elif elem.tag.endswith('img'):
                from MAG.GEN_IMG_sections import img
                if 'imggroupID' in elem.attrib:
                    imgID = elem.attrib['imggroupID']
                else:
                    imgID = None
                if 'holdingsID' in elem.attrib:
                    holdingsID = elem.attrib['holdingsID']
                else:
                    holdingsID = None
                for se in elem:
                    if se.tag.endswith('sequence_number'):
                        newimg = img(se.text,imggroupID=imgID,holdingsID=holdingsID)
                    elif se.tag.endswith('datetimecreated'):
                        newimg.set_datetimecreated(se.text)
                    elif se.tag.endswith('dpi'):
                        newimg.set_dpi(se.text)
                    elif se.tag.endswith('file'):
                        loc = se.attrib['Location']
                        link = se.attrib['{http://www.w3.org/TR/xlink}href']
                        newimg.set_file(link=link,Location=loc)
                    elif se.tag.endswith('filesize'):
                        newimg.set_filesize(se.text)
                    elif se.tag.endswith('md5'):
                        newimg.set_md5(se.text)
                    elif se.tag.endswith('nomenclature'):
                        newimg.set_nomenclature(se.text)
                    elif se.tag.endswith('note'):
                        newimg.set_note(se.text)
                    elif se.tag.endswith('ppi'):
                        newimg.set_ppi(se.text)
                    elif se.tag.endswith('scale'):
                        newimg.set_scale(se.text)
                    elif se.tag.endswith('side'):
                        newimg.set_side(se.text)
                    elif se.tag.endswith('usage'):
                        newimg.set_usage(stringapersonalizzata=se.text)
                    elif se.tag.endswith('image_dimensions'):
                        load_image_dimension(se,newimg.image_dimensions)
                    elif se.tag.endswith('image_metrics'):
                        load_image_metrics(se,newimg.metrics)
                    elif se.tag.endswith('format'):
                        load_format(se,newimg.format)
                    else:
                        print('Non convertito: %s' %se)
                self.imgs.append(newimg)
                self.imgs_counter+=1





            else:
                print("Non convertito%s" %elem)

    def write(self, filepath):
        p = ET.Element('mag:metadigit')
        p.set("xmlns:mag","http://www.iccu.sbn.it/metaAG1.pdf") 
        p.set("xmlns","http://www.iccu.sbn.it/metaAG1.pdf")
        p.set("xmlns:dc","http://purl.org/dc/elements/1.1/")
        p.set("xmlns:niso","http://www.niso.org/pdfs/DataDict.pdf" )
        p.set("xmlns:xlink","http://www.w3.org/TR/xlink" )
        p.set("xmlns:xsi","http://www.w3.org/2001/XMLSchema-instance")
        p.set("version","2.0.1")
        p.set("xsi:schemaLocation","http://www.iccu.sbn.it/metaAG1.pdf http://www.iccu.sbn.it/directories/metadigit201/metadigit.xsd")

        gen = ET.SubElement(p, 'gen')
        # L'elemento <gen> è il primo figlio dell'elemento root <metadigit> ed è obbligatorio. 
        # Esso contiene una serie di elementi figli che contengono informazioni relative all'istituzione 
        # responsabile del progetto di digitalizzazione, al progetto stesso, alla completezza o integrità del file,
        #  all'accessibilità dell'oggetto (o gli oggetti) descritto nella sezione BIB.
        # L'elemento, inoltre, può contenere informazioni tecniche condivise da più oggetti descritti dal documento MAG. L'elemento non è ripetibile.
        # Per l'elemento sono definiti due attributi opzionali:
        # creation : la data di creazione della sezione
        # last_update : la data dell'ultimo aggiornamento della sezione
        # Entrambi gli attributi sono di tipo xsd:dateTime, vale a dire che la data deve essere necessariamente espressa nel 
        # seguente formato: Anno (4 cifre) - Mese (2 cifre) - Giorno (2 cifre) T Ora (2 cifre) : Minuti (2 cifre) : Secondi (2 cifre) o,
        #  più formalmente, aaaa-mm-ggThh:mm:ss; per esempio:
        # <mag:gen creation="2005-08-04T13:00:00" last_update="2005-08-04T13:00:00">
        gen.set("creation",creation) # opzionale implenta check
        gen.set("last_update",last_update)
        # riferimento agli standard di progetto OB,NR
        # contiene la URI dove è possibile trovare la documentazione relativa la progetto di digitalizzazione.
        #  Tipicamente si tratta della pagina web in cui sono specificate le scelte relative alla 
        # digitalizzazione del progetto; in alternativa si suggerisce di puntare a
        # alla home page dell'istituzione responsabile del progetto. Il suo contenuto è xsd:anyURI.
        #  L'elemento è obbligatorio, non ripetibile e non sono definiti attributi.
        magstprog = ET.SubElement(gen,'stprog')
        magstprog.text = magstprogtxt

        # contiene la URI (tipicamente l'indirizzo di una pagina web) di un documento in cui viene 
        # specificata la collezione cui fa parte la risorsa o le risorse digitalizzate. 
        # Il suo contenuto è xsd:anyURI. L'elemento è opzionale, non ripetibile e non sono definiti attributi.

        collection = ET.SubElement(gen,'collection')
        collection.text = collectiontxt
        # contiene il nome dell'istituzione responsabile del progetto di digitalizzazione. Il suo contenuto è xsd:string, ma si raccomanda di 
        # usare la sintassi UNIMARC definita per il campo 801, cioè cod. paese (due caratteri):codice Agenzia 
        # per intero, per esempio: IT:BNCF. In alternativa è possibile usare una sigla riconosciuta, per esempio dall'Anagrafe biblioteche 
        # italiane: http://anagrafe.iccu.sbn.it/, per esempio: IT:VE0049 o IT:RM1316. L'elemento è obbligatorio, non ripetibile e non sono 
        # definiti attributi.
        # -- meglio usare l'anagrafe che il codice Agenzia che non riesco a capire che cos'è.
        # controlla nell'anagrafe https://anagrafe.iccu.sbn.it/isil/IT-ZR0055
        agency = ET.SubElement(gen,'agency')
        agency.text = agencytxt
        # <access_rights> : dichiara le condizioni di accessibilità dell'oggetto descritto nella sezione BIB. Il suo contenuto deve assumere uno dei seguenti valori:
        # 0 : uso riservato all'interno dell'istituzione
        # 1 : uso pubblico
        # L'elemento è obbligatorio, non ripetibile e non sono definiti attributi.
        access_rights = ET.SubElement(gen,'access_rights')
        access_rights.text = access_rightstxt

        # <completeness> : dichiara la completezza della digitalizzazione. Il suo contenuto deve assumere uno dei seguenti valori:
        # 0 : digitalizzazione completa
        # 1 : digitalizzazione incompleta
        # L'elemento è obbligatorio, non ripetibile e non sono definiti attributi.
        completeness = ET.SubElement(gen,'completeness')
        completeness.text = completenesstxt
        # La digitalizzazione di un oggetto analogico (per esempio un volume) può dar luogo a molti oggetti digitali (per esempio le immagini che
        # riproducono ogni pagina del volume). Normalmente tali oggetti condividono un certo numero di caratteristiche, specie se la digitalizzazione è stata 
        # compiuta nello stesso momento. In questi casi è normale descrivere tutte le immagini ottenute dalla digitalizzazione di un singolo oggetto analogico
        # all'interno di un unico documento MAG.
        # Per esempio se digitalizziamo le pagine di un volume usando il medesimo scanner e, una volta settata la risoluzione, 
        # il formato di output e una serie di altri parametri, tutte le immagini ottenute dalla scansione delle pagine avranno caratteristiche tecniche comuni. 
        # Lo stesso discorso vale per tracce audio e per stream video.
        # Al fine di non dover ripetere all'interno dello stesso documento MAG le medesime informazioni, è possibile inserirle una volta sola all'interno
        #  dell'elemento <gen> e successivamente fare richiamare tali definizioni ogni volta che si descrive un nuovo oggetto digitale. 
        # Gli elementi definiti a tale scopo sono tre: <img_group>, <audio_group> e <video_group>. Tali elementi sono così formalmente definiti (file metaype.xsd):

        # Le caratteristiche comuni a un gruppo omogeneo immagini possono essere definite all'interno dell'elemento <img_group>. 
        # L'elemento è opzionale, ripetibile e ha un attributo obbligatorio:


        # creo l'elemento 
        img_group = ET.SubElement(gen,'img_group')
        # creo il grupppo ID seguendo le formule
        imggroupID1 = create_img_groupID('Masters')
        # assegno l'ID all gruppo
        img_group.set('ID', imggroupID1)


        image_metrics = ET.SubElement(img_group,'image_metrics')
        # informazioni sul campionamento
        nisosamplingfrequencyunit = ET.SubElement(image_metrics, 'niso:samplingfrequencyunit')
        nisosamplingfrequencyunit.text = nisosamplingfrequencyunittxt
        nisosamplingfrequencyplane = ET.SubElement(image_metrics, 'niso:samplingfrequencyplane')
        nisosamplingfrequencyplane.text = nisosamplingfrequencyplanetxt
        nisosamplingfrequencyunit = ET.SubElement(image_metrics, 'niso:samplingfrequencyunit')
        nisosamplingfrequencyunit.text = nisosamplingfrequencyunittxt
        nisobitpersample = ET.SubElement(image_metrics, 'niso:bitpersample')
        nisobitpersample.text = nisobitpersampletxt
        # ppi and dpi
        ppi = ET.SubElement(img_group, 'ppi')
        ppi.text = ppitxt
        dpi = ET.SubElement(img_group, 'dpi')
        dpi.text = dpitxt
        # formato immagine
        fromat_ = ET.SubElement(img_group,'format')
        nisoname = ET.SubElement(fromat_, 'niso:name')
        nisoname.text = nisonametxt
        nisomime = ET.SubElement(fromat_, 'niso:mime')
        nisomime.text = nisomimetxt
        nisocompression = ET.SubElement(fromat_, 'niso:compression')
        nisocompression.text = nisocompressiontxt
        # informazione sulla procedura di scansione
        scanning = ET.SubElement(img_group,'scanning')
        nisoscanningagency = ET.SubElement(scanning,'niso:scanningagency')
        nisoscanningsystem = ET.SubElement(scanning,'niso:scanningsystem')
        nisoscanner_manufacturer = ET.SubElement(nisoscanningsystem,'niso:scanner_manufacturer')
        nisoscanner_manufacturer.text = nisoscanner_manufacturertxt
        nisoscanner_model = ET.SubElement(nisoscanningsystem,'niso:scanner_model')
        nisoscanner_model.text = nisoscanner_modeltxt
        nisocapture_software = ET.SubElement(nisoscanningsystem,'niso:capture_software')
        nisocapture_software.text = nisocapture_softwaretxt

            
        # https://www.iccu.sbn.it/export/sites/iccu/documenti/manuale.html#sez_bib
        # L'elemento <bib> è il secondo figlio dell'elemento root <metadigit> ed è obbligatorio. 
        # Esso contiene una serie di elementi figli che raccolgono metadati descrittivi relativamente all'oggetto
        #  analogico digitalizzato o, nel caso di
        # documenti born digital, relativamente al documento stesso. L'elemento non è ripetibile.
        bib = ET.SubElement(p, 'bib')
        # Per l'elemento è definito un attributo obbligatorio:
        # level : indica il livello della descrizione bibliografica. Il suo valore deve essere scelto fra i seguenti:
        # a: spoglio
        # m: monografia
        # s: seriale
        # c: raccolta prodotta dall'istituzione
        biblevel = 'c'
        if biblevel not in ['a','m','s','c']:
            raise ValueError(("Il campo level deve essere scelto fra i seguenti: a (spoglio),"
                            "m (monografia), s (seriale), c (raccolta prodotta dall'isituzione)."
                            "Ho ricevuto %s." %biblevel))
        # c: raccolta prodotta dall'istituzione")
        bib.set('level',biblevel)



        #https://www.iccu.sbn.it/export/sites/iccu/documenti/manuale.html#DC
        # Il primo degli elementi Dublin Core è il <dc:identifier> che contiene un identificatore univoco di un record 
        # descrittivo nell'ambito di un dato contesto. Di solito si usa un identificatore di un record bibliografico 
        # (opportunamente normalizzato) appartenente a un qualche schema di catalogazione (per es. SBN, Library of Congress).

        caracter_tohex = {"/":"%2F","?":"%3F","#":"%23","[":"%5B","]":"%5D",
        ";":"%3B",":":"%3A","@":"%40","&":"%26","=":"%3D","+":"%2B","$":"%24",
        ",":"%2C","<":"%3C",">":"%3E","%":"%25","\"":"%22","{":"%7B","}":"%7D",
        "|":"%7C","\\":"%5C","^":"%5E","`":"%60"," ":"%20"}

        identifiertxt = r'my+strange\"'
        for i in caracter_tohex:
            identifiertxt = identifiertxt.replace(i,caracter_tohex[i])
        # può essere ripetibile info:bni/2004-778
        # Nel caso di <dc:identifier> plurimi, nella versione 1.5 di MAG era consentito differenziarli tramite 
        # l'utilizzo dell'attributo xsi:type. Tale soluzione, però, poneva complessi problemi di validazione. 
        # In questa versione, nel caso si vogliano inserire più <dc:identifier>, si propone l'utilizzo di un 
        # identificatore standardizzato da porre nel contenuto dell'elemento, vale a dire lo schema URI info 
        # che serve a referenziare tramite una URI gli asset riconosciuti che, pur avendo un identificatore pubblico, 
        # non possono essere dereferenziati a partire dalla stessa URI (ad esempio, non si possono presentare nella 
        # forma http://CFI0342793). Per poter usare tale sistema, è necessario registrare preventivamente un namespace 
        # al sito http://info-uri.info/. Ulteriori informazioni sullo schema URI info possono essere lette al sito 
        # http://info-uri.info/registry/docs/misc/faq.html oppure al sito http://www.loc.gov/standards/uri/info.html#openurl
        # Aggiungere la possibiltà per le seguenti:
        # <dc:identifier>info:sbn/CFI0342793</dc:identifier>
        # <dc:identifier>info:bni/2004-778</dc:identifier>

        dcidentifier = ET.SubElement(bib, 'dc:identifier')
        dcidentifier.text = identifiertxt

        dctitle = ET.SubElement(bib, 'dc:title')
        dctitle.text = dctitletxt

        dccreator = ET.SubElement(bib, 'dc:creator')
        dccreator.text = dccreatortxt
        # e via dicendo... 
        # Opzionali:
        holdings = ET.SubElement(bib, 'holdings')
        # contiene il nome dell'istituzione proprietaria dell'oggetto analogico o
        # di parte dell'oggetto analogico. Di tipo xsd:string, è opzionale e non ripetibile.
        library = ET.SubElement(holdings,'library')
        library.text = librarytxt
        inventory_number = ET.SubElement(holdings,'inventory_number')
        # contiene il numero di inventario attribuito all'oggetto analogico dall'istituzione 
        # che lo possiede. Di tipo xsd:string, è opzionale e non ripetibile.
        inventory_number.text = inventory_numbertxt
        shelfmark = ET.SubElement(holdings,'shelfmark')
        shelfmark.text = shelfmarktxt
        # lAlcuni progetti di digitalizzazione che hanno adottato MAG come standard per la 
        # raccolta dei metadati amministrativi e gestionali, hanno messo in evidenza la necessità 
        # di dotare lo schema di alcuni elementi per la raccolta di particolari informazioni
        #  specialistiche relativamente all'oggetto analogico raccolte durante il processo
        #  di digitalizzazione. Tali informazioni non potevano essere agevolmente codificate 
        # all'interno del set Dublin Core poiché la scelta di non avvalersi degli elementi 
        # Dublin Core qualificati rendevano difficilmente identificabili tali contenuti. � stato 
        # perciò creato l'elemento <local_bib> di tipo xsd:sequence, per il quale 
        # non sono definiti attributi.
        # https://www.iccu.sbn.it/export/sites/iccu/documenti/manuale.html#local_bib
        local_bib = ET.SubElement(bib, 'local_bib')
        # L'elemento è opzionale così pure come gli elementi ivi contenuti:
        # <geo_coord> : di tipo xsd:string, contiene le coordinate geografiche relative
        #  a una carta o a una mappa. L'elemento è opzionale e ripetibile. Non sono definiti attributi.
        geo_coord = ET.SubElement(local_bib, 'geo_coord')
        # <not_date> : di tipo xsd:string, contiene la data di notifica relativa a un bando
        #  o a un editto. L'elemento è opzionale e ripetibile. Non sono definiti attributi.
        not_date = ET.SubElement(local_bib, 'not_date')
        # https://www.iccu.sbn.it/export/sites/iccu/documenti/manuale.html#piece
        # Pubblicazioni seriali e unità componenti di opere più vaste possono essere minuziosamente
        #  descritte. Tali informazioni sono raccolte dall'elemento <piece>, di tipo xsd:choice, 
        # vale a dire che può avere due contenuti diversi a seconda che contenga dati relativi a 
        # una pubblicazione seriale (per esempio il fascicolo di una rivista) o all'unità 
        # componente di un'opera più vasta (per esempio il singolo volume di un'enciclopedia). 
        # L'elemento è opzionale e non ripetibile; non sono definiti attributi.
        piece = ET.SubElement(bib, 'piece')
        # non lo completiamo
        # ....

        # https://www.iccu.sbn.it/export/sites/iccu/documenti/manuale.html#piece
        # L'elemento <stru> è il terzo figlio dell'elemento root <metadigit>; l'elemento è opzionale, 
        # ripetibile e nidificabile. Esso contiene informazioni circa la struttura logica del documento digitalizzato. Tramite le informazioni codificate in questa sezione del record MAG è infatti possibile documentare la suddivisione interna di un documento (capitoli di un libro, articoli di una rivista), realizzare record MAG radice e record MAG di spoglio oppure collegare diversi MAG fra loro.
        # La sezione STRU trova la sua tipica utilizzazione nei seguenti tre casi:
        # quando si ritenga opportuno mettere in evidenza le eventuali partizioni interne di un oggetto digitale (es. capitoli di un libro);
        # nel caso di spogli, laddove le partizioni spogliate (es. articoli di una rivista) siano discrete autonomamente e come tali possano avere una propria sezione BIB;
        # per far riferimento ad altri oggetti MAG correlati non appartenenti alla stessa tipologia, per esempio nel caso di un cofanetto contenente CD musicali e un fascicolo di testo.
        # Non ha invece senso nel caso di un oggetto unitario, privo di strutture interne.
        # L'elemento <stru> è opzionale, ripetibile e ricorsivo, nel senso che è possibile innestare un numero indeterminato di elementi <stru>
        # gli uni dentro agli altri, al fine di documentare l'eventuale articolazione interna di un documento.
        # Il suo contenuto è di tipo xsd:sequence e può contenere i seguenti elementi:
        # 
        # <sequence_number> : contiene un numero progressivo che identifica un particolare <stru>. L'elemento è opzionale e non ripetibile
        # <nomenclature> : contiene il nome o la descrizione di una particolare struttura. L'elemento è opzionale e non ripetibile
        # <element> : opzionale e ripetibile, contiene:
        # un collegamento fra una particolare struttura e un contenuto precisato nelle sezioni IMG, OCR, DOC, AUDIO o VIDEO descritto all'interno del medesimo record MAG
        # un collegamento fra una particolare struttura e un contenuto precisato nelle sezioni IMG, OCR, DOC, AUDIO o VIDEO descritto all'interno di altri record MAG.
        # <stru> : contiene un ulteriore livello strutturale gerarchicamente subordinato rispetto all'elemento genitore. L'elemento è opzionale e ripetibile.
        # Per l'elemento <stru> sono definiti tre attributi, tutti opzionali. Il loro uso è deprecato in favore dell'uso degli elementi contenuti nella sezione. Tali attributi sono stati mantenuti per garantire la compatibilità della presente versione rispetto alle versioni precedenti.
        # descr : di tipo xsd:string, contiene il nome o la descrizione di una particolare struttura. Al posto di tale attributo è preferibile usare l'elemento <nomenclature>
        # start : di tipo xsd:string, contiene il numero di sequenza che segna l'inizio del range di contenuti (precisati nelle sezioni IMG, OCR, DOC, AUDIO o VIDEO) da collegare. Al posto di tale attributo è preferibile usare l'elemento <start> contenuto all'interno di <element>.
        # stop : di tipo xsd:string, contiene il numero di sequenza che segna la fine del range di contenuti (precisati nelle sezioni IMG, OCR, DOC, AUDIO o VIDEO) da collegare. Al posto di tale attributo è preferibile usare l'elemento <stop> contenuto all'interno di <element>.
        stru = ET.SubElement(p, 'stru')
        sequence_number = ET.SubElement(stru, 'sequence_number')
        nomenclature = ET.SubElement(stru, 'nomenclature')
        element = ET.SubElement(stru, 'element')
        resource = ET.SubElement(element, 'resource')
        start = ET.SubElement(element, 'start')
        stop = ET.SubElement(element, 'resource')

        # La sezione IMG raccoglie i metadati amministrativi e gestionali relativi alle immagini statiche. 
        # Alcuni di questi dati, in realtà, possono essere raccolti direttamente all'interno della sezione GEN, grazie all'elemento <img_group>, il cui contenuto verrà tuttavia trattato in questa sezione per omogeneità tematica.
        # 
        # La sezione IMG utilizza il namespace niso: che fa riferimento a uno schema che traduce le linee guida del Data Dictionary NISO. Tale schema è stato realizzato dal Comitato MAG e verrà quindi qui interamente documentato di volta in volta nei successivi paragrafi e complessivamente nel paragrafo Lo schema Niso .
        # 
        # La sezione IMG è costituita di una sequenza di elementi <img>, uno per ciascuna immagine digitale descritta da MAG. L'elemento è opzionale e ripetibile. Il suo contenuto è di tipo xsd:sequence, e può contenere i seguenti elementi:
        # 
        # <sequence_number> : contiene il numero di sequenza identificativo dell'immagine. Obbligatorio e non ripetibile
        # <nomenclature> : contiene la denominazione o titolo dell'immagine. Obbligatorio e non ripetibile
        # <usage> : definisce l'ambito d'uso dell'immagine in relazione agli standard di progetto. Opzionale e ripetibile
        # <side> : indica se l'immagine acquisita comprende una o due pagine del libro. Opzionale e non ripetibile
        # <scale> : indica la presenza di una scala millimetrica in fase di digitalizzazione. Opzionale e non ripetibile
        # <file> : localizza il file contenente l'immagine. Obbligatorio e non ripetibile
        # <md5> : contiene l'impronta del file. Obbligatorio e non ripetibile
        # <filesize> : fornisce la dimensione del file contenente l'immagine in byte. Opzionale e non ripetibile
        # <image_dimentions> : definisce le dimensioni dell'immagine digitale. Obbligatorio e non ripetibile
        # <image_metrics> : fornisce le principale caratteristiche tecniche dell'immagine secondo lo standard NISO. Opzionale e non ripetibile
        # <ppi> : risoluzione dell'immagine espressa in ppi. Opzionale e non ripetibile
        # <dpi> : risoluzione dell'immagine espressa in dpi. Opzionale e non ripetibile
        # <format> : dichiara formato dell'immagine secondo lo standard NISO. Opzionale e non ripetibile
        # <scanning> : registra le modalità di scansione dell'immagine. Opzionale e non ripetibile
        # <datetimecreated> : dichiara la data e l'ora di creazione dell'immagine. Opzionale e non ripetibile
        # <target> : indica la presenza di un target (scala cromatica) durante scansione dell'immagine secondo lo standard NISO. Opzionale e ripetibile
        # <altimg> : contiene la descrizione di un eventuale altro formato della medesima immagine. Opzionale e ripetibile
        # <note> : eventuali annotazioni all'immagine. Opzionale e non ripetibile. L'elemento è presente in ogni sezione; è di tipo xsd:string e può contenere qualsiasi tipo di annotazione.
        # Per l'elemento sono inoltre definiti i seguenti attributi:
        # 
        # imggroupID : di tipo xsd:IDREF contiene un riferimento all'attributo ID dell'elemento <img_group> . Tale attributo consente di collegare un <img> con le caratteristiche tecniche definite globalmente da <img_group>. L'attributo è opzionale; qualora non sia usato si assume che le caratteristiche tecniche dell'immagine non siano state altrove descritte e quindi l'elemento <image_metrics> deve ritenersi obbligatorio, così come <format> e <scanning>.
        # holdingsID : di tipo xsd:IDREF contiene un riferimento all'attributo ID dell'elemento <holdings> e serve a definire a quale istituzione appartiene l'oggetto analogico digitalizzato. L'attributo è opzionale.
        images = ['my imag','myimg3']
        for image in images:
            img = ET.SubElement(p, 'img')
            sequence_number = ET.SubElement(img,'sequence_number')
            nomenclature = ET.SubElement(img,'nomenclature')
            # A ciascuna immagine deve inoltre essere attribuita una denominazione, per esempio Pagina 1, Carta 2v, ecc. Tale denominazione viene codificata dall'elemento <nomenclature>. L'elemento è di tipo xsd:string; si consiglia comunque di definire una nomenclatura controllata negli standard di progetto. L'elemento è obbligatorio e non ripetibile
            # Dello stesso oggetto digitale (tipicamente un foglio di carta) possono essere tratte più immagini digitali, più o meno definite, in diversi formati, ognuna delle quali con una diversa finalità. � infatti usuale creare immagini di alta qualità per l'archiviazione interna e immagini di qualità più limitata per la diffusione esterna. La finalità dell'immagine digitale viene registrata dall'elemento <usage>. L'elemento è di tipo xsd:string; al fine di favorire la portabilità dei dati, si consiglia tuttavia di adottare le seguenti due tassonomie (adottate dai maggiori progetti di digitalizzazione italiani), la prima relativa alle modalità d'uso, la seconda al possesso del copyright da parte dell'istituzione:
            #  1 : master  2 : alta risoluzione 3 : bassa risoluzione 4 : preview e   a : il repository non ha il copyright dell'oggetto digitale b : il repository ha il copyright dell'oggetto digitale
            # L'elemento è opzionale e ripetibile.
            usage = ET.SubElement(img,'usage')
            # <side>, per il quale è definito un tipo semplice specializzato denominato a sua volta side. Tale tipo è definito come restrizione di xsd:string ed è costituito dall'enumerazione dei seguenti valori:    
            # left : l'immagine contiene la digitalizzazione della pagina sinistra di un volume o di un fascicolo
            # right : l'immagine contiene la digitalizzazione della pagina destra di un volume o di un fascicolo
            # double : l'immagine contiene la digitalizzazione di una doppia pagina di un volume o di un fascicolo
            # part : l'immagine contiene la digitalizzazione parziale dell'oggetto analogico fonte.
            side = ET.SubElement(img,'side')
            # Durante la scansione è possibile impiegare una scala millimetrica da affiancare all'oggetto sottoposto a scansione in modo da
            # ricostruire le dimensioni dell'originale partendo dalla sua riproduzione digitale. L'informazione può essere registrata
            # grazie all'elemento opzionale e non ripetibile <scale> per il quale è definito un tipo semplice specializzato denominato millimetric_scale.
            # Tale tipo è definito come restrizione di xsd:string ed è costituito dall'enumerazione dei seguenti valori:
            # 0 : non è presente alcuna scala millimetrica
            # 1 : è presente una scala millimetrica
            scale = ET.SubElement(img,'scale')
            # L'elemento <file> consente di localizzare il file che contiene l'immagine digitale. � di tipo link,
            # vale è dire che è un elemento vuoto che supporta attributi definiti dal namespace xlink .
            # L'elemento è obbligatorio e non ripetibile.
            # L'integrità del contenuto digitale è verificata grazie alla sua impronta digitale, registrata dall'elemento <md5>, 
            # un codice standard di 32 caratteri che viene rilevato automaticamente grazie all'impiego di apposti applicativi. 
            # Le regole per il rilevamento dell'impronta devono essere definite localmente, così come i momenti per il rilievo 
            # stesso (prima del momento del deposito, al momento del deposito, o in entrambi i momenti). Si tratta di una 
            # raccomandazione NISO e come tale il tipo specializzato che governa il contenuto dell'elemento 
            # appartiene al namespace niso ed è denominato niso:checksum . Tale tipo è definito come
            # restrizione di xsd:string che limita la lunghezza massima della stringa a 32 caratteri.

            # La grandezza del file (che va espressa in byte) è registrata dell'elemento <filesize>.
            # L'elemento è di tipo xsd:Integer (un numero positivo), è opzionale e non ripetibile.
            # Anche l'elemento <filesize> è una raccomandazione NISO (Cfr. Data Dictionary, p. 13).

            file_ = ET.SubElement(img,'file')
            md5 = ET.SubElement(img,'md5')
            image_dimentions = ET.SubElement(img,'image_dimentions')
            image_metrics = ET.SubElement(img,'image_metrics')
            ppi = ET.SubElement(img,'ppi')
            format_img = ET.SubElement(img,'format')
            scanning_img = ET.SubElement(img,'scanning')
            datetimecreated_img = ET.SubElement(img,'datetimecreated')
            target_img = ET.SubElement(img,'target')
            altimg = ET.SubElement(img,'altimg')
            note = ET.SubElement(img,'note')
            # imggroupID : di tipo xsd:IDREF contiene un riferimento all'attributo ID dell'elemento <img_group> . 
            # Tale attributo consente di collegare un <img> con le caratteristiche tecniche definite globalmente da <img_group>.
            #  L'attributo è opzionale; qualora non sia usato si assume che le caratteristiche tecniche dell'immagine non siano 
            # state altrove descritte e quindi l'elemento <image_metrics> deve ritenersi obbligatorio, così come <format> e <scanning>.
            img.set('imggroupID',img_ID)
            # holdingsID : di tipo xsd:IDREF contiene un riferimento all'attributo ID dell'elemento <holdings> e serve a 
            # definire a quale istituzione appartiene l'oggetto analogico digitalizzato. L'attributo è opzionale.
            img.set('holdingsID',holdingsID)

        xml = ET.tostring(p, encoding='utf-8')




        def indent(elem, level=0):
            i = "\n" + level*"  "
            j = "\n" + (level-1)*"  "
            if len(elem):
                if not elem.text or not elem.text.strip():
                    elem.text = i + "  "
                if not elem.tail or not elem.tail.strip():
                    elem.tail = i
                for subelem in elem:
                    indent(subelem, level+1)
                if not elem.tail or not elem.tail.strip():
                    elem.tail = j
            else:
                if level and (not elem.tail or not elem.tail.strip()):
                    elem.tail = j
            return elem  

        indent(p)
        tree = ET.ElementTree(p)
        tree.write('%s.xml'%filepath)