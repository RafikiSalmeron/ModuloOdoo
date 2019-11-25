from odoo import models, fields

class Procesador(models.Model):
    _name = 'ordenador.placa'
    codigo = fields.Integer('Codigo', required=True)
    modelo = fields.Char('Modelo de Placa Base', required=True)
    capacidad = fields.Char('Capacidad de RAM', required=True)

    def name_get(self):
        res=[]
        for record in self:
            model = record.modelo
            res.append((record.id, model))
        return res