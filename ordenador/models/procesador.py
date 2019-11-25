from odoo import models, fields

class Procesador(models.Model):
    _name = 'ordenador.procesador'
    codigo = fields.Integer('Codigo', required=True)
    modelo = fields.Char('Modelo del procesador', required=True)
    frecuencia = fields.Char('Frecuencia del procesador', required=True)

    def name_get(self):
        res=[]
        for record in self:
            model = record.modelo
            res.append((record.id, model))
        return res