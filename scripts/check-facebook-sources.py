"""Require verified Facebook source locations and buttons for imported exhibits."""
import json,re,sys,html
from pathlib import Path
from urllib.parse import urlparse,parse_qs
root=Path(__file__).resolve().parents[1]
rows=json.loads((root/'collection.json').read_text(encoding='utf-8'))
evidence=json.loads((root/'facebook-sources.json').read_text(encoding='utf-8'))
errors=[]
for r in rows:
    if not r.get('id','').startswith('facebook-'):continue
    source=r.get('source_url','');u=urlparse(source)
    post=bool(re.fullmatch(r'/hellboymuseum/posts/[A-Za-z0-9]+/?',u.path))
    proof=evidence.get(r['id'],{})
    photo=(u.path=='/photo/' and parse_qs(u.query).get('fbid')==[proof.get('photo_id')])
    if not (u.scheme=='https' and u.hostname=='www.facebook.com' and (post or photo) and proof.get('url')==source):
        errors.append(r['id']+': missing verified original Facebook location');continue
    page=root/'exhibits'/(r['id']+'.html')
    if not page.is_file():errors.append(r['id']+': missing exhibit page');continue
    content=page.read_text(encoding='utf-8')
    if ('href="'+html.escape(source,quote=True)+'"') not in content or 'View original Facebook post' not in content:
        errors.append(r['id']+': missing original Facebook button')
if len({r['id'] for r in rows})!=len(rows):errors.append('Duplicate exhibit IDs')
if len({r.get('source_url') for r in rows if r['id'].startswith('facebook-')})!=sum(r['id'].startswith('facebook-') for r in rows):errors.append('Duplicate Facebook source locations')
if errors:print('\n'.join(errors));sys.exit(1)
print('Verified Facebook source locations, matching buttons and unique IDs/sources.')
