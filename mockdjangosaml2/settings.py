from django.conf import settings


# Attribute names and values are taken from Croatian AAI@EduHr infrastructure.
# If needed, these default names and values can be modified in project 
# by redefining MOCK_SAML2_USERS in project's settings.py file.
MOCK_SAML2_USERS = getattr(settings, 'MOCK_SAML2_USERS', {
    'admin@aai-test.hr': {
        'password': 'admin',
        'session_info': {
            'ava': {
                'hrEduPersonUniqueID': ['admin@aai-test.hr'],
                'hrEduPersonPrimaryAffiliation': ['djelatnik'],
                'cn': ['Admin Surname'],
                'hrEduPersonOIB': ['12345678901'],
                'sn': ['Surname'],
                'hrEduPersonHomeOrg': ['aai-test.hr'],
                'mail': ['admin.surname@aai-test.hr'],
                'givenName': ['Admin']
            },
        },
    },
    'employee@aai-test.hr': {
        'password': 'somepwd1',
        'session_info': {
            'ava': {
                'hrEduPersonUniqueID': ['employee@aai-test.hr'],
                'hrEduPersonPrimaryAffiliation': ['djelatnik'],
                'cn': ['Employee Surname'],
                'hrEduPersonOIB': ['12345678902'],
                'sn': ['Surname'],
                'hrEduPersonHomeOrg': ['aai-test.hr'],
                'mail': ['employee.surname@aai-test.hr'],
                'givenName': ['Employee']
            },
        },
    },
    'student@aai-test.hr': {
        'password': 'somepwd2',
        'session_info': {
            'ava': {
                'hrEduPersonUniqueID': ['student@aai-test.hr'],
                'hrEduPersonPrimaryAffiliation': ['student'],
                'cn': ['Student Surname'],
                'hrEduPersonOIB': ['12345678903'],
                'sn': ['Surname'],
                'hrEduPersonHomeOrg': ['aai-test.hr'],
                'mail': ['student.surname@aai-test.hr'],
                'givenName': ['Student']
            },
        },
    },
}
)