from odoo import models, fields, api

class OrdenadorOrdenador(models.Model):
    _name = 'ordenador.ordenador'
    codigo = fields.Integer('Codigo', required=True)
    marca = fields.Char('Marca', required=True)
    modelo = fields.Char('Modelo', required=True)





    @api.one
    def limpiar(self):
        self.marca = ""
        return True

    @api.multi
    def limpia_todo(self):
        done_recs = self.search([('marca', '=', 'fender')])
        done_recs.write({'marca': 'Fender'})
        return True