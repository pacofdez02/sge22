# -*- coding: utf-8 -*-
from odoo import models, fields, api




class player(models.Model):
    _name = 'white_clover.player'
    _description = 'Player'

    image = fields.Image(max_width = 200, max_height = 200)
    name = fields.Char(string = "Nombre", required = True)
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

    name = fields.Selection([('1','mana_production'),('2','gold_production'),('3','wizard_production')])
    image = fields.Image(related = 'building_type.image')

    player_village = fields.Many2one('white_clover.player',ondelete="cascade")
    npc_village = fields.Many2one('white_clover.npc_village', ondelete="cascade")

    #type = fields.Selection([('1','magic_institute'),('2','creation_institute'),('3','wizard_institute')])

    building_type = fields.Many2one('white_clover.building_type')

    mana_production = fields.Float(related = 'building_type.mana_production')
    gold_production = fields.Float(related = 'building_type.gold_production')
    wizard_production = fields.Float(related = 'building_type.wizard_production')


class building_type(models.Model):
    _name = 'white_clover.building_type'

    name = fields.Char()
    building_type = fields.One2many('white_clover.building', 'building_type')
    image = fields.Image(max_width = 200, max_height = 200)

    mana_production = fields.Float()
    gold_production = fields.Float()
    wizard_production = fields.Float()





class grimoire(models.Model):
    _name = 'white_clover.grimoire'
    _description = 'Grimoire'


    level = fields.Integer(compute = "get_lvl")
    xp = fields.Float()


    player = fields.Many2one('white_clover.player')
    npc_village = fields.Many2one('white_clover.npc_village') 

    #@api.depends('xp')
    #def get_lvl(self):
     #   for actual in self:
