# -*- coding: utf-8 -*-
# Copyright 2020 PlanetaTIC - Marc Poch <mpoch@planetatic.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models, _
from odoo.exceptions import UserError


class PosUpdatePaymentMethodWizard(models.TransientModel):
    _name = 'pos.update.payment.method.wizard'

    pos_statement_line_id = fields.Many2one(
        'account.bank.statement.line', string='Payment')

    available_journal_ids = fields.Many2many(
        'account.journal', string='Available journals',
        compute='_compute_available_journals')

    journal_id = fields.Many2one('account.journal', string='Journal',
                                 required=True)

    def _compute_available_journals(self):
        journal_obj = self.env['account.journal']

        if not self.pos_statement_line_id:
            journals = journal_obj.search([]).ids
        else:
            journals = [
                statement.journal_id.id for statement in
                self.pos_statement_line_id.pos_statement_id.session_id.
                statement_ids
            ]
        self.available_journal_ids = journals

    def pos_update_payment(self):
        self.ensure_one()
        if self.pos_statement_line_id.pos_statement_id.state != 'paid':
            raise UserError(_('You can only change payment of paid tickets.'))
        pos_session = self.pos_statement_line_id.pos_statement_id.session_id
        selected_statement = False
        for statement in pos_session.statement_ids:
            if statement.journal_id == self.journal_id:
                selected_statement = statement
        self.pos_statement_line_id.journal_id = self.journal_id
        self.pos_statement_line_id.statement_id = selected_statement
        return True
