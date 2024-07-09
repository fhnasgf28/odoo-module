from odoo import fields, models, api, _
from datetime import timedelta,date


class ManageProduct(models.Model):
    _name = 'manage.product'
    _description = 'Manage Product'

    name = fields.Char(string='Product Name', required=True)
    description = fields.Text(string='Description')
    price = fields.Float(string='Price', required=True)
    stock = fields.Integer(string='Stock', required=True)
    code_barang = fields.Char(string='Kode Barang')
    kelompok_barang = fields.Char(string='Kelompok Barang')
    group_id = fields.Many2one('product.group', string='Product Group')
    category_id = fields.Many2one('product.category', string='Category')
    supplier_id = fields.Many2one('res.partner', string='Supplier')
    purchase_date = fields.Date(string='Purchase Date')
    expiry_date = fields.Date(string='Expiry Date')
    barcode = fields.Char(string='Barcode')
    location = fields.Char(string='Location')
    active = fields.Boolean(string='Active', default=True)

