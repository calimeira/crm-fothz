# Part of Fothz. See LICENSE file for full copyright and licensing details.

from odoo import models
from odoo.http import request, Response


class IrHttp(models.AbstractModel):
    _inherit = 'ir.http'

    @classmethod
    def get_utm_domain_cookies(cls):
        return request.httprequest.host

    @classmethod
    def _set_utm(cls, response):
        # Make sure response is an odoo Response.
        response = Response.load(response)
        domain = cls.get_utm_domain_cookies()
        for url_parameter, __, cookie_name in request.env['utm.mixin'].tracking_fields():
            if url_parameter in request.params and request.httprequest.cookies.get(cookie_name) != request.params[url_parameter]:
                response.set_cookie(cookie_name, request.params[url_parameter], max_age=31 * 24 * 3600, domain=domain, cookie_type='optional')

    @classmethod
    def _post_dispatch(cls, response):
        cls._set_utm(response)
        super()._post_dispatch(response)
