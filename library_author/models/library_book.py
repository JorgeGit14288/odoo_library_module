from odoo import models, fields, api # importamos las clases en odoo que vamos a utilizar


class LibraryBook(models.Model):  # el modelo hereda de Models
    _inherit = "library.book"  # Este modelo hereda de library.book, un modelo ya existente

    author_id = fields.Many2one("library.author")
