import argparse
import json
import os
from dataclasses import dataclass

@dataclass
class TranslationTarget:
    language: str
    translations: dict

def run_translation_pipeline(sample_dir):
    source_strings = json.load(open(os.path.join(sample_dir, 'source.json')))
    translation_target = TranslationTarget('en', {})
    for key, value in source_strings.items():
        translation_target.translations[key] = f'Translated {value}'
    with open(os.path.join(sample_dir, 'translations.json'), 'w') as f:
        json.dump(translation_target.translations, f, indent=4)
    return translation_target

def main():
    parser = argparse.ArgumentParser(description='Run the localization pipeline')
    parser.add_argument('--sample', action='store_true', help='Run the pipeline with a sample project')
    args = parser.parse_args()
    if args.sample:
        sample_dir = 'sample'
        os.makedirs(sample_dir, exist_ok=True)
        with open(os.path.join(sample_dir, 'source.json'), 'w') as f:
            json.dump({'hello': 'Hello', 'world': 'World'}, f)
        translation_target = run_translation_pipeline(sample_dir)
        print(f'Translation pipeline completed successfully. Translations saved to {sample_dir}/translations.json')
        return 0
    else:
        print('Please provide a valid configuration')
        return 1

if __name__ == '__main__':
    exit(main())
