# -*- coding: utf-8 -*-
from odoo import api, fields, models, _

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    cantidad_alumnos = fields.Integer('Cantidad alumnos')
