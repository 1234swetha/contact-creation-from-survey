{
    'name': 'Contact Creation',
    'version': '16.0.1.0.0',
    'sequence': 1,
    'summary': 'Contact Creation From Survey',
    'description': """ 
                Contact is created from the submitted 
                answers of the survey forms.
                 """,
    'author': 'Cybrosys Techno Solutions',
    'company': 'Cybrosys Techno Solutions',
    'website': 'https://www.cybrosys.com',
    'maintainer': 'Cybrosys Techno Solutions',
    'support': 'Cybrosys Techno Solutions',
    'depends': [
        'survey',
        'base',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/survey_view.xml',
        'views/survey_question_views.xml',
    ],
}
