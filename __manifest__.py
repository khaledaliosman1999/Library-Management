{
    'name': 'Library Management',
    'author': 'Khaled Ali',
    'version': '1.0',
    'sequence' :'-100',
    'depends': ['base','mail'],
    
    'data': [
        'security/ir.model.access.csv',
        'views/library_members.xml',
        'views/library_books.xml',
        'views/library_booking.xml',

    ],
    'application': True,
    'installable': True,
    'license': 'LGPL-3',
}