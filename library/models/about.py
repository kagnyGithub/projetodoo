from odoo import http
from odoo.http import request

class About(http.Controller):
    
    @http.route('/about', auth='public', type='http', website='True')
    def about(self, **kwargs):
        return request.render("library.about_id", {})
