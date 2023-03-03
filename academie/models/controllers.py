from odoo import http


class Academy(http.Controller):
    @http.route('/academy/model', auth='public')
    def index(self, **kw):
        Teachers = http.request.env['academy.teachers']
        return http.request.render('academy.index', {
            'teachers': Teachers.search([])
        })