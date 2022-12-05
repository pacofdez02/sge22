# -*- coding: utf-8 -*-
from odoo import models, fields, api
import random



class player(models.Model):
    _name = 'white_clover.player'
    _description = 'Player'

    image = fields.Image(max_width = 200, max_height = 200)
    name = fields.Char(string = "Name", required = True)
    password = fields.Char()
    reputation = fields.Char(readonly = True)

    mana = fields.Float(readonly=True)
    gold = fields.Float(default = 100)
    evolver = fields.Float(readonly = True)

    

    buildings = fields.One2many('white_clover.building', 'player')
    available_buildings = fields.Many2many('white_clover.building_type', compute="get_available_buildings")
    
    grimoires = fields.One2many('white_clover.grimoire', 'player')
    grimoires_qty = fields.Integer(compute="get_grimoires_qty")

    @api.depends('grimoires')
    def get_grimoires_qty(self):
        for p in self:
            p.grimoires_qty = len(p.grimoires)


    @api.depends('gold')
    def get_available_buildings(self):
        for c in self:
            c.available_buildings = self.env['white_clover.building_type'].search([('gold_build_cost', '<=', c.gold)])



class npc_village(models.Model):
    _name = 'white_clover.npc_village'
    _description = 'NPC Village'

    name = fields.Char(required = True)
    image = fields.Image(max_width = 200, max_height = 200)

    mana = fields.Float(readonly=True)
    gold = fields.Float(readonly=True)
    evolver = fields.Float(readonly = True)

    grimoires = fields.One2many('white_clover.grimoire', 'npc_village')
    buildings = fields.One2many('white_clover.building', 'npc_village')


class building(models.Model):
    _name = 'white_clover.building'
    _description = 'Building'

    name = fields.Char(related = 'building_type.name')
    image = fields.Image(related = 'building_type.image')

    player = fields.Many2one('white_clover.player',ondelete="cascade")
    npc_village = fields.Many2one('white_clover.npc_village', ondelete="cascade")

    building_type = fields.Many2one('white_clover.building_type')
    

    mana_production = fields.Float(related = 'building_type.mana_production')
    gold_production = fields.Float(related = 'building_type.gold_production')
    evolver_production = fields.Float(related = 'building_type.evolver_production')
    
    gold_build_cost = fields.Float(related = 'building_type.gold_build_cost')
    mana_build_cost = fields.Float(related = 'building_type.mana_build_cost')
    evolver_build_cost = fields.Float(related = 'building_type.evolver_build_cost')
    
    @api.model
    def produce(self):
       for b in self.search([]):
            if(b.player):
                player = b.player
                mana = player.mana + b.mana_production*10
                gold = player.gold + b.gold_production*10
                evolver = player.evolver + b.evolver_production*10
                player.write({
                    "mana":mana,
                    "gold":gold,
                    "evolver":evolver})

            if(b.npc_village):
                npc_village = b.npc_village
                mana = npc_village.mana + b.mana_production*20
                gold = npc_village.gold + b.gold_production*20
                evolver = npc_village.evolver + b.evolver_production*20
                npc_village.write({
                    "mana":mana,
                    "gold":gold,
                    "evolver":evolver})

   



class building_type(models.Model):
    _name = 'white_clover.building_type'

    name = fields.Char()
    buildings = fields.One2many('white_clover.building', 'building_type')
    image = fields.Image(max_width = 200, max_height = 200)

    mana_production = fields.Float()
    gold_production = fields.Float()
    evolver_production = fields.Float()

    gold_build_cost = fields.Float(default = 100)
    mana_build_cost = fields.Float(default = 250)
    evolver_build_cost = fields.Float(default = 500)

    def create_building(self):
        for b in self:
            player = self.env['white_clover.player'].browse(self.env.context['ctx_player'])[0]
            if player.gold >= b.gold_build_cost:
                self.env['white_clover.building'].create({
                    "player": player.id,
                    "building_type": b.id
                })
                player.gold -= b.gold_build_cost
            
    
            
            

class grimoire(models.Model):
    _name = 'white_clover.grimoire'
    _description = 'Grimoire'

    name = fields.Char(required = True)

    image = fields.Image()
    
    level = fields.Integer(readonly = True)
    #level = fields.Integer(compute = "get_lvl")
    xp = fields.Float()
    
    def getGrimoireType(self):
        grimoiresList = self.env["white_clover.grimoire_type"].search([]).ids
        return random.choice(grimoiresList)


    grimoire_type = fields.Many2one('white_clover.grimoire_type', default = getGrimoireType)
    grimoire_type_write = fields.Many2one('white_clover.grimoire_type')

    player = fields.Many2one('white_clover.player')
    npc_village = fields.Many2one('white_clover.npc_village') 

    hp = fields.Integer(readonly = True)
    attack = fields.Integer(readonly = True)
    defense = fields.Integer(readonly = True)
    speed = fields.Integer(readonly = True)

    

    @api.onchange('grimoire_type')
    def _onchange_stats(self):
        if self.grimoire_type.name == "White grimoire":
            image = self.grimoire_type.image
            hp = random.betavariate(5,1.3)*10
            attack = random.betavariate(1.5,1.5)*10
            defense = random.betavariate(1.5,1.5)*10
            speed = random.betavariate(1.5,1.5)*10

        if self.grimoire_type.name == "Red grimoire":
            image = self.grimoire_type.image
            attack = random.betavariate(5,1.3)*10
            hp = random.betavariate(1.5,1.5)*10
            defense = random.betavariate(1.5,1.5)*10
            speed = random.betavariate(1.5,1.5)*10

        if self.grimoire_type.name == "Blue grimoire":
            image = self.grimoire_type.image
            defense = random.betavariate(5,1.3)*10
            attack = random.betavariate(1.5,1.5)*10
            hp = random.betavariate(1.5,1.5)*10
            speed = random.betavariate(1.5,1.5)*10

        if self.grimoire_type.name == "Green grimoire":
            image = self.grimoire_type.image
            speed = random.betavariate(5,1.3)*10
            attack = random.betavariate(1.5,1.5)*10
            defense = random.betavariate(1.5,1.5)*10
            hp = random.betavariate(1.5,1.5)*10
        
        if self.hp == 0:
            hp += 1
        if self.attack == 0:
            attack += 1
       
            
        self.write({
                    "grimoire_type_write":self.grimoire_type.id,
                    "image":image,
                    "hp":hp,
                    "attack":attack,
                    "defense":defense,
                    "speed": speed})


    #check_xp = fields.Integer()
    #check_lvl = fields.Integer(compute="check_level")
    
    #@api.constrains('xp')
    #def check_xp(self):
        #for b in self:
         #   if b.xp > 1000000:
        #        raise ValidationError("You cant have more than 1m xp %s" % b.xp)
            
    #igual hay que tocar este constrains porque el xp puede pasarse un poco y dar mas de nivel 100
    #@api.constrains('level')
    #def check_level(self):
     #   for b in self:
      #      if b.level > 100:
       #         raise ValidationError("Level cant be more than 100 levels")

    #hacer que los grimorios tengan tipos y cada grimorio hechizos que se pueden sustituir, un modelo nuevo que sea hechizo, hacer varios grimorios de demo 
    
    
class grimoire_type(models.Model):
    _name = 'white_clover.grimoire_type'
    
    #name = fields.Selection([('1','Red Grimoire'),('2','Blue Grimoire'),('3','Green Grimoire'),('4','White Grimoire')],required =True)
    name = fields.Char(required=True)
    image = fields.Image(max_width = 200, max_height = 200)
    grimoires = fields.One2many('white_clover.grimoire', 'grimoire_type')

    hp = fields.Integer()
    attack = fields.Integer()
    defense = fields.Integer()
    speed = fields.Integer()

