import requests
from datetime import datetime
import warnings
import re

returnwarning = False


class obbligatorio(object):
    """ Oggetto usato per definire campi obligatorio.
    """
    def __str__(self):
      return "Campo obbligatorio non presente!"

def check_notnanorempty(value,url=None,minlen=0):  
    if value in ['',None]:
        msg = ('Il valore deve essere non nullo e non vuoto'
            ' Era invece %s\n%s' %(value,url))
        warnings.warn(msg,stacklevel=2)
        msg = "<-!!ERRORE:" + msg
        value = None
        if returnwarning:
            value = "None <-!!ERRORE:" + msg
        return value
    value = str(value)
    msg = ""
    if len(value)<minlen:
       msg = "Il valore %s sembra avere una lunghezza anomala."%value
       print(msg)
       value = "None <-!!ERRORE:" + msg
    if returnwarning:
        value +=msg
    return value

def check_md5(value):
    msg = ""
    if value is not None:
        if len(re.findall(r"([a-fA-F\d]{32})", value)) != 1:
            msg = "Non sembra un md5 valido."
            warnings.warn(msg,stacklevel=2)
            msg = "<-!!ERRORE:" + msg
    if returnwarning:
        value = str(value)+msg
    return value 
    


def check_datetime(datetime_str,url=None):
    datetime_str = check_notnanorempty(datetime_str)
    msg =''
    if datetime_str is not None:
        try:
            datetime.strptime(datetime_str, '%Y-%m-%dT%H:%M:%S')
        except ValueError:
            msg = ('La data non è nel formato corretto!'
            ' dovrebbe essere per es. 2020-6-14T18:30:29\n'
            ' %s' %(url))
            warnings.warn(msg+"\n Era invece %s"%datetime_str,stacklevel=3)
            msg = "<-!!ERRORE:" + msg
    if returnwarning:
        datetime_str = datetime_str + msg
    return datetime_str


def check_url(url):
    msg = ""
    try:
        request = requests.get(url)
        if request.status_code != 200:
            print(request.status_code)
            msg = 'Esiste il server ma non la pagina'
            warnings.warn(msg,stacklevel=3)
            msg = "<-!!ERRORE:" + msg
    except ConnectionError:
        print("Errore di connessione indirizzo non valido!")
    except requests.exceptions.MissingSchema:
        print("Schema non valido.")
    if returnwarning:
        url+=msg
    return url


def check_agency(codice):
    """
    
    """
    # nell'anagrafe ICCU il codice e separato da - mentre nel MAG da :
    codice = codice.replace(':','-')
    url = "https://anagrafe.iccu.sbn.it/it/ricerca/dettaglio.html?monocampo=" + codice
    try:
        request = requests.get(url)
        if request.status_code != 200:
            print(request.status_code)
            print(""" Errore nella riceca con l'anagrafe""")
        else:
            mes = "La biblioteca con codice %s non esiste." %codice
            if mes in str(request.content):
                print("Il codice %s non esiste nell'anagrafe ICCU" %codice)
    except ConnectionError:
        print("L'anagrafe ICCU sembra non sia più disponibile.")
    codice = codice.replace('-',':')
    return codice


def checkgroupID(func):
    def function_wrapper(self,ID):
        """
        ID : l'attributo è di tipo xsd:ID, vale a dire che contiene un identificatore 
        univoco che consentirà poi di richiamare l'intera sezione. Tale identificatore 
        dovrà necessariamente cominciare con una lettera (non un numero), 
        non dovrà contenere al suo interno spazi o segni di punteggiatura diversi 
        dal punto, il trattino e il trattino basso.
        """
        link = "https://www.iccu.sbn.it/export/sites/iccu/documenti/manuale.html#img_group"
        if ID[0].isdigit():
            warnings.warn("L'ID non può cominciare con un numero. Invece comincia con %s.\n%s" %(ID[0],link),stacklevel=3)
        for indx, carat in enumerate(ID):
            if carat in r"""!"#$%&'()*+, /:;<=>?@[\]^`{|}~ """:
                if carat == " ":
                    carat = "uno spazio"
                arrow = " "*(indx) + "^"
                msg = "L'attributo ID non può contenere segni di punteggiatura \
diversi dal punto, il trattino e il trattino basso. Ho trovato %s: \n%s\n%s\n%s" %(carat,ID,arrow,link)
                warnings.warn(msg,stacklevel=3)
        func(self,ID)
        return ID
    return function_wrapper


def validvalue(value,valuedict,url):
    value = str(value)
    msg=""
    if value in valuedict or value in valuedict.values():
        if value in valuedict:
            value = valuedict[value]
    else:
        fields = list(valuedict) + list(set(valuedict.values()))
        msg = ("Il valore può essere: %s. \n Maggiori informazioni:%s \n"
                        "Era invece: %s " %(", ".join(fields),url,value))
        warnings.warn(msg,stacklevel=4)
        msg+="<-!!ERRORE:"
    if returnwarning:
        value+=msg
    return value

def valueinlist(value,lista,url):
    msg = ""
    if value not in lista:
        msg = ("Il valore può essere: %s. \n Maggiori informazioni:%s \n"
                        "Era invece: %s " %(", ".join(lista),url,value))
        warnings.warn(msg,stacklevel=4)
        msg+="<-!!ERRORE:"
    if returnwarning:
        if value is None:
            value = "None "
        value+=msg
    return value



def checkpositiveinteger(value,url):
    try:
        int(value)
    except ValueError:
        msg = ("Il valore può essere deve essere un intero positivo.\nMaggiori informazioni:%s \n"
                        "Era invece: %s " %(url,value))
        warnings.warn(msg,stacklevel=3)
    if int(value) < 11:
        print("Atteznione valore anomalo: %s" %value)
    return str(value)

def URIescaping(uri):
    """ Codifica i caratteri nell'URI con gli escape necessari.
    In un URI (Uniform Resource Identifier) alcuni caratteri hanno infatti un significato particolare e quindi per usarli al di fuori del loro significato è necessario impiegare una codifica particolare. Nel dettaglio, per forzare il sistema ad accettare un carattere dotato di un particolare significato senza tale significato è necessario introdurre un escape, vale a dire il simbolo di percento % seguito dalla codifica esadecimale (composta di due cifre) del carattere stesso. Per esempio lo spazio ha il significato speciale di "fine di un URI", se vogliamo invece che non venga considerato in questo modo, dovremo sostituirlo con %20. Un altro carattere che ha un significato particolare è il segno di slash "/" che significa "gerarchicamente inferiore" e che può essere forzato grazie alla codifica %2F.

    I seguenti caratteri sono riservati e devono essere codificati con un escape:

    /	%2F
    ?	%3F
    #	%23
    [ e ]	%5B e %5D
    ;	%3B
    :	%3A
    @	%40
    &	%26
    =	%3D
    +	%2B
    $	%24
    ,	%2C
    <	%3C
    >	%3E
    %	%25
    "	%22
    { e }	%7B e %7D
    |	%7C
    \	%5C
    ^	%5E
    `	%60
    (spazio)	%20
    Sono invece utilizzabili i seguenti caratteri:
    numeri
    lettere maiuscole e minuscole
    segni di punteggiatura quali (separati da |) - | _ | . | ! | ~ | * | ' | ( | )

    Parameters
    ----------
    uri : [type]
        [description]
    """
    caracter_tohex = {"/":"%2F","?":"%3F","#":"%23","[":"%5B","]":"%5D",
    ";":"%3B",":":"%3A","@":"%40","&":"%26","=":"%3D","+":"%2B","$":"%24",
    ",":"%2C","<":"%3C",">":"%3E","%":"%25","\"":"%22","{":"%7B","}":"%7D",
    "|":"%7C","\\":"%5C","^":"%5E","`":"%60"," ":"%20"}

    for chraracter in caracter_tohex.keys():
        uri = uri.replace(chraracter,caracter_tohex[chraracter])
    return uri


def checkSICI():
    raise NotImplementedError

def createSICI():
    raise NotImplementedError