from odoo import fields, api
from odoo.models import Model
from odoo.exceptions import ValidationError

class Libro(Model):
    _name = "biblioteca.libro" 
    _description = "Es una obra impresa, manuscrita o pintada en una serie de hojas de papel, pergamino, vitela u otro material, encuadernadas y protegidas con cubiertas"
    _order="ISBN desc"
    
    ISBN = fields.Char(required=True)
    name = fields.Char(required=True)
    descripcion = fields.Text()
    numPags = fields.Integer()
    edadLector = fields.Integer()
    fechaPublicacion = fields.Date(copy=False)
    # precio = fields.Float(required=True, copy=False)
    autor = fields.Char(default="Anónimo")
    idioma = fields.Char()
    numEjemplares = fields.Integer(default=1, string="Ejemplares")

    categoria = fields.Many2one("biblioteca.categoria", string="Categoria")
    tags = fields.Many2many("biblioteca.tags", string="Tags")
    prestamo = fields.One2many("biblioteca.prestamo", "idEjemplar", string="Prestamo")

    estado = fields.Selection(related="prestamo.estado", readonly=True)

    _sql_constraints = [
        ("unique_nombre", "UNIQUE (name)", "El nombre del libro debe ser único.")
    ]