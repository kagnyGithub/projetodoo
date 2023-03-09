from odoo import http
from odoo.http import request

class Accueil(http.Controller):
    
    @http.route('/accueil', auth='public', type='http', website='True')
    def accueil(self, **kwargs):
        return request.render("library.home_id", {})
