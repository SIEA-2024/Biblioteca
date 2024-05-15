from odoo.models import Model
from odoo import fields

class Usuario(Model):
    _inherit = "res.users"
    _description = "Datos de los miembros de la biblioteca que pueden tomar prestados ejemplares"
    _order="name"

    dni = fields.Char(required=True)
    telefono = fields.Char()
    tarjeta = fields.Boolean()
    edad = fields.Selection([("adulto","Adulto"),
                             ("joven","Joven")])
    
    prestamo = fields.One2many("biblioteca.prestamo", "idUsuario")

    _sql_constraints = [
        ("unique_DNI", "UNIQUE (dni)", "El DNI del miembro debe ser único.")
    ]