from flask_appbuilder import Model
from flask_appbuilder.models.mixins import AuditMixin
from sqlalchemy import Column, Integer, String, ForeignKey 
from sqlalchemy.orm import relationship
from time import gmtime, strftime
from flask import Markup
from .momentjs import momentjs
from flask_babel import lazy_gettext as _
#from .helpers import gen_excel_byreq


"""

You can use the extra Flask-AppBuilder fields and Mixin's

AuditMixin will add automatic timestamp of created and modified by who


"""
def mydefault():
    print('by mydefaul function')
    return 'func'


class Job(Model):
    __tablename__ = "job"
    id = Column(Integer, primary_key=True)
    job = Column(String(5), unique=True, nullable=False)
    name = Column(String(100))
    description = Column(String(100))

    def __repr__(self):
        return self.job + " | " + self.name
    


class Discipline(Model):
    __tablename__ = "discipline"
    id = Column(Integer, primary_key=True)
    discipline = Column(String(1), unique=True, nullable=False)
    name = Column(String(100))
    description = Column(String(100))

    def __repr__(self):
        return self.discipline + " | " + self.name



class Unit(Model):
    __tablename__ = "unit"
    id = Column(Integer, primary_key=True)
    unit = Column(String(3), unique=True, nullable=False)
    name = Column(String(100))
    start = Column(Integer, default=0)
    stop = Column(Integer)
    unit_type = Column(String(20), default='standard') 
    description = Column(String(100))

    def __repr__(self):
        return self.unit + " | " + self.name

class Application(Model):
    __tablename__ = "application"
    id = Column(Integer, primary_key=True)
    application = Column(String(2), unique=True, nullable=False)
    name = Column(String(100))
    description = Column(String(100))

    def __repr__(self):
        return self.application + " | " + self.name
    
class Doctype(Model):
    __tablename__ = "doctype"
    id = Column(Integer, primary_key=True)
    doctype = Column(String(1), unique=True, nullable=False)
    name = Column(String(100))
    description = Column(String(100))
    
    def __repr__(self):
        return self.doctype + " | " + self.name

class Subdoctype(Model):
    __tablename__ = "subdoctype"
    id = Column(Integer, primary_key=True)
    doctype_id = Column(Integer, ForeignKey('doctype.id'), nullable=False)
    doctype = relationship('Doctype')
    subdoctype = Column(String(1), unique=True, nullable=False)
    name = Column(String(100))
    description = Column(String(100))

    
    def __repr__(self):
        return self.subdoctype + " | " + self.name + " | " + self.description

class Domain(Model):
    __tablename__ = "domain"
    id = Column(Integer, primary_key=True)
    domain = Column(String(1), unique=True, nullable=False)
    name = Column(String(100))
    description = Column(String(100))
    
    def __repr__(self):
        return self.domain + " | " + self.name


class Partner(Model):
    __tablename__ = "partner"
    id = Column(Integer, primary_key=True)
    partner = Column(String(50), unique=True, nullable=False)
    name = Column(String(100))
    description = Column(String(100))
    common_start = Column(Integer, default=0)
    common_stop = Column(Integer, default=0)
    
    def __repr__(self):
        return self.partner + " | " + self.name


class Documentclass(Model):
    __tablename__ = "documentclass"
    id = Column(Integer, primary_key=True)
    documentclass = Column(String(1), unique=True, nullable=False)
    name = Column(String(100))
    description = Column(String(100))

    def __repr__(self):
        return self.documentclass + " | " + self.name


class Cdrlitem(Model):
    __tablename__ = "cdrlitem"
    id = Column(Integer, primary_key=True)
    cdrlitem = Column(String(35), unique=True, nullable=False)
    name = Column(String(100))
    description = Column(String(100))

    def __repr__(self):
        return self.cdrlitem + " | " + self.name


class Vendor(Model):
    __tablename__ = "vendor"
    id = Column(Integer, primary_key=True)
    vendor = Column(String(50), unique=True, nullable=False)
    name = Column(String(100))
    description = Column(String(100))

    def __repr__(self):
        return self.vendor + " | " + self.name


class Mr(Model):
    __tablename__ = "mr"
    id = Column(Integer, primary_key=True)
    mr = Column(String(50), unique=True, nullable=False)
    name = Column(String(100))
    description = Column(String(100))

    def __repr__(self):
        return self.mr + " | " + self.name


class Matrix(Model):
    __tablename__ = "matrix"
    id = Column(Integer, primary_key=True)
    matrix = Column(String(50))
    counter = Column(Integer, default=1)
    #document_id = Column(Integer, ForeignKey("document.id"))
    #document = relationship('Document')
    
    def __repr__(self):
        return self.matrix


class DocRequests(AuditMixin, Model):
    __tablename__ = "docrequests"
    id = Column(Integer, primary_key=True)
    unit_id = Column(Integer, ForeignKey('unit.id'), nullable=False)
    unit = relationship('Unit')
    application_id = Column(Integer, ForeignKey('application.id'), nullable=False)
    application = relationship('Application')
    job_id = Column(Integer, ForeignKey('job.id'), nullable=False)
    job = relationship('Job')
    subdoctype_id = Column(Integer, ForeignKey('subdoctype.id'), nullable=False)
    subdoctype = relationship('Subdoctype')
    domain_id = Column(Integer, ForeignKey('domain.id'), nullable=False)
    domain = relationship('Domain')
    discipline_id = Column(Integer, ForeignKey('discipline.id'), nullable=False)
    discipline = relationship('Discipline')
    doctype_id = Column(Integer, ForeignKey('doctype.id'), nullable=False)
    doctype = relationship('Doctype')
    sheet = Column(String(3), default='001')
    partner_id = Column(Integer, ForeignKey('partner.id'), nullable=False)
    partner = relationship('Partner')
    cdrlitem_id = Column(Integer, ForeignKey('cdrlitem.id'))
    cdrlitem = relationship('Cdrlitem')
    documentclass_id = Column(Integer, ForeignKey('documentclass.id'))
    documentclass = relationship('Documentclass')
    vendor_id = Column(Integer, ForeignKey('vendor.id'))
    vendor = relationship('Vendor')
    mr_id = Column(Integer, ForeignKey('mr.id'))
    mr = relationship('Mr')
    matrix_id = Column(Integer, ForeignKey('matrix.id'))
    matrix = relationship('Matrix')
    quantity = Column(Integer, default=1)
    request_type = Column(String(20))
    

    def __repr__(self):
        doc_param = "-".join([str(x) for x in [self.job,
                                                self.discipline, 
                                                self.unit, 
                                                self.application, 
                                                str(self.doctype) + str(self.subdoctype), 
                                                self.domain
                                                ]])

        return '[ '+ str(self.quantity) +' ] '+ doc_param + ' by ' + str(self.created_by) + ' on ' + Markup(self.created_on) 
    
    # def __init__(self):
    def csv(self):
        #filename = gen_excel_byreq(self)
        #return Markup('<a href="/static/csv/' + filename +'" download>'+'<img border="0" src="/static/img/excel.png" alt="W3Schools" width="24" height="24">'+'</a>')
        return 'nothing'
        
    def created(self):
        #date = self.created_on
        #return date.strftime('We are the %d, %b %Y')
        #return Markup(_(momentjs(self.created_on).calendar() + ' | ' + momentjs(self.created_on).fromNow()))
        return Markup(momentjs(self.created_on).format('D MMM Y | LT'))
        #return self.created_on.strftime('%d, %b %Y - %H:%M:%S')
    
    def pretty_month_year(self):
        return self.created_on.strftime('%d, %b %Y')

    def user_create(self):
        return str(self.created_by)

    def modified(self):
        date = self.created_on
        #return date.strftime('We are the %d, %b %Y')
        return self.changed_on.strftime('%d, %b %Y - %H:%M:%S')

    def req_type(self):

        if self.request_type == 'vendor':  
            return Markup('<img border="0" src="/static/img/vendor.png" alt="W3Schools" width="24" height="24"> ') 
            
        elif self.request_type == 'engineering':
            return Markup('<img border="0" src="/static/img/engineering.png" alt="W3Schools" width="24" height="24"> ')
    
        else:
            return '#ND'    
        
    
    def req_description(self):
        req_code = str(self.unit) + ' '+ str(self.application) + ' '+  str(self.doctype)
        req_quantity = str(self.quantity)
        desc_eng = req_code
        desc_vend = req_code  + ' | <span style="color:#4b1f68">'+ str(self.vendor)+'</span> -> '+ str(self.mr)+' |'
        
        if self.request_type == 'vendor':
            return Markup(desc_vend)
            #return 'description1'
        return Markup(desc_eng)

    def doctype_c(self):
        return str(self.doctype)
    
    def unit_c(self):
        return str(self.unit)
    
    def application_c(self):
        return str(self.application)
    
    def job_c(self):
        return str(self.job)
    
    def subdoctype_c(self):
        return str(self.subdoctype)
    
    def discipline_c(self):
        return str(self.discipline)
    
    def domain_c(self):
        return str(self.domain)
    
    def cdrlitem_c(self):
        return str(self.cdrlitem)
    
    def documentclass_c(self):
        return str(self.documentclass)
    
    def vendor_c(self):
        return str(self.vendor)
    
    def mr_c(self):
        return str(self.mr)
    
    def matrix_c(self):
        return str(self.matrix)

    def partner_c(self):
        return str(self.partner)
    
    

class Document(AuditMixin, Model):
    __tablename__ = "document"
    id = Column(Integer, primary_key=True)
    code = Column(String(35))
    oldcode = Column(String(35), default='empty')
    docrequests_id = Column(Integer, ForeignKey('docrequests.id'))
    docrequests = relationship(DocRequests)
    #comments = Column(String(150))
    notes = Column(String(150))
    status = Column(String(30))

    unit_id = Column(Integer, ForeignKey('unit.id'), nullable=False)
    unit = relationship('Unit')
    application_id = Column(Integer, ForeignKey('application.id'), nullable=False)
    application = relationship('Application')
    job_id = Column(Integer, ForeignKey('job.id'), nullable=False)
    job = relationship('Job')
    subdoctype_id = Column(Integer, ForeignKey('subdoctype.id'), nullable=False)
    subdoctype = relationship('Subdoctype')
    domain_id = Column(Integer, ForeignKey('domain.id'), nullable=False)
    domain = relationship('Domain')
    discipline_id = Column(Integer, ForeignKey('discipline.id'), nullable=False)
    discipline = relationship('Discipline')
    doctype_id = Column(Integer, ForeignKey('doctype.id'), nullable=False)
    doctype = relationship('Doctype')
    sheet = Column(String(3), default='001')
    partner_id = Column(Integer, ForeignKey('partner.id'), nullable=False)
    partner = relationship('Partner')
    cdrlitem_id = Column(Integer, ForeignKey('cdrlitem.id'))
    cdrlitem = relationship('Cdrlitem')
    documentclass_id = Column(Integer, ForeignKey('documentclass.id'))
    documentclass = relationship('Documentclass')
    vendor_id = Column(Integer, ForeignKey('vendor.id'))
    vendor = relationship('Vendor')
    mr_id = Column(Integer, ForeignKey('mr.id'))
    mr = relationship('Mr')
    matrix_id = Column(Integer, ForeignKey('matrix.id'))
    matrix = relationship('Matrix')



    def __repr__(self):
        return self.code

    def oldcode_p(self):
        if self.oldcode == 'empty' or self.oldcode == 'void':
            return ''
        return self.oldcode

    def status(self):
        if self.oldcode == 'empty':
            return Markup('<img border="0" src="/static/img/pending.png" alt="W3Schools" width="16" height="16">'+' Pending')
        elif self.oldcode == 'void':
            return Markup('<img border="0" src="/static/img/destroyed.png" alt="W3Schools" width="16" height="16">'+' Destroyed')
        else:
            return Markup('<img border="0" src="/static/img/reserved.png" alt="W3Schools" width="16" height="16">'+' Reserved')

    def code_type(self):
        return self.docrequests.req_type()

    def created(self):
        date = self.created_on
        #return date.strftime('We are the %d, %b %Y')
        
        #return Markup(_(momentjs(self.created_on).calendar() + ' | ' + momentjs(self.created_on).fromNow()))
        #return self.created_on.strftime('%d, %b %Y - %H:%M:%S')
        return Markup(momentjs(self.created_on).format('D MMM Y | LT'))
    
    def modified(self):
        #date = self.created_on
        #return date.strftime('We are the %d, %b %Y')
        return self.changed_on.strftime('%d, %b %Y - %H:%M:%S')
    
    def bapco_code(self):
        if self.oldcode == 'empty':
            return Markup('<span style="color:#f89406">[ '+'<span style="color:#4b1f68">'+ self.code + '<span style="color:#f89406"> ]')
        
        elif self.oldcode == 'void':
            return Markup('<span style="color:#ee5f5b">[ '+'<span style="color:#4b1f68">'+ self.code + '<span style="color:#ee5f5b"> ]')

        else:
            return Markup('<span style="color:#5bc0de">[ '+'<span style="color:#4b1f68">'+ self.code + '<span style="color:#5bc0de"> ]') 

    def cdrl_item(self):
        if self.docrequests.cdrlitem:
            return self.docrequests.cdrlitem
        return ''
    



class Comments(AuditMixin,Model):
    __tablename__ = "comments"
    id = Column(Integer, primary_key=True)
    doc_id = Column(Integer, ForeignKey('document.id'), nullable=False)
    doc = relationship(Document)
    comment = Column(String(250))
    closed = Column(String(3), default='no')

    def created(self):
        date = self.created_on
        #return date.strftime('We are the %d, %b %Y')
        
        #return Markup(_(momentjs(self.created_on).calendar() + ' | ' + momentjs(self.created_on).fromNow()))
        #return self.created_on.strftime('%d, %b %Y - %H:%M:%S')
        return Markup(momentjs(self.created_on).format('D MMM Y | LT'))
    
    def modified(self):
        #date = self.created_on
        #return date.strftime('We are the %d, %b %Y')
        return self.changed_on.strftime('%d, %b %Y - %H:%M:%S')
