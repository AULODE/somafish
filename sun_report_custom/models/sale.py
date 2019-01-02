
from odoo import models, api
from odoo.tools import formatLang

class sale_order(models.Model):
    _inherit = 'sale.order'

    @api.multi
    def get_proper_format(self, amount):
        number =  formatLang(self.env, amount, monetary=True, currency_obj=self.currency_id)
        return number.rstrip('0').rstrip('.')