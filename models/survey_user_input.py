import re
from odoo import models
from odoo.exceptions import ValidationError


class SurveyUser(models.Model):
    _inherit = 'survey.user_input'

    def _mark_done(self):
        """
        Override function _mark_done to create a contact
        at the time of submitting the survey.
        """
        vals = {}
        values = super()._mark_done()
        contact_id = self.env['contact.relation'].search([
            ('survey_id', '=', self.survey_id.id)])
        quest_id = contact_id.mapped('question_id')
        for line in self.user_input_line_ids:
            if not line.skipped and line.question_id in quest_id:
                for rec in contact_id:
                    if rec.question_id == line.question_id:
                        vals.update({
                            rec.field_id.name: line.display_name})
        self.env['res.partner'].create(vals)
        return values
