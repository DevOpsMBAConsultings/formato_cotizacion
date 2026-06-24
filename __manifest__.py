{
    'name': 'Formato Cotizacion Suplidora JC',
    'version': '19.0.1.0.0',
    'license': 'LGPL-3',
    'summary': 'Custom Sale Order Report for Suplidora JC',
    'description': 'Replicates the design of _COT 285 PETROLEOS DELTA.pdf for Sale Orders.',
    'category': 'Sales',
    'author': 'Antigravity',
    'depends': ['sale', 'facturacion_electronica'],
    'data': [
        'views/report_saleorder.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}
