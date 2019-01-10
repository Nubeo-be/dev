# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    'name': "Web Ressources",
    'summary': "Interactive visualization Ressources in time",
    "version": "11.0.1.4.1",
    'author': 'Nubeo', 
    "category": "web",
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "website": "http://nubeo.be",
    'depends': [
        'web',
        'calendar'
    ],

    'data': [
        'views/web_ressources.xml',
        'views/calendar.xml',

    ],
}
