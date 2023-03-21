from odoo import models, fields, api


class ContactRelation(models.Model):
    _name = 'contact.relation'

    survey_id = fields.Many2one('survey.survey')
    question_id = fields.Many2one('survey.question', string="Question",
                                  domain="[('survey_id', '=', survey_id )]")
    field_id = fields.Many2one('ir.model.fields', string="Contact",
                               domain=[('model', '=', 'res.partner')])

    @api.onchange('question_id')
    def _onchange_question_id(self):
        """To set a survey id."""
        self.survey_id = self.survey_id._origin.id
