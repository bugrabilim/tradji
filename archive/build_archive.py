from pathlib import Path
from zipfile import ZipFile, ZIP_DEFLATED

root = Path(__file__).resolve().parent
artifacts = root / 'artifacts'
output = root / 'Tradji_Gorusme_Arsivi.zip'

with ZipFile(output, 'w', ZIP_DEFLATED) as archive:
    for path in sorted(root.glob('*.md')):
        archive.write(path, path.relative_to(root.parent))
    for path in sorted(artifacts.glob('*')):
        if path.is_file():
            archive.write(path, path.relative_to(root.parent))

print(f'Archive created: {output}')
