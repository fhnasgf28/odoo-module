from odoo import models, fields, api
from odoo.exceptions import ValidationError


class Supplier(models.Model):
    _name = 'supplier'
    _description = 'Supplier'

    name = fields.Char(string='Supplier Name', required=True)
    contact_person = fields.Char(string='Contact Person')
    phone = fields.Char(string='Phone')
    email = fields.Char(string='Email')
    address = fields.Text(string='Address')
    products_supplied_ids = fields.One2many('manage.product', 'supplier_id', string='Products Supplied')

    @api.constrains('name', 'email')
    def _check_unique_name_email(self):
        for supplier in self:
            duplicate_suppliers = self.search([
                ('name', '=', supplier.name),
                ('email', '=', supplier.email),
                ('id', '!=', supplier.id),
            ])
            if duplicate_suppliers:
                raise ValidationError('A supplier with the same name and email already exists.')

    @api.depends('name', 'phone')
    def _compute_display_name(self):
        for record in self:
            record.display_name = '%s (%s)' % (record.name, record.phone) if record.phone else record.name