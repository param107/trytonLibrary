from trytond.model import ModelView, ModelSQL, fields

#list of all classes in the file
__all__ = ['Library']


class Library(ModelSQL, ModelView):
    #description
    'Library'
    #Internal class name. Always used as a reference inside Tryton
    #default: <module name> + . + <class name> on Tryton
    #and on database <modules name> + _ + <class name>
    __name__ = 'library.library'
    title = fields.Char('Title', required=True)
    isbn = fields.Char('ISBN')
    subject = fields.Char('Subject')
    abstract = fields.Text('Abstract')
