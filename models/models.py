# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ratings(models.Model):
    _name = 'ratings.ratings'
    _description = 'ratings.ratings'

    proveedor = fields.Many2one('res.partner',domain=[('tipo','=','proveedor')])
    # provedor = fields.Char()
    rating = fields.Selection([('0','Muy malo'),('1','Malo'),('2','Regular'),('3','Bueno'),('4','Muy bueno'),('5','Excelente')],string="rating")
    descripcion = fields.Text()

   
