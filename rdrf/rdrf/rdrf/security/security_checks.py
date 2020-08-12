from registry.patients.models import Patient
from registry.patients.models import ParentGuardian
from django.core.exceptions import PermissionDenied
from django.conf import settings
import logging

logger = logging.getLogger(__name__)


def _get_prop(user, prop):
    # case where site does not have prop defined
    try:
        return getattr(user, prop)
    except BaseException:
        return False


def _user_is_patient_type(user):
    return any([_get_prop(user, "is_patient"),
                _get_prop(user, "is_parent"),
                _get_prop(user, "is_carrier")])


def _security_violation(user, patient_model):
    logger.warning("SECURITY VIOLATION User %s Patient %s" % (user.pk,
                                                              getattr(patient_model, settings.LOG_PATIENT_FIELDNAME)))
    raise PermissionDenied()


def security_check_user_patient(user, patient_model):
    # either user is allowed to act on this record ( return True)
    # or not ( raise PermissionDenied error)
    if user.is_anonymous:
        return False
    if user.is_superuser:
        return True

    if _user_is_patient_type(user):
        # check patients who have registered as users with this user
        for user_patient in Patient.objects.filter(user=user):
            if user_patient.pk == patient_model.pk:
                # user IS patient
                return True

        # check parent guardian self patient and own children
        for parent in ParentGuardian.objects.filter(user=user):
            if patient_model in parent.children:
                return True
            if parent.self_patient and parent.self_patient.pk == patient_model.pk:
                return True

    registry = patient_model.rdrf_registry.first()
    if Patient.objects.get_by_user_and_registry(user, registry).filter(pk=patient_model.pk).exists():
        return True

    _security_violation(user, patient_model)


def get_object_or_permission_denied(klass, *args, **kwargs):
    """
    Use get() to return an object, or raise a PermissionDenied exception if the object
    does not exist. This is used to raise PermissionDenied for records which do not exist.

    klass may be a Model, Manager, or QuerySet object. All other passed
    arguments and keyword arguments are used in the get() query.

    Like with QuerySet.get(), MultipleObjectsReturned is raised if more than
    one object is found.
    """
    queryset = klass
    if hasattr(klass, '_default_manager'):
        queryset = klass._default_manager.all()
    if not hasattr(queryset, 'get'):
        klass__name = klass.__name__ if isinstance(klass, type) else klass.__class__.__name__
        raise ValueError(
            "First argument to get_object_or_404() must be a Model, Manager, "
            "or QuerySet, not '%s'." % klass__name
        )
    try:
        return queryset.get(*args, **kwargs)
    except queryset.model.DoesNotExist:
        raise PermissionDenied()
