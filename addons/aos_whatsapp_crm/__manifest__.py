# See LICENSE file for full copyright and licensing details.

{
    'name': 'Whatsapp CRM',
    'version': '17.0.0.1.0',
    'license': 'OPL-1',
    'author': "Alphasoft",
    'sequence': 1,
    'website': 'https://www.alphasoft.co.id/',
    'images':  ['images/main_screenshot.png'],
    'summary': 'This module is used for Whatsapp CRM',
    'category': 'Extra Tools',
    'depends': ['base_automation', 'crm', 'aos_whatsapp'],
    'data': [
        'data/crm_data.xml',
        'views/crm_lead.xml',
        'wizard/whatsapp_compose_view.xml',
    ],
    'external_dependencies': {'python': ['html2text']},
    'demo': [],
    'test': [],
    'css': [],
    'js': [],
    'price': 0,
    'currency': 'EUR',
    'installable': True,
    'application': False,
    'auto_install': False,
}
