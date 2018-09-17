from odoo import models, fields, api # importamos las clases en odoo que vamos a utilizar


class LibraryBook(models.Model):  # el modelo hereda de Models
    _inherit = "library.book"  # Este modelo hereda de library.book, un modelo ya existente

    date = fields.Date(string="Release Date") # creamos un campo date para registrar la fecha
    purchase_price = fields.Float(string="Purchase price")
    sale_price = fields.Float(string="Sale Price")
    gain_price = fields.Float(compute='compute_gain') #este campo sera calculado, tiene la propiedad compute

    @api.depends('sale_price', 'purchase_price')  # para la funcion compute_gain pasamos los dos campos de depencencia
    def compute_gain(self): # la variable self contiene todos los datos dependientes y el modelo
        for record in self: # iteramos el modelo
                record.gain_price = record.sale_price - record.purchase_price # calculamos la ganancia
