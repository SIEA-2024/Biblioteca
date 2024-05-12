from odoo import fields
from odoo.models import Model

class Tags(Model):
    _name = "biblioteca.tags" 
    _description = "Tags de los libros"
    _order="name"
    
    name = fields.Char(required=True)

    _sql_constraints = [
        ("unique_nombre", "UNIQUE (name)", "El nombre de la etiqueta debe ser único.")
    ]