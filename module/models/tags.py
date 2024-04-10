from odoo import fields, models

class Tags(models.Model):
    _name = "biblioteca.tags" 
    _description = "Tags de los libros"
    _order="id desc"
    
    name = fields.Char(required=True)