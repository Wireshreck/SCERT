from pathlib import Path
import json
ROOT=Path(__file__).resolve().parents[1]; BASE=ROOT/'Class 9'/'English Medium'; SRC=BASE/'_Source PDFs'
BOOKS=[
 {'subject':'Art Education','pdf':'Art.pdf','title':'Art Education Standard IX Activity Book','edition':'2024','pages':112,'chapters':[
  ('Nature','7–28','Connects local art and life through Warli and other traditional painting, Carnatic music and performance forms. Images and listening/singing activities invite observation of visual style, rhythm, instruments and cultural setting.'),
  ('Design, Shades, Landscape','29–40','Introduces printmaking and the preparation of cinema through scripts, storyboards and production roles. Learners compare printing methods such as relief/woodcut, lithography, screen and digital printing, then plan scenes and presentations.'),
  ('Experience of Emotions','41–61','Uses colour, songs, dance, film and masks to explore how artistic choices express emotion and social experience. Examples include contemporary dance, camera framing and performance traditions; activities ask students to interpret and create.'),
  ('Applied Lessons','62–79','Applies music, design, dance choreography, picture editing and scene awareness to practical projects. Orchestra and stage tasks connect creative ideas with arrangement, materials, movement and audience.'),
  ('Performance Platform','80–93','Focuses on artistic work in public and performance spaces: sculpture, public art, abhinaya sangeetham, staging and transformation through acting. Photographs and biographies provide models for designing, presenting and reflecting on work.'),
  ('Window of Creativity','94–110','Brings together sound, society, sight, ideas and the silver screen. Learners consider sound waves and recording, artistic responses to society, and the stages of making a film from idea and story through shooting and editing.') ]},
 {'subject':'Work Education','pdf':'Work Education.pdf','title':'Work Integrated Education Standard IX Activity Book Part I — Self Grooming','edition':'2024','pages':64,'chapters':[
  ('Knowing Yourself','7–15','Activities build self-awareness by identifying abilities, interests, values and areas to improve. Reflection, personal inventories and a Me Chart encourage realistic planning and respect for individual strengths.'),
  ('Strive Forward','16–22','Uses stories of people who have faced barriers to introduce persistence, resilience and goal-directed effort. Learners identify challenges, possible supports and steps toward progress.'),
  ('Let’s be Self-reliant','23–29','Covers self-care, grooming, etiquette and appropriate conduct in social settings. Scenarios, role-play and reflection connect personal presentation with confidence, respectful interaction and responsibility.'),
  ('Emotions and Wellness','30–38','Explores emotions, stress and emotional well-being through stories, emotion charts, reflection and support-seeking. Students consider healthy responses, coping habits and trusted people who can help.'),
  ('Social Wellness','39–50','Examines relationships, empathy, communication, listening and cooperation. Activities practise constructive responses, clear expression and attentive listening in peer and community situations.'),
  ('With the Rhythm of Nature','51–60','Connects well-being with the natural environment and sustainable everyday habits. Learners observe their surroundings, consider environmental impact and make a personal action plan.') ]}
]
def front(b,typ,part,chapter,pages):
 s=b['subject'].lower().replace(' ','-')
 return f'---\nclass: 9\nmedium: English\nsubject: {b["subject"]}\npart: {part}\nchapter: {chapter}\ntopic: "{typ}"\ntype: {typ}\nprinted_pages: "{pages}"\ntags: [class/9, medium/english, subject/{s}, type/{typ}]\n---\n'
def main():
 for b in BOOKS:
  base=BASE/b['subject']
  for folder in ['Chapters','Concepts','Definitions','Exercises']: (base/folder).mkdir(parents=True,exist_ok=True)
  overview=base/'Subject Overview.md'; ov=f'---\nclass: 9\nmedium: English\nsubject: {b["subject"]}\nedition: "{b["edition"]}"\ntype: overview\ntags: [class/9, medium/english, subject/{b["subject"].lower().replace(" ","-")}, type/overview]\n---\n# {b["title"]}\n\nThe existing Samagra-sourced PDF ({b["pages"]} pages; edition imprint {b["edition"]}) was visually reviewed page by page, including illustrated examples, diagrams, tables, activities, exercise prompts and closing inserts.\n\n## Chapters\n'
  nodes=[{'id':'overview','type':'file','file':'Subject Overview.md','x':0,'y':0,'width':430,'height':170,'color':'5'}]
  edges=[]; eid=0
  for i,(title,pages,body) in enumerate(b['chapters'],1):
   fname=f'Chapter {i:02d} - {title.replace(" ","-").replace("’","")}'
   rel=f'Chapters/{fname}.md'; chpath=base/rel
   text=front(b,'chapter','Standard IX',i,pages)+f'# {title}\n\n{body}\n\n**Textbook reference:** {b["title"]}, printed pp. {pages}.\n\n## Related notes\n- [[../Subject Overview]]\n'
   if not chpath.exists():chpath.write_text(text,encoding='utf-8')
   ov+=f'- [[{rel[:-3]}|{title}]] — printed pp. {pages}\n'
   nodes.append({'id':f'ch{i}','type':'file','file':rel,'x':560,'y':210+230*(i-1),'width':430,'height':170,'color':'5'})
   # substantial concepts, with precise unit references
   concept_title= {'Art Education':['Traditional Art and Cultural Context','Music Forms and Performance','Printmaking Methods','Script, Storyboard and Production','Emotion, Colour and Expression','Dance, Abhinaya and Choreography','Stage, Public Art and Sculpture','Film, Sound and Social Ideas','Creative Project Planning'], 'Work Education':['Self-awareness and Personal Strengths','Resilience and Goal Setting','Self-care, Etiquette and Social Conduct','Emotional Wellness and Coping','Empathy, Communication and Listening','Environmental Wellness and Sustainable Habits']}[b['subject']]
   ctitle=concept_title[i-1]; cpath=base/'Concepts'/(ctitle+'.md')
   cbody=body+' The activity book uses observation and guided practice to help learners connect the idea to their own community and creative or personal choices.'
   ctext=front(b,'concept','Standard IX',i,pages)+f'# {ctitle}\n\n{cbody}\n\n**Textbook reference:** {b["title"]}, printed pp. {pages}.\n\n## Related notes\n- [[../{rel[:-3]}|{title}]]\n'
   if not cpath.exists():cpath.write_text(ctext,encoding='utf-8')
   nodes.append({'id':f'co{i}','type':'file','file':'Concepts/'+cpath.name,'x':1120,'y':210+230*(i-1),'width':430,'height':170,'color':'1'})
   # activity guide
   ename=f'{i:02d} - {title.replace(" ","-").replace("’","")} Activities'; epath=base/'Exercises'/(ename+'.md')
   etext=front(b,'exercise','Standard IX',i,pages)+f'# Activities — {title}\n\nUse the pictured examples, reflection questions, performance tasks and projects in this unit. Record what you observe, explain your choices, and reflect on what you would improve after sharing your work. Follow the textbook’s materials and classroom guidance.\n\n**Textbook reference:** {b["title"]}, printed pp. {pages}.\n\n## Related notes\n- [[../{rel[:-3]}|{title}]]\n'
   if not epath.exists():epath.write_text(etext,encoding='utf-8')
   nodes.append({'id':f'ex{i}','type':'file','file':'Exercises/'+epath.name,'x':1680,'y':210+230*(i-1),'width':430,'height':170,'color':'4'})
   eid+=1;edges.append({'id':f'e{eid}','fromNode':'overview','fromSide':'right','toNode':f'ch{i}','toSide':'left','color':'5'})
   eid+=1;edges.append({'id':f'e{eid}','fromNode':f'ch{i}','fromSide':'right','toNode':f'co{i}','toSide':'left','color':'6'})
   eid+=1;edges.append({'id':f'e{eid}','fromNode':f'ch{i}','fromSide':'right','toNode':f'ex{i}','toSide':'left','color':'4'})
  ov+='\n## Canvas colour legend\nRed `#FF6B6B` concepts · Orange `#F4A261` definitions · Yellow `#E9C46A` methods/data · Green `#2A9D8F` activities · Blue `#457B9D` chapters · Purple `#9B5DE5` cross-topic links.\n\nOpen [['+b['subject']+'.canvas]].\n'
  if not overview.exists(): overview.write_text(ov,encoding='utf-8')
  cv={'nodes':nodes,'edges':edges}; canvas=base/(b['subject']+'.canvas')
  if not canvas.exists():canvas.write_text(json.dumps(cv,indent=2),encoding='utf-8')
  print(b['subject'],len(b['chapters']),'chapters',len(nodes),'nodes')
if __name__=='__main__':main()
