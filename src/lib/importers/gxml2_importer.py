import xml.sax, re, sys, xml.sax.saxutils
import xml_importer
from gourmet.gdebug import *
from gourmet.gglobals import *
import base64

class RecHandler (xml_importer.RecHandler):
    ING_ATTRS =  {
        # XML : DATABASE COLUMN
        "item":"item",
        "unit":"unit",
        "amount":"amount",
        "key":"ingkey",
        }
    def __init__ (self, recData, total=None, prog=None):
        xml_importer.RecHandler.__init__(self,recData,total,prog)
        self.REC_ATTRS = [r[0] for r in REC_ATTRS]
        
    def startElement(self, name, attrs):
        gt.gtk_update()
        self.elbuf = ""        
        if name=='recipe':
            self.start_rec()
        if name=='ingredient':
            self.start_ing(id=self.rec['id'])
            if attrs.get('optional',False):
                if attrs.get('optional',False) not in ['no','No','False','false','None']:
                    self.ing['optional']=True
        if name=='ingref':
            self.start_ing(id=self.rec['id'])
            self.add_ref(unquoteattr(attrs.get('refid')))
            self.add_amt(unquoteattr(attrs.get('amount')))
            
    def endElement (self, name):
        if name=='recipe':
            self.commit_rec()
        elif name=='groupname':
            self.group=xml.sax.saxutils.unescape(self.elbuf)
        elif name=='inggroup':
            self.group=None
        elif name=='ingref':
            self.add_item(xml.sax.saxutils.unescape(self.elbuf))
            self.commit_ing()
        elif name=='ingredient':
            self.commit_ing()
        elif name=='image':
            self.rec['image']=base64.b64decode(self.elbuf)
        elif name in self.REC_ATTRS:
            self.rec[name]=xml.sax.saxutils.unescape(self.elbuf)
        elif name in self.ING_ATTRS.keys():
            self.ing[self.ING_ATTRS[name]]=xml.sax.saxutils.unescape(self.elbuf)


class converter (xml_importer.converter):
    def __init__ (self, filename, rd, threaded=False, progress=None):
        xml_importer.converter.__init__(self,filename,rd,RecHandler,
                                        recMarker="</recipe>",threaded=threaded,
                                        progress=progress)

def unquoteattr (str):
    return xml.sax.saxutils.unescape(str).replace("_"," ")
