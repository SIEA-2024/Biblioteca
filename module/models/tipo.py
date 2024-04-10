from odoo import fields, models

class Tipo(models.Model):
    _name = "biblioteca.tipo" 
    _description = "Categoría del libro"
    _order="id desc"
    
    name = fields.Char(required=True)