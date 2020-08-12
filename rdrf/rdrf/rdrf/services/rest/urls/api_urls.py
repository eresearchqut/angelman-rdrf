from django.urls import re_path
from rdrf.services.rest.views import api_views
from rdrf.routing.custom_rest_router import DefaultRouterWithSimpleViews


router = DefaultRouterWithSimpleViews()
router.register(r'countries', api_views.ListCountries, basename='country')
router.register(r'users', api_views.CustomUserViewSet)
# Disabled as no registries use Family Linkage currently. Make sure it is secure if it needs to be re-enabled!
# router.register(r'registries/(?P<registry_code>\w+)/indices', api_views.LookupIndex, basename='index')
router.register(r'genes', api_views.LookupGenes, base_name='gene')
router.register(r'laboratories', api_views.LookupLaboratories, base_name='laboratory')
router.register(r'calculatedcdes', api_views.CalculatedCdeValue, base_name='calculatedcde')

urlpatterns = [
    re_path(r'registries/(?P<registry_code>\w+)/patients/(?P<pk>\d+)/$',
            api_views.PatientDetail.as_view(), name='patient-detail'),
    re_path(r'^countries/(?P<country_code>[A-Z]{2})/states/$',
            api_views.ListStates.as_view(), name="state_lookup"),
] + router.urls
