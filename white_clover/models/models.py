# -*- coding: utf-8 -*-
from odoo import models, fields, api




class player(models.Model):
    _name = 'white_clover.player'
    _description = 'White Clover'

    image = fields.Image(max_width = 200, max_height = 200)
    name = fields.Char(String = "Nombre", required = True)
    password = fields.Char()

    grimorios = fields.One2many('white_clover-grimorios', 'player')

class villa(models.Model):
    _name = 'white_clover.villa'
    _description = 'Villas'

    name = fields.Char(required = True)
    image = fields.Image(max_width = 200, max_height = 200)
    size = fields.Float()

    grimorios = fields.One2many('white_clover-grimorios', 'villa')


class grimorio(models.Model):
    _name = 'white_clover.grimorio'
    _description = 'Grimorios'

    villas = fields.Many2One('white_clover.villa')
    player = fields.Many2One('white_clover.player')