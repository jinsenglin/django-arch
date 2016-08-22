from app1 import apps


def test_config_menu():
    assert hasattr(apps.App1Config, 'menu')
    assert 'dashboard' in apps.App1Config.menu
    assert 'name' in apps.App1Config.menu
    assert 'order' in apps.App1Config.menu
    assert 'path' in apps.App1Config.menu
    assert 'scope' in apps.App1Config.menu
