# -*- coding: utf-8 -*-
from odoo import models, fields, api




class player(models.Model):
    _name = 'white_clover.player'
    _description = 'White Clover'

    name = fields.Char(required = True)