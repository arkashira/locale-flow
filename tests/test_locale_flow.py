from locale_flow import LocaleFlow, TranslationSettings
import pytest

def test_configure_translation_settings():
    locale_flow = LocaleFlow()
    settings = locale_flow.configure_translation_settings(True, True, "workflow")
    assert settings.translation_memory
    assert settings.terminology
    assert settings.workflow == "workflow"

def test_save_settings():
    locale_flow = LocaleFlow()
    locale_flow.configure_translation_settings(True, True, "workflow")
    settings = locale_flow.save_settings()
    assert settings["translation_memory"]
    assert settings["terminology"]
    assert settings["workflow"] == "workflow"

def test_validate_settings():
    locale_flow = LocaleFlow()
    settings = {"translation_memory": True, "terminology": True, "workflow": "workflow"}
    assert locale_flow.validate_settings(settings)

def test_validate_settings_missing_key():
    locale_flow = LocaleFlow()
    settings = {"translation_memory": True, "terminology": True}
    assert not locale_flow.validate_settings(settings)

def test_save_settings_not_configured():
    locale_flow = LocaleFlow()
    with pytest.raises(ValueError):
        locale_flow.save_settings()
