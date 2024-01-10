# -*- coding: utf-8 -*-

from odoo import models, fields, api, _

class AccountMove(models.Model):
    _inherit = 'account.move'

    def action_register_mass_payment(self):
        return {
            'name': _('Register Mass Payment'),
            'res_model': 'mass.payments.group',
            'view_mode': 'form',
            'context': {
                'active_model': 'account.move',
                #'active_ids': self.account_move_id.ids
            },
            'target': 'new',
            'type': 'ir.actions.act_window',
        }
