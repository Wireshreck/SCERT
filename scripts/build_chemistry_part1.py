from pathlib import Path, PurePosixPath
import posixpath
import json, re

ROOT=Path(__file__).resolve().parents[1]
BASE=ROOT/'Class 9'/'English Medium'/'Chemistry'
for folder in ('Chapters','Concepts','Definitions','Formulas','Exercises'):
    (BASE/folder).mkdir(parents=True,exist_ok=True)

chapters=[
('Chapter 01 - Structure of Atom', 'Structure of Atom', '7-22', 'Atomic structure explains how subatomic particles determine an element and its isotope. The chapter traces evidence from discharge tubes and radioactivity to nuclear and shell models. Thomson inferred negatively charged electrons from cathode rays; Goldstein observed canal rays; Rutherford’s alpha-scattering experiment established a compact positive nucleus; Chadwick identified the neutron. Bohr described electrons in fixed energy levels. Atomic number Z counts protons (and electrons in a neutral atom); mass number A counts protons plus neutrons. Isotopes share Z but differ in neutron count and A; the text connects carbon-14 dating, carbon-13 metabolic research and deuterium heavy water to applications. Shell diagrams and tables practise configurations through atomic number 18, using K/L/M shells and the 2n² capacity rule alongside the textbook’s octet emphasis.'),
('Chapter 02 - Periodic Table', 'Periodic Table', '23-42', 'Mendeleev arranged elements mainly by atomic mass and recurring properties; Moseley’s atomic-number evidence underpins the modern periodic law: chemical and physical properties are periodic functions of atomic number. The modern table has 7 periods and 18 groups. Main-group electron configurations help infer group and period: periods correspond to occupied shells; group 1–2 outer electrons equal the group number, and groups 13–18 add ten to the number of valence electrons. Families include alkali metals, alkaline earth metals, transition elements, boron, carbon, nitrogen and oxygen families, halogens and noble gases. The chapter distinguishes transition elements and inner-transition lanthanoids/actinoids, then examines atomic-size trends: size increases down a group as shells are added and generally decreases across a period as nuclear attraction rises without adding shells.'),
('Chapter 03 - Chemical Bonding', 'Chemical Bonding', '43-68', 'Atoms combine through attraction between constituent particles. Noble-gas duplet/octet configurations provide a stability model. Ionic bonding involves electron transfer and electrostatic attraction between oppositely charged ions (NaCl and MgO diagrams); covalent bonding involves shared electron pairs (single, double and triple bonds in F₂, O₂ and N₂, then molecular examples such as H₂O and HCl). The unit compares properties of ionic and covalent compounds, introduces electronegativity and polarity, hydrogen bonding in water, valency and variable valency, and formula writing by balancing charges/valencies and simplifying indices. It applies formula construction to compounds, acids, bases and salts. Figures and tables model electron-shell transfer, Lewis dot structures, electronegativity differences, ion composition and conductivity experiments.'),
('Chapter 04 - Redox Reactions', 'Redox Reactions', '69-86', 'Experiments and balanced equations introduce chemical change and conservation of mass: in a reaction total reactant mass equals total product mass. A chemical equation is balanced by making atom counts equal on both sides, changing coefficients rather than formula subscripts. Oxidation is electron loss and reduction electron gain; both occur together in redox reactions. Oxidising agents promote oxidation and are themselves reduced; reducing agents promote reduction and are themselves oxidised. Oxidation number tracks electron accounting: elemental substances have 0; in compounds the sum is zero, and common values (H +1, O −2, alkali metals +1, halogens −1) support calculations. Increasing oxidation number signals oxidation; decreasing signals reduction. Examples include Na/Cl, Mg/O, carbon combustion, Zn/HCl and everyday combustion, respiration and corrosion. The chapter contains worked balancing and oxidation-number examples, assessment questions and lab investigations.'),
]
concepts={
'Atomic Number, Mass Number and Isotopes':('Concepts','Structure of Atom','18-20','Atomic number Z is the proton count; for a neutral atom it also equals electron count. Mass number A = protons + neutrons, so neutrons = A − Z. Isotopes are atoms of one element with the same Z and different A. The textbook depicts protium, deuterium and tritium; it notes carbon isotopes 12, 13 and 14, including radiocarbon dating and a stated use of carbon-13 in metabolic studies. Isotopes retain similar chemical properties but may differ physically.'),
'Shells and Electron Configuration':('Concepts','Structure of Atom','15-18','Electrons occupy shells (K, L, M, N); the introductory capacity relation is 2n². The text says lower energy shells fill before higher ones and presents configurations through atomic number 18, with an outer-shell octet convention. Examples include Al 2,8,3 and Ar 2,8,8. Orbit diagrams represent nucleus protons/neutrons and shell electrons; they connect atomic number, neutral-atom electron count and configuration.'),
'Periodic Law and Table Structure':('Concepts','Periodic Table','24-30','The modern periodic law states that chemical and physical properties of elements are periodic functions of their atomic numbers. The table organizes 118 elements in 7 horizontal periods and 18 vertical groups; elements in a group generally share outer-electron patterns and chemical properties. Mendeleev’s mass-based table had limitations for isotopes and mass-order anomalies; Moseley’s atomic-number basis addresses those cases. Table reading activities identify element name, symbol, atomic number and electron configuration.'),
'Groups, Periods and Periodic Families':('Concepts','Periodic Table','28-36','For main-group elements, shell count gives period number. In groups 1 and 2 the number of outer electrons gives the group; for groups 13–18, add 10 to the outer-electron count. Families named in the text include alkali metals (1), alkaline earth metals (2), transition elements (3–12), and groups 13–18 families through noble gases. Noble gases have stable outer configurations (helium duplet; others octet) and are generally unreactive.'),
'Atomic Size Trend':('Concepts','Periodic Table','37-39','Atomic radius expresses atomic size as distance from nucleus centre to the outermost electron shell. Down a group, added shells outweigh increased nuclear charge, so atoms become larger. Across a period, shell count stays fixed while nuclear charge rises, pulling outer electrons closer; size generally decreases. The textbook introduces inner-shell screening as a reason nuclear attraction on outer electrons is reduced.'),
'Ionic and Covalent Bonding':('Concepts','Chemical Bonding','45-55','Ionic bonding forms when atoms transfer electrons and oppositely charged ions attract, as Na⁺/Cl⁻ in NaCl and Mg²⁺/O²⁻ in MgO. Covalent bonds form through shared electron pairs: one pair is a single bond, two a double bond, three a triple bond. Lewis electron-dot diagrams mark valence electrons. The chapter associates ionic compounds with crystalline solids, relatively high melting/boiling points and conductivity when molten or aqueous; covalent compounds may be solids, liquids or gases, often have lower melting/boiling points and generally do not conduct electricity. These are textbook-level generalizations.'),
'Electronegativity, Polarity and Hydrogen Bonding':('Concepts','Chemical Bonding','55-58','Electronegativity is an atom’s relative ability to attract a shared electron pair. Unequal attraction can create partial charges and a polar covalent molecule (the H–Cl diagram shows δ+ and δ−); the text uses electronegativity difference as a guide to ionic versus covalent character and cautions that molecular geometry also affects polarity. Hydrogen bonding is described as an intermolecular attraction involving partially positive hydrogen bonded to a more electronegative atom, used to explain notable properties of water.'),
'Valency and Chemical Formulae':('Concepts','Chemical Bonding','58-64','Valency is the number of electrons an atom loses, gains or shares in a reaction. Formula writing combines symbols and uses valencies/ionic charges as subscripts, then simplifies to the smallest whole-number ratio; a subscript 1 is omitted. The unit extends the method to acids (formula determined by the charge of the negative ion and acid basicity), hydroxide bases, and salts formed from positive and negative ions. Salts are electrically neutral: the total positive and negative charge sums to zero.'),
'Oxidation, Reduction and Agents':('Concepts','Redox Reactions','75-83','Oxidation is loss of electrons; reduction is gain. In a redox reaction both happen simultaneously. An oxidising agent causes another species to oxidise and itself gets reduced; a reducing agent causes another species to reduce and itself gets oxidised. The examples include Na + Cl₂, Mg + O₂, H₂ + Cl₂ and Fe + S. Oxidation-number increase indicates oxidation, decrease indicates reduction.'),
'Conservation of Mass and Balancing':('Concepts','Redox Reactions','70-75','The chapter states the law of conservation of mass: total mass of reactants equals total mass of products in a chemical reaction. A balanced equation has equal numbers of atoms of every element on both sides. Balance by adjusting coefficients only; preserve chemical formula subscripts. Worked examples include 2H₂ + O₂ → 2H₂O, 2Mg + O₂ → 2MgO, Zn + 2HCl → ZnCl₂ + H₂, and 4Al + 3O₂ → 2Al₂O₃.'),
}
definitions={
'Chemical Bond':('Chemical Bonding','45','The force of attraction that holds together the constituent particles of a compound.'),
'Ionisation Energy':('Chemical Bonding','47','The amount of energy required to remove the most loosely bound electron from the outermost shell of an isolated gaseous atom.'),
'Electron Gain Enthalpy':('Chemical Bonding','48','The energy released when an electron is added to a neutral gaseous atom to form a negative ion.'),
'Ionic Bond':('Chemical Bonding','50','The electrostatic force of attraction that holds oppositely charged ions together in an ionic compound; also called an electrovalent bond.'),
'Covalent Bond':('Chemical Bonding','52','A chemical bond formed by sharing electrons between combining atoms. The text calls sharing of one pair a single bond.'),
'Electronegativity':('Chemical Bonding','55','The relative ability of an atom to attract the shared pair of electrons between covalently bonded atoms towards itself.'),
'Valency':('Chemical Bonding','58','The number of electrons lost, gained or shared by an atom during a chemical reaction.'),
'Oxidation':('Redox Reactions','76','The process involving loss of electrons in a chemical reaction.'),
'Reduction':('Redox Reactions','76','The process involving gain of electrons in a chemical reaction.'),
'Oxidising Agent and Reducing Agent':('Redox Reactions','77-78','An oxidising agent helps oxidation and is itself reduced. A reducing agent helps reduction and is itself oxidised.'),
'Oxidation Number':('Redox Reactions','79-80','For ionic compounds, the charge on each ion is its oxidation number. For covalent compounds, the text assigns shared electrons to the more electronegative atom. The sum of oxidation numbers in a compound is zero; in an elemental molecule, it is zero.'),
'Balanced Chemical Equation':('Redox Reactions','73-74','An equation balanced by equalising the number of atoms of each element in reactants and products.'),
}
formulas={
'Atomic and Neutron Counts':('Structure of Atom','18-20','A = Z + N; N = A − Z. Here A is mass number, Z is atomic number (protons), and N is neutron count. For a neutral atom, electron count = Z.'),
'Maximum Shell Capacity':('Structure of Atom','16','The introductory shell-capacity relation is 2n² electrons for shell number n (K=1, L=2, M=3, N=4). The textbook also emphasizes filling lower energy shells first.'),
'Chemical Formula Charge Balance':('Chemical Bonding','60-64','For an electrically neutral ionic formula, choose the smallest whole-number ratio of ions for which total positive charge + total negative charge = 0. The text demonstrates valency interchange followed by simplification, e.g. Ca²⁺ and SO₄²⁻ give CaSO₄.'),
'Conservation in Balanced Equations':('Redox Reactions','71-74','For each element, atom count on reactant side = atom count on product side; coefficients may change, formula subscripts may not. Example: 2H₂ + O₂ → 2H₂O.'),
'Oxidation Number Sum Rule':('Redox Reactions','79-81','For a neutral compound, Σ oxidation numbers = 0. In an element in its uncombined state, oxidation number = 0. Use known values such as H=+1 and O=−2 to solve for an unknown.'),
}
exercises={
'Structure of Atom - Assessment and Activities':('Structure of Atom','21-22','The assessment asks students to infer cathode-ray properties, derive proton/neutron/electron counts from atomic and mass numbers, draw shell configurations, identify isotope/isobar pairs and match historical models/scientists. Extended activities ask for scientist biographies, a discovery timeline, radioisotope uses and interview questions for Rutherford.'),
'Periodic Table - Assessment and Activities':('Periodic Table','40-42','Exercises practise configurations, group/period/family identification, noble-gas stability, relative atomic size, periodic-table positions and deriving real element symbols from placeholder grids and mass/neutron data. Extended work includes a scientist biography, table model and Kalzium-supported element chart.'),
'Chemical Bonding - Assessment and Activities':('Chemical Bonding','65-68','Exercises ask for Lewis diagrams, ionic/covalent classifications, valencies and formulae for salts, acids and bases, electron transfer in ionic compounds, shared-electron counts and bond order. Extended tasks include magnesium nitride, hydrocarbon bonding and a conductivity comparison using salt and glucose solutions.'),
'Redox Reactions - Assessment and Activities':('Redox Reactions','84-86','Assessment covers balancing equations, mass calculations, oxidation-number assignment, identifying oxidised/reduced species and agents, and distinguishing redox from non-redox reactions. Extended investigations include iron/sulphur, calcium carbide, aluminium/iodine and industrial importance of redox. No answer key is provided here.'),
}

def write_note(folder,name,kind,chapter,topic,pages,body,links=()):
    p=BASE/folder/(name+'.md')
    rel=lambda x: f'[[{x}]]'
    linktxt='\n'.join('- '+rel(posixpath.relpath(x, folder)) for x in links)
    tags=['class/9','medium/english','subject/chemistry',f'type/{kind.lower()}']
    yaml='---\nclass: 9\nmedium: English\nsubject: Chemistry\nchapter: "'+chapter+'"\ntopic: "'+topic+'"\ntype: '+kind.lower()+'\ntextbook: Chemistry Standard IX Part I\nprinted_pages: "'+pages+'"\ntags: ['+', '.join(tags)+']\n---\n'
    p.write_text(yaml+f'# {name}\n\n{body}\n\n**Textbook reference:** Chemistry Standard IX Part I, printed pp. {pages}.\n\n## Related notes\n'+(linktxt or '- [[Subject Overview]]')+'\n',encoding='utf-8')
    return p

chapter_paths=[]
for filename,title,pages,body in chapters:
    refs=[f'Concepts/{n}' for n,v in concepts.items() if v[1]==title]
    refs += [f'Definitions/{n}' for n,v in definitions.items() if v[0]==title]
    refs += [f'Formulas/{n}' for n,v in formulas.items() if v[0]==title]
    refs += [f'Exercises/{n}' for n,v in exercises.items() if v[0]==title]
    p=write_note('Chapters',filename,'chapter',title,title,pages,body,refs)
    chapter_paths.append('Chapters/'+filename)
for name,(folder,chapter,pages,body) in concepts.items():
    refs=[f'Chapters/Chapter {i:02d} - {chapters[i-1][1]}' for i in range(1,5) if chapters[i-1][1]==chapter]
    refs += [f'Definitions/{n}' for n,v in definitions.items() if v[0]==chapter]
    write_note(folder,name,'concept',chapter,name,pages,body,refs)
# Explicit, content-based links that bridge chapters (isotopes/periodicity,
# electron configurations/bonding, and electron transfer/redox).
cross_links={
    'Atomic Number, Mass Number and Isotopes':['Periodic Law and Table Structure'],
    'Shells and Electron Configuration':['Groups, Periods and Periodic Families'],
    'Groups, Periods and Periodic Families':['Valency and Chemical Formulae'],
    'Ionic and Covalent Bonding':['Oxidation, Reduction and Agents'],
    'Valency and Chemical Formulae':['Oxidation, Reduction and Agents'],
    'Oxidation, Reduction and Agents':['Ionic and Covalent Bonding','Conservation of Mass and Balancing'],
}
for source,targets in cross_links.items():
    p=BASE/'Concepts'/(source+'.md'); raw=p.read_text(encoding='utf-8')
    for target in targets:
        entry=f'- [[{target}]]'
        if entry not in raw: raw=raw.rstrip()+f'\n{entry}\n'
    p.write_text(raw,encoding='utf-8')
for name,(chapter,pages,body) in definitions.items():
    write_note('Definitions',name,'definition',chapter,name,pages,body,[f'Chapters/Chapter {i:02d} - {chapters[i-1][1]}' for i in range(1,5) if chapters[i-1][1]==chapter])
for name,(chapter,pages,body) in formulas.items():
    write_note('Formulas',name,'formula',chapter,name,pages,body,[f'Chapters/Chapter {i:02d} - {chapters[i-1][1]}' for i in range(1,5) if chapters[i-1][1]==chapter])
for name,(chapter,pages,body) in exercises.items():
    write_note('Exercises',name,'exercise',chapter,name,pages,body,[f'Chapters/Chapter {i:02d} - {chapters[i-1][1]}' for i in range(1,5) if chapters[i-1][1]==chapter])

overview='''---
class: 9
medium: English
subject: Chemistry
part: 1
edition: First Edition 2024
type: overview
tags: [class/9, medium/english, subject/chemistry, type/overview]
---
# Chemistry — Part I

**Kerala SCERT Standard IX, First Edition 2024.** This volume contains four units: Structure of Atom (printed pp. 7–22), Periodic Table (23–42), Chemical Bonding (43–68), and Redox Reactions (69–86). Notes were checked against the rendered pages, including shell and periodic-table diagrams, electron-transfer and Lewis diagrams, data tables, worked equations, assessment pages and practical activities.

## Chapter map
'''+''.join(f'- [[{p}|{title}]]\n' for p,(_,title,_,_) in zip(chapter_paths,chapters))+'''
## Colour legend
- Red `#FF6B6B`: important concepts
- Orange `#F4A261`: definitions
- Yellow `#E9C46A`: formulas and rules
- Green `#2A9D8F`: examples, assessments and activities
- Blue `#457B9D`: chapters and overview
- Purple `#9B5DE5`: cross-topic links

Part II remains to be read. This map covers Part I only.
'''
(BASE/'Subject Overview Part 1.md').write_text(overview,encoding='utf-8')

# Build a readable two-row chapter map with file nodes only.
allnotes=[BASE/'Subject Overview Part 1.md']+sorted(p for folder in ['Chapters','Concepts','Definitions','Formulas','Exercises'] for p in (BASE/folder).glob('*.md'))
nodes=[]; edges=[]; ids={}
for i,p in enumerate(allnotes):
    rel=p.relative_to(BASE).as_posix(); nid=f'n{i+1}'; ids[rel]=nid
    if p.name.startswith('Subject Overview'):
        x,y,w,h,color=-420,-150,360,140,'5'
    else:
        typ=p.parent.name; ix=len([n for n in nodes if n.get('type')=='file' and n.get('file','').startswith(typ+'/')])
        col={'Chapters':0,'Concepts':1,'Definitions':2,'Formulas':3,'Exercises':4}.get(typ,1)
        x=col*380; y=ix*150; w=320; h=110
        color={'Chapters':'5','Concepts':'1','Definitions':'2','Formulas':'3','Exercises':'4'}[typ]
    nodes.append({'id':nid,'type':'file','file':rel,'x':x,'y':y,'width':w,'height':h,'color':color})
for p in allnotes:
    src=p.relative_to(BASE).as_posix()
    if src not in ids: continue
    text=p.read_text(encoding='utf-8')
    for target in re.findall(r'\[\[([^\]|#]+)',text):
        target=target.strip()
        if target.endswith('.md'): dest=posixpath.normpath(posixpath.join(posixpath.dirname(src),target))
        elif target.startswith(('Chapters/','Concepts/','Definitions/','Formulas/','Exercises/')): dest=target+'.md'
        elif target.startswith('../'): dest=posixpath.normpath(posixpath.join(posixpath.dirname(src),target+'.md'))
        else: continue
        if dest in ids and ids[src]!=ids[dest]: edges.append({'id':f'e{len(edges)+1}','fromNode':ids[src],'toNode':ids[dest],'fromSide':'right','toSide':'left','color':'6'})
# de-duplicate reciprocal/duplicate links
uniq=[]; seen=set()
for e in edges:
    k=(e['fromNode'],e['toNode'])
    if k not in seen: seen.add(k); uniq.append(e)
(BASE/'Chemistry Part 1.canvas').write_text(json.dumps({'nodes':nodes,'edges':uniq},indent=2),encoding='utf-8')
print(f'Chemistry Part I notes: {len(allnotes)}; canvas nodes {len(nodes)}, edges {len(uniq)}')
