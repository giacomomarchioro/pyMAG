import requests
from datetime import datetime
import warnings



def check_datetime(datetime_str):
    try:
        datetime.strptime(datetime_str, '%Y-%m-%dT%H:%M:%S')
    except ValueError:
        warnings.warn('La data non è nel formato corretto! (es. 2020-6-14T18:30:29)')
    return datetime_str


def check_url(url):
    try:
        request = requests.get(url)
        if request.status_code != 200:
            print(request.status_code)
            warnings.warn('Esiste il server ma non la pagina')
    except ConnectionError:
        print("Errore di connessione indirizzo non valido!")

    return url


def check_agency(codice):
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

    return codice


def checkgroupID(func):
    def function_wrapper(self,ID,raiseerror):
        """
        ID : l'attributo è di tipo xsd:ID, vale a dire che contiene un identificatore 
        univoco che consentirà poi di richiamare l'intera sezione. Tale identificatore 
        dovrà necessariamente cominciare con una lettera (non un numero), 
        non dovrà contenere al suo interno spazi o segni di punteggiatura diversi 
        dal punto, il trattino e il trattino basso.
        """
        link = "https://www.iccu.sbn.it/export/sites/iccu/documenti/manuale.html#img_group"
        if ID[0].isdigit():
            warnings.warn("L'ID non può cominciare con un numero. Invece comincia con %s.\n%s" %(ID[0],link))
        for indx, carat in enumerate(ID):
            if carat in r"""!"#$%&'()*+, /:;<=>?@[\]^`{|}~ """:
                if carat == " ":
                    carat = "uno spazio"
                arrow = " "*(indx) + "^"
                msg = "L'attributo ID non può contenere segni di punteggiatura \
diversi dal punto, il trattino e il trattino basso. Ho trovato %s: \n%s\n%s\n%s" %(carat,ID,arrow,link)
                warnings.warn(msg)
        func(self,ID)
        return ID
    return function_wrapper


def validvalue(value,valuedict,url):
    value = str(value)
    if value in valuedict or value in valuedict.values():
        if value in valuedict:
            value = valuedict[value]
    else:
        fields = list(valuedict) + list(set(valuedict.values()))
        warnings.warn(("Il valore può essere: %s. \n Maggiori informazioni:%s \n"
                        "Era invece: %s " %(", ".join(fields),url,value)))
    return value

def valueinlist(value,lista,url):
    if value not in lista:
        warnings.warn(("Il valore può essere: %s. \n Maggiori informazioni:%s \n"
                        "Era invece: %s " %(", ".join(lista),url,value)))
    return value



def checkpositiveinteger(value,url):
    try:
        int(value)
    except ValueError:
        warnings.warn(("Il valore può essere deve essere un intero positivo.\nMaggiori informazioni:%s \n"
                        "Era invece: %s " %(url,value)))
    if int(value) < 11:
        print("Atteznione valore anomalo: %s" %value)
    return str(value)
