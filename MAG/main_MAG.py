from __future__ import print_function
import hashlib
import xml.etree.ElementTree as ET
import numpy as np
import GEN_IMG_sections
import BIB_section
import STRU_section
"""

"""
__all__ = ['MAGFile']

class MAGFile(object):
    """An object oriented representation of the MAG application schema."""
    def __init__(self, filepath=None):
        self.gen = GEN_IMG_sections.gen()
        self.structs = [] 
        self.bib = BIB_section.bib()
        self.imgs = []
        # counters
        self.struct_counter = 1
        if filepath is not None:
            self.load(filepath)

 


#### da rimuovere
    def set_VendorSpecificID(self, url):
        '''This is an extension hook for vendor specific data formats derived
        from ISO5436_2_XML. This tag contains a vendor specific ID which is the
        URL of the vendor. It does not need to be valid but it must be
        worldwide unique!Example: http://www.example-inc.com/myformat
        '''
        raise NotImplementedError


    def load(self, filepath):
        tree = ET.parse(zfile.open('main.xml'))
        root = tree.getroot()
        # return tree,root #for debug
        # We first get the records it would not be efficient to iter all the
        # root because sometimes Record3 contains very long profiles

        records = {}
        for child in root:
            records[child.tag] = child

        axes = None
        # We must take care that field with minOccurs = 0 could not be present
        # we use "if" structure to avoid using execption.
        # We also use the setter method for double check the import.
        for item in records['Record1']:
            if item.tag == 'Revision':
                self.record1.revision = item.text
            if item.tag == 'FeatureType':
                self.record1.set_featuretype(item.text)
            if item.tag == 'Axes':
                axes = item
        for ax in axes:
            if ax.tag == 'CX':
                for elem in ax:
                    if elem.tag == 'AxisType':
                        self.record1.axes.CX.set_axistype(elem.text)
                    if elem.tag == 'Increment':
                        self.record1.axes.CX.set_increment(elem.text)
                    if elem.tag == 'Offset':
                        self.record1.axes.CX.set_offset(elem.text)
                    if elem.tag == 'DataType':
                        self.record1.axes.CX.set_datatype(elem.text)

            if ax.tag == 'CY':
                for elem in ax:
                    if elem.tag == 'AxisType':
                        self.record1.axes.CY.set_axistype(elem.text)
                    if elem.tag == 'Increment':
                        self.record1.axes.CY.set_increment(elem.text)
                    if elem.tag == 'Offset':
                        self.record1.axes.CY.set_offset(elem.text)
                    if elem.tag == 'DataType':
                        self.record1.axes.CY.set_datatype(elem.text)

            if ax.tag == 'CZ':
                for elem in ax:
                    if elem.tag == 'AxisType':
                        self.record1.axes.CZ.set_axistype(elem.text)
                    if elem.tag == 'Increment':
                        self.record1.axes.CZ.set_increment(elem.text)
                    if elem.tag == 'Offset':
                        self.record1.axes.CZ.set_offset(elem.text)
                    if elem.tag == 'DataType':
                        self.record1.axes.CZ.set_datatype(elem.text)

            if ax.tag == 'Rotation':
                # we construct the rotation matrix using the set rotation and
                # the indexes taken from the element tag.
                self.infos['Rotation'] = True
                for elem in ax:
                    col, row = elem.tag[1:]
                    self.record1.axes.set_rotation(int(row),
                                                   int(col), elem.text)

        def xml2dict(elem):
            xdict = {}
            for item in elem.iter():
                xdict[item.tag] = item.text
            return xdict

        # Records2 is optional so we check if it's in the records list
        if 'Record2' in records:
            # fileds in record2 are unique we use a dict
            xd = xml2dict(records['Record2'])
            # even though the whole record is not mandatory some value are
            self.record2.set_date(xd['Date'])
            self.record2.probingsystem.set_type(xd['Type'])
            self.record2.probingsystem.set_identification(xd['Identification'])
            self.record2.instrument.set_model(xd['Model'])
            self.record2.instrument.set_serial(xd['Serial'])
            self.record2.instrument.set_manufacturer(xd['Manufacturer'])
            self.record2.instrument.set_version(xd['Version'])
            self.record2.set_calibrationdate(xd['CalibrationDate'])
            if 'Creator' in xd:
                self.record2.set_creator(xd['Creator'])
            if 'Comment' in xd:
                self.record2.set_comment(xd['Comment'])

        else:
            self.record2 = None

        # Records3 is more problematic because it could contain a lot of data
        for elem in records['Record3']:
            if elem.tag == 'MatrixDimension':
                xd = xml2dict(elem)
                self.record3.matrixdimension.set_sizeX(xd['SizeX'])
                self.record3.matrixdimension.set_sizeY(xd['SizeY'])
                self.record3.matrixdimension.set_sizeZ(xd['SizeZ'])

            if elem.tag == 'DataLink':
                self.record3.datalist = False
                # This mean that we have a binary file
                print('Found a binary file')
                mask = np.ma.nomask
                for i in elem:
                    if i.tag == 'PointDataLink':
                        self.record3.datalink.set_PointDataLink(i.text)
                        binfile = zfile.read(i.text)
                    if i.tag == 'MD5ChecksumPointData':
                        self.record3.datalink.set_MD5ChecksumPointData(i.text)
                        # We check the checksum on the way
                        checksum_calc = hashlib.md5(binfile).hexdigest()
                        if checksum_calc.lower() != i.text.lower():
                            print("Checksums bin data are different!")

                    if i.tag == 'ValidPointsLink':
                        self.record3.datalink.set_ValidPointsLink(i.text)
                        validpoints = zfile.read(i.text)

                    if i.tag == 'MD5ChecksumValidPoints':
                        self.record3.datalink.set_MD5ChecksumValidPoints(i.text)
                        # We check the checksum on the way
                        checksum_calc = hashlib.md5(validpoints).hexdigest()
                        if checksum_calc.lower() != i.text.lower():
                            print("Checksums valid bin data are different!")

                    if self.record3.matrixdimension.sizeZ == 1:
                        size = (self.record3.matrixdimension.sizeX,
                                self.record3.matrixdimension.sizeY)
                        dtypes = self.record1.axes.get_axes_dataype()
                        if len(dtypes) == 1:
                            dtype = self.convert_datatype(dtypes.pop())
                            data = np.frombuffer(binfile, dtype=dtype)
                            self.data = np.ma.masked_array(data,
                                                           mask=mask,
                                                           dtype=dtype
                                                           ).reshape(size)

                    elif self.record3.matrixdimension.sizeZ > 1:
                        size = (self.record3.matrixdimension.sizeX,
                                self.record3.matrixdimension.sizeY,
                                self.record3.matrixdimension.sizeZ)
                        dtypes = self.record1.axes.get_axes_dataype()
                        if len(dtypes) == 1:
                            dtype = self.convert_datatype(dtypes.pop())
                            data = np.frombuffer(binfile, dtype=dtype)
                            self.data = np.ma.masked_array(data,
                                                           mask=mask,
                                                           dtype=dtype
                                                           ).reshape(size)

            #np.ma.masked_array([(1,2,3),(3,4,5),(5,6,7)],dtype = [('x', 'i8'), ('y',   'f4'),('z','i8')])

            if elem.tag == 'DataList':
                print('Found a datalist')
                self.record3.datalink = False
                datalist = []
                # it could be reasonable to espect sizeZ to be the number of
                # profiles
                n_profiles = self.record3.matrixdimension.sizeZ
                for value in elem:
                    if value.text is None:  # it means its an invalid entry
                    # actualy xsd:float has also a NaN value that could be used
                        nanarr = [np.nan]*n_profiles
                        datalist.append(nanarr)
                    else:
                        values = value.text.split(';')
                        datalist.append(values)
                        if len(values) > n_profiles:
                            n_profiles = len(values)


                dtypes = self.record1.axes.get_axes_dataype()
                if len(dtypes) == 1:
                    dtype = self.convert_datatype(dtypes.pop())
                    data = np.array(datalist, dtype=dtype)
                    self.data = data.T
            # Record4 contains only one element
            self.record4.checksumfile = records['Record4'][0].text

    def write(self, filepath):
        # XML file creation: > check if the element present (if not mandatory)
        #                    > recreate the datastructure from the numpy arrays
        p = ET.Element('p:ISO5436_2')
        p.set("xmlns:p", "http://www.opengps.eu/2008/ISO5436_2")
        p.set("xmlns:xsi", "http://www.w3.org/2001/XMLSchema-instance")
        p.set("xsi:schemaLocation",
              "http://www.opengps.eu/2008/ISO5436_2 http://www.opengps.eu/2008/ISO5436_2/ISO5436_2.xsd")
        Record1 = ET.SubElement(p, 'Record1')
        Revision = ET.SubElement(Record1, 'Revision')
        Revision.text = self.record1.revision
        FeatureType = ET.SubElement(Record1, 'FeatureType')
        FeatureType.text = self.record1.featuretype