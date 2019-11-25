from odoo import models, fields

class Prueba(models.Model):
    _name = 'ordenador.prueba'
    codigo = fields.Integer('Codigo', required=True)
    modelo = fields.Char('Modelo de Prueba', required=True)
    potencia = fields.Char('Potencia', required=True)

    def name_get(self):
        res=[]
        for record in self:
            model = record.modelo
            res.append((record.id, model))
        return res