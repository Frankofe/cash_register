# -*- coding: utf-8 -*-
{
    'name': "Cash register",

    'summary': """
        Registration of income / expenses in the cash register.""",

    'description': """
        Shows the movements made by the contacts, whether they are in/out, and the date on which they were made.
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Accounting',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'contacts'],

    # always loaded
    'data': [
        'security/cash_register_group.xml',
        'security/ir.model.access.csv',
        'views/movements.xml',
        'views/res_partner.xml',
    ],
    
    #Aplications
    'application': True,
}
