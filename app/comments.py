from flask_appbuilder import ModelView
from flask_appbuilder.models.sqla.interface import SQLAInterface
from .models import (DocRequests, Unit, Application, Doctype, Subdoctype, Domain, Job, Discipline,
                     Partner, Matrix, Document, Cdrlitem, Documentclass,
                     Vendor, Mr, Comments)
from flask_appbuilder.widgets import ListThumbnail, ListBlock

class CommentsView(ModelView):
    datamodel = SQLAInterface(Comments)
    order_columns = ['changed_on', 'created_on']
    list_columns = ['comment', 'changed_by', 'modified']
    #add_columns = ['comment'] 
    #add_exclude_columns = ['unit','created_on','changed_on']
    #show_columns = ['doc', 'comment', 'changed_by', 'modified']
    edit_columns = ['comment','included','closed'] 
    list_widget = ListBlock
     

    add_fieldsets = [
                        (
                            'Text',
                            {'fields': ['comment']}
                        ),
                        (
                            'Related To',
                            {'fields': [
                                        'job',
                                        'unit',
                                        'doc',
                                        'discipline',
                                        'application',
                                        'doctype',
                                        'subdoctype',
                                        'domain',
                                        'cdrlitem',
                                        'documentclass',
                                        'partner', 
                                        ],
                                        'expanded':False}
                        ),
                     ]
    show_fieldsets = [
                        (
                            'Text',
                            {'fields': ['comment']}
                        ),
                        (
                            'Related To',
                            {'fields': [
                                        'job',
                                        'unit',
                                        'doc',
                                        'discipline',
                                        'application',
                                        'doctype',
                                        'subdoctype',
                                        'domain',
                                        'cdrlitem',
                                        'documentclass',
                                        'partner', 
                                        ],
                                        'expanded':True}
                        ),
                     ]
