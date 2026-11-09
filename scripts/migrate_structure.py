"""
One-shot migration: per-chapter folder restructuring.

Old:
  <Subject>/Chapters/<ChapterNote>.md
  <Subject>/Concepts/<Concept>.md
  <Subject>/Exercises/<Exercise>.md
  <Subject>/Definitions/, Formulas/  (kept at subject root)
  <Subject>/Subject Overview*.md, *.canvas (kept at subject root)
  Class 9/English Medium/_Source PDFs/<*.pdf> (if present)

New:
  <Subject>/<ChapterStem>/<ChapterNote>.md
  <Subject>/<ChapterStem>/Concepts/<Concept>.md
  <Subject>/<ChapterStem>/Questions/<Exercise>.md
  <Subject>/Definitions/, Formulas/, Subject Overview*.md, *.canvas (unchanged)
  <Subject>/<ChapterStem>/<*.pdf>  (PDF placed in first chapter folder of its part)
"""
import pathlib, re, json, sys, subprocess, shutil, posixpath

ROOT = pathlib.Path(__file__).resolve().parents[1]
EM = ROOT / 'Class 9' / 'English Medium'
APPLY = '--apply' in sys.argv

def norm(s, nospace=False):
    s = (s or '').strip().strip('"').lower()
    s = s.replace('-', ' ').replace('_', ' ')
    s = re.sub(r'[^a-z0-9 ]', ' ', s)
    s = re.sub(r'\s+', ' ', s).strip()
    if nospace:
        s = s.replace(' ', '')
    return s

def parse_fm(p):
    try:
        txt = p.read_text(encoding='utf-8-sig', errors='ignore')
    except Exception:
        return {}
    fm = {}
    if txt.startswith('---'):
        end = txt.find('---', 3)
        if end > 0:
            for line in txt[3:end].splitlines():
                m = re.match(r'([a-z_]+):\s*(.*)', line.strip())
                if m:
                    fm[m.group(1)] = m.group(2).strip().strip('"')
    return fm

def posix_rel(path):
    return pathlib.Path(path).relative_to(ROOT).as_posix() if pathlib.Path(path).absolute().is_relative_to(ROOT) else str(path)

def rel_posix_from_to(new_from_parent_posix, new_target_posix, omit_ext=False):
    # both are vault-root relative posix paths
    # compute relative from dir
    target = new_target_posix
    if omit_ext and target.lower().endswith('.md'):
        target = target[:-3]
    rel = posixpath.relpath(target, new_from_parent_posix)
    return rel

# ---------- build chapter maps ----------
subjects = sorted([p for p in EM.iterdir() if p.is_dir() and p.name not in ('_Source PDFs', '.review')])
old_to_new = {}   # posix vault-root old -> new
stem_to_old = {}  # stem (filename w/o ext) -> list of old posix paths
move_stats = []
chapter_info = {}  # subject -> list of dicts {stem, folder, num, title, part, pages}

for subj in subjects:
    sname = subj.name
    ch_dir = subj / 'Chapters'
    if not ch_dir.exists():
        continue
    chapters = sorted(ch_dir.glob('*.md'))
    by_num = {}
    by_title = {}      # norm -> stem
    by_title_ns = {}   # norm nospace -> stem
    by_stem = {}
    infos = []
    for ch in chapters:
        fm = parse_fm(ch)
        stem = ch.stem
        suffix = stem.split(' - ', 1)[-1] if ' - ' in stem else stem
        # numeric prefix
        m = re.match(r'(?:Chapter\s*|Unit\s*|Ch\s*)?(\d+)', stem, re.I)
        num_from_name = m.group(1) if m else None
        chval = fm.get('chapter', '')
        num = chval if str(chval).isdigit() else num_from_name
        title = suffix
        part = fm.get('part', '') or fm.get('textbook', '')
        pages = fm.get('printed_pages', '')
        infos.append({'stem': stem, 'folder': stem, 'num': num, 'title': title, 'part': part, 'pages': pages, 'fm': fm, 'path': ch})
        by_stem[norm(stem)] = stem
        by_title.setdefault(norm(suffix), stem)
        by_title_ns.setdefault(norm(suffix, nospace=True), stem)
        # frontmatter chapter string
        if chval and not str(chval).isdigit():
            by_title.setdefault(norm(str(chval)), stem)
            by_title_ns.setdefault(norm(str(chval), nospace=True), stem)
        # num map
        for key in {num, num_from_name}:
            if key:
                by_num.setdefault(str(key), [])
                if stem not in by_num[str(key)]:
                    by_num[str(key)].append(stem)
    chapter_info[sname] = (infos, by_num, by_title, by_title_ns, by_stem)

    def find_target(f, fm, subj_name, src):
        infos_local, by_num_l, by_title_l, by_title_ns_l, by_stem_l = chapter_info[subj_name]
        chval = str(fm.get('chapter', '')).strip().strip('"')
        # 1. numeric
        if chval.isdigit():
            lst = by_num_l.get(chval, [])
            if len(lst) == 1:
                return lst[0]
            if len(lst) > 1:
                stem_ns = norm(f.stem, nospace=True)
                for c in lst:
                    t_ns = norm(c.split(' - ', 1)[-1], nospace=True)
                    if t_ns and t_ns in stem_ns:
                        return c
                for c in lst:
                    t_ns = norm(c.split(' - ', 1)[-1], nospace=True)
                    if t_ns and (t_ns[:12] in stem_ns or stem_ns in t_ns):
                        return c
                # fallback: first
                return lst[0]
        # 2. title string
        if chval:
            for d in (by_title_l, by_title_ns_l):
                t = d.get(norm(chval)) or d.get(norm(chval, nospace=True))
                if t:
                    return t
            # substring fuzzy
            cv = norm(chval)
            cv_ns = norm(chval, nospace=True)
            for k, v in by_title_l.items():
                if k and ((k in cv and len(k) >= 4) or (cv in k and len(cv) >= 4)):
                    return v
            for k, v in by_title_ns_l.items():
                if k and ((k in cv_ns) or (cv_ns in k)):
                    return v
        # 3. printed_pages overlap fallback
        pages = str(fm.get('printed_pages', ''))
        pm = re.match(r'(\d+)\D+(\d+)?', pages)
        if pm:
            try:
                start = int(pm.group(1))
                for info in infos_local:
                    ip = str(info.get('pages', ''))
                    m2 = re.match(r'(\d+)\D+(\d+)?', ip)
                    if m2:
                        s2 = int(m2.group(1))
                        e2 = int(m2.group(2)) if m2.group(2) else s2
                        e1 = int(pm.group(2)) if pm.group(2) else start
                        if s2 <= start <= e2 or s2 <= e1 <= e2:
                            return info['stem']
            except Exception:
                pass
        return None

    # chapters themselves
    for info in infos:
        old = posix_rel(info['path'])
        new = f"Class 9/English Medium/{sname}/{info['folder']}/{info['path'].name}"
        old_to_new[old] = new
        move_stats.append(('CHAPTER', old, new))
    # concepts -> concepts/
    for src, dst in [('Concepts', 'Concepts'), ('Exercises', 'Questions')]:
        d = subj / src
        if not d.exists():
            continue
        for f in sorted(d.glob('*.md')):
            fm = parse_fm(f)
            target_stem = find_target(f, fm, sname, src)
            if target_stem is None:
                print(f"ORPHAN (skipped, kept in {src}/): {sname}/{src}/{f.name} chapter={fm.get('chapter','')}")
                # keep unmoved, no map entry
                continue
            old = posix_rel(f)
            new = f"Class 9/English Medium/{sname}/{target_stem}/{dst}/{f.name}"
            old_to_new[old] = new
            move_stats.append((src.upper(), old, new))

# ---------- PDF map ----------
# SOURCE_CATALOG.json: file -> subject
pdf_old_to_new = {}
catalog_path = EM / 'SOURCE_CATALOG.json'
pdf_by_subject = {}
if catalog_path.exists():
    try:
        catalog = json.loads(catalog_path.read_text(encoding='utf-8-sig'))
        for entry in catalog:
            pdf_by_subject.setdefault(entry.get('subject', ''), []).append(entry.get('file', ''))
    except Exception as e:
        print(f"WARNING: could not parse SOURCE_CATALOG.json: {e}")

# first chapter per part per subject
part_first_folder = {}
for sname, (infos, by_num, by_title, by_title_ns, by_stem) in chapter_info.items():
    # sort chapters by printed page start for stable part ordering
    def _pstart(info):
        m = re.match(r'(\d+)', str(info.get('pages', '')))
        return int(m.group(1)) if m else 9999
    infos_sorted = sorted(infos, key=_pstart)
    folders_by_part = {}
    for info in infos_sorted:
        part_val = str(info.get('part', '')).strip().lower()
        # part field may be "1"/"2", "Part 1", "Part I", etc.
        if part_val in ('2', 'part 2', 'part ii'):
            k = 'part2'
        elif part_val in ('1', 'part 1', 'part i'):
            k = 'part1'
        elif 'part 2' in part_val or 'part ii' in part_val:
            k = 'part2'
        elif 'part 1' in part_val or 'part i' in part_val:
            k = 'part1'
        else:
            k = 'single'
        folders_by_part.setdefault(k, []).append(info['folder'])
    part_first_folder[sname] = folders_by_part

# For each known PDF filename (from catalog), compute target
# ICT has two "Part 1" PDFs (2025 + 2019 legacy) -> both go to part1 first folder
for entry in (json.loads(catalog_path.read_text(encoding='utf-8-sig')) if catalog_path.exists() else []):
    subj = entry.get('subject', '')
    fname = entry.get('file', '')
    if subj not in chapter_info:
        continue
    folders_by_part = part_first_folder.get(subj, {})
    part_raw = entry.get('official_title', '').lower() + ' ' + str(entry.get('edition_year', ''))
    # decide part
    target_folder = None
    if 'part ii' in str(entry.get('official_title', '')).lower() or 'part 2' in str(entry.get('official_title', '')).lower():
        target_folder = folders_by_part.get('part2', [None])[0]
    elif 'part i' in str(entry.get('official_title', '')).lower() or 'part 1' in str(entry.get('official_title', '')).lower():
        target_folder = folders_by_part.get('part1', [None])[0]
    if not target_folder:
        # single or fallback: first available part
        for k in ('part1', 'single', 'part2'):
            if k in folders_by_part and folders_by_part[k]:
                target_folder = folders_by_part[k][0]
                break
    if target_folder:
        old = f"Class 9/English Medium/_Source PDFs/{fname}"
        new = f"Class 9/English Medium/{subj}/{target_folder}/{fname}"
        pdf_old_to_new[old] = new
        move_stats.append(('PDF', old, new))

print(f"Total moves mapped: {len(move_stats)} (notes: {len(old_to_new)}, pdfs: {len(pdf_old_to_new)})")
for kind, o, n in move_stats[:20]:
    print(f"  {kind}: {o} -> {n}")
if len(move_stats) > 20:
    print(f"  ... +{len(move_stats)-20} more")
print("--- PDF mappings ---")
for kind, o, n in move_stats:
    if kind == 'PDF':
        print(f"  PDF: {o} -> {n}")

# stem index for bare links (based on old paths)
for old in list(old_to_new.keys()) + list(pdf_old_to_new.keys()):
    stem = pathlib.PurePosixPath(old).stem
    stem_to_old.setdefault(stem, []).append(old)
# IMPORTANT: include ALL old paths (unmoved overviews/canvas/definitions + root files)
# from HEAD so exact-path links to unmoved files resolve correctly before stem fallback.
try:
    head_files = subprocess.run(['git', 'ls-tree', '-r', '--name-only', 'HEAD'], cwd=ROOT, capture_output=True, text=True).stdout.splitlines()
except Exception:
    head_files = []
all_old_set = set(head_files) | set(old_to_new.keys()) | set(pdf_old_to_new.keys())
# HEAD has no PDFs (git-ignored); pdf old paths come from pdf_old_to_new keys (already included).

if not APPLY:
    print("\nDRY RUN complete. Re-run with --apply to move files and rewrite links.")
    sys.exit(0)

# ---------- APPLY: move files ----------
print("\nApplying moves...")
for kind, old, new in move_stats:
    src = ROOT / old
    dst = ROOT / new
    dst.parent.mkdir(parents=True, exist_ok=True)
    if kind == 'PDF' and not src.exists():
        # PDF not present in this checkout; keep mapping for link rewrite only
        continue
    if not src.exists():
        print(f"  MISSING source (skip): {old}")
        continue
    # use git mv if tracked, else shutil
    try:
        res = subprocess.run(['git', 'mv', old, new], cwd=ROOT, capture_output=True, text=True)
        if res.returncode != 0:
            shutil.move(str(src), str(dst))
            print(f"  moved (shutil, git mv failed): {old}")
    except Exception:
        shutil.move(str(src), str(dst))

# cleanup empty old dirs + remove _Source PDFs if empty
for subj in subjects:
    for sub in ['Chapters', 'Concepts', 'Exercises']:
        d = subj / sub
        if d.exists() and not any(d.iterdir()):
            try:
                d.rmdir()
                print(f"  removed empty dir: {posix_rel(d)}")
            except Exception:
                pass

# ---------- rewrite wiki links in all md files ----------
all_md = list(ROOT.rglob('*.md'))
# build full old->new combined map (notes + pdfs)
combined = {**old_to_new, **pdf_old_to_new}

# helper to resolve base link to old vault-root path
import collections
def _subject_from_parent(parent_posix):
    # parent like "Class 9/English Medium/<Subject>/..." or "Class 9/English Medium/<Subject>"
    parts = parent_posix.split('/')
    if len(parts) >= 4 and parts[0] == 'Class 9':
        return parts[3]
    return None

def resolve_old(base, old_parent_posix):
    # 1. Exact path first (covers moved targets AND unmoved overviews/canvas/definitions).
    cand_paths = []
    if base.startswith('Class 9/'):
        cand_paths.append(posixpath.normpath(base))
    else:
        cand_paths.append(posixpath.normpath(posixpath.join(old_parent_posix, base)))
        cand_paths.append(posixpath.normpath(base))
    # For exact, try all extensions; .md/.canvas/.pdf without extension required.
    for c in cand_paths:
        for cand in [c, c + '.md', c + '.canvas', c + '.pdf']:
            if cand in all_old_set or cand in combined:
                return cand
    # 2. Bare-title fallback (same-folder links like [[Homeostasis...]]).
    # Consider every old file with this stem (moved + unmoved), prefer same subject + same folder.
    bstem = pathlib.PurePosixPath(base).stem if '/' in base else base
    # merge stem sources: moved stems + all_old stems
    all_cands = list(stem_to_old.get(bstem, []))
    if 'all_stem' in globals():
        for v in all_stem.get(bstem, []):
            if v not in all_cands:
                all_cands.append(v)
    for v in all_old_set:
        if pathlib.PurePosixPath(v).stem == bstem and v not in all_cands:
            all_cands.append(v)
    if not all_cands:
        return None
    if len(all_cands) == 1:
        return all_cands[0]
    subj = _subject_from_parent(old_parent_posix)
    # exact same-parent-folder match first
    for v in all_cands:
        if posixpath.dirname(v) == old_parent_posix:
            return v
    if subj:
        for v in all_cands:
            if f"/{subj}/" in f"/{v}/" or v.startswith(f"Class 9/English Medium/{subj}/"):
                return v
    return all_cands[0]

# global stem -> old paths for ALL md/pdf (including unmoved), for bare fallback
all_stem = {}
for p in list(ROOT.rglob('*.md')):
    # NOTE: after moves, filesystem paths are new; for resolving OLD links we need OLD paths.
    # old paths are keys of combined plus unmoved olds (= news for unmoved)
    pass
# Instead construct all old stems from combined + unmoved list
unmoved = []
for p in EM.rglob('*.md'):
    # p is now NEW location (after move); old location for unmoved == new, for moved == key in old_to_new whose value == this
    # For moved files, their old stem already in stem_to_old; for unmoved, add
    newp = posix_rel(p)
    # find old by reverse lookup
    oldp = None
    for k, v in old_to_new.items():
        if v == newp:
            oldp = k
            break
    if oldp is None:
        oldp = newp  # unmoved
    stem = pathlib.PurePosixPath(oldp).stem
    all_stem.setdefault(stem, [])
    if oldp not in all_stem[stem]:
        all_stem[stem].append(oldp)

# need new parent map for each moved file's old parent -> new parent
# For rewriting, we iterate over files at their NEW location, but links are OLD-relative.
# So for each file at new location, its old location = reverse map or itself.
new_to_old = {v: k for k, v in old_to_new.items()}
# also pdfs have no content

link_pat = re.compile(r'\[\[([^\]|#]+)(#[^\]|]*)?(\|[^\]]*)?\]\]')

rewritten = 0
unresolved = []
for p in list(ROOT.rglob('*.md')):
    if '.git' in p.parts:
        continue
    newp = posix_rel(p)
    oldp = new_to_old.get(newp, newp)
    old_parent = posixpath.dirname(oldp)
    new_parent = posixpath.dirname(newp)
    txt = p.read_text(encoding='utf-8-sig', errors='ignore')
    orig_txt = txt
    def repl(m):
        global rewritten
        base = m.group(1).strip()
        heading = m.group(2) or ''
        alias = m.group(3) or ''
        if not base:
            return m.group(0)
        # skip external URLs? not in wiki links
        old_target = resolve_old(base, old_parent)
        if old_target is None:
            unresolved.append((newp, base))
            return m.group(0)
        new_target = combined.get(old_target, old_target)
        # preserve extension style: if base ends with .pdf/.md include ext, else strip .md
        has_ext = pathlib.PurePosixPath(base).suffix in ('.md', '.pdf', '.canvas')
        if new_target.lower().endswith('.md') and not has_ext:
            omit = True
        else:
            omit = False
        # if original was bare (no slash) and new relative would be bare in same folder, it's fine
        rel = rel_posix_from_to(new_parent if new_parent else '.', new_target, omit_ext=omit)
        # avoid leading ./ 
        if rel.startswith('./'):
            rel = rel[2:]
        rewritten += 1
        return f"[[{rel}{heading}{alias}]]"
    txt = link_pat.sub(repl, txt)
    if txt != orig_txt:
        p.write_text(txt, encoding='utf-8')

print(f"Rewrote {rewritten} wiki links; unresolved: {len(unresolved)}")
for u in unresolved[:20]:
    print("  UNRESOLVED:", u)

# ---------- canvas JSON ----------
for c in list(ROOT.rglob('*.canvas')):
    if '.git' in c.parts:
        continue
    try:
        data = json.loads(c.read_text(encoding='utf-8-sig'))
    except Exception as e:
        print(f"canvas parse error {c}: {e}")
        continue
    changed = False
    for n in data.get('nodes', []):
        f = n.get('file', '')
        if f in combined:
            n['file'] = combined[f]
            changed = True
        elif f in old_to_new:
            n['file'] = old_to_new[f]
            changed = True
    if changed:
        c.write_text(json.dumps(data, indent=2), encoding='utf-8')

print("Canvas paths updated.")

print("\nMigration applied.")
