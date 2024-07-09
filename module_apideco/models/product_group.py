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
        for group in self:
            total_value = sum(product.price * product.stock for product in group.product_ids)
            group.total_value = total_value

    def _compute_total_products(self):
        for group in self:
            total_products = len(group.product_ids)
            group.total_products = total_products

    def _compute_average_price(self):
        for group in self:
            total_price = sum(product.price for product in group.product_ids)
            total_products = len(group.product_ids)
            group.average_price = total_price / total_products if total_products > 0 else 0