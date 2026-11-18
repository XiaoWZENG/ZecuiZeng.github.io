from pathlib import Path
import json,shutil
root=Path(__file__).resolve().parents[1]
data=json.loads((root/'content.json').read_text())
assert isinstance(data['papers'],list)
assert len({p['id'] for p in data['papers']})==len(data['papers'])
(root/'content.js').write_text('window.PORTFOLIO = '+json.dumps(data,ensure_ascii=False,indent=2)+';\n')
dist=root/'dist';dist.mkdir(exist_ok=True)
for name in ['index.html','style.css','app.js','content.js']:shutil.copy2(root/name,dist/name)
shutil.copytree(root/'assets',dist/'assets',dirs_exist_ok=True)
(dist/'.nojekyll').touch()
print('Built',dist)
