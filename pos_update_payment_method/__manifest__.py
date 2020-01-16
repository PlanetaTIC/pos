# -*- coding: utf-8 -*-
# Copyright 2020 PlanetaTIC - Marc Poch <mpoch@planetatic.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "POS Update Payment Method",
    "version": "10.0.1.0.0",
    "author": "PlanetaTIC, Odoo Community Association (OCA)",
    "description": "Permits you to change the journal of a ticket in TPV",
    "website": "https://github.com/OCA/pos",
    "license": "AGPL-3",
    "category": "Point Of Sale",
    'depends': [
        'point_of_sale',
    ],
    "data": [
        'views/account_view.xml',
        'wizard/pos_update_payment_method_view.xml'
    ],
    "installable": True,
}
