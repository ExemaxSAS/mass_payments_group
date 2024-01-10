# -*- coding: utf-8 -*-

from odoo import models, fields, api


class MassPaymentsGroup(models.Model):
    _name = 'mass.payments.group'
    _description = 'Mass Payments Group'

    journal_id = fields.Many2one('account.journal', string='Journal')
