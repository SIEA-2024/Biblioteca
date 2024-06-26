from odoo import fields
from odoo.models import Model

class Tags(Model):
    _name = "biblioteca.tags" 
    _description = "Tags de los libros"
    _order="secuencia,name"
    
    name = fields.Char(required=True)
    color = fields.Integer()
    secuencia = fields.Integer()

    _sql_constraints = [
        ("unique_nombre", "UNIQUE (name)", "El nombre de la etiqueta debe ser único.")
    ]