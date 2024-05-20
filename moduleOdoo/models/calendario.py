from odoo.models import Model

class Calendario(Model):
    _inherit = "biblioteca.prestamo"
    
    def actionPrestamo(self):
        for record in self:
            values = {"name":"Devolución del libro: "+record.idEjemplar.name,
                      "start_date":record.fechaFin,
                      "stop_date": record.fechaFin,
                      "allday": True,
                      "show_as": "busy",
                      "privacy":"private",
                      "user_id":record.idUsuario.id
                      }
            self.env["calendar.event"].create(values)
        return super().actionPrestamo()

