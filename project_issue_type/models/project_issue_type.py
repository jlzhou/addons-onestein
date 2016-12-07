# -*- coding: utf-8 -*-
# Copyright 2016 ONESTEiN BV (<http://www.onestein.eu>)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import models, fields


class ProjectIssueType(models.Model):

    _name = 'project.issue.type'

    name = fields.Char('Name', required=True)
