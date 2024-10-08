{
    'name': 'Modul Pemesanan Ruangan',
    'version': '1.0',
    'category': 'Management',
    'summary': 'Modul untuk memesan ruangan di Odoo',
    'description': """
        Modul untuk memesan ruangan di Odoo.
        Modul ini mencakup fitur untuk mengelola master ruangan dan pemesanan ruangan.
    """,
    'depends': ['base'],
    'data': [
        'views/master_ruangan_views.xml',
        'views/pemesanan_ruangan_views.xml',
        'data/ir_sequence_data.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'AGPL-3',
}
