from app2_2 import apps


def test_config_menu():
    assert hasattr(apps.App22Config, 'menu')
    assert 'dashboard' in apps.App22Config.menu
    assert 'panel' in apps.App22Config.menu
    assert 'name' in apps.App22Config.menu
    assert 'order' in apps.App22Config.menu
    assert 'path' in apps.App22Config.menu
    assert 'scope' in apps.App22Config.menu
