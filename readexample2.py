import xml.etree.ElementTree as ET
import MAG 
import importlib
from collections import defaultdict

importlib.reload(MAG)
self = MAG.MAGFile()
tree = ET.parse('MagExporteample.xml')
root = tree.getroot()
root

xmls = "{http://www.iccu.sbn.it/metaAG1.pdf}"

def xml2dict(elem):
    xdict = defaultdict(list)
    for item in elem.iter():
        xdict[item.tag.replace(xmls,'')].append(item.text)
    return xdict


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
            else:
                print("Non convertito: %s" %se)


    else:
        print("Non convertito%s" %elem)




def printclas(myobj,root):
    fields = dir(myobj)
    for i in fields:
        if i.startswith('set'):
            print("self.%s.%s(elem.attrib['%s'])" %(root,i,i.split('set_')[-1]))

def printclas2(myobj,root):
    fields = dir(myobj)
    for i in fields:
        if i.startswith('set'):
            print("self.%s.%s(dicte['%s'])" %(root,i,i.split('set_')[-1]))

def printclas3(myobj,root):
    fields = dir(myobj)
    for i in fields:
        if i.startswith('set'):
            print("elif se.tag.endswith('%s'):" %(i.split('set_')[-1]))
            print("\tself.%s.set_%s(se.text)" %(root,i.split('set_')[-1]))

def printclas4(myobj,root):
    fields = dir(myobj)
    for i in fields:
        if i.startswith('set'):
            print("elif se.tag.endswith('%s'):" %(i.split('set_')[-1]))
            print("\t%s.set_%s(se.text)" %(root,i.split('set_')[-1]))
        if i.startswith('add'):
            print("elif se.tag.endswith('%s'):" %(i.split('add_')[-1]))
            print("\t%s.add_%s(se.text)" %(root,i.split('add_')[-1]))
    print("else:")
    print("\tprint(Non convertito: %s)" %i)

def printclas4(myobj,root):
    fields = dir(myobj)
    for i in fields:
        if i.startswith('add'):
            print("elif se.tag.endswith('%s'):" %(i.split('add_')[-1]))
            print("\t%s.add_%s(se.text)" %(root,i.split('add_')[-1]))
    print("else:")
    print("\tprint('Non convertito: %s'%se)" )
