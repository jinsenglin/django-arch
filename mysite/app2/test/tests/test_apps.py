from app2 import apps


def test_config_menu():
    assert hasattr(apps.App2Config, 'menu')
    assert 'dashboard' in apps.App2Config.menu
    assert 'name' in apps.App2Config.menu
    assert 'order' in apps.App2Config.menu
    assert 'scope' in apps.App2Config.menu
