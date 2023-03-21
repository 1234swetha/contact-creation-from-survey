from odoo import models, fields


class Survey(models.Model):
    _inherit = 'survey.survey'

    relation_ids = fields.One2many('contact.relation', 'survey_id')
