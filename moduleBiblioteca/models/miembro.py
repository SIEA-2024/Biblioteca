from odoo import fields, api
from odoo.models import Model

class Miembro(Model):
    _name = "biblioteca.miembro" 
    _description = "Datos de los miembros de la biblioteca que pueden tomar prestados ejemplares"
    _order="name"
    
    DNI = fields.Char(required=True)
    name = fields.Char(required=True)
    email = fields.Char()
    telefono = fields.Integer()
    targeta = fields.Boolean()
    
    prestamo = fields.One2many("biblioteca.prestamo", "idMiembro", string="Prestamo")
    
    _sql_constraints = [
        ("unique_DNI", "UNIQUE (DNI)", "El DNI del miembro debe ser único.")
    ]