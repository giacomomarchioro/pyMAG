from __future__ import print_function
#https://www.iccu.sbn.it/export/sites/iccu/documenti/manuale.html#sez_bib
from datetime import datetime
from . import MAGtools  
import warnings


class holdings(object):
    """
    Al gruppo degli elementi DC, seguono una serie di elementi che servono a localizzare l'oggetto analogico all'interno di una particolare istituzione. Tali elementi sono racchiusi dall'elemento <holdings> . L'elemento è opzionale e ripetibile per contemplare la possibilità che un oggetto analogico possa essere posseduto da più istituzioni (è il caso, per esempio, di una rivista le cui annate non sono integralmente possedute da un'unica biblioteca). Per l'elemento è definito un unico attributo opzionale:
    """

    def __init__(self,ID):
        self.ID = ID
        self.library = None 
        self.inventory_number = None 
        self.shelfmarks = [] 
        self.type = None

    def set_library(self,value):
        """contiene il nome dell'istituzione proprietaria dell'oggetto analogico o di parte dell'oggetto analogico.

        Parameters
        ----------
        value : str
            nome dell'istituzione
        """
        self.library = value

    def set_inventory_number(self,value):
        """contiene il numero di inventario attribuito all'oggetto analogico dall'istituzione che lo possiede.

        Parameters
        ----------
        value : str
            numero di inventario
        """
        self.inventory_number = value
    
    def add_shelfmark(self,value,collocation_type=None):
        """contiene la collocazione dell'oggetto digitale all'interno del catalogo dell'istituzione che lo possiede.
        Ci possono essere più shelfmark antichi e moderni. I valori vengono aggiunti come tuple a self.shelfmarks.
        come segue:
        (value,collocation_type)

        Parameters
        ----------
        value : str
            collocazione dell'oggetto digitale.
        collocation_type : str
            si usa per definire il tipo di collocazione nel caso di collocazioni plurime, per esempio quando si vuole registrare una collocazione antica e una moderna.
        """
        self.shelfmarks.append((value,collocation_type))

    def get_vars(self):
        return vars(self)

class local_bib(object):
    """[summary]
Alcuni progetti di digitalizzazione che hanno adottato MAG come standard per la raccolta dei metadati amministrativi e gestionali, hanno messo in evidenza la necessità di dotare lo schema di alcuni elementi per la raccolta di particolari informazioni specialistiche relativamente all'oggetto analogico raccolte durante il processo di digitalizzazione. Tali informazioni non potevano essere agevolmente codificate all'interno del set Dublin Core poich� la scelta di non avvalersi degli elementi Dublin Core qualificati rendevano difficilmente identificabili tali contenuti. � stato perciò creato l'elemento <local_bib> di tipo xsd:sequence, per il quale non sono definiti attributi. L'elemento è opzionale così pure come gli elementi ivi contenuti:
    """

    def __init__(self):
        self.geo_coords = []
        self.not_dates = []
        self._used = False

    def add_geo_coord(self,geocoord):
        """contiene le coordinate geografiche relative a una carta o a una mappa. L'elemento è opzionale e ripetibile. Non sono definiti attributi.

        Parameters
        ----------
        geocoord : str
            le coordinate geografiche.
        """
        self._used = True
        self.geo_coords.append(geocoord)

    def add_not_date(self,not_date):
        """contiene la data di notifica relativa a un bando o a un editto. L'elemento è opzionale e ripetibile. Non sono definiti attributi.

        Parameters
        ----------
        not_date : la data di notifica
            la data di notifica relativa a un bando o a un editto
        """
        self._used = True
        self.not_dates.append(not_date)

    
class piece_rivista(object):
    """Pubblicazioni seriali e unità componenti di opere più vaste possono essere minuziosamente descritte. Tali informazioni sono raccolte dall'elemento <piece>, di tipo xsd:choice, vale a dire che può avere due contenuti diversi a seconda che contenga dati relativi a una pubblicazione seriale (per esempio il fascicolo di una rivista) o all'unità componente di un'opera più vasta (per esempio il singolo volume di un'enciclopedia). L'elemento è opzionale e non ripetibile; non sono definiti attributi.
    """
    def __init__(self):
        self.tipo = "periodico"
        self.year = MAGtools.obbligatorio
        self.issue = MAGtools.obbligatorio
        self.stpiece_per = None

    def set_year(self,value):
        """
        contiene l'annata di copertura editoriale di una pubblicazione seriale nella forma in cui si trova sulla pubblicazione stessa; per esempio 1913-1914 o anche 1987.
        """
        self.year = value

    def set_issue(self,value):
        """contiene gli estremi identificatori di un fascicolo di una pubblicazione seriale nella forma in cui si trova sulla pubblicazione stessa; per esempio n.� 8. L'elemento è obbligatorio qualora si scelga l'opzione periodici, anche se formalmente opzionale, e non ripetibile. Non sono definiti attributi.

        Parameters
        ----------
        value : str
            issue
        """
        self.issue = value
    
    def set_stpiece_per(self,value):
        """il campo permette di registrare in una forma normalizzata il riferimento a un fascicolo di un periodico; questo sia per poter scambiare i dati, sia per poter ordinare in modo automatico i vari record. Il campo <stpiece_per> è opzionale, non ripetibile e non è inteso a sostituire le informazioni contenute negli altri campi di <piece>. Formalmente è definito come restrizione del tipo xsd:string, essendo il suo contenuto regolato da una complessa espressione regolare. La sintassi utilizzata per la normalizzazione è quella dello standard SICI (ANSI/NISO Z39.56) per i segmenti Chronology, Enumeration e Supplements and Indexes http://www.niso.org/standards/standard_detail.cfm?std_id=530. Sinteticamente il risultato si presenta come
(cronologia)livello_numerazione:livello_numerazione:livello_numerazione :livello_numerazione.
Le regole per la sua creazione sono descritte ai punti 6.3.2, 6.3.3 e 6.3.4 del SICI e vengono qui di seguito richiamate.
        
        https://www.iccu.sbn.it/export/sites/iccu/documenti/manuale.html#per
        Parameters
        ----------
        value : [type]
            [description]
        """

        raise NotImplementedError


class piece_volume(object):
    """usato per unità componente di un'opera più vasta (per esempio il singolo volume di un'enciclopedia).
    ATTENZIONE: si utilizza nel caso di RACCOLTE VOLUMI.
    """
    def __init__(self):
        self.tipo = "volume di raccolta"
        self.part_number = MAGtools.obbligatorio
        self.part_name = MAGtools.obbligatorio
        self.stpiece_vol = None

    def set_part_number(self,value):
        """numero di unità componente. Per esempio: 2, IV, 4.5. L'elemento è obbligatorio nel caso di unità componenti, anche se formalmente opzionale, e non ripetibile

        Parameters
        ----------
        value : [type]
            [description]
        """
        #TODO: check
        self.part_number = value

    def set_part_name(self,value):
        """nome/titolo di una unità componente. Per esempio: Volume II; Parte III, Tomo 2. L'elemento è obbligatorio nel caso di unità componenti, anche se formalmente opzionale, e non ripetibile.

        Parameters
        ----------
        value : [type]
            [description]
        """
        #TODO: check
        self.part_name = value

    def set_stpiece_col(self,value):
        """forma normalizzata del riferimento a una parte di una unità componente. Formalmente è definito come restrizione del tipo xsd:string, essendo il suo contenuto regolato da un'espressione regolare. La sintassi da adottare è la seguente: volume:parte:parte, volume può avere fino a 3 cifre, parte fino a quattro; entrambe le sezioni parte sono opzionali.
        Volume 3, parte 2, tomo 1 -> 3:2:1
        Volume 47 -> 47
        Volume 2, parte 1 --> 2:1                
                    
        L'elemento è opzionale e non ripetibile.

        Parameters
        ----------
        value : [type]
            [description]
        """
        #TODO: check
        self.stpiece_vol = value



class bib(object):
    """
L'elemento <bib> è il secondo figlio dell'elemento root <metadigit> ed è obbligatorio. Esso contiene una serie di elementi figli che raccolgono metadati descrittivi relativamente all'oggetto analogico digitalizzato o, nel caso di documenti born digital, relativamente al documento stesso. L'elemento non è ripetibile.

Per l'elemento è definito un attributo obbligatorio level.


    """

    def __init__(self):
        # Attrubutes
        self.level = MAGtools.obbligatorio
        # Elements
        self.holdings = dict()
        #obbligatorio
        self.identifiers = []
        self.local_bib = local_bib()
        self.piece_volume = piece_volume()
        self.piece_rivista = piece_rivista()
        self.titles = []
        self.creators = []
        self.publishers = [] 
        self.subjects = [] 
        self.descriptions = [] 
        self.contributors = [] 
        self.dates = [] 
        self.types = [] 
        self.formats = [] 
        self.sources = [] 
        self.languages = [] 
        self.relations = [] 
        self.coverages = [] 
        self.rightss = [] 

    def create_holidngwithoutID(self):
        """Usato quando si vuole creare un holding senza ID. Verrà assegnato un ID numerico non valido per un file MAG. 
        """
        count = 0
        while count in self.holdings.keys():
            count+=1
        self.holdings[count] = holdings()

    @MAGtools.checkgroupID
    def create_holdingsID(self,ID):
        """
        Non è chiaro se dobbiamo applicare le stesse regolo di img_groupID. MA le applichiamo per sicurezza.
        Parameters
        ----------
        ID : [type]
            [description]
        """
        if ID in self.holdings.keys():
            warnings.warn("L'ID è già presente nella lista degli ID.")
        self.holdings[ID] = holdings()

    def set_level(self,value):
        """level : indica il livello della descrizione bibliografica. Il suo valore deve essere scelto fra i seguenti:

        level : indica il livello della descrizione bibliografica. Il suo valore deve essere scelto fra i seguenti:
        a: spoglio
        m: monografia
        s: seriale
        c: raccolta prodotta dall'istituzione
        Parameters
        ----------
        None : [type]
            [description]
        """
        conv_dict = {"monografia": "m",
                        "seriale": "s",
                        "raccolta prodotta dall'istituzione": "c"}
        url = "https://www.iccu.sbn.it/export/sites/iccu/documenti/manuale.html#sez_bib"
        value = MAGtools.validvalue(value=value,valuedict=conv_dict,url=url)
        self.level = value


    def add_identifier(self,value):
        """contiene un identificatore univoco di un record descrittivo nell'ambito di un dato contesto. Di solito si usa un identificatore di un record bibliografico (opportunamente normalizzato) appartenente a un qualche schema di catalogazione (per es. SBN, Library of Congress).

    Il <dc:identifier>, tuttavia, non va confuso con la segnatura dell'oggetto analogico o con la sua classificazione catalografica. Si tratta infatti di un codice identificativo che serve per fare riferimento in modo univoco a un dato oggetto; come tale pertanto, non dovrebbe contenere al suo interno alcuno spazio o altro carattere dotato di significato speciale. Nel caso in cui si voglia comunque usare segnature o sigle catalografiche, poich� un identificatore meccanico deve sottostare a regole particolari, è comunque necessario normalizzare tale segnatura applicando le cosiddette URI Escaping Techniques

        Parameters
        ----------
        value : str
            identificatore univoco di un record descrittivo
        """
        newvalue = MAGtools.URIescaping(value)
        if newvalue != value:
            print("Applichati escape chr. %s" %newvalue)
        self.identifiers.append(newvalue)

    def add_title(self,value):
        """ aggiunge l'elemento DoublinCore alla lista"""
        self.titles.append(value)

    def add_creator(self,value):
        """ aggiunge l'elemento DoublinCore alla lista"""
        self.creators.append(value)

    def add_publisher(self,value):
        """ aggiunge l'elemento DoublinCore alla lista"""
        self.publishers.append(value)

    def add_subject(self,value):
        """ aggiunge l'elemento DoublinCore alla lista"""
        self.subjects.append(value)

    def add_description(self,value):
        """ aggiunge l'elemento DoublinCore alla lista"""
        self.descriptions.append(value)

    def add_contributor(self,value):
        """ aggiunge l'elemento DoublinCore alla lista"""
        self.contributors.append(value)

    def add_date(self,value):
        """ aggiunge l'elemento DoublinCore alla lista"""
        self.dates.append(value)

    def add_type(self,value):
        """ aggiunge l'elemento DoublinCore alla lista"""
        self.types.append(value)

    def add_format(self,value):
        """ aggiunge l'elemento DoublinCore alla lista"""
        self.formats.append(value)

    def add_source(self,value):
        """ aggiunge l'elemento DoublinCore alla lista"""
        self.sources.append(value)

    def add_language(self,value):
        """ aggiunge l'elemento DoublinCore alla lista"""
        self.languages.append(value)

    def add_relation(self,value):
        """ aggiunge l'elemento DoublinCore alla lista"""
        self.relations.append(value)

    def add_coverage(self,value):
        """ aggiunge l'elemento DoublinCore alla lista"""
        self.coverages.append(value)

    def add_rights(self,value):
        """ aggiunge l'elemento DoublinCore alla lista"""
        self.rightess.append(value)

    def get_vars(self):
        return vars(self)


