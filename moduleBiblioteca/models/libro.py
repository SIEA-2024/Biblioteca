from odoo import fields, api
from odoo.models import Model
from odoo.exceptions import ValidationError, UserError

class Libro(Model):
    _name = "biblioteca.libro" 
    _description = "Es una obra impresa, manuscrita o pintada en una serie de hojas de papel, pergamino, vitela u otro material, encuadernadas y protegidas con cubiertas"
    _order="saga"
    
    isbn = fields.Char(required=True)
    name = fields.Char(required=True)
    descripcion = fields.Text()
    numPags = fields.Integer()
    edadLector = fields.Integer(required=True)
    fechaPublicacion = fields.Date(copy=False)
    autor = fields.Char(default="Anónimo")
    numEjemplares = fields.Integer(default=1, copy=False)
    saga = fields.Char(default="Ninguna")
    editorial = fields.Char()
    fechaAdquisicion = fields.Date()

    categoria = fields.Many2one("biblioteca.categoria", string="Categoria")
    tags = fields.Many2many("biblioteca.tags", string="Tags")
    prestamo = fields.One2many("biblioteca.prestamo", "idEjemplar", string="Prestamo")
    idioma = fields.Many2many("biblioteca.idioma", string="Idioma")
    
    estado = fields.Selection(related="prestamo.estado", readonly=True)
    state = fields.Selection(related="prestamo.estado", readonly=True, store=True)

    _sql_constraints = [
        ("unique_isbn", "UNIQUE (isbn)", "El isbn del libro debe ser único.")
    ]

        
    @api.ondelete(at_uninstall=False)
    def _unlink_si_estado_no_devuelto(self):
        for record in self:
            if not record.estado in ["devuelto"]:
                raise UserError("Solo los ejemplares devueltos se pueden eliminar.")
