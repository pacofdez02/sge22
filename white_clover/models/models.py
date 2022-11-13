# -*- coding: utf-8 -*-
from odoo import models, fields, api




class player(models.Model):
    _name = 'white_clover.player'
    _description = 'Player'

    image = fields.Image(max_width = 200, max_height = 200)
    name = fields.Char(string = "Nombre", required = True)
    password = fields.Char()
    avatar = fields.Image(max_width=200, max_height=200)

    name_village = fields.Char(required = True)
    image_village = fields.Image(max_width = 200, max_height = 200)
    size_village = fields.Float()

    buildings = fields.One2many('white_clover.building', 'player_village')

    grimoires = fields.One2many('white_clover.grimoire', 'player')
    grimoires_qty = fields.Integer(compute="get_grimoires_qty")

    @api.depends('grimoires')
    def get_grimoires_qty(self):
        for p in self:
            p.grimoires_qty = len(p.grimoires)


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

    #name = fields.Selection([('1','mana_production'),('2','gold_production'),('3','wizard_production')])
    name = fields.Char(related = 'building_type.name')
    image = fields.Image(related = 'building_type.image')

    player_village = fields.Many2one('white_clover.player',ondelete="cascade")
    npc_village = fields.Many2one('white_clover.npc_village', ondelete="cascade")

    #type = fields.Selection([('1','magic_institute'),('2','creation_institute'),('3','wizard_institute')])

    building_type = fields.Many2one('white_clover.building_type')

    mana_production = fields.Float(related = 'building_type.mana_production')
    gold_production = fields.Float(related = 'building_type.gold_production')
    wizard_production = fields.Float(related = 'building_type.wizard_production')
    

    #def produce(self):
     #   for b in self:
      #      print("Produce",b.food_production)


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
    check_xp = fields.Integer()
    check_lvl = fields.Integer(compute="check_level")
    
    
    
    @api.constrains('xp')
    def check_xp(self):
        for b in self:
            if b.xp > 1000000:
                raise ValidationError("You cant have more than 1m xp %s" % b.xp)
            
    #igual hay que tocar este constrains porque el xp puede pasarse un poco y dar mas de nivel 100
    @api.constrains('level')
    def check_level(self):
        for b in self:
            if b.level > 100:
                raise ValidationError("Level cant be more than 100 levels")

    #hacer que los grimorios tengan tipos y cada grimorio hechizos que se pueden sustituir, un modelo nuevo que sea hechizo, hacer varios grimorios de demo 