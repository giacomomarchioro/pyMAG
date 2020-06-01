import xml.etree.ElementTree as ET
import MAG 
import importlib

importlib.reload(MAG)
self = MAG.MAGFile()
tree = ET.parse('MagExporteample.xml')
root = tree.getroot()

def add_newstruct(elem):
    from MAG.STRU_section import stru
    for se in elem:
        if se.tag.endswith('sequence_number'):
            mystru = stru(se.text)
        if se.tag.endswith('element'):
            for sse in se:
                pass
            #TODO:Element
            #mystru.add_element()
        if se.tag.endswith('stru'):
            mystru.add_stru(add_newstruct(se))

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
    imglengt, imgheight = None, None
    source_xdimension, source_ydimension = None, None

    for se in elem:
        if se.tag.endswith('imagelength'):
            imglengt = se.text
        elif se.tag.endswith('imageheight'):
            imgheight = se.text
        elif se.tag.endswith('source_xdimension'):
            source_xdimension = se.text
        elif se.tag.endswith('source_ydimension'):
            source_ydimension = se.text

    if imglengt is not None and imgheight is not None:
        root.set_imagelengthandwidth(imglengt,imgheight)
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
    if se.tag.endswith('shelfmark'):
        self.gen.holdings.add_shelfmark(se.text)
    elif se.tag.endswith('inventory_number'):
        self.gen.holdings.set_inventory_number(se.text)
    elif se.tag.endswith('library'):
        self.gen.holdings.set_library(se.text)
    else:
        print('Non convertito: %s' %se)


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
        #TODO:Holdings
        
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
    print("\tprint('Non convertito: %s' %se)")


