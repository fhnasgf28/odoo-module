from odoo import models, fields


class Supplier(models.Model):
    _name = 'supplier'
    _description = 'Supplier'

    name = fields.Char(string='Supplier Name', required=True)
    contact_person = fields.Char(string='Contact Person')
    phone = fields.Char(string='Phone')
    email = fields.Char(string='Email')
    address = fields.Text(string='Address')
    products_supplied_ids = fields.One2many('manage.product', 'supplier_id', string='Products Supplied')
