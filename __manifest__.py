# -*- coding: utf-8 -*-
{
    'name': "Mass Payments Group",

    'summary': """Mass Payments Group""",

    'description': """
        Mass Payments Group
    """,

    'author': "Exemax",
    'website': "https://www.exemax.com.ar",

    'category': 'Uncategorized',
    'version': '0.1',

    'depends': ['base', 'account', 'account_payment_group'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'wizard/mass_payments_group.xml',
    ],
    'demo': [],
}
