# -*- coding: utf-8 -*-
{
    'name': "white_clover",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','mail'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/player.xml',
        'views/building.xml',
        'views/building_type.xml',
        'views/grimoire.xml',
        'views/grimoire_type.xml',
        'views/views.xml',
        'views/templates.xml',
        'views/cron.xml',
        'demo/data.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
