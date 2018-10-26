from flask_appbuilder.widgets import ListWidget, FormWidget

            
class MyListWidget(ListWidget):
    template = 'widgets/listRev1.html'             

class MyEditWidget(FormWidget):
    template = 'widgets/edit_form_sub.html'

