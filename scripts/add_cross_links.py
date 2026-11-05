from pathlib import Path
import json
ROOT=Path(__file__).resolve().parents[1]; BASE=ROOT/'Class 9'/'English Medium'
SOCIAL={
'Social Science I':{'Social Science I — Part I':[(1,2),(2,3),(3,5),(4,5)],'Social Science I — Part II':[(1,2),(2,3)]},
'Social Science II':{'Social Science II — Part I':[(1,2),(2,3),(2,4),(3,4)],'Social Science II — Part II':[(1,2),(1,4),(3,4)]}}
ACTIVITY={
'Art Education':[(1,2),(1,4),(2,6),(3,5),(4,5),(5,6)],
'Work Education':[(1,2),(1,3),(3,4),(4,5),(5,6)]}
def add_note_link(src,dst):
 rel=dst.with_suffix('').name; txt=src.read_text(encoding='utf-8-sig'); link=f'- [[{rel}]]'
 if link not in txt: src.write_text(txt.rstrip()+'\n'+link+'\n',encoding='utf-8')
def add_edge(canvas,a,b,prefix='ch',offset=0):
 cv=json.loads(canvas.read_text(encoding='utf-8')); pair=(f'{prefix}{a+offset}',f'{prefix}{b+offset}')
 if not any((e.get('fromNode'),e.get('toNode'))==pair for e in cv['edges']):
  cv['edges'].append({'id':f'cross{len(cv["edges"])+1}','fromNode':pair[0],'fromSide':'bottom','toNode':pair[1],'toSide':'top','color':'6'})
 canvas.write_text(json.dumps(cv,indent=2),encoding='utf-8')
for subject,books in SOCIAL.items():
 for book,links in books.items():
  folder=BASE/subject; chapters=sorted((folder/'Chapters').glob('Chapter *.md'),key=lambda p:(int(p.name[8:10]),p.name))
  # Keep Part I and Part II chapters in their printed textbook order.
  part='Part 1' if book.endswith('Part I') else 'Part 2'
  over=folder/f'Subject Overview {part}.md'; text=over.read_text(encoding='utf-8-sig'); import re
  m=re.search(r'^part: (.+)$',text,re.M); part_value=m.group(1) if m else ''
  subset=[]
  for p in chapters:
   if re.search(r'^part: '+re.escape(part_value)+r'$',p.read_text(encoding='utf-8-sig'),re.M):subset.append(p)
  for a,b in links: add_note_link(subset[a-1],subset[b-1])
  cv=folder/(book+'.canvas')
  for a,b in links:add_edge(cv,a,b,'n',1)
for subject,links in ACTIVITY.items():
 folder=BASE/subject; chapters=sorted((folder/'Chapters').glob('Chapter *.md'))
 for a,b in links:add_note_link(chapters[a-1],chapters[b-1])
 cv=folder/(subject+'.canvas')
 for a,b in links:add_edge(cv,a,b)
print('Added durable cross-chapter wiki links and Canvas edges.')
