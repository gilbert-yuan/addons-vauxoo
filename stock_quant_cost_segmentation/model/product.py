# -*- coding: utf-8 -*-
##############################################################################
#
#    Copyright 2016 Vauxoo
#    Author : Humberto Arocha <hbto@vauxoo.com>
#             Osval Reyes <osval@vauxoo.com>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published
#    by the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
from openerp import models, fields


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    material_cost = fields.Float(
        string='Material Cost', readonly=True)
    production_cost = fields.Float(
        string='Production Cost', readonly=True)
    subcontracting_cost = fields.Float(
        string='Subcontracting Cost', readonly=True)
    landed_cost = fields.Float(
        string='Landed Cost', readonly=True)
