from odoo import models, fields

class ProductGroup(models.Model):
    _name = 'product.group'
    _description = 'Product Group'

    name = fields.Char(string='Group Name', required=True)
    description = fields.Text(string='Description')
    parent_id = fields.Many2one('product.group', string='Parent Group')
    child_ids = fields.One2many('product.group', 'parent_id', string='Child Groups')
    product_ids = fields.One2many('manage.product', 'group_id', string='Products')
    creation_date = fields.Date(string='Creation Date', default=fields.Date.today)
    is_active = fields.Boolean(string='Active', default=True)
    manager_id = fields.Many2one('res.users', string='Group Manager')
    total_value = fields.Float(string='Total Value', compute='_compute_total_value')
    total_products = fields.Integer(string='Total Products', compute='_compute_total_products')
    average_price = fields.Float(string='Average Price', compute='_compute_average_price')

    def _compute_total_value(self):
        pass

    def _compute_total_products(self):
        pass

    def _compute_average_price(self):
        pass