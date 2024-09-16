# Part of Fothz. See LICENSE file for full copyright and licensing details.
{
    'name': 'Turkey - Accounting',
    'website': 'https://www.fothz.com/documentation/17.0/applications/finance/fiscal_localizations.html',
    'icon': '/account/static/description/l10n.png',
    'countries': ['tr'],
    'version': '1.2',
    'category': 'Accounting/Localizations/Account Charts',
    'description': """
    Turkish charts of accounts
    ========================================
        * Defines the default chart of accounts
        * Defines the default taxes
        * Defines default tax report

    This was done in collaboration with Broadmax Partner in Turkey.
    """,
    'author': 'Fothz',
    'depends': [
        'account',
    ],
    'data': [
        'data/account_tax_report_data.xml',
    ],
    'demo': [
        'demo/demo_company.xml',
    ],
    'license': 'LGPL-3',
}
