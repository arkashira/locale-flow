import pytest
from locale_flow import run_translation_pipeline, TranslationTarget
import json
import os
import tempfile

def test_run_translation_pipeline():
    with tempfile.TemporaryDirectory() as tmpdir:
        source_strings = {'hello': 'Hello', 'world': 'World'}
        with open(os.path.join(tmpdir, 'source.json'), 'w') as f:
            json.dump(source_strings, f)
        translation_target = run_translation_pipeline(tmpdir)
        assert translation_target.language == 'en'
        assert translation_target.translations == {key: f'Translated {value}' for key, value in source_strings.items()}
        with open(os.path.join(tmpdir, 'translations.json')) as f:
            assert json.load(f) == translation_target.translations

def test_run_translation_pipeline_empty_source():
    with tempfile.TemporaryDirectory() as tmpdir:
        with open(os.path.join(tmpdir, 'source.json'), 'w') as f:
            json.dump({}, f)
        translation_target = run_translation_pipeline(tmpdir)
        assert translation_target.language == 'en'
        assert translation_target.translations == {}

def test_main_sample():
    import sys
    import io
    sys.argv = ['locale_flow.py', '--sample']
    old_stdout = sys.stdout
    capturedOutput = io.StringIO()
    sys.stdout = capturedOutput
    from locale_flow import main
    exit_code = main()
    sys.stdout = old_stdout
    assert exit_code == 0
    assert 'Translation pipeline completed successfully' in capturedOutput.getvalue()

def test_main_no_sample():
    import sys
    import io
    sys.argv = ['locale_flow.py']
    old_stdout = sys.stdout
    capturedOutput = io.StringIO()
    sys.stdout = capturedOutput
    from locale_flow import main
    exit_code = main()
    sys.stdout = old_stdout
    assert exit_code == 1
    assert 'Please provide a valid configuration' in capturedOutput.getvalue()
