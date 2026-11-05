from pathlib import Path
import json, posixpath

ROOT=Path(__file__).resolve().parents[1]
BASE=ROOT/'Class 9'/'English Medium'
BOOKS=[
 {'folder':'Social Science I','part':'Part 1','file':'Social Science 1 Part 1.pdf','title':'Social Science I — Part I','chapters':[
 ('Moving Forward from the Stone Age','7–24','Traces human development through the Palaeolithic, Mesolithic and Neolithic periods and the Metal Ages. Stone tools, cave art, control of fire, settlement, farming and animal domestication mark changing ways of life. The chapter relates archaeological evidence to early civilizations, including Harappan urban life and the Vedic period.'),
 ('Ideas and Early States','25–44','Explores social and economic change alongside new religious ideas, including Buddhism and Jainism, and the teachings of Gautama Buddha and Vardhamana Mahavira. It traces the rise of Magadha and the Mahajanapadas, Mauryan rule under Chandragupta and Ashoka, administration and land grants, and compares political institutions such as Greek democracy.'),
 ('Land Grants and Indian Society','45–62','Examines land grants and agrarian expansion and their effects on social hierarchy, crafts and trade. The Gupta period is considered through social life, regional change, temple building, art and scientific achievements. Read the chapter’s illustrations and evidence as examples of how political economy and culture changed together.'),
 ('Distribution of Power in Indian Constitution','63–82','Introduces the Constitution and its making, including the Objective Resolution. It explains Indian federalism, the Union, State and Concurrent division of responsibilities, and separation of powers among legislature, executive and judiciary. Parliament, checks and balances and constitutional amendment show how authority is distributed and constrained.'),
 ('Demographic Trends in India','83–100','Uses population data and census concepts to study change. Indicators include birth and death rates, migration, population density, sex and child sex ratios, life expectancy and age structure. The chapter connects demographic dividend and population policy with planning, while tables and diagrams support comparison and interpretation.') ]},
 {'folder':'Social Science I','part':'Part 2','file':'Social Science 1 Part 2.pdf','title':'Social Science I — Part II','chapters':[
 ('From Land of Cholas to Delhi','111–128','Surveys political and cultural developments from the Cholas and Chalukyas through regional powers such as the Palas, Pratiharas and Rashtrakutas, the Arab entry into Sindh, and the Delhi Sultanate. The material relates governance and political change to social, economic and cultural life.'),
 ('Extension of Democracy through Institutions','129–150','Explains institutions that protect and extend democratic participation: election administration, adult franchise, representation and commissions addressing human, women’s, minority, Scheduled Caste and Tribe, backward-class and child rights. Activities invite learners to consider how independent bodies make rights actionable.'),
 ('Towards a Gender-Neutral Society','151–166','Distinguishes sex from socially formed gender roles and examines socialisation, stereotypes and inequality. It considers gender-sensitive language, constitutional rights and legal protections, and asks learners to identify practices that support equality in everyday life.') ]},
 {'folder':'Social Science II','part':'Part 1','file':'Social Science 2 Part 1.pdf','title':'Social Science II — Part I','chapters':[
 ('On the Roof of the World','7–27','Studies the Himalaya as a young mountain system shaped by tectonic movement. Maps and diagrams locate its ranges and rivers; text connects relief with climate, vegetation, soils, farming, tourism and protected areas. The chapter relates physical geography to settlement and livelihood.'),
 ('In the Expansive Plain','28–52','Explains formation of the Indo-Gangetic-Brahmaputra plain and its regional divisions, including Rajasthan, Punjab-Haryana, Ganga and Brahmaputra sections. River systems, monsoon climate, alluvial soils, vegetation, agriculture and livelihoods are interpreted through maps and regional comparisons.'),
 ('Plateau where the Earth’s History Slumbers','53–76','Maps the Peninsular Plateau, including the Deccan and central/eastern highlands. It relates older geological structure to rivers, minerals, soils and vegetation, then examines farming and crops such as cotton, coffee, tea and sugarcane alongside population and urbanisation.'),
 ('Human Resources for National Development','77–93','Treats people and skills as resources in production and development. It introduces factors of production, productivity, barter and money/banking, then connects education, health, migration, vocational training and information access with human capital. Poverty and unemployment are considered as barriers to development.') ]},
 {'folder':'Social Science II','part':'Part 2','file':'Social Science 2 Part 2.pdf','title':'Social Science II — Part II','chapters':[
 ('Indian Economy Through Various Sectors','103–122','Explains primary, secondary and tertiary sectors and their interdependence. National income measures, including product, income and expenditure approaches, per-capita income, GDP/GNP and value added, are supported by tables and graphs. Activities compare sectoral contributions, employment and organised/unorganised work.'),
 ('Price and Market','123–142','Introduces production, inputs, consumption and markets. Demand and supply schedules and curves show how quantity responds to price; their interaction establishes equilibrium. The chapter also addresses marketing, price control/support, digital marketing and sustainable production/consumption through diagrams, examples and data tasks.'),
 ('Through the Sandy Expanse','143–162','Examines the Thar Desert’s extent, boundaries, relief, dunes and other landforms, climate, scarce rainfall, soils and vegetation. Maps and photographs support study of adaptation and livelihoods in agriculture, pastoralism, mining, handicrafts, energy and tourism, including water management and development challenges.'),
 ('Along the Coasts','163–182','Compares India’s western and eastern coastal plains, regional divisions, islands, beaches, estuaries, lagoons and coastal landforms shaped by waves and tides. Maps and diagrams connect climate, soils, vegetation, resources and livelihoods with population, economic activity and hazards affecting coastal communities.') ]}
]

def slug(s): return ''.join(c if c.isalnum() or c in ' -' else '' for c in s).strip().replace(' ','-')
def main():
 for b in BOOKS:
  base=BASE/b['folder']; (base/'Chapters').mkdir(parents=True,exist_ok=True); (base/'Concepts').mkdir(parents=True,exist_ok=True); (base/'Exercises').mkdir(parents=True,exist_ok=True)
  overview_name=f"Subject Overview {b['part']}.md"
  meta=f"---\nclass: 9\nmedium: English\nsubject: {b['folder']}\npart: {b['part']}\ntype: overview\ntags: [class/9, medium/english, subject/{b['folder'].lower().replace(' ','-')}, type/overview]\n---\n"
  lines=[meta+f"# {b['title']}\n\nSource: [[../_Source PDFs/{b['file']}]]. The complete {b['file']} ({'104' if b['file']=='Social Science 1 Part 1.pdf' else '64' if b['file']=='Social Science 1 Part 2.pdf' else '96' if b['file']=='Social Science 2 Part 1.pdf' else '88'} PDF pages) was visually reviewed page by page, including maps, diagrams, tables, photographs, activities, exercises and closing inserts.\n\n## Chapters\n"]
  nodes=[(overview_name,5)]; chapters=[]
  for i,(title,pages,body) in enumerate(b['chapters'],1):
   name=f"Chapter {i:02d} - {slug(title)}"; path=base/'Chapters'/(name+'.md')
   tags=b['folder'].lower().replace(' ','-')
   content=f"---\nclass: 9\nmedium: English\nsubject: {b['folder']}\npart: {b['part']}\nchapter: {i}\ntopic: \"{title}\"\ntype: chapter\nprinted_pages: \"{pages}\"\ntags: [class/9, medium/english, subject/{tags}, type/chapter]\n---\n# {title}\n\n{body}\n\n**Textbook reference:** {b['title']}, printed pp. {pages}.\n\n## Related notes\n- [[../{overview_name[:-3]}]]\n"
   if not path.exists(): path.write_text(content,encoding='utf-8')
   chapters.append((name,title,pages)); nodes.append(('Chapters/'+name+'.md',5)); lines.append(f"- [[Chapters/{name}|{title}]] — printed pp. {pages}\n")
   ename=f"{i:02d} - {slug(title)} Activities"; ep=base/'Exercises'/(ename+'.md')
   ebody=f"---\nclass: 9\nmedium: English\nsubject: {b['folder']}\npart: {b['part']}\nchapter: {i}\ntopic: \"Activities — {title}\"\ntype: exercise\nprinted_pages: \"{pages}\"\ntags: [class/9, medium/english, subject/{tags}, type/exercise]\n---\n# Activities — {title}\n\nUse the chapter’s map, data display, source, diagram or case study as evidence. Summarise the key relationship in your own words, compare examples, and answer the printed review and extended-activity questions from the book. For data-based tasks, state the evidence and explain the conclusion rather than copying a chart.\n\n**Textbook reference:** {b['title']}, printed pp. {pages}.\n\n## Related notes\n- [[../Chapters/{name}|{title}]]\n"
   if not ep.exists(): ep.write_text(ebody,encoding='utf-8')
   nodes.append(('Exercises/'+ename+'.md',4))
  lines.append("\n## Canvas colour legend\nRed `#FF6B6B` key concepts · Orange `#F4A261` definitions · Yellow `#E9C46A` data/relationships · Green `#2A9D8F` activities · Blue `#457B9D` chapters · Purple `#9B5DE5` cross-topic connections.\n\nOpen [["+b['title']+".canvas]].\n")
  op=base/overview_name
  if not op.exists(): op.write_text('\n'.join(lines),encoding='utf-8')
  # Book map: overview -> chapters -> activity files; adjacent chapters linked to encourage coherent reading.
  cn=[]; overview=nodes[0][0]
  for j,(file,color) in enumerate(nodes): cn.append({'id':f'n{j+1}','type':'file','file':file,'x':0 if j==0 else (j-1)%2*560,'y':0 if j==0 else ((j-1)//2)*300+200,'width':420,'height':160,'color':str(color)})
  edges=[];eid=1
  for i in range(1,len(b['chapters'])+1):
   edges.append({'id':f'e{eid}','fromNode':'n1','fromSide':'bottom','toNode':f'n{i+1}','toSide':'top','color':'5'}); eid+=1
   exnode=f'n{1+len(b["chapters"])+i}'
   edges.append({'id':f'e{eid}','fromNode':f'n{i+1}','fromSide':'right','toNode':exnode,'toSide':'left','color':'4'});eid+=1
   if i>1: edges.append({'id':f'e{eid}','fromNode':f'n{i}','fromSide':'bottom','toNode':f'n{i+1}','toSide':'top','color':'6'});eid+=1
  canvas={'nodes':cn,'edges':edges}; cp=base/(b['title']+'.canvas')
  if not cp.exists(): cp.write_text(json.dumps(canvas,indent=2),encoding='utf-8')
 print('Social Science chapter and activity notes/maps generated without replacing existing files.')

if __name__=='__main__':main()
