from odoo import fields, api
from dateutil.relativedelta import relativedelta
from odoo.exceptions import UserError, ValidationError
from odoo.models import Model
import logging

_logger = logging.getLogger(__name__)

class Prestamo(Model):
    _name = "biblioteca.prestamo" 
    _description = "Es un servicio que permite a los usuarios utilizar el fondo documental de la Biblioteca fuera del recinto de la misma"
    _order="fechaDevolucion desc"
    
    diasEnPrestamo = fields.Integer(default=14)
    diasExtraReserva = fields.Integer(default=10)

    fechaInicio = fields.Date(default = fields.Date.today())
    fechaDevolucion = fields.Date(readonly=True)

    estado = fields.Selection([("prestado", "Prestado"),
                               ("devuelto", "Devuelto"),
                               ("renovado","Renovado"),
                               ("reservado","Reservado")])

    #Refs
    idEjemplar = fields.Many2one("biblioteca.libro", string="Ejemplar")
    idUsuario = fields.Many2one("res.users", string="Miembros")
    
    #Computed
    fechaFin = fields.Date(compute="_compute_tiempo_prestamo", readonly=True)

    #Constrains
    @api.constrains("estado")
    def _check_estsdo_targeta_prestamo(self):
        for record in self:
            for miembro in record.idUsuario:
                if miembro.tarjeta == False:
                    raise ValidationError("Este miembro no tiene activado el carné de préstamo de la biblioteca.")
            
    @api.constrains("diasExtraReserva")
    def _check_dias_maximo_libro_prestado(self):
        for record in self:
            if record.diasExtraReserva>100:
                raise UserError("Las reservas no pueden superar los 100 días de prestamo.")
            
    
    @api.constrains("idUsuario", "idEjemplar")
    def _check_menor_edad(self):
        for record in self:
            if record.idEjemplar.edadLector >= 18 and record.idUsuario.edad in ["joven"]: 
                    raise UserError("Los libros de adultos no pueden prestarse a niños.")

    # Private methods
    @api.depends("diasEnPrestamo")
    def _compute_tiempo_prestamo(self):
        for record in self:
            base_date = record.fechaInicio if record.fechaInicio else fields.Datetime.now()
            record.fechaFin = base_date + relativedelta(days=record.diasEnPrestamo)

    # Actions
    def actionPrestamo(self):
        for record in self:
            if record.estado == "prestado":
                raise UserError("Un ejemplar prestado no se puede volver a prestar")
            elif record.estado == "devuelto": 
                raise UserError("Un ejemplar devuelto no se puede volver a prestar. Cree otro prestamo")
            elif record.estado == "renovado":
                raise UserError("Un ejemplar renovado no se puede volver a prestar")
            else:
                if record.idEjemplar.numEjemplares > 0:
                    record.estado = "prestado"
                    record.idEjemplar.numEjemplares = record.idEjemplar.numEjemplares-1
                else:
                    record.estado = "reservado"
        return True
    
    def actionDevolucion(self):
        for record in self:
            if record.estado == "devuelto":
                raise UserError("Un ejemplar devuelto no se puede volver a devolver")
            elif record.estado == "reservado":
                raise UserError("Un ejemplar reservado no se puede devolver")
            else:
                record.estado = "devuelto"
                record.fechaDevolucion = fields.Datetime.now()
                record.idEjemplar.numEjemplares = record.idEjemplar.numEjemplares + 1
        return True
    
    def actionRenovacion(self):
        for record in self:
            if record.diasEnPrestamo >100:
                raise UserError("El miembro ha superado el máximo de días que puede renovar.")
            if record.estado == "devuelto":
                raise UserError("Un ejemplar devuelto no se puede renovar")
            else:
                record.estado = "renovado"
                record.diasEnPrestamo = record.diasEnPrestamo+record.diasExtraReserva
        return True
