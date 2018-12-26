# © 2013 Akretion (http://www.akretion.com)
# Raphaël Valyi <raphael.valyi@akretion.com>
# Sébastien BEAU <sebastien.beau@akretion.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).


from odoo import fields, models


class SeBackendAlgolia(models.Model):
    _name = 'se.backend.algolia'
    _inherit = 'se.backend.spec.abstract'
    _description = 'Algolia Backend'

    # TODO: load values from server env
    algolia_app_id = fields.Char(string="APP ID")
    # v12: we removed keychain inheritance
    # which was providing the field `password`.
    # This field was related to it, this is why `oldname` is here.
    algolia_api_key = fields.Char(string="API KEY", oldname='password')

    def init(self):
        # The init is called at install/update only before loading xml data
        # and demo data. Moreovoer these data are loaded before the end of
        # the initialization of the registry. Therefore we must also
        # register our backend to avoid error when loading the data since
        # the _register_hook is not yet called when the xml data are imported
        self.env['se.backend'].register_spec_backend(self)

    def _register_hook(self):
        # The register hook is called each time the registry is initialized,
        # not only at install.
        # Register our specialized backend
        self.env['se.backend'].register_spec_backend(self)
