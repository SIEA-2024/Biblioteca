from odoo import fields, models, api
from dateutil.relativedelta import relativedelta

class Libro(models.Model):
    _name = "biblioteca.libro" 
    _description = "Es una obra impresa, manuscrita o pintada en una serie de hojas de papel, pergamino, vitela u otro material, encuadernadas y protegidas con cubiertas"
    _order="id desc"
    
    ISBN = fields.Char(required=True)
    name = fields.Char(required=True)
    description = fields.Text()
    published_date = fields.Date(copy=False)
    selling_price = fields.Float(required=True, copy=False)
    author = fields.Char(default="Anónimo")

    type = fields.Many2one("biblioteca.tipo", string="Tipo")
    tags = fields.Many2many("biblioteca.tags", string="Tags")
