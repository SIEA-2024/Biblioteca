from odoo import fields
from odoo.models import Model

class Idioma(Model):
    _name = "biblioteca.idioma" 
    _description = "Idioma del libro"
    _order="secuencia,name"
    
    name = fields.Char(required=True)
    color = fields.Integer()
    secuencia = fields.Integer()

    _sql_constraints = [
        ("unique_nombre", "UNIQUE (name)", "El idioma de la categoría debe ser única.")
    ]