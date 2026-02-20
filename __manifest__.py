{
    'name': 'Formato Cotizacion Truck Solution GP',
    'version': '1.0',
    'summary': 'Custom Sale Order Report for Truck Solution',
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
