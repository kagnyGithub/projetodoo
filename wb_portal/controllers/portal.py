from odoo.addons.portal.controllers.portal import CustomerPortal, pager
from odoo.http import request
from odoo import http

class WebPortal(CustomerPortal):

    def _prepare_home_portal_values(self, counters):

        rtn = super(WebPortal, self)._prepare_home_portal_values(counters)
        rtn['student_counts'] = request.env['university.student'].search_count([])
        return rtn
    @http.route(['/my/students','/my/students/page/<int:page>'],type='http',website=True)
    def wbStudentListviews(self,page=1, **kw):
        student_obj = request.env['university.student']
        total_students = student_obj.search_count([])
        page_detail =  pager(url='/my/students',
                             total= total_students,
                             page = page,
                             step = 30
                              )
        students = student_obj.search([],limit=5, offset=page_detail['offset'])

        vals = {'students':students,'page_name':'student_view_list','pager':page_detail}
        return request.render("wb_portal.wb_student_list_view_template",vals)

    @http.route(['/my/students/<model("university.student"):student_id>'], type='http', website=True)
    def wbStudentFormview(self,student_id,**kw):
        vals = {'student':student_id,'page_name':'student_form_list'}
        return request.render("wb_portal.wb_student_form_view_template",vals)
