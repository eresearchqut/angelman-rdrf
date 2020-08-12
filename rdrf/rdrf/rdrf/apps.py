# flake8: noqa
# ignoring the linting because of all unused imports which were necessary for missed migrations.

from django.apps import AppConfig
import logging

logger = logging.getLogger(__name__)


class RDRFConfig(AppConfig):
    name = 'rdrf'

    def ready(self):
        logger.info("running RDRFConfig.ready ... ")
        import rdrf.account_handling.backends
        import rdrf.models.definition.models
        # migration wasn't being found - importing here fixed that
        import rdrf.models.proms.models
