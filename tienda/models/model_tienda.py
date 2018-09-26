
from odoo import models, fields, api, exceptions


class categoria(models.Model):
    _name = 'tienda.categoria'
    id_categoria = fields.Integer(
        string='codigo de categoria'
    )
    nombre=fields.Char(string="Nombre de la Categoria",required=True,size=20)
    descripcion = fields.Html(string="Descripcion de la categoria")
    imagen=fields.Binary(string="Imagen de Categoria")

    @api.constrains('nombre')
    def check_name(self):
        if not self.nombre:
            raise exceptions.ValidationError("Es necesario ingresar un nombre")