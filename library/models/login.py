from odoo import http
from odoo.http import request

class Login(http.Controller):
    
    @http.route('/login', auth='public', type='http', website='True')
    def log(self, **kwargs):
        return request.render("library.log_id", {})
