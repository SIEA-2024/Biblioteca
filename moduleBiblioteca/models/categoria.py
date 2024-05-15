from odoo import fields
from odoo.models import Model

class Categoria(Model):
    _name = "biblioteca.categoria" 
    _description = "Categoría del libro"
    _order="secuencia,name"
    
    name = fields.Char(required=True)
    secuencia = fields.Integer()

    idEjemplar = fields.One2many("biblioteca.libro", "categoria", string="Ejemplar")

    _sql_constraints = [
        ("unique_nombre", "UNIQUE (name)", "El nombre de la categoría debe ser única.")
    ]