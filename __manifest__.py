{
    'name': 'Customer Service Desk',
    'version': '1.0',
    'summary': 'Manage customer service tickets and support requests',
    'category': 'Services',
    'author': 'OpenAI',
    'website': 'https://example.com',
    'depends': ['base', 'mail'],
    'data': [
        'security/ir.model.access.csv',
        'views/custom_demo_views.xml',
        'views/custom_demo_menus.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
