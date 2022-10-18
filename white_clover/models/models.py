# -*- coding: utf-8 -*-
from odoo import models, fields, api




class player(models.Model):
    _name = 'white_clover.player'
    _description = 'Player'

    image = fields.Image(max_width = 200, max_height = 200)
    name = fields.Char(String = "Nombre", required = True)
    password = fields.Char()

    name_village = fields.Char(required = True)
    image_village = fields.Image(max_width = 200, max_height = 200)
    size_village = fields.Float()

    buildings = fields.One2many('white_clover.building', 'player_village')

    grimoires = fields.One2many('white_clover.grimoire', 'player')



class npc_village(models.Model):
    _name = 'white_clover.npc_village'
    _description = 'NPC Village'

    name = fields.Char(required = True)
    image = fields.Image(max_width = 200, max_height = 200)
    size = fields.Float()

    grimoires = fields.One2many('white_clover.grimoire', 'npc_village')
    buildings = fields.One2many('white_clover.building', 'npc_village')


class building(models.Model):
    _name = 'white_clover.building'
    _description = 'Building'

    name = fields.Char(required = True)
    image = fields.Image(max_width = 200, max_height = 200)
    size = fields.Float()

    player_village = fields.Many2one('white_clover.player')
    npc_village = fields.Many2one('white_clover.npc_village')

    #type = fields.Selection([('1','magic_institute'),('2','creation_institute'),('3','wizard_institute')])

    type = fields.Many2one('white_clover.building_type')
    magic_institute = fields.Float(related = 'type.magic_institute')
    creation_institute = fields.Float(related = 'type.creation_institute')
    wizard_institute = fields.Float(related = 'type.wizard_institute')


class building_type(models.Model):
    _name = 'white_clover.building_type'

    magic_institute = fields.Float()
    creation_institute = fields.Float()
    wizard_institute = fields.Float()





class grimoire(models.Model):
    _name = 'white_clover.grimoire'
    _description = 'Grimoire'


    level = fields.Float(compute = "get_lvl")
    xp = fields.Float()


    player = fields.Many2one('white_clover.player')
    npc_village = fields.Many2one('white_clover.npc_village') 

    @api.depends('xp')
    def get_lvl(self):
        for actual in self:



