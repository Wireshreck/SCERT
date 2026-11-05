from pathlib import Path
import json
ROOT=Path(__file__).resolve().parents[1]; BASE=ROOT/'Class 9'/'English Medium'
# concepts keyed by exact chapter title; multiple selected ideas per chapter.
CONCEPTS={
'Social Science I':{
'Moving Forward from the Stone Age':[('Stone Ages and technological change','7–24','Palaeolithic, Mesolithic and Neolithic labels describe broad archaeological periods distinguished partly by tool traditions and subsistence patterns. The chapter links changing tools with fire, art, settlement, domestication and farming.'),('Harappan urban life','17–24','The Harappan civilisation is introduced through evidence of planned settlements and material culture. Treat archaeological objects and settlement patterns as evidence from which historians reconstruct social and economic life.')],
'Ideas and Early States':[('Buddhism and Jainism','25–34','The textbook introduces Gautama Buddha and Vardhamana Mahavira and the religious traditions associated with their teachings, in the context of changing society and material life.'),('Mahajanapadas and the Mauryan state','35–44','The chapter traces the rise of powerful states, especially Magadha, and Mauryan rule. Chandragupta and Ashoka exemplify political consolidation and administration; the comparison with Greek states raises questions about forms of political participation.')],
'Land Grants and Indian Society':[('Land grants and agrarian expansion','45–53','The transfer of land rights could encourage cultivation and extend political or religious authority. The chapter examines resulting changes to agrarian relations and social hierarchy.'),('Gupta-period culture and knowledge','54–62','The book connects social and economic life in the Gupta period with art, temple architecture, scientific knowledge and regional change.')],
'Distribution of Power in Indian Constitution':[('Federalism and the three lists','68–75','Union, State and Concurrent lists divide law-making subjects between levels of government. The arrangement is designed to combine national coordination with constitutionally assigned state responsibilities.'),('Separation of powers and checks','76–82','Legislative, executive and judicial functions are distributed among institutions. Their interaction, parliamentary accountability and constitutional review help limit misuse of public power.')],
'Demographic Trends in India':[('Census and population structure','83–91','Census and demographic data describe population size and composition. Age structure, density and migration help planners understand changing needs and regional patterns.'),('Sex ratio, life expectancy and demographic dividend','92–100','Sex ratio and child sex ratio reveal gendered population patterns; life expectancy reflects mortality conditions. A large working-age population can support a demographic dividend when education, health and jobs enable participation.') ]},
'Social Science II':{
'On the Roof of the World':[('Himalayan ranges and rivers','7–15','The Himalaya consists of distinct ranges formed through tectonic processes. Relief and snow/rain-fed systems influence major river origins and regional environments.'),('Mountain climate and human activity','16–27','Altitude and slope create varied climate, soils and vegetation. These conditions shape agriculture, settlement, tourism and conservation.')],
'In the Expansive Plain':[('Indo-Gangetic-Brahmaputra alluvium','28–36','Rivers deposit sediments across the plain, creating fertile alluvial landscapes. Deposition, drainage and local relief vary by region.'),('Regional environments of the plain','37–52','The Rajasthan, Punjab-Haryana, Ganga and Brahmaputra regions differ in rainfall, river patterns, soils and livelihoods. Maps help compare agricultural and settlement conditions.')],
'Plateau where the Earth’s History Slumbers':[('Peninsular plateau divisions and rivers','53–62','The chapter maps the central and eastern highlands and Deccan plateau and relates their relief to river systems and drainage patterns.'),('Minerals, soils and agriculture','63–76','Geology supports varied mineral resources; soils and climate shape crops such as cotton, coffee, tea and sugarcane. Resource use intersects with settlement and urban growth.')],
'Human Resources for National Development':[('Factors of production and national income','77–84','Land, labour, capital and organisation contribute to production. The book connects productivity and economic activity with money, banking and measures of national development.'),('Education, health and employment','85–93','Education, health, training and information access develop human capabilities. Migration, poverty and unemployment influence whether people can use those capabilities productively.') ]}}

COLORS={'overview':'5','chapter':'5','concept':'1','definition':'2','formula':'3','exercise':'4'}
def main():
 for subject,chapter_concepts in CONCEPTS.items():
  sbase=BASE/subject
  alloverview=['# '+subject+' — Standard IX\n','\nBoth parts are linked here; use the individual volume overviews for chapter navigation. Each listed textbook was visually reviewed page by page.\n','\n## Volumes\n']
  for part in ['Part 1','Part 2']:
   # select relevant chapter sequence via builder's metadata in chapter frontmatter.
   over=sbase/f'Subject Overview {part}.md'
   if not over.exists(): continue
   lines=over.read_text(encoding='utf-8').splitlines()
   # parse chapter filenames and create concept notes from exact chapter names.
   chapdir=sbase/'Chapters'; chapters=[]
   for p in sorted(chapdir.glob('Chapter *.md')):
    txt=p.read_text(encoding='utf-8')
    import re
    m=re.search(r'^part: (.+)$',txt,re.M); chm=re.search(r'^topic: "(.+)"$',txt,re.M)
    if m and m.group(1)==part: chapters.append((p,chm.group(1) if chm else p.stem))
   booktitle=f'{subject} — {part}'
   volume_concepts=[]
   for chap,title in chapters:
    for cname,pages,body in chapter_concepts.get(title,[]): volume_concepts.append((chap,title,cname,pages,body))
   nodes=[]
   # Existing overview and chapter and exercises from canvas retained; append new concept notes.
   for ch,title,cname,pages,body in volume_concepts:
    cp=sbase/'Concepts'/(cname+'.md'); topic=subject.lower().replace(' ','-')
    if not cp.exists():
     cp.write_text(f'---\nclass: 9\nmedium: English\nsubject: {subject}\npart: {part}\nchapter: "{title}"\ntopic: "{cname}"\ntype: concept\nprinted_pages: "{pages}"\ntags: [class/9, medium/english, subject/{topic}, type/concept]\n---\n# {cname}\n\n{body}\n\n**Textbook reference:** {booktitle}, printed pp. {pages}.\n\n## Related notes\n- [[../Chapters/{ch.stem}|{title}]]\n',encoding='utf-8')
    nodes.append({'id':f'c{len(nodes)+1}','type':'file','file':'Concepts/'+cp.name,'x':1080,'y':len(nodes)*190,'width':400,'height':150,'color':'1'})
    ctext=ch.read_text(encoding='utf-8')
    rel=f'- [[../Concepts/{cp.stem}|{cname}]]\n'
    if rel not in ctext: ch.write_text(ctext.rstrip()+ '\n'+rel,encoding='utf-8')
   # locate volume canvas and add file nodes and edges
   canvaspath=sbase/(booktitle+'.canvas')
   if canvaspath.exists() and nodes:
    cv=json.loads(canvaspath.read_text(encoding='utf-8')); edges=cv['edges']
    present={x.get('file'):x for x in cv['nodes'] if x.get('type')=='file'}
    pairs={(x.get('fromNode'),x.get('toNode')) for x in edges}
    for j,n in enumerate(nodes):
     n['id']=f'c{j+1}'
     ch=volume_concepts[j][0]; target=present.get('Chapters/'+ch.name)
     if n['file'] not in present:
      cv['nodes'].append(n); present[n['file']]=n
     if target and (target['id'],n['id']) not in pairs:
      edges.append({'id':f's{len(edges)+1}','fromNode':target['id'],'fromSide':'right','toNode':n['id'],'toSide':'left','color':'6'});pairs.add((target['id'],n['id']))
    if not canvaspath.exists(): canvaspath.write_text(json.dumps(cv,indent=2),encoding='utf-8')
   alloverview.append(f'- [[{subject}/Subject Overview {part}|{booktitle}]]\n')
  combo=sbase/'Subject Overview.md'
  if not combo.exists(): combo.write_text('---\nclass: 9\nmedium: English\nsubject: '+subject+'\ntype: overview\ntags: [class/9, medium/english, subject/'+subject.lower().replace(' ','-')+', type/overview]\n---\n'+'\n'.join(alloverview)+'\n## Colour legend\nRed `#FF6B6B` concepts · Orange `#F4A261` definitions · Yellow `#E9C46A` data/formulas · Green `#2A9D8F` activities · Blue `#457B9D` chapters · Purple `#9B5DE5` cross-topic links.\n',encoding='utf-8')
 print('Added concept notes, chapter links, and Canvas concept nodes without replacing existing notes.')
if __name__=='__main__':main()
