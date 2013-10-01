from django.conf import settings

MOCK_SAML2_USERS = getattr(settings, 'MOCK_SAML2_USERS', {
    'nsurname@aai-test.hr': {
        'password': 'somepwd1',
        'session_info': {
            'ava': {
                'hrEduPersonPrimaryAffiliation': ['djelatnik'],
                'cn': ['Name Surname'],
                'hrEduPersonOIB': ['12345678901'],
                'hrEduPersonUniqueID': ['nsurname@aai-test.hr'],
                'sn': ['Surname'],
                'hrEduPersonHomeOrg': ['aai-test.hr'],
                'mail': ['name.aurname@aai-test.hr'],
                'givenName': ['Name']
            },
        },
    },
    'student@aai-test.hr': {
        'password': 'somepwd2',
        'session_info': {
            'ava': {
                'hrEduPersonPrimaryAffiliation': ['student'],
                'cn': ['Name Surname'],
                'hrEduPersonOIB': ['12345678901'],
                'hrEduPersonUniqueID': ['nsurname@aai-test.hr'],
                'sn': ['Surname'],
                'hrEduPersonHomeOrg': ['aai-test.hr'],
                'mail': ['name.aurname@aai-test.hr'],
                'givenName': ['Name']
            },
        },
    },
}
)