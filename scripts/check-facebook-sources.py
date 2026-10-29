"""Check Facebook-imported exhibits before publication. No network or dependencies."""
import json,re,sys
from pathlib import Path
from urllib.parse import urlparse
root=Path(__file__).resolve().parents[1]
rows=json.loads((root/'collection.json').read_text(encoding='utf-8'))
errors=[]
for r in rows:
    if not r.get('id','').startswith('facebook-'):continue
    source=r.get('source_url','')
    u=urlparse(source)
    if not (u.scheme=='https' and u.hostname=='www.facebook.com' and re.fullmatch(r'/hellboymuseum/posts/[A-Za-z0-9]+/?',u.path)):
        errors.append(r['id']+': missing direct Hellboy Museum Facebook post link')
        continue
    page=root/'exhibits'/(r['id']+'.html')
    if not page.is_file() or ('href="'+source+'"') not in page.read_text(encoding='utf-8'):
        errors.append(r['id']+': individual page is missing its Facebook button')
if errors:
    print('\n'.join(errors));sys.exit(1)
print('All Facebook-imported exhibits have original post links and page buttons.')
