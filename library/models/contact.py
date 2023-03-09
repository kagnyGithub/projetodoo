from odoo import http
from odoo.http import request

class Contact(http.Controller):
    
    @http.route('/contact', auth='public', type='http', website='True')
    def contact(self, **kwargs):
        return request.render("library.contact_id", {})
