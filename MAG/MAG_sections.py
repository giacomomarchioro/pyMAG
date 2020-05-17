from __future__ import print_function


class stprog(object):
    def __init__(self):
        self.tet = None


class img(object):
    def __init__(self):
        self.

class gen(object):
    def __init__(self):
        self.creation = None
        self.last_update = None
        self.stprog = None
        self.collection = None
        self.agency
        self.access_rights = None
        self.completeness = None
        self.img_group = None
        self.audio_group = None
        self.video_group = None

    def set_stprog(self):
        pass

    def set_access_rights(access_rights):
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
        access_rights = str(access_rights)
        conv_dict = {"uso riservato all'interno dell'istituzione": "0",
                     "uso pubblico": "1"}
        if access_rights in [
                            '0',
                            "uso riservato all'interno dell'istituzione",
                            "1",
                            "uso pubblico"]:
            if access_rights in ["uso pubblico",
                                 "uso riservato all'interno dell'istituzione"]:
                access_rights = conv_dict[access_rights]
            self.access_rights = access_rights
            return True

        else:
            raise ValueError(("Access rights deve essere: 0,1, uso riservato"
            "all'interno dell'istituzione. Era invece %s " % access_rights)


    def set_completeness(self,completeness):
        """dichiara la completezza della digitalizzazione. Il suo contenuto deve assumere uno dei seguenti valori:
        0 : digitalizzazione completa
        1 : digitalizzazione incompleta
        L'elemento è obbligatorio, non ripetibile e non sono definiti attributi.
        L'esempio che segue riguarda un oggetto digitale completamente digitalizzato il cui accesso è libero
        """
        access_rights=str(access_rights)
        conv_dict={"digitalizzazione completa": "0",
                     "uso pubblico": "1"}
        if access_rights in [
    '0',
    "digitalizzazione completa",
    "1",
     "digitalizzazione incompleta"]:
            if access_rights in [
    "digitalizzazione completa",
     "digitalizzazione incompleta"]:
                access_rights=conv_dict[access_rights]
            self.access_rights=access_rights
            return True

        else:
            raise ValueError(("Completeness deve essere: 0,1, uso riservato"
            "all'interno dell'istituzione. Era invece %s " % access_rights)

    def check_obligatory(self):
        if self.stprog is None:
            print(" campo stprog è obbligatorio")
        if self.access_rights is None:
            print(" campo access_rights è obbligatorio")
        if self.completeness is None:
            print(" campo completeness è obbligatorio")
