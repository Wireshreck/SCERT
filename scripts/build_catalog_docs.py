import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; BASE=ROOT/'Class 9'/'English Medium'
rows=json.loads((BASE/'SOURCE_CATALOG.json').read_text(encoding='utf-8'))
current=[r for r in rows if r.get('processed')=='yes']; legacy=[r for r in rows if r.get('processed')!='yes']
pages=sum(r['pages'] for r in rows); lines=['# Class 9 English Medium — Samagra Edition Audit','',f'The current collection contains {len(rows)} source PDFs across {pages:,} PDF pages: {len(current)} current textbooks/activity books and {len(legacy)} preserved legacy source. Every current PDF opens and its class/edition was identified from the cover/imprint. Files initially present from earlier work were preserved; official verification copies came only from the user-authorized Samagra KITE portal.','', '| Local source file | Official title | Pages | Edition | Official Samagra PDF | SHA-256 |','|---|---|---:|---|---|---|']
for r in rows:
 if r.get('processed')=='yes':
  lines.append(f"| `{r['file']}` | {r['official_title']} | {r['pages']} | {r['edition_year']} | [Samagra]({r['samagra_portal_pdf_url']}) | `{r.get('official_download_sha256','')}` |")
 else: lines.append(f"| `{r['file']}` | {r['official_title']} | {r['pages']} | {r['edition_year']} | [Legacy Samagra link]({r.get('official_pdf_url','')}) | local `{r.get('local_sha256','')}`; not current |")
lines+=['','## Verification method','','Current Samagra PDFs were selected from the Class 9 English-medium portal and verified against the preserved local files. SHA-256 comparison matched for Biology, Chemistry, English, ICT 2025, Mathematics, Physical Education, Physics, and both Social Science subjects. Art Education and Work Integrated Education were downloaded directly from their visible Samagra links. Covers show 2024 for the revised textbooks/activity books and 2025 for ICT. The ICT Part I 2019 file remains as a separate legacy source; the current curriculum uses the 2025 Part I PDF.','',f'Official catalogue: https://samagra.kite.kerala.gov.in/#/textbook/page','']
(BASE/'EDITION_AUDIT.md').write_text('\n'.join(lines),encoding='utf-8')
scope='''# Samagra Class 9 English-medium catalogue scope

## Core collection processed

The Samagra portal's Standard 9 / English medium filter provides the common academic textbooks and activity books: English, Biology, Chemistry, ICT, Mathematics, Physical Education, Physics, Social Science I, Social Science II, Art Education and Work Integrated Education. All available parts of these current titles are in [[SOURCE_CATALOG]] and are read, mapped and validated in this vault.

## Choice-based language offerings

The same selector also lists language and elective entries (for example Arabic academic/oriental, Hindi, Kannada AT/BT, Malayalam AT/BT, Sanskrit academic/oriental and Tamil AT/BT, plus optional/second-language labels). These are alternatives selected according to a learner's language course; processing all of them as one student's English-medium core curriculum would combine mutually selectable courses. The selector exposes no current download for several optional labels. They are therefore recorded as catalogue choices, not counted as missing required textbooks. No Malayalam-medium core textbooks were added.

The current 11-subject common collection is the completion scope for this Class 9 English-medium vault. This scope note preserves the distinction between required/common texts and portal language choices.
'''.replace('+','')
(BASE/'CATALOG_SCOPE.md').write_text(scope,encoding='utf-8')
print('Edition audit and portal scope note written.')
