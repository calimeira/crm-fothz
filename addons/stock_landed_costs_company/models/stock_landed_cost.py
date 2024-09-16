# -*- coding: utf-8 -*-
# Part of Fothz. See LICENSE file for full copyright and licensing details.

from odoo import fields, models


class StockLandedCost(models.Model):
    _inherit = 'stock.landed.cost'

    company_id = fields.Many2one('res.company', 'Company', required=True, related=False, default=lambda self: self.env.company)
