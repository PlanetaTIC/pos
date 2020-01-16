# -*- coding: utf-8 -*-
# Copyright 2020 PlanetaTIC - Marc Poch <mpoch@planetatic.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class AccountBankStatementLine(models.Model):
    _inherit = 'account.bank.statement.line'

    pos_order_state = fields.Selection(
        related='pos_statement_id.state', string='Status', readonly=True)

    def open_pos_update_payment_wizard(self):
        wiz_obj = self.env['pos.update.payment.method.wizard']
        self.ensure_one()
        wiz = wiz_obj.create({
            'pos_statement_line_id': self.id,
            'journal_id': self.journal_id.id,
        })
        return {
            'res_id': wiz.id,
            'view_id': self.env.ref(
                'pos_update_payment_method'
                '.pos_update_payment_method_wizard_view').ids,
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'pos.update.payment.method.wizard',
            'type': 'ir.actions.act_window',
            'context': {},
            'target': 'new'
        }
