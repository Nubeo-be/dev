# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import fields, models


RESSOURCES_VIEW = ('ressources', 'Ressources')


class IrUIView(models.Model):
    _inherit = 'ir.ui.view'

    type = fields.Selection(selection_add=[RESSOURCES_VIEW])
