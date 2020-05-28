from __future__ import print_function
#https://www.iccu.sbn.it/export/sites/iccu/documenti/manuale.html
from datetime import datetime
import MAGtools 
import warnings
import re


class image_dimension(object):
    """
Le dimensioni dell'immagini digitale sono codificate grazie all'elemento <image_dimensions>, per il quale è definito un tipo complesso specializzato, niso:dimensions, appartenente al namespace niso . L'elemento <image_dimensions> è obbligatorio e non ripetibile. Il tipo niso:dimensions è definito come xsd:sequence e comprende i seguenti elementi:
    
    ATTENZIONE: Non sembrano corrispondere ad i termini aggiornati.
    """
    def __init__(self):
        self.imagelenght = None
        self.imagewidth = None
        self.source_xdimension = None
        self.source_ydimension = None

    def set_imagelengthandwidth(self,length,width):
        """
        Metodo per settare il numero di pixel verticali e orizzontali dell'immagine.

        Parameters
        ----------
        length : int
            contiene la lunghezza dell'immagine, vale a dire la dimensione verticale espressa in pixel. L'elemento è obbligatorio e non ripetibile. Raccomandazione NISO (Data Dictionary, p. 23)
        width : int
            contiene la larghezza dell'immagine, vale a dire la dimensione orizzontale espressa in pixel. L'elemento è obbligatorio e non ripetibile. Raccomandazione NISO (Data Dictionary, p. 22)
        """
        lenght = MAGtools.checkpositiveinteger(lenght)
        width = MAGtools.checkpositiveinteger(width)
        self.imagelenght = lenght
        self.imagewidth = width

    def set_xydimensions(self,x_inches,y_inches):
        """[summary]
        Attenzione: non sembra sia aggiornato.
        Parameters
        ----------
        x_inches : float
             contiene la larghezza (dimensione orizzontale) dell'oggetto analogico digitalizzato espresso in pollici (inches). L'elemento è opzionale e non ripetibile. Raccomandazione NISO (Data Dictionary, pp. 25-26)
        y_inches : float
            contiene la lunghezza (dimensione verticale) dell'oggetto analogico digitalizzato espresso in pollici (inches). L'elemento è opzionale e non ripetibile. Raccomandazione NISO (Data Dictionary, p. 26)
        """
        self.source_xdimension = x_inches
        self.source_ydimension = y_inches


class image_metrics(object):
    def __init__(self):
        self.samplingfrequencyunit = None
        self.samplingfrequencyplane = None
        self.xsamplingfrequency = None
        self.ysamplingfrequency = None
        self.photometricinterpretation = None
        self.bitpersample = None


    def set_samplingfrequencyunit(self,value):
        """obbligatorio e non ripetibile, definisce l'unità di misura usata 
        per il contenuto degli elementi <niso:xsamplingfrequency> e <niso:ysamplingfrequency>.
         Per l'elemento è definito un tipo semplice specializzato, anch'esso 
         contenuto nel file niso-mag.xsd, denominato niso:samplingfrequencyunittype. 
         Tale tipo è definito come restrizione di xsd:string ed è costituito 
         dall'enumerazione dei seguenti valori:
        1 : nessuna unità di misura definita
        2 : inch, pollice
        3 : centimetro

        Il valore può essere il numero o la stringa di descrzione. In quest'utlimo caso
        la funzione lo convertira nel codice relativo.

        Parameters
        ----------
        value : str,int
            campo da impostare può essere il numero oppure il valore in lettere.
        """
        conv_dict = {"nessuna unità di misura definita": "1",
                     "inch, pollice": "2",
                     "pollice": "2",
                     "inch": "2",
                     "centimetro": "3"}
        url = "https://www.iccu.sbn.it/export/sites/iccu/documenti/manuale.html#image_metrics"
        value = MAGtools.validvalue(value=value,valuedict=conv_dict,url=url)
        self.samplingfrequencyunit = value

    def set_samplingfrequencyplane(self,value):
        """obbligatorio e non ripetibile, dichiara il piano focale del campionamento. Per l'elemento è definito un tipo semplice specializzato, anch'esso contenuto nel file niso-mag.xsd, denominato niso:samplingfrequencyplanetype. Tale tipo è definito come restrizione di xsd:string ed è costituito dall'enumerazione dei seguenti valori:
1 : camera/scanner focal plane, quando non sono definite le dimensioni dell'oggetto che si sta digitalizzando (per es. quando si riproduce con una fotocamera)
2 : object plane, quando l'oggetto e la riproduzione hanno la stessa dimensione (per es. quando si riproduce con uno scanner)
3 : source object plane, quando la dimensione della riproduzione è maggiore dell'oggetto originale (per es. quando si riproduce da un microfilm)

        Il valore può essere il numero o la stringa di descrzione. In quest'utlimo caso
        la funzione lo convertira nel codice relativo.

        Parameters
        ----------
        value : str,int
            campo da impostare può essere il numero oppure il valore in lettere.
        """
        conv_dict = {"camera/scanner focal plane": "1",
                     "object plane": "2",
                     "source object plane": "3"}
        url = "https://www.iccu.sbn.it/export/sites/iccu/documenti/manuale.html#image_metrics"
        value = MAGtools.validvalue(value=value,valuedict=conv_dict,url=url)
        self.samplingfrequencyplane = value

    def set_xsamplingfrequency(self,value):
        """opzionale (ma obbligatorio se applicabile) e non ripetibile, contiene la frequenza di campionamento nella direzione orizzontale, presente in alternativa a <ppi> e <dpi> (elementi obsoleti), con <niso:samplingfrequencyunit> = 2 (inch) o 3 (centimetro); con 1 il campo è nullo. Il suo contenuto è di tipo xsd:positiveInteger, vale a dire un numero positivo

        Parameters
        ----------
        value : str,int
            campo da impostare può essere il numero oppure il valore in lettere.
        """
        url = "https://www.iccu.sbn.it/export/sites/iccu/documenti/manuale.html#image_metrics"
        value = MAGtools.checkpositiveinteger(value=value,url=url)
        self.xsamplingfrequency = value

    def set_ysamplingfrequency(self,value):
        """opzionale (ma obbligatorio se applicabile) e non ripetibile, contiene la frequenza di campionamento nella direzione verticale, presente in alternativa a <ppi> e <dpi> (elementi obsoleti), con <niso:samplingfrequencyunit> = 2 (inch) o 3 (centimetro); con 1 il campo è nullo. Il suo contenuto è di tipo xsd:positiveInteger, vale a dire un numero positivo
        Il valore può essere il numero o la stringa di descrzione. 

        Parameters
        ----------
        value : str,int
            campo da impostare può essere il numero oppure il valore in lettere.
        """
        conv_dict = {"nessuna unità di misura definita": "1",
                     "inch, pollice": "2",
                     "pollice": "2",
                     "inch": "2",
                     "centimetro": "3"}
        value = MAGtools.checkpositiveinteger(value=value,url=url)
        self.ysamplingfrequency = value

    def set_photometricinterpretation(self,value):
        """obbligatorio e non ripetibile, definisce l'interpretazione fotometrica dei bit del campione. Per l'elemento è definito un tipo semplice specializzato, anch'esso contenuto nel file niso-mag.xsd, denominato niso:photometricinterpretationtype. Tale tipo è definito come restrizione di xsd:string ed è costituito dall'enumerazione dei seguenti valori:
        WhiteIsZero
        BlackIsZero
        RGB
        Palette color
        Transparency Mask
        CMYK
        YcbCr
        CIELab

        Parameters
        ----------
        value : str
            campo da impostare può essere il numero oppure il valore in lettere.
        """
        lista = [   "WhiteIsZero",
                    "BlackIsZero",
                    "RGB",
                    "Palette color",
                    "Transparency Mask",
                    "CMYK",
                    "YcbCr",
                    "CIELab",]
        url = "https://www.iccu.sbn.it/export/sites/iccu/documenti/manuale.html#image_metrics"
        value = MAGtools.valueinlist(value=value,lista=lista,url=url)
        self.photometricinterpretation = value

    def set_bitpersample(self,value):
        """obbligatorio e non ripetibile, definisce il numero di bit per ciascun campione, esplicitando il rapporto profondità/colore. Per l'elemento è definito un tipo semplice specializzato, anch'esso contenuto nel file niso-mag.xsd, denominato niso:bitpersampletype. Tale tipo è definito come restrizione di xsd:string ed è costituito dall'enumerazione dei seguenti valori:
        1 : bitonale, bianco e nero
        4 : scala di grigi a 4 bit
        8 : scala di grigi o gamma di 256 colori a 8 bit
        8,8,8 : colori RGB a 24 bit
        16,16,16 : per immagini TIFF o HDR a 48 bit
        8,8,8,8 : CMYK a 32 bit
        Parameters
        ----------
        value : str,int
            campo da impostare può essere il numero oppure il valore in lettere.
        """
        value = str(value)
        lista = [   "1",
                    "4",
                    "8",
                    "8,8,8",
                    "16,16,16",
                    "8,8,8,8"]
        url = "https://www.iccu.sbn.it/export/sites/iccu/documenti/manuale.html#image_metrics"
        value = MAGtools.valueinlist(value=value,lista=lista,url=url)
        self.bitpersample = value


class  format_(object):
    """
    Il formato delle immagini (tipologia e modalità di compressione) è gestito dall'elemento <format> ed è codificato secondo lo standard NISO. L'elemento, oltre che dentro <img>, può essere usato dentro <img_group> ; è formalmente opzionale, ma in pratica deve sempre essere usato, o dentro <img> o dentro <img_group>. Per <format> è definito un tipo specializzato appartenente al namespace niso denominato niso:format che presenta una sequenza di tre elementi:
    """
    def __init__(self):
        self.name = None
        self.mime = None
        self.compression = None

    def set_name(self,value):
        """obbligatorio e non ripetibile, contiene il formato dell'immagine. � di tipo xsd:string, si consiglia di usare valori come JPG, GIF, TIF, PDF ecc. Si raccomanda di usare valori formati da tre caratteri. Una sintassi alternativa può essere adottata per i formati che codificano il numero di revisione nel file header: [formato file][numero di revisione], per esempio: TIFF/EP 1.0.0.0.

        Parameters
        ----------
        value : str
            estensione del file.
        """
        lista = ["JPG","GIF","TIF","PDF","PNG"]
        url = "https://www.iccu.sbn.it/export/sites/iccu/documenti/manuale.html#img_format"
        value = MAGtools.valueinlist(value=value,lista=lista,url=url)
        self.name = value

    def set_mime(self,value):
        """obbligatorio e non ripetibile, contiene il tipo mime dell'immagine. Per l'elemento è definito un tipo semplice specializzato, anch'esso contenuto nel file niso-mag.xsd, denominato niso:img_mimetype. Tale tipo è definito come restrizione di xsd:string ed è costituito dall'enumerazione dei seguenti valori (si noti la presenza del formato PDF, che per sua natura si presta sia per contenuti testuali - e come tale il valore è previsto fra i mime type delle sezioni OCR e DOC -, sia per veicolare immagini):
        image/jpeg
        image/tiff
        image/gif
        image/png
        image/vnd.djvu
        application/pdf
        Parameters
        ----------
        value : str
            estensione del file dopo slash.
        """
        lista = [ "image/jpeg",
                  "image/tiff",
                  "image/gif",
                  "image/png",
                  "image/vnd.djvu",
                  "application/pdf",]
        url = "https://www.iccu.sbn.it/export/sites/iccu/documenti/manuale.html#img_format"
        value = MAGtools.valueinlist(value=value,lista=lista,url=url)
        self.mime = value
    
    def set_compression(self,value):
        """obbligatorio e non ripetibile, dichiara il tipo di compressione applicato all'immagine. Per l'elemento è definito un tipo semplice specializzato, anch'esso contenuto nel file niso-mag.xsd, denominato niso:compressiontype. Tale tipo è definito come restrizione di xsd:string ed è costituito dall'enumerazione dei seguenti valori:
            Uncompressed
            CCITT 1D
            CCITT Group 3
            CCITT Group 4
            LZW
            JPG
            PNG
            DJVU
        Parameters
        ----------
        value : str
            estensione del file dopo slash.
        """
        lista = [ "Uncompressed",
                  "CCITT 1D",
                  "CCITT Group 3",
                  "CCITT Group 4",
                  "LZW",
                  "JPG",
                  "PNG",
                  "DJVU"]
        url = "https://www.iccu.sbn.it/export/sites/iccu/documenti/manuale.html#img_format"
        value = MAGtools.valueinlist(value=value,lista=lista,url=url)
        self.compression = value

class scanning(object):
    """
    Le modalità della scansione dell'oggetto sono codificate dell'elemento <scanning> secondo lo standard NISO. L'elemento è, oltre che dentro <img>, può essere usato dentro <img_group> ; è formalmente opzionale, ma in pratica deve sempre essere usato, o dentro <img> o dentro <img_group>. Per <scanning> è definito un tipo specializzato appartenente al namespace niso denominato niso:image_creation. � di tipo xsd:sequence e contiene quattro elementi tutti opzionali; si consiglia comunque di usarne almeno uno. Gli esempi dei valori sono desunte dalla normativa ICCD per la catalogazione delle fotografie: http://www.iccd.beniculturali.it/download/schedaf.pdf:     
    """

    def __init__(self):
        self.sourcetype = None
        self.scanningagency = None
        self.devicesource = None
        self.scanningsystem = None
        self.scanner_manufacturer = None
        self.scanner_model = None
        self.capture_software = None

    def set_sourcetype(self,value):
        """opzionale e non ripetibile, descrive le caratteristiche fisiche del supporto analogico di partenza. Di tipo xsd:string, si suggerisce comunque di adottare uno dei seguenti valori:
negativo : per immagini fotografiche i cui valori tonali risultino invertiti rispetto a quelli del soggetto raffigurato e che permettono di produrre un numero illimitato di "positivi"
positivo : per immagini fotografiche, ottenute da "negativi", i cui valori tonali corrispondano a quelli del soggetto raffigurato; sono da considerarsi "positivi" anche i prodotti ottenuti da matrici virtuali attraverso stampanti, plotter, etc.
diapositiva : per immagini fotografiche positive realizzate su supporti trasparenti e visibili per trasparenza o per proiezione
unicum : per immagini fotografiche "uniche", ottenute cioè senza mediazione di "negativi" e che, a loro volta, non possono essere utilizzate come "matrici"; sono da considerarsi "unicum", ad esempio, dagherrotipi, ambrotipi, ferrotipi, polaroid ed inoltre prodotti unici ottenuti con procedimenti elettronici analogico-digitali, come fax o fotocopie
fotografia virtuale : per "matrici virtuali", cioè per immagini latenti memorizzate su memorie di massa analogiche, analogico-digitali e digitali
vario: .../... : per oggetti complessi e/o compositi costituiti da elementi appartenenti a categorie diverse. Es.: vario: positivo/unicum; vario: unicum/positivo/fotografia virtuale

        Parameters
        ----------
        value : str
            una stringa tra i campi possibili.
        """
        lista = [ "negativo",
                  "positivo",
                  "diapositiva",
                  "unicum",
                  "fotografia virtuale",
                  "vario: .../...",]
        url = "https://www.iccu.sbn.it/export/sites/iccu/documenti/manuale.html#scanning"
        if "vario:" in value:
            splitted = value.split(":")
            splitted = splitted[1].split("/")
            for value in splitted:
                MAGtools.valueinlist(value=value,lista=lista,url=url)
        else:
            value = MAGtools.valueinlist(value=value,lista=lista,url=url)
        self.sourcetype = value

    def set_scanningagency(self,value):
        """opzionale e non ripetibile, contiene il nome della persona, società o ente produttore dell'immagine digitale, cioè dell'entità che ha realizzato la scansione. � di tipo xsd:string. Se assente, si assume che la scansione sia stata effettuata all'interno dell'istituzione responsabile del progetto di digitalizzazione.
        Parameters
        ----------
        value : str
            una stringa contentente il nome dell'ente o della persona.
        """
        self.scanningagency = value

    def set_devicesource(self,value):
        """opzionale e non ripetibile, descrive la tipologia dell'apparecchiatura di scansione, per esempio "scanner", "fotocamera digitale", "videocamera". 

        Parameters
        ----------
        value : str
            una stringa tra i campi possibili.
        """
        lista = [ "scanner", "fotocamera digitale", "videocamera",]
        url = "https://www.iccu.sbn.it/export/sites/iccu/documenti/manuale.html#scanning"
        value = MAGtools.valueinlist(value=value,lista=lista,url=url)
        self.devicesource = value

    def set_scanner_manufacturer(self,value):
        """obbligatorio e non ripetibile, contiene il nome del produttore del dispositivo

        Parameters
        ----------
        value : str
            una stringa tra i campi possibili.
        """
        lista = [ "scanner", "fotocamera digitale", "videocamera",]
        url = "https://www.iccu.sbn.it/export/sites/iccu/documenti/manuale.html#scanning"
        value = MAGtools.valueinlist(value=value,lista=lista,url=url)
        self.scanner_manufacturer = value
    
    def set_scanner_model(self,value):
        """obbligatorio e non ripetibile, contiene la marca e il modello dell'apparecchiatura di acquisizione.

        Parameters
        ----------
        value : str
            una stringa con il modello dell'apparecchiatura di acquisizione.
        """
   
        url = "https://www.iccu.sbn.it/export/sites/iccu/documenti/manuale.html#scanning"
        value = MAGtools.valueinlist(value=value,lista=lista,url=url)
        self.scanner_manufacturer = value
    
    def set_capture_software(self,value):
        """obbligatorio e non ripetibile, contiene il nome del software usato per l'acquisizione dell'immagine e la versione:
        es. OmniScan 10.01
        Aggiungere la versione dopo uno spazio bianco.

        Parameters
        ----------
        value : str
            contiene il nome del software usato per l'acquisizione dell'immagine.
        """
        splitted = value.split(" ")
        name = " ".join(splitted[:-1])
        version = splitted[-1]
        url = "https://www.iccu.sbn.it/export/sites/iccu/documenti/manuale.html#scanning"
        value = MAGtools.valueinlist(value=value,lista=lista,url=url)
        self.scanner_manufacturer = value


        
class img(object):
    """https://www.iccu.sbn.it/export/sites/iccu/documenti/manuale.html#sez_img
    La sezione IMG raccoglie i metadati amministrativi e gestionali relativi alle immagini statiche. Alcuni di questi dati, in realtà, possono essere raccolti direttamente all'interno della sezione GEN, grazie all'elemento <img_group>, il cui contenuto verrà tuttavia trattato in questa sezione per omogeneità tematica.

La sezione IMG utilizza il namespace niso: che fa riferimento a uno schema che traduce le linee guida del Data Dictionary NISO. Tale schema è stato realizzato dal Comitato MAG e verrà quindi qui interamente documentato di volta in volta nei successivi paragrafi e complessivamente nel paragrafo Lo schema Niso .

La sezione IMG è costituita di una sequenza di elementi <img>, uno per ciascuna immagine digitale descritta da MAG. L'elemento è opzionale e ripetibile. Il suo contenuto è di tipo xsd:sequence, e può contenere i seguenti elementi:
    L'elemento file si torva qui già scomposto in fileLocation (tipo di link es. URL) e fileLink (il percorso del file)
    """
    def __init__(self,sequence_number):
        # attributi
        self.ID = None
        self.imggroupID = None
        self.holdingsID = None
        # elementi
        self.sequence_number = sequence_number
        self.nomenclature = None
        self.usage = None 
        self.scale = None 
        self.file = None
        self.filesize = None
        self.image_dimensions = image_dimension()
        self.image_metrics = image_metrics()
        self.ppi = None
        self.dpi = None
        self.format = format_()
        self.scanning = scanning()
        self.datetimecreated = None
        self.target = None 
        self.altimg = None
        self.note = None 
        self.fileLocation = None
        self.fileLink = None

    

    def set_nomencalature(self,value):
        """A ciascuna immagine deve inoltre essere attribuita una denominazione, per esempio Pagina 1, Carta 2v, ecc. Tale denominazione viene codificata dall'elemento <nomenclature>. L'elemento è di tipo xsd:string; si consiglia comunque di definire una nomenclatura controllata negli standard di progetto. L'elemento è obbligatorio e non ripetibile
        Parameters
        ----------
        value : int
            numero di pixels.
        """
        url = "https://www.iccu.sbn.it/export/sites/iccu/documenti/manuale.html#img_el"
        msg = "Tali misurazione è sconsigliata in quanto obsoleta e imprecisa; è conservata solo per garantire la compatibilità con le versioni precedenti di MAG. Si consiglia, invece di usare <niso:xsamplingfrequency> e <niso:ysamplingfrequency> all'interno di <image_metrics>. L'uso di <dpi> e <ppi> di fatto equivalgono a <niso:xsamplingfrequency> e <niso:ysamplingfrequency> con valori uguali e con <niso:samplingfrequencyunit> = 2."
        self.nomenclature = value

    def set_usage(self,uso,copyright):
        """A ciascuna immagine deve inoltre essere attribuita una denominazione, per esempio Pagina 1, Carta 2v, ecc. Tale denominazione viene codificata dall'elemento <nomenclature>. L'elemento è di tipo xsd:string; si consiglia comunque di definire una nomenclatura controllata negli standard di progetto. L'elemento è obbligatorio e non ripetibile
        Parameters
        ----------
        value : int
            numero di pixels.
        """
        url = "https://www.iccu.sbn.it/export/sites/iccu/documenti/manuale.html#img_el"
        conv_dict={"digitalizzazione completa": "0",
                     "uso pubblico": "1",
                     "bassa risoluzione":"2",
                     "preview":"4"}

        conv_dict2 = {"a":"il repository non ha il copyright dell'oggetto digitale",
                      "b":"il repository ha il copyright dell'oggetto digitale"}
        url = "https://www.iccu.sbn.it/export/sites/iccu/documenti/manuale.html#img_group"
        uso = MAGtools.validvalue(value=uso,valuedict=conv_dict,url=url)
        copyright = MAGtools.validvalue(value=copyright,valuedict=conv_dict2,url=url)
        self.usage = uso+copyright

    def set_side(self,side):
        """
        Esattamente come per la fotocopiatura, la scansione di un oggetto analogico può procedere in vario modo, è possibile infatti procedere per una pagina alla volta oppure per pagine affiancate. Tale informazione può essere registrata grazie all'elemento opzionale e non ripetibile <side>, per il quale è definito un tipo semplice specializzato denominato a sua volta side. Tale tipo è definito come restrizione di xsd:string ed è costituito dall'enumerazione dei seguenti valori:

            left : l'immagine contiene la digitalizzazione della pagina sinistra di un volume o di un fascicolo
            right : l'immagine contiene la digitalizzazione della pagina destra di un volume o di un fascicolo
            double : l'immagine contiene la digitalizzazione di una doppia pagina di un volume o di un fascicolo
            part : l'immagine contiene la digitalizzazione parziale dell'oggetto analogico fonte.
        
        """
        lista = ['left','right','double','part']
        url = "https://www.iccu.sbn.it/export/sites/iccu/documenti/manuale.html#scansione"
        self.side = valueinlist(value,lista,url)

    def set_file(self,link,Location,):
        """
        Il link è in genere il percorso che punta alla risorsa. 

        Il tipo complesso link contiene anche la definizione di un ulteriore attributo Location che specifica il tipo di link definito da xlink:href. I valori possibili sono:

        URN: Uniform Resource Name;
        URL: Uniform Resource Locator;
        URI: Uniform Resource Identifier (sui primi tre tipi di identificatori di risorsa, si veda la panoramica informativa del W3C http://www.w3.org/Addressing/)
        PURL: Persistent URL, sviluppato dalla OCLC, Online Computer Library Center (si veda il sito PURL http://purl.oclc.org/).
        HANDLE: tipologia di riferimenti definiti secondo il sistema Handle della CNRI, Corporation for National Research Initiatives (si veda il sito dell'Handle System http://www.handle.net/).
        DOI: Digital Object Identifier (si veda il sito della Doi Foundation http://www.doi.org/).
        OTHER: altro.
        Un percorso su rete locale può essere indicato come URL.

        """
        lista = ['URN','URL','URI','PURL','HANDLE','DOI','OTHER']
        url = "https://www.iccu.sbn.it/export/sites/iccu/documenti/manuale.html#xlink"
        Location = valueinlist(Location,lista,url)
        self.fileLocation = Location
        self.fileLink = link

    def set_md5(self,value):
        """
        L'integrità del contenuto digitale è verificata grazie alla sua impronta digitale, registrata dall'elemento <md5>, un codice standard di 32 caratteri che viene rilevato automaticamente grazie all'impiego di apposti applicativi. Le regole per il rilevamento dell'impronta devono essere definite localmente, così come i momenti per il rilievo stesso (prima del momento del deposito, al momento del deposito, o in entrambi i momenti). Si tratta di una raccomandazione NISO e come tale il tipo specializzato che governa il contenuto dell'elemento appartiene al namespace niso ed è denominato niso:checksum . Tale tipo è definito come restrizione di xsd:string che limita la lunghezza massima della stringa a 32 caratteri.
        
        Parameters
        ----------
        value : str
            la checksum md5
        """
        if len(re.findall(r"([a-fA-F\d]{32})", value)) == 1:
            warnings.warn("Non sembra un md5 valido.")
        self.md5 = value

    def set_scale(self,value):
        """Durante la scansione è possibile impiegare una scala millimetrica da affiancare all'oggetto sottoposto a scansione in modo da ricostruire le dimensioni dell'originale partendo dalla sua riproduzione digitale. L'informazione può essere registrata grazie all'elemento opzionale e non ripetibile <scale> per il quale è definito un tipo semplice specializzato denominato millimetric_scale. Tale tipo è definito come restrizione di xsd:string ed è costituito dall'enumerazione dei seguenti valori:

        0 : non è presente alcuna scala millimetrica
        1 : è presente una scala millimetrica

        Parameters
        ----------
        value : [type]
            [description]
        """
        url = "https://www.iccu.sbn.it/export/sites/iccu/documenti/manuale.html#img_el"
        conv_dict={"0" : "non è presente alcuna scala millimetrica",
                   "1" : "è presente una scala millimetrica"}
        self.scale = MAGtools.validvalue(value=value,valuedict=conv_dict,url=url)

    def set_filesize(self,value):
        """La grandezza del file (che va espressa in byte) è registrata dell'elemento <filesize>. L'elemento è di tipo xsd:Integer (un numero positivo), è opzionale e non ripetibile. Anche l'elemento <filesize> è una raccomandazione NISO (Cfr. Data Dictionary, p. 13).

        Parameters
        ----------
        value : int
            la dimensione del file in byte
        """
        url = "https://www.iccu.sbn.it/export/sites/iccu/documenti/manuale.html#img_file"
        value = MAGtools.checkpositiveinteger(value,url)
        self.filesize = value

    def set_ppi(self,value):
        """pixel per inch, cioè il numero di pixel presenti per ogni pollice quadrato,
        Parameters
        ----------
        value : int
            numero di pixels.
        """
        url = "https://www.iccu.sbn.it/export/sites/iccu/documenti/manuale.html#ppi"
        msg = "Tali misurazione è sconsigliata in quanto obsoleta e imprecisa; è conservata solo per garantire la compatibilità con le versioni precedenti di MAG. Si consiglia, invece di usare <niso:xsamplingfrequency> e <niso:ysamplingfrequency> all'interno di <image_metrics>. L'uso di <dpi> e <ppi> di fatto equivalgono a <niso:xsamplingfrequency> e <niso:ysamplingfrequency> con valori uguali e con <niso:samplingfrequencyunit> = 2."
        warnings.warn(msg + "\nPer maggiori informazioni:\n" + url, category=DeprecationWarning)
        MAGtools.checkpositiveinteger(value=value,url=url)
        self.ppi = value

    def set_dpi(self,value):
        """dots per inch, cioè il numero di punti presenti per ogni pollice quadrato. Si applica propriamente agli output (testo, immagini) prodotti dalle stampanti e non alle immagini memorizzate su supporto digitale; tale misurazione è tuttavia normalmente utilizzata anche all'interno di progetti di digitalizzazione.
        Parameters
        ----------
        value : int
            numero di punti.
        """
        url = "https://www.iccu.sbn.it/export/sites/iccu/documenti/manuale.html#ppi"
        msg = "Tali misurazione è sconsigliata in quanto obsoleta e imprecisa; è conservata solo per garantire la compatibilità con le versioni precedenti di MAG. Si consiglia, invece di usare <niso:xsamplingfrequency> e <niso:ysamplingfrequency> all'interno di <image_metrics>. L'uso di <dpi> e <ppi> di fatto equivalgono a <niso:xsamplingfrequency> e <niso:ysamplingfrequency> con valori uguali e con <niso:samplingfrequencyunit> = 2."
        warnings.warn(msg + "\nPer maggiori informazioni:\n" + url, category=DeprecationWarning)
        MAGtools.checkpositiveinteger(value=value,url=url)
        self.dpi = value


class img_group(object):
    def __init__(self):
        # attributi
        self.ID = None
        # elementi
        self.image_metrics =  image_metrics()
        self.ppi = None
        self.dpi = None
        self.format = format_()
        self.scanning = scanning()

    
    def set_ppi(self,value):
        """pixel per inch, cioè il numero di pixel presenti per ogni pollice quadrato,
        Parameters
        ----------
        value : int
            numero di pixels.
        """
        url = "https://www.iccu.sbn.it/export/sites/iccu/documenti/manuale.html#ppi"
        msg = "Tali misurazione è sconsigliata in quanto obsoleta e imprecisa; è conservata solo per garantire la compatibilità con le versioni precedenti di MAG. Si consiglia, invece di usare <niso:xsamplingfrequency> e <niso:ysamplingfrequency> all'interno di <image_metrics>. L'uso di <dpi> e <ppi> di fatto equivalgono a <niso:xsamplingfrequency> e <niso:ysamplingfrequency> con valori uguali e con <niso:samplingfrequencyunit> = 2."
        warnings.warn(msg + "\nPer maggiori informazioni:\n" + url, category=DeprecationWarning)
        MAGtools.checkpositiveinteger(value=value,url=url)
        self.ppi = value

    def set_dpi(self,value):
        """dots per inch, cioè il numero di punti presenti per ogni pollice quadrato. Si applica propriamente agli output (testo, immagini) prodotti dalle stampanti e non alle immagini memorizzate su supporto digitale; tale misurazione è tuttavia normalmente utilizzata anche all'interno di progetti di digitalizzazione.
        Parameters
        ----------
        value : int
            numero di punti.
        """
        url = "https://www.iccu.sbn.it/export/sites/iccu/documenti/manuale.html#ppi"
        msg = "Tali misurazione è sconsigliata in quanto obsoleta e imprecisa; è conservata solo per garantire la compatibilità con le versioni precedenti di MAG. Si consiglia, invece di usare <niso:xsamplingfrequency> e <niso:ysamplingfrequency> all'interno di <image_metrics>. L'uso di <dpi> e <ppi> di fatto equivalgono a <niso:xsamplingfrequency> e <niso:ysamplingfrequency> con valori uguali e con <niso:samplingfrequencyunit> = 2."
        warnings.warn(msg + "\nPer maggiori informazioni:\n" + url, category=DeprecationWarning)
        MAGtools.checkpositiveinteger(value=value,url=url)
        self.dpi = value




class gen(object):
    def __init__(self):
        # attributi
        self.creation = None
        self.last_update = None
        # elementi
        self.stprog = None
        self.collection = None
        self.agency = None
        self.access_rights = None
        self.completeness = None
        self.img_groups = dict()
        self.audio_groups = dict()
        self.video_groups = dict()

   

    def set_creation(self,creation_date=None):
        """la data di creazione della sezione (opzionale)

        Parameters
        ----------
        creation_date : str, optional
            La data di creazione della sezione, by default None
        """
        if creation_date == None:
            creation_date = datetime.now().strftime('%Y-%m-%dT%H:%M:%S')
        self.creation = MAGtools.check_datetime(creation_date)

    def set_last_update(self,timestamp=None):
        """la data dell'ultimo aggiornamento della sezione (opzionale)

        Parameters
        ----------
        timestamp : str, optional
            la data dell'ultimo aggiornamento della sezione, by default None
        """
        if timestamp == None:
            timestamp = datetime.now().strftime('%Y-%m-%dT%H:%M:%S')
        self.last_update = MAGtools.check_datetime(timestamp)

    def set_stprog(self,stprog):
        """contiene la URI dove è possibile trovare la documentazione relativa 
        la progetto di digitalizzazione. Tipicamente si tratta della pagina web 
        in cui sono specificate le scelte relative alla digitalizzazione del 
        progetto; in alternativa si suggerisce di puntare alla home page 
        dell'istituzione responsabile del progetto. Il suo contenuto è 
        xsd:anyURI. L'elemento è obbligatorio, non ripetibile e non 
        sono definiti attributi.

        Parameters
        ----------
        stprog : str
            la stringa con l'url per esempio 'http://marciana.venezia.sbn.it/admv.htm'
        """
        self.stprog = MAGtools.check_url(stprog)
    
    def set_collection(self,collection):
        """contiene la URI (tipicamente l'indirizzo di una pagina web) di un 
        documento in cui viene specificata la collezione cui fa parte la 
        risorsa o le risorse digitalizzate. Il suo contenuto è xsd:anyURI.
         L'elemento è opzionale, non ripetibile e non sono definiti attributi.
        Parameters
        ----------
        collection : str
            la stringa con l'urlper esempio 'http://marciana.venezia.sbn.it/admv.htm'
        """
        self.collection = MAGtools.check_url(collection)

    def set_agency(self,agency):
        """contiene il nome dell'istituzione responsabile del progetto di digitalizzazione. 
        Il suo contenuto è xsd:string, ma si raccomanda di usare la sintassi UNIMARC definita 
        per il campo 801, cioè cod. paese (due caratteri):codice Agenzia per intero, per esempio: 
        IT:BNCF. In alternativa è possibile usare una sigla riconosciuta, 
        per esempio dall'Anagrafe biblioteche italiane: http://anagrafe.iccu.sbn.it/, 
        per esempio: IT:VE0049 o IT:RM1316. L'elemento è obbligatorio, non ripetibile e 
        non sono definiti attributi.

        PyMAG consiglia di usare quest'ultima opzione in quanto più facilmente tracciabile.

        Parameters
        ----------
        agency : str
            Il codice dell'agenzie per esempio IT:RM1316
        """
        self.agency = MAGtools.check_agency(agency)


    def set_access_rights(self,value):
        """dichiara le condizioni di accessibilità dell'oggetto descritto nella sezione BIB. 
        Il suo contenuto deve assumere uno dei seguenti valori:
    0 : uso riservato all'interno dell'istituzione
    1 : uso pubblico
    L'elemento è obbligatorio, non ripetibile e non sono definiti attributi.

        Parameters
        ----------
        access_rights : str or int
            condizioni di accessibilità può essere 0 : uso riservato all'interno dell'istituzione
    1 : uso pubblico in stringa o numero.
        """
        conv_dict = {"uso riservato all'interno dell'istituzione": "0",
                     "uso pubblico": "1"}
        url = "https://www.iccu.sbn.it/export/sites/iccu/documenti/manuale.html#img_group"
        value = MAGtools.validvalue(value=value,valuedict=conv_dict,url=url)
        self.access_rights = value


    def set_completeness(self,completeness):
        """dichiara la completezza della digitalizzazione. Il suo contenuto deve assumere uno dei seguenti valori:
        0 : digitalizzazione completa
        1 : digitalizzazione incompleta
        L'elemento è obbligatorio, non ripetibile e non sono definiti attributi.
        L'esempio che segue riguarda un oggetto digitale completamente digitalizzato il cui accesso è libero
        """
        completeness=str(completeness)
        conv_dict={"digitalizzazione completa": "0",
                     "uso pubblico": "1"}
        url = "https://www.iccu.sbn.it/export/sites/iccu/documenti/manuale.html#img_group"
        value = MAGtools.validvalue(value=value,valuedict=conv_dict,url=url)
        self.completeness = value

    @MAGtools.checkgroupID
    def create_img_groupID(self,ID):
        if ID in self.img_groups.keys():
            warnings.warn("L'ID è già presente nella lista degli ID.")
        self.img_groups[ID] = img_group()

    def check_obligatory(self):
        if self.stprog is None:
            warnings.warn(" campo stprog è obbligatorio")
        if self.agency is None:
            warnings.warn(" campo stprog è obbligatorio")
        if self.access_rights is None:
            warnings.warn(" campo access_rights è obbligatorio")
        if self.completeness is None:
            warnings.warn(" campo completeness è obbligatorio")
