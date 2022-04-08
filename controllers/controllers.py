# -*- coding: utf-8 -*-
from odoo import http


class Ratings(http.Controller):
    @http.route('/ratings/ratings/', auth='public')
    def index(self, **kw):
        return "Hello, world"

    @http.route('/ratings/ratings/objects/', auth='public')
    def list(self, **kw):
        return http.request.render('ratings.listing', {
            'root': '/ratings/ratings',
            'objects': http.request.env['ratings.ratings'].search([]),
        })

    @http.route('/ratings/ratings/objects/<model("ratings.ratings"):obj>/', auth='public')
    def object(self, obj, **kw):
        return http.request.render('ratings.object', {
            'object': obj
        })
