from mysite import constants


def test_constants():
    assert hasattr(constants, 'ROLE_SUPER_ADMIN')
    assert hasattr(constants, 'ROLE_SYSTEM_ADMIN')
    assert hasattr(constants, 'ROLE_PROJECT_ADMIN')
    assert hasattr(constants, 'ROLE_PROJECT_USER')
    assert hasattr(constants, 'ROLE_AUDIT_USER')
