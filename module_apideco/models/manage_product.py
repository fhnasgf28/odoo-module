from odoo import fields, models, api, _
from odoo.exceptions import ValidationError
from datetime import timedelta, date


class ManageProduct(models.Model):
    _name = 'manage.product'
    _description = 'Manage Product'

    name = fields.Char(string='Product Name', required=True)
    description = fields.Text(string='Description')
    price = fields.Float(string='Price', required=True)
    stock = fields.Integer(string='Stock', required=True)
    code_barang = fields.Char(string='Kode Barang')
    kelompok_barang = fields.Selection([
        ('electronic', 'Electronic'),
        ('furniture', 'Furniture'),
        ('clothing', 'Clothing'),
        ('food', 'Food'),
        ('other', 'Other')
    ], string='Group Type', required=True, default='other')
    group_id = fields.Many2one('product.group', string='Product Group')
    category_id = fields.Many2one('product.category', string='Category')
    supplier_id = fields.Many2one('res.partner', string='Supplier')
    purchase_date = fields.Date(string='Purchase Date')
    expiry_date = fields.Date(string='Expiry Date')
    barcode = fields.Char(string='Barcode', compute='_compute_no_barcode')
    location = fields.Many2one('res.country',string='Location')
    active = fields.Boolean(string='Active', default=True)

    @api.depends('code_barang')
    def _compute_no_barcode(self):
        for barcode in self:
            if not barcode.code_barang:
                barcode.barcode = ''
            else:
                barcode.barcode = '15674' + '' + barcode.code_barang

    @api.onchange('code_barang')
    def _onchange_code_barang(self):
        if self.code_barang and len(self.code_barang) > 5:
            raise ValidationError('Kode Barang tidak boleh lebih dari 5 angka')

    @api.depends('name', 'code_barang')
    def _compute_display_name(self):
        for record in self:
            record.display_name = '%s (%s)' % (record.name, record.code_barang) if record.code_barang else record.name
