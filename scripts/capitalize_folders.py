import pathlib, re, json, subprocess, shutil, posixpath
ROOT = pathlib.Path(__file__).resolve().parents[1]
EM = ROOT / 'Class 9' / 'English Medium'

renames = []
for d in sorted(EM.rglob('concepts')) + sorted(EM.rglob('questions')):
    if d.is_dir():
        target = d.parent / (d.name[0].upper() + d.name[1:])
        # Windows is case-insensitive: go via temp name
        tmp = d.parent / (d.name + '_CAP_TMP')
        tmp_exists = tmp.exists()
        if tmp_exists:
            shutil.rmtree(tmp)
        d.rename(tmp)
        tmp.rename(target)
        renames.append((str(d.relative_to(ROOT)).replace('\\','/'), str(target.relative_to(ROOT)).replace('\\','/')))
print(f"Renamed {len(renames)} directories")
for o,n in renames[:10]:
    print(f"  {o} -> {n}")

# Update wiki links in all md files: /concepts/ -> /Concepts/, /questions/ -> /Questions/
# and leading [[concepts/ and [[questions/
link_replacements = 0
for p in ROOT.rglob('*.md'):
    if '.git' in p.parts:
        continue
    txt = p.read_text(encoding='utf-8-sig', errors='ignore')
    orig = txt
    # full path segments (covers ../..., Concepts/... etc with leading / or start)
    txt = txt.replace('/concepts/', '/Concepts/').replace('/questions/', '/Questions/')
    # leading [[concepts/ or [[questions/ (at start of link target)
    txt = re.sub(r'\[\[concepts/', '[[Concepts/', txt)
    txt = re.sub(r'\[\[questions/', '[[Questions/', txt)
    # bare folder names without slash at link start? e.g. [[concepts]] not used, skip.
    if txt != orig:
        # count changes roughly
        link_replacements += orig.count('/concepts/') + orig.count('/questions/') + len(re.findall(r'\[\[concepts/', orig)) + len(re.findall(r'\[\[questions/', orig))
        p.write_text(txt, encoding='utf-8')
print(f"Updated link segments in md files: ~{link_replacements}")

# Canvas JSON file paths: /concepts/ -> /Concepts/
for c in ROOT.rglob('*.canvas'):
    if '.git' in c.parts:
        continue
    try:
        data = json.loads(c.read_text(encoding='utf-8-sig'))
    except Exception:
        continue
    changed = False
    for n in data.get('nodes', []):
        f = n.get('file', '')
        if '/concepts/' in f or '/questions/' in f:
            n['file'] = f.replace('/concepts/', '/Concepts/').replace('/questions/', '/Questions/')
            changed = True
    if changed:
        c.write_text(json.dumps(data, indent=2), encoding='utf-8')
print("Canvas paths updated.")

print("Done.")
