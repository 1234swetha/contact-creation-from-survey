import re

from odoo import models, fields, _


class SurveyQuestion(models.Model):
    _inherit = 'survey.question'

    validation_phone = fields.Boolean(string='Phone number validation')

    def _validate_char_box(self, answer):
        """Override the function _validate_char_box
           to create a validation error while entering
           invalid phone number.
        """
        super()._validate_char_box(self)
        if self.validation_phone:
            if re.match('\\+{0,1}[0-9]{10,12}', answer) is None:
                return {self.id: self.validation_error_msg or _('The answer you entered is not valid.')}
        return {}
