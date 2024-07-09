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
    installment_ids = fields.One2many('installment', 'supplier_id', string='Installments')
    has_installments = fields.Boolean(string='Has Installments', compute='_compute_has_installments')

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

    @api.depends('installment_ids')
    def _compute_has_installments(self):
        for supplier in self:
            supplier.has_installments = bool(supplier.installment_ids)


class Installment(models.Model):
    _name = 'installment'
    _description = 'Supplier Installment'

    supplier_id = fields.Many2one('supplier', string='Supplier', required=True)
    amount = fields.Float(string='Amount', required=True)
    due_date = fields.Date(string='Due Date', required=True)
    paid = fields.Boolean(string='Paid', default=False)
    payment_amount = fields.Float(string='Payment Amount')

    @api.depends('supplier_id', 'amount')
    def _compute_display_name(self):
        for record in self:
            record.display_name = '%s (%s)' % (
            record.supplier_id.name, record.due_date) if record.supplier_id.name else record.due_date

