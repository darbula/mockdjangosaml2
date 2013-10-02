from django.conf import settings


# Attribute names and values are taken from Croatian AAI@EduHr infrastructure
# If needed this deafult names and values can be modified in projects 
# specific MOCK_SAML2_USERS in settings.py  
MOCK_SAML2_USERS = getattr(settings, 'MOCK_SAML2_USERS', {
    'admin@aai-test.hr': {
        'password': 'admin',
        'session_info': {
            'ava': {
                'hrEduPersonPrimaryAffiliation': ['djelatnik'],
                'cn': ['Admin Surname'],
                'hrEduPersonOIB': ['12345678901'],
                'hrEduPersonUniqueID': ['asurname@aai-test.hr'],
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
                'hrEduPersonPrimaryAffiliation': ['djelatnik'],
                'cn': ['Employee Surname'],
                'hrEduPersonOIB': ['12345678902'],
                'hrEduPersonUniqueID': ['esurname@aai-test.hr'],
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
                'hrEduPersonPrimaryAffiliation': ['student'],
                'cn': ['Student Surname'],
                'hrEduPersonOIB': ['12345678903'],
                'hrEduPersonUniqueID': ['ssurname@aai-test.hr'],
                'sn': ['Surname'],
                'hrEduPersonHomeOrg': ['aai-test.hr'],
                'mail': ['student.surname@aai-test.hr'],
                'givenName': ['Student']
            },
        },
    },
}
)