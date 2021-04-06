from __future__ import print_function
#https://www.iccu.sbn.it/export/sites/iccu/documenti/manuale.html
from datetime import datetime
from . import MAGtools 
import warnings

class element(object):
    """Il contenuto di un livello strutturale viene inserito all'interno di <element>. L'elemento permette di individuare prima la risorsa di riferimento tramite l'elemento <dc:identifier> di un altro record MAG, oppure di localizzare un particolare file contenente un record MAG privo di <dc:identifier> tramite l'elemento <file>, di dichiarare la denominazione di tale contenuto tramite l'elemento <nomenclature>, di far riferimento a una particolare risorsa tramite <resource>, infine di definire il range di attribuzione tramite gli elementi <start> e <stop>.
     <element>
      <resource>img</resource>
      <start sequence_number="001"/>
      <stop sequence_number="004"/>
    </element>
    https://www.iccu.sbn.it/export/sites/iccu/documenti/manuale.html#stru_element_desc

    serve a dichiarare l'ordine degli <element> nel caso di un oggetto digitale logicamente unitario ma fisicamente diviso in più oggetti analogici dello stesso tipo.
    """
    def __init__(self,start,stop,num,piece=None,resource=None):
        self.resource = resource
        # attributo 
        self.num = num
        # come attributi di start a stop
        self.start_sequence_number = start
        self.stop_sequence_number = stop
        self.offset = None
        # elementi
        self.identifier = None
        self.piece = piece
        self.descr = None
        self.file = None
        

    def set_descr(self,value):
        """mantenuto solo per compatibilità con le precedenti versioni MAG, contiene la denominazione di uno <stru>. Il suo uso è deprecato in favore dell'elemento <nomenclature>.

        Parameters
        ----------
        value : str
            [description]
        """
        warnings.warn("Il suo uso è deprecato in favore dell'elemento <nomenclature>.",DeprecationWarning)
        self.descr = value


    def set_sequence_startnstop(self,start,stop):
        """Ogni <element> contiene al suo interno la coppia di elementi <start> e <stop> i cui attributi sequence_number fanno riferimento all'elemento <sequence_number> della sezione <img> ."""
        if start > stop:
            raise ValueError("La sequenza di start non può essere maggiore di quella di stop")
        self.start_sequence_number = start
        self.stop_sequence_number = stop

    def set_resource(self,value):
        """elemento <resource> per indicare che il tipo di contenuti cui si far riferimento è un'immagine statica solo nel primo caso, poich� nel caso di immagini, l'elemento <resource> può anche essere omesso visto che IMG è il valore di default.

        Parameters
        ----------
        value : str
            tipo di risorsa
        """
        lista = ['img','audio','video','ocr','doc']
        url = "https://www.iccu.sbn.it/export/sites/iccu/documenti/manuale.html#stru_element_desc"
        self.resource = valueinlist(value,lista,url)

    def set_identifier(self,value,path=None):
        """dc:identifier di una risorsa non contenuta nel file.

        Parameters
        ----------
        value : str
            tipo di risorsa
        """
        #TODO: controlla che l'identifier sia correto
        self.identifier = value



class stru(object):
    """
    https://www.iccu.sbn.it/export/sites/iccu/documenti/manuale.html#sez_stru
    """
    def __init__(self,sequence_number=None):
        self.structs = []
        self.sequence_number = sequence_number
        self.nomenclature = None
        self.elements = []
        # deprecated attributes
        self.descr = None
        self.start = None
        self.stop = None
        self.nested_sequence_number = 1
        self.element_sequence_number = 1


    def add_stru(self):
        """Metodo per aggiungere un elemento stru.
        """
        newstru = stru(sequence_number=self.nested_sequence_number)
        self.structs.append(newstru)
        self.nested_sequence_number += 1
        return newstru

    def set_nomenclature(self,value):
        """La denominazione del livello strutturale è contenuta dall'elemento <nomenclature>. L'elemento, opzionale e non ripetibile, ha un contenuto di tipo xsd:string, vale a dire che può contenere una qualsiasi sequenza di caratteri. Il formato che tale denominazione può assumere dipende dagli standard di progetto che possono prevedere di riproporre i titoli dei vari livelli strutturali del documento analogico, oppure di adottare denominazioni standardizzate.

        <stru>
            <sequence_number>001</sequence_number>
            <nomenclature>Sonata 1</nomenclature>
            <!-- omissis -->
        </stru>
        Parameters
        ----------
        value : str
            identifica il tipo di struttura es. Capitolo, Sonata
        #https://www.iccu.sbn.it/export/sites/iccu/documenti/manuale.html#sequence_n
        """
        self.nomenclature = value

    def set_descr(self,value):
        msg = "La descrizione come attributo è deprecata."
        warnings.warn(msg,DeprecationWarning)
        self.descr = value
    
    def set_start(self,value):
        msg = "L'uso di start come attributo è deprecato."
        warnings.warn(msg,DeprecationWarning)
        self.start = value

    def set_stop(self,value):
        msg = "L'uso di stop come attributo è deprecato."
        warnings.warn(msg,DeprecationWarning)
        self.stop = value

    def add_element(self,start,stop,resource=None,num=None):
        "Aggiunge un attriubuto elemento all'interno della struttura"
        if start > stop:
            raise ValueError("La sequenza di start non può essere maggiore di quella di stop")
        if num is None:
            num = self.element_sequence_number
        self.elements.append(element(start,stop,resource=resource,num=num))
        self.element_sequence_number +=1

