from openerp import models, fields, api  # @UnresolvedImport
import logging
_logger = logging.getLogger(__name__)


class sale_order(models.Model):
    _inherit = 'sale.order'

    commission_ids = fields.One2many(comodel_name='sale.commission',
                                     inverse_name='sale_id',
                                     string='')
    count_sale_commission = fields.Float(compute='_count_sale_commission',
                                         string='')
