from plone.app.testing import PloneSandboxLayer
from plone.app.testing import applyProfile
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import IntegrationTesting
from plone.app.testing import FunctionalTesting

from plone.testing import z2

from zope.configuration import xmlconfig


class TdfextensiontemplatecenterthemeLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load ZCML
        import tdf.extensiontemplatecentertheme
        xmlconfig.file(
            'configure.zcml',
            tdf.extensiontemplatecentertheme,
            context=configurationContext
        )

        # Install products that use an old-style initialize() function
        #z2.installProduct(app, 'Products.PloneFormGen')

#    def tearDownZope(self, app):
#        # Uninstall products installed above
#        z2.uninstallProduct(app, 'Products.PloneFormGen')

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'tdf.extensiontemplatecentertheme:default')

TDF_EXTENSIONTEMPLATECENTERTHEME_FIXTURE = TdfextensiontemplatecenterthemeLayer()
TDF_EXTENSIONTEMPLATECENTERTHEME_INTEGRATION_TESTING = IntegrationTesting(
    bases=(TDF_EXTENSIONTEMPLATECENTERTHEME_FIXTURE,),
    name="TdfextensiontemplatecenterthemeLayer:Integration"
)
TDF_EXTENSIONTEMPLATECENTERTHEME_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(TDF_EXTENSIONTEMPLATECENTERTHEME_FIXTURE, z2.ZSERVER_FIXTURE),
    name="TdfextensiontemplatecenterthemeLayer:Functional"
)
