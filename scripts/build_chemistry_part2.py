from pathlib import Path
import json, re, posixpath

ROOT=Path(__file__).resolve().parents[1]
BASE=ROOT/'Class 9'/'English Medium'/'Chemistry'
for folder in ('Chapters','Concepts','Definitions','Formulas','Exercises'):
    (BASE/folder).mkdir(parents=True,exist_ok=True)

chapters=[
('Chapter 05 - Chemical Kinetics','Chemical Kinetics','95-112','This unit first classifies chemical changes from evidence such as colour change, gas evolution, smell, precipitate and energy change. It distinguishes combination, decomposition, double decomposition (including precipitation, gas-forming and neutralisation examples) and displacement reactions. The rate of a chemical reaction is then explored through examples (explosion, rusting, weathering and dental filling) and experiments. Factors examined are nature of reactants, concentration, surface area, temperature and catalysts. Collision theory explains that effective collisions need sufficient threshold energy; higher concentration, greater exposed solid surface, higher temperature, or a suitable catalyst can increase reaction rate. The chapter connects catalysis to Haber and Contact processes, enzymes, hydrogen peroxide decomposition and applications in nature. Assessment and extended activities include gas-volume/time graphs and controlled experiments.'),
('Chapter 06 - Solutions','Solutions','113-132','A solution is a homogeneous mixture of solute and solvent; examples include liquid solutions, alloys and atmospheric air. The text uses “like dissolves like” to explain why polar/ionic solutes often dissolve in polar water while non-polar solvents behave differently, and illustrates salt hydration. Concentration is the amount of solute dissolved in a fixed amount of solvent; mass percentage is solute mass divided by solution mass times 100. Solutions are classified as unsaturated, saturated and supersaturated at a given temperature. Solubility is the grams of solute needed to saturate 100 g of solvent at a given temperature; graphs compare salts and show anomalous Glauber’s salt behaviour. Temperature, solvent/solute nature and pressure (for gases) affect solubility. It distinguishes true solutions, suspensions and colloids by particle visibility, settling, filtration and light scattering (Tyndall effect), and discusses colloid types, food stabilisers and preservatives.'),
('Chapter 07 - Non Metals','Non Metals','133-152','The chapter studies hydrogen, carbon, nitrogen, oxygen and chlorine through preparation, properties, reactions and uses. Hydrogen is prepared in the lab from zinc and dilute acid and industrially by water electrolysis; its combustion yields water and its high calorific value is balanced against storage and explosion limitations. Carbon allotropes include crystalline diamond, graphite, graphene and fullerene, and amorphous charcoal/coke/lampblack/coal; structures explain hardness, electrical conductivity and uses. Carbon dioxide preparation/identification and carbon monoxide toxicity are covered alongside carbonate tests. Nitrogen fixation, atmospheric reactions and fertilizers connect nitrogen to plant growth. Oxygen preparation and uses lead to ozone formation, UV absorption, ozone depletion and CFCs. Chlorine preparation, bleaching action requiring moisture, bleaching powder and chloride-ion identification are supported by apparatus diagrams and equations.'),
('Chapter 08 - Organic Chemistry','Organic Chemistry','153-174','Organic chemistry studies carbon compounds. The unit develops carbon’s valency and catenation through structural, condensed and molecular formulae. Hydrocarbons contain only carbon and hydrogen. Open-chain hydrocarbons are classified by bond type: alkanes (single bonds, saturated), alkenes (at least one double bond) and alkynes (at least one triple bond), each with general formulae and homologous-series patterns. IUPAC naming uses carbon-count word roots and suffixes -ane, -ene and -yne. Cyclic hydrocarbons are divided into alicyclic and aromatic; examples include cycloalkanes, benzene and naphthalene. The chapter surveys petroleum fractional distillation products and uses, coal formation/types and natural gas, then connects greenhouse gases and the greenhouse effect to global warming. Structural diagrams and ball-and-stick models support exercises on formulae, names, chain/ring isomers and fuels.'),
]
concepts={
'Reaction Types':('Chemical Kinetics','97-102','The unit groups reactions by observable transformation: combination forms one compound from simpler reactants; decomposition breaks a compound into two or more substances; double decomposition exchanges ions between two compounds; displacement occurs when an element in a compound is replaced by another element. Examples include CaO + H₂O, thermal decomposition, NaCl + AgNO₃ precipitation, acid-base neutralisation, and Zn + HCl. Equations and precipitate/gas illustrations distinguish the types.'),
'Factors Affecting Reaction Rate':('Chemical Kinetics','102-109','Rate depends on reactant nature, concentration, exposed surface area of solids, temperature and catalysts. The textbook’s experiments compare Cu/Zn/Mg with acid, concentrated/dilute acid, marble chips/powder, heating, and MnO₂-catalysed hydrogen peroxide. Increasing available particles or their effective collision frequency raises rate; temperature increases the fraction reaching threshold energy. A catalyst speeds the reaction without permanent chemical change to itself.'),
'Collision Theory and Threshold Energy':('Chemical Kinetics','103-108','The textbook explains reactions through collisions between reactant particles. Only effective collisions lead to products; particles need a sufficient excess amount of energy, called threshold energy. Higher particle concentration and temperature increase effective collisions and reaction rate. The model is used qualitatively to interpret the textbook’s demonstrations.'),
'Solution, Solute and Solvent':('Solutions','114-117','A solution is a homogeneous mixture with the same property throughout. The solute is the substance dissolved; the solvent is the substance that dissolves it. The state of a solution is usually the state of the solvent. Examples include salt water, brass (Zn in Cu), soda water, alcohol-water and atmospheric air. In an aqueous solution, water is treated as the solvent.'),
'Concentration and Mass Percentage':('Solutions','117-118','Concentration describes the amount of solute dissolved in a fixed amount of solvent. A dilute solution has relatively little solute; a concentrated one has more. The unit introduces mass percentage as grams of solute in 100 g of solution and shows an example with 10 g salt plus 90 g water. It also mentions ppm, volume percentage, molarity and molality without developing them here.'),
'Saturated, Unsaturated and Supersaturated Solutions':('Solutions','118-120','At a particular temperature, a saturated solution contains the maximum amount of solute that dissolves; an unsaturated solution contains less and can dissolve more. Heating can dissolve additional solute; cooling a carefully prepared supersaturated solution may cause excess solute to crystallise. The chapter uses ammonium chloride and seed crystals of copper sulphate/potassium nitrate to demonstrate these states and crystallisation.'),
'Solubility and Solubility Curves':('Solutions','121-122','Solubility is the mass in grams of solute required to saturate 100 g of a solvent at a given temperature. Curves compare salts such as KNO₃, NaCl and CaSO₄: solubility often increases with temperature, but each substance behaves differently. The book highlights Glauber’s salt as anomalous, with a maximum around 32.4°C, and notes gas solubility rises with pressure (carbon dioxide in soda water) while generally falling as temperature rises.'),
'True Solutions, Suspensions and Colloids':('Solutions','123-126','A true solution is homogeneous with very small particles that cannot be seen, filtered out or scatter a light beam. Suspension particles are larger, can settle, scatter light and can be filtered. Colloids are intermediate: particles do not settle readily and are not seen with the naked eye, but scatter light (Tyndall effect). The text gives approximate size bands and introduces dispersed phase/dispersion medium and colloid classes such as sol, gel, emulsion, foam and aerosols.'),
'Carbon Allotropes':('Non Metals','137-140','Allotropes are different forms of the same element with different physical properties. Carbon’s crystalline allotropes include diamond, graphite, graphene and fullerene; amorphous forms include charcoal, coke, lampblack and coal. Diamond’s four covalent bonds per atom explain hardness and lack of electrical conduction; graphite’s layered structure and free electrons explain lubrication and conductivity; graphene is a single graphite layer with high electrical/thermal conductivity; fullerenes include hollow buckyballs and nanotube-like buckytubes.'),
'Hydrogen, Oxygen and Chlorine':('Non Metals','134-150','The chapter pairs each gas with laboratory preparation, properties, reactions and uses. Hydrogen is formed by Zn + dilute HCl and burns with a pop; oxygen can be released by heating KMnO₄ or water electrolysis and supports combustion; chlorine is prepared using KMnO₄ and concentrated HCl, dried and collected after washing. Moist chlorine bleaches via hypochlorous acid/nascent oxygen; chlorine has water-treatment and disinfectant uses. The pages include apparatus drawings and identification tests.'),
'Nitrogen Cycle and Fertilizers':('Non Metals','143-145','Atmospheric nitrogen is relatively inert; lightning can form nitrogen oxides that lead to soil nitrates, and Rhizobium bacteria in legume roots fix nitrogen into usable compounds. Plants also receive nutrients from organic or chemical fertilizers. The table compares organic fertilizers (soil-friendly, slower nutrient release) and chemical fertilizers (quick N/P/K supply, but possible soil-structure, acidity and pollution impacts); the book recommends judicious scientific use.'),
'Ozone and Ozone Depletion':('Non Metals','146-147','Ozone (O₃) forms when ultraviolet radiation splits O₂ and oxygen atoms recombine with O₂. Ozone absorbs ultraviolet radiation and cycles back to oxygen. The textbook explains that CFC-derived chlorine disrupts this cycle and depletes the ozone layer; it names alternative refrigerant categories and references International Ozone Day.'),
'Hydrocarbon Families and Homologous Series':('Organic Chemistry','154-161','Hydrocarbons contain only carbon and hydrogen. Alkanes have only single C–C bonds and are saturated (general formula CₙH₂ₙ₊₂ for open chains); alkenes contain at least one double bond (CₙH₂ₙ); alkynes contain at least one triple bond (CₙH₂ₙ₋₂). Successive members of a homologous series differ by –CH₂–, share a general formula and similar chemical properties, and show gradual physical-property changes.'),
'Hydrocarbon Nomenclature and Cyclic Compounds':('Organic Chemistry','161-166','The unit builds IUPAC names from carbon-count roots meth-, eth-, prop-, but-, pent- and onward, plus -ane/-ene/-yne according to carbon-carbon bond type. Cyclic hydrocarbons include alicyclic rings (named with cyclo-) and aromatic compounds such as benzene and naphthalene. Structural diagrams teach students to infer molecular/condensed formulae and compare open-chain and ring structures.'),
'Fossil Fuels and Global Warming':('Organic Chemistry','167-170','Petroleum is a fossil-fuel hydrocarbon mixture separated by fractional distillation into gases, petrol, naphtha, kerosene, diesel, lubricating oil, fuel oil, wax and bitumen, each with uses. Coal forms by carbonisation of buried plant remains; natural gas is mainly methane. Combustion and other human activity increase greenhouse gases; these trap some outgoing infrared heat (greenhouse effect), contributing to global warming. The textbook presents a table/graph of gas contributions and asks students to consider consequences and remedies.'),
}
definitions={
'Combination Reaction':('Chemical Kinetics','98','A reaction in which two or more simple substances (elements or compounds) combine to form a compound.'),
'Decomposition Reaction':('Chemical Kinetics','99','The process by which a compound breaks down into two or more substances.'),
'Double Decomposition Reaction':('Chemical Kinetics','100','A reaction in which two compounds interchange their ions to form two new compounds.'),
'Displacement Reaction':('Chemical Kinetics','101','A reaction in which an element in a compound is displaced by another element.'),
'Catalyst':('Chemical Kinetics','108','A substance that increases the rate of a chemical reaction without itself undergoing permanent chemical change.'),
'Threshold Energy':('Chemical Kinetics','107','The minimum energy requirement described in the chapter for reactants to undergo effective collisions leading to products.'),
'Solute, Solvent and Solution':('Solutions','114','Solute is the substance dissolved; solvent is the substance in which it dissolves; the homogeneous mixture formed is a solution.'),
'Saturated Solution':('Solutions','118-119','A solution containing the maximum amount of solute that dissolves at a given temperature.'),
'Unsaturated Solution':('Solutions','119','A solution containing less solute than required to saturate it at a particular temperature.'),
'Supersaturated Solution':('Solutions','120','A solution containing more dissolved solute than is required to saturate it at a particular temperature.'),
'Solubility':('Solutions','121','The mass of solute in grams required to saturate 100 g of a solvent at a given temperature.'),
'Colloid and Tyndall Effect':('Solutions','125-126','A colloidal mixture lies between a true solution and suspension; its dispersed particles scatter a beam of light. This scattering is the Tyndall effect.'),
'Allotropy':('Non Metals','137','The phenomenon in which an element occurs in different forms that have different physical properties; the forms are allotropes.'),
'Calorific Value':('Non Metals','135','The heat energy released by complete combustion of a unit mass of fuel.'),
'Hydrocarbon':('Organic Chemistry','155','A compound containing only carbon and hydrogen.'),
'Alkane, Alkene and Alkyne':('Organic Chemistry','155-159','Open-chain hydrocarbons with only single carbon-carbon bonds are alkanes; those with at least one C=C bond are alkenes; those with at least one C≡C bond are alkynes.'),
'Homologous Series':('Organic Chemistry','160-161','A series of organic compounds represented by a general formula whose successive members differ by a –CH₂– group and show similar chemical properties.'),
'Catenation':('Organic Chemistry','166','The ability of atoms of an element to combine among themselves; the chapter identifies carbon’s high catenation as a reason for the large number of carbon compounds.'),
'Carbonisation':('Organic Chemistry','168','The process by which plant remains are converted into carbon at high temperature and pressure in the absence of air.'),
'Greenhouse Effect and Global Warming':('Organic Chemistry','169','The greenhouse effect is trapping and re-radiation of some outgoing infrared heat by atmospheric greenhouse gases. Global warming is the increase in average temperature of Earth and its atmosphere.'),
}
formulas={
'Mass Percentage of a Solution':('Solutions','117','Mass percentage = (mass of solute ÷ mass of solution) × 100. Mass of solution = mass of solute + mass of solvent.'),
'Hydrocarbon General Formulae':('Organic Chemistry','156-159','For the open-chain families taught here: alkane CₙH₂ₙ₊₂; alkene CₙH₂ₙ; alkyne CₙH₂ₙ₋₂. These relations are for the introductory families represented in the textbook.'),
'Representative Reaction Equations':('Chemical Kinetics','98-101','Examples shown in the chapter include combination: N₂ + 3H₂ → 2NH₃; decomposition: CaCO₃ → CaO + CO₂; double decomposition: NaCl + AgNO₃ → AgCl↓ + NaNO₃; displacement: Zn + 2HCl → ZnCl₂ + H₂.'),
}
exercises={
'Chemical Kinetics - Assessment and Activities':('Chemical Kinetics','110-112','Assessment classifies equations by reaction type and balances products, and asks how concentration, surface area, temperature and catalysts affect rate. Extended experiments measure hydrogen volume over time for magnesium with dilute/concentrated acid and varied temperature/surface area, and investigate potassium persulphate/iodide and hydrogen-iodine reactions. The map records tasks, not unprovided answer keys.'),
'Solutions - Assessment and Activities':('Solutions','130-132','Exercises cover solute/solvent, mass percentage, saturated/unsaturated conversion, reading solubility data and gas-solubility graphs, and classifying household mixtures as true solutions, suspensions or colloids. Extended work includes crystal growth and food safety/mixture investigations.'),
'Non Metals - Assessment and Activities':('Non Metals','150-152','Exercises identify gases from preparation/use clues, compare carbon allotropes, test chloride salts, explain hydrogen fuel and chlorine bleaching, and interpret carbon dioxide preparation/identification. Extended activities include a chlorine bleaching note, gas-use table and fertilizer-factory report.'),
'Organic Chemistry - Assessment and Activities':('Organic Chemistry','171-174','Assessment asks for structural/condensed/molecular formulae, family/general formula, naming, cyclic versus open-chain structures, petroleum separation and global warming. Extended tasks build ball-and-stick models, discuss climate change and organic chemistry, and construct six-carbon cyclic models. No textbook answer key is supplied in these notes.'),
}

def note(folder,name,kind,chapter,topic,pages,body,links=()):
    p=BASE/folder/(name+'.md'); rel=lambda x:f'[[{posixpath.relpath(x,folder)}]]'
    tags=['class/9','medium/english','subject/chemistry',f'type/{kind.lower()}']
    fm='---\nclass: 9\nmedium: English\nsubject: Chemistry\nchapter: "'+chapter+'"\ntopic: "'+topic+'"\ntype: '+kind.lower()+'\ntextbook: Chemistry Standard IX Part II\nprinted_pages: "'+pages+'"\ntags: ['+', '.join(tags)+']\n---\n'
    p.write_text(fm+f'# {name}\n\n{body}\n\n**Textbook reference:** Chemistry Standard IX Part II, printed pp. {pages}.\n\n## Related notes\n'+''.join('- '+rel(x)+'\n' for x in links),encoding='utf-8')
    return p

for i,(filename,title,pages,body) in enumerate(chapters,1):
    links=[f'Concepts/{n}' for n,v in concepts.items() if v[0]==title]
    links += [f'Definitions/{n}' for n,v in definitions.items() if v[0]==title]
    links += [f'Formulas/{n}' for n,v in formulas.items() if v[0]==title]
    links += [f'Exercises/{n}' for n,v in exercises.items() if v[0]==title]
    note('Chapters',filename,'chapter',title,title,pages,body,links)
for name,(chapter,pages,body) in concepts.items():
    links=[f'Chapters/{filename}' for filename,title,_,_ in chapters if title==chapter]
    note('Concepts',name,'concept',chapter,name,pages,body,links)
# Cross-unit links connect rate/energy, solutions, non-metal chemistry and fuels.
cross_links={
    'Reaction Types':['Factors Affecting Reaction Rate','Hydrocarbon Families and Homologous Series'],
    'Factors Affecting Reaction Rate':['Collision Theory and Threshold Energy','Reaction Types'],
    'Concentration and Mass Percentage':['Solubility and Solubility Curves'],
    'Saturated, Unsaturated and Supersaturated Solutions':['Solubility and Solubility Curves','True Solutions, Suspensions and Colloids'],
    'Carbon Allotropes':['Hydrocarbon Families and Homologous Series'],
    'Hydrogen, Oxygen and Chlorine':['Reaction Types','Fossil Fuels and Global Warming'],
    'Hydrocarbon Families and Homologous Series':['Hydrocarbon Nomenclature and Cyclic Compounds','Fossil Fuels and Global Warming'],
    'Fossil Fuels and Global Warming':['Hydrocarbon Families and Homologous Series','Hydrogen, Oxygen and Chlorine'],
}
for source,targets in cross_links.items():
    p=BASE/'Concepts'/(source+'.md'); raw=p.read_text(encoding='utf-8')
    for target in targets:
        entry=f'- [[{target}]]'
        if entry not in raw: raw=raw.rstrip()+f'\n{entry}\n'
    p.write_text(raw,encoding='utf-8')
for name,(chapter,pages,body) in definitions.items():
    note('Definitions',name,'definition',chapter,name,pages,body,[f'Chapters/{filename}' for filename,title,_,_ in chapters if title==chapter])
for name,(chapter,pages,body) in formulas.items():
    note('Formulas',name,'formula',chapter,name,pages,body,[f'Chapters/{filename}' for filename,title,_,_ in chapters if title==chapter])
for name,(chapter,pages,body) in exercises.items():
    note('Exercises',name,'exercise',chapter,name,pages,body,[f'Chapters/{filename}' for filename,title,_,_ in chapters if title==chapter])

overview='''---
class: 9
medium: English
subject: Chemistry
part: 2
edition: First Edition 2024
type: overview
tags: [class/9, medium/english, subject/chemistry, type/overview]
---
# Chemistry — Part II

**Kerala SCERT Standard IX, First Edition 2024.** This volume contains Chemical Kinetics (printed pp. 95–112), Solutions (113–132), Non Metals (133–152), and Organic Chemistry (153–174). The rendered pages were visually reviewed for reaction demonstrations, equipment, tables, graphs, allotrope and molecular diagrams, worked formula patterns, assessments and extended activities.

## Chapters
'''+''.join(f'- [[Chapters/{filename}|{title}]]\n' for filename,title,_,_ in chapters)+'''
## Colour legend
- Red `#FF6B6B`: important concepts
- Orange `#F4A261`: definitions
- Yellow `#E9C46A`: formulas and rules
- Green `#2A9D8F`: examples, assessments and activities
- Blue `#457B9D`: chapters and overview
- Purple `#9B5DE5`: cross-topic links

## Related links
- [[Subject Overview Part 1|Chemistry Part I]]
- [[Chemistry Part 2.canvas|Part II Canvas]]
'''
(BASE/'Subject Overview Part 2.md').write_text(overview,encoding='utf-8')
combined='''---
class: 9
medium: English
subject: Chemistry
type: overview
tags: [class/9, medium/english, subject/chemistry, type/overview]
---
# Chemistry — Class 9 English Medium

Both 2024 volumes have been visually reviewed page by page and mapped. [[Subject Overview Part 1|Part I]] covers Structure of Atom, Periodic Table, Chemical Bonding and Redox Reactions. [[Subject Overview Part 2|Part II]] covers Chemical Kinetics, Solutions, Non Metals and Organic Chemistry.
'''
(BASE/'Subject Overview.md').write_text(combined,encoding='utf-8')

notes=[BASE/'Subject Overview Part 2.md']+sorted(p for folder in ('Chapters','Concepts','Definitions','Formulas','Exercises') for p in (BASE/folder).glob('*.md') if 'Part II' in p.read_text(encoding='utf-8').split('---',2)[1])
nodes=[]; ids={}
for i,p in enumerate(notes):
    rel=p.relative_to(BASE).as_posix(); nid=f'n{i+1}'; ids[rel]=nid
    if p.name.startswith('Subject Overview'):
        x,y,w,h,color=-420,-150,360,140,'5'
    else:
        typ=p.parent.name; ix=sum(1 for n in nodes if n.get('file','').startswith(typ+'/'))
        col={'Chapters':0,'Concepts':1,'Definitions':2,'Formulas':3,'Exercises':4}.get(typ,1)
        x=col*380;y=ix*150;w=320;h=110;color={'Chapters':'5','Concepts':'1','Definitions':'2','Formulas':'3','Exercises':'4'}[typ]
    nodes.append({'id':nid,'type':'file','file':rel,'x':x,'y':y,'width':w,'height':h,'color':color})
edges=[]
for p in notes:
    src=p.relative_to(BASE).as_posix()
    for target in re.findall(r'\[\[([^\]|#]+)',p.read_text(encoding='utf-8')):
        target=target.strip()
        if target.startswith('../'): dest=posixpath.normpath(posixpath.join(posixpath.dirname(src),target+'.md'))
        elif target.endswith('.md'): dest=target
        elif target.startswith(('Chapters/','Concepts/','Definitions/','Formulas/','Exercises/')): dest=target+'.md'
        else: continue
        if dest in ids and ids[src]!=ids[dest]: edges.append({'fromNode':ids[src],'toNode':ids[dest],'fromSide':'right','toSide':'left','color':'6'})
uniq=[];seen=set()
for e in edges:
    k=(e['fromNode'],e['toNode'])
    if k not in seen: seen.add(k);e['id']=f'e{len(uniq)+1}';uniq.append(e)
(BASE/'Chemistry Part 2.canvas').write_text(json.dumps({'nodes':nodes,'edges':uniq},indent=2),encoding='utf-8')
print(f'Chemistry Part II notes: {len(notes)} including overview; canvas nodes {len(nodes)}, edges {len(uniq)}')
