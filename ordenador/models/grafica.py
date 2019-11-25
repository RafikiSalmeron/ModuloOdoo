from odoo import models, fields

class Grafica(models.Model):
    _name = 'ordenador.grafica'
    codigo = fields.Integer('Codigo', required=True)
    modelo = fields.Char('Modelo de Grafica', required=True)
    frecuencia = fields.Char('Frecuencia', required=True)

    def name_get(self):
        res=[]
        for record in self:
            model = record.modelo
            res.append((record.id, model))
        return res