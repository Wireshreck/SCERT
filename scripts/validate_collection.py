from pathlib import Path
import json, re, sys
try:
 import fitz
except ImportError:
 fitz=None
root=Path(__file__).resolve().parents[1]
# Source PDFs now live inside the per-chapter folders.
em_dir=root/'Class 9'/'English Medium'
errors=[]; warnings=[]; pdf_rows=[]
pdf_files=sorted(em_dir.rglob('*.pdf')) if em_dir.exists() else []
if not pdf_files:
 warnings.append('No local source PDFs found under Class 9/English Medium (expected in a fresh clone: PDFs are git-ignored). Restore them to the Chapter folders listed in PDF mappings from SOURCE_CATALOG.json to re-enable PDF checks.')
for f in pdf_files:
 if fitz is None:
  pdf_rows.append({'file':str(f.relative_to(root)).replace('\\','/'),'pages':None,'bytes':f.stat().st_size})
  continue
 try:
  d=fitz.open(f)
  if not d.is_pdf or d.page_count < 10: errors.append(f'PDF invalid or implausible page count: {f.name}'); continue
  texts=[page.get_text() for page in d]
  opening='\n'.join(texts[:8])
  title_ix=bool(re.search(r'(Standard|STANDARD)\s*(IX|9)|\bIX\b',opening))
  year=re.search(r'First Edition\s*:?\s*(20(?:19|2\d))',opening,re.I) or re.search(r'\b(20(?:19|2\d))\b',opening,re.I)
  if not title_ix: warnings.append(f'Class marker not machine-detected in opening text (manual confirmation may apply): {f.name}')
  blank=[i+1 for i,t in enumerate(texts) if not t.strip()]
  pdf_rows.append({'file':str(f.relative_to(root)).replace('\\','/'),'pages':d.page_count,'bytes':f.stat().st_size,'edition_year':year.group(1) if year else None,'text_pages':sum(bool(t.strip()) for t in texts),'blank_text_pages':blank})
 except Exception as e: errors.append(f'Could not open {f.name}: {e}')
expected_pdf_count=20
# PDFs are git-ignored, so a fresh clone legitimately has zero; only error when some are present but the count is wrong.
if pdf_rows and len(pdf_rows)!=expected_pdf_count: errors.append(f'Expected {expected_pdf_count} source PDFs in the current Class 9 English Medium inventory; found {len(pdf_rows)}')
# Frontmatter and wiki links for Markdown notes.
md_files=list(root.rglob('*.md'))
pdf_link_warnings=set()
for p in md_files:
 if '.git' in p.parts: continue
 raw=p.read_text(encoding='utf-8-sig')
 if p.is_relative_to(root/'Class 9'/'English Medium') and (p.parent != root/'Class 9'/'English Medium' or p.name == 'Class 9 English Medium.md'):
  if not raw.startswith('---\n') or '\n---\n' not in raw[4:]: errors.append(f'Missing or malformed YAML frontmatter: {p.relative_to(root)}')
 for target in re.findall(r'\[\[([^\]|#]+)',raw):
  target=target.strip()
  if not target: continue
  dest=(p.parent/target)
  candidates=[dest,Path(str(dest)+'.md'),Path(str(dest)+'.canvas'),Path(str(dest)+'.pdf')]
  if not any(c.exists() for c in candidates):
   # Missing PDFs are git-ignored and expected in a fresh clone; warn, do not fail the link check.
   if target.lower().endswith('.pdf'):
    pdf_link_warnings.add(target)
   else:
    errors.append(f'Unresolved wiki link in {p.relative_to(root)}: [[{target}]]')
for t in sorted(pdf_link_warnings):
 warnings.append(f'Local source PDF not present (git-ignored; restore from SOURCE_CATALOG.json to the Chapter folder): {t}') if len(pdf_link_warnings)<=5 else None
if len(pdf_link_warnings)>5:
 warnings.append(f'{len(pdf_link_warnings)} local source PDF links point to git-ignored PDFs not present in this checkout; restore them to the Chapter folders per SOURCE_CATALOG.json / migrate_structure.py mappings.')
# Canvas JSON, file nodes, IDs/edges, and geometric overlap checks.
canvas_rows=[]
for p in root.rglob('*.canvas'):
 try:
  data=json.loads(p.read_text(encoding='utf-8-sig')); nodes=data['nodes']; edges=data['edges']; ids={n['id'] for n in nodes}
  if len(ids)!=len(nodes): errors.append(f'Duplicate Canvas node IDs: {p.relative_to(root)}')
  for n in nodes:
   if n.get('type')!='file': errors.append(f'Non-file Canvas node in {p.relative_to(root)}: {n.get("id")}'); continue
   f=root/n['file']
   if not f.is_file(): errors.append(f'Missing Canvas file node target: {p.relative_to(root)} -> {n.get("file")}')
  for e in edges:
   if e.get('fromNode') not in ids or e.get('toNode') not in ids: errors.append(f'Canvas edge has missing endpoint: {p.relative_to(root)}')
  for i,a in enumerate(nodes):
   for b in nodes[i+1:]:
    if a['x']<b['x']+b['width'] and a['x']+a['width']>b['x'] and a['y']<b['y']+b['height'] and a['y']+a['height']>b['y']:
     errors.append(f'Overlapping Canvas nodes in {p.relative_to(root)}: {a["id"]}, {b["id"]}')
  canvas_rows.append({'file':str(p.relative_to(root)).replace('\\','/'),'nodes':len(nodes),'edges':len(edges)})
 except Exception as e: errors.append(f'Invalid Canvas JSON {p.relative_to(root)}: {e}')
print(json.dumps({'pdfs':pdf_rows,'total_pdf_count':len(pdf_rows),'total_pages':sum(x['pages'] for x in pdf_rows),'markdown_count':len(md_files),'canvases':canvas_rows,'errors':errors,'warnings':warnings},indent=2))
sys.exit(bool(errors))
