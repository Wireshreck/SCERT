from pathlib import Path
import json, re, posixpath

ROOT=Path(__file__).resolve().parents[1]
BASE=ROOT/'Class 9'/'English Medium'/'Mathematics'
for d in ('Chapters','Concepts','Definitions','Formulas','Exercises'):(BASE/d).mkdir(parents=True,exist_ok=True)
chapters=[
('Circle Measures','151-164','A circle’s circumference is developed by comparing it with perimeters of regular polygons placed around and inside it. The ratio of circumference to diameter is constant, π, so C=πd=2πr. Polygon perimeters converge toward the circle circumference as the number of sides increases. Area is developed by rearranging sectors into an approximate rectangle, yielding A=πr². The chapter applies these ideas to circles, rings, regular polygons and circle-inscribed/circumscribed figures, with Kerala architectural references and approximation examples.'),
('Real Numbers','165-176','The number line extends beyond rational numbers to represent lengths such as circle circumferences and square-root values. Numbers are ordered by position. Absolute value gives distance from zero; distance between two numbers is the absolute value of their difference. The midpoint of two points is the average of their coordinates. The chapter works with positive and negative rational values, irrational lengths and number-line geometry.'),
('Polynomials','177-184','Measurement problems motivate expressions whose value changes with a variable. Terms combine numerical coefficients and powers of variables; the degree is the highest exponent. The chapter distinguishes constant, linear and quadratic forms and uses algebraic notation to express perimeter, area and volume changes. It introduces operations and interprets polynomial expressions from geometric dimensions.'),
('Parts of Circles','185-194','A full rotation is 360 degrees. An arc’s length is the same fraction of the circumference as its central angle is of 360 degrees. A sector’s area is the same fraction of the circle’s area. The chapter models rotations, angles and sectors, then combines these relationships to find arc lengths and sector areas, including shaded figures formed from sectors and triangles.'),
('Prisms','195-208','A prism has congruent parallel polygonal bases and rectangular/parallelogram side faces; its cross-section remains constant along its length. The volume is base area multiplied by perpendicular height. Surface area is built from the base faces and lateral faces; for a right prism, lateral area is base perimeter times height. The unit develops triangular and polygonal prisms, cylinders as curved analogues, and nets/cut-and-fold models for volume and surface-area reasoning.'),
('Polynomial Pictures','209-222','A polynomial can be represented by a table of values and a graph. Linear polynomials produce straight-line graphs; quadratic examples form curves. The graph makes roots (where the value is zero), intercepts, sign, growth and turning behaviour visible. The chapter uses plotted points, perpendicular constructions and GeoGebra screenshots to infer polynomial expressions and compare related graphs.'),
('Proportion','223-232','Proportional change compares two quantities through a constant ratio or constant multiplier. Direct proportion is represented by y=kx; inverse proportion by xy=k. Similar figures preserve side ratios while areas change by the square of the scale factor. The chapter tests proportionality in photographs, maps, triangles, circumference/angle relations, volume and other real contexts, and contrasts proportional with non-proportional changes.'),
('Statistics','233-242','Statistics condenses a large set of observations into useful summaries. The arithmetic mean is total value divided by count; frequency tables use the sum of value×frequency divided by total frequency. Graphs display values and departures from an average. Grouped data are handled by class intervals and representative values, with explicit assumptions where individual observations are unknown. Examples use cricket scores, wages, marks, rainfall, age and weight distributions.'),
]
concepts=[
('Circumference and Pi','Circle Measures','151-156','The circumference-to-diameter ratio is constant for every circle and is denoted π. Thus C/d=π, C=πd=2πr. The textbook approximates π by comparing inscribed and circumscribed regular polygons; additional sides narrow the bounds.'),
('Circle Area and Rings','Circle Measures','157-164','Rearranging many narrow sectors approximates a rectangle with base πr and height r, so circle area A=πr². A ring or shaded region is found by subtracting the inner circle area from the outer circle area.'),
('Absolute Value, Distance and Midpoint','Real Numbers','165-176','The absolute value |x| is the distance of x from zero. Distance between points a and b on a number line is |a−b|. The midpoint coordinate is (a+b)/2. These definitions apply to rational and irrational coordinates.'),
('Polynomial Terms and Degree','Polynomials','177-184','A polynomial is a finite sum of terms with nonnegative integer powers of its variables. The coefficient is the numerical factor, and the degree is the largest exponent (for the single-variable expressions emphasized here). Examples include constant, first-degree and second-degree forms.'),
('Arc Length and Sector Area','Parts of Circles','185-194','For central angle θ degrees, arc length is θ/360 × 2πr and sector area is θ/360 × πr². The fraction of a full turn is the same fraction of circumference and circle area.'),
('Prism Volume and Surface Area','Prisms','195-208','For a prism with base area B, base perimeter P and perpendicular height h, volume V=Bh and lateral surface area L=Ph. Total surface area adds the areas of the two congruent bases: S=Ph+2B. For a cylinder, B=πr² and P=2πr.'),
('Polynomial Graphs and Roots','Polynomial Pictures','209-222','Plot ordered pairs (x,p(x)) to represent a polynomial. A root is an x-value where p(x)=0, shown by intersection with the horizontal axis. Linear polynomials graph as straight lines; quadratic examples curve and may have zero, one or two real roots.'),
('Direct and Inverse Proportion','Proportion','223-232','In direct proportion y/x=k (equivalently y=kx), so scaling x by a factor scales y by the same factor. In inverse proportion xy=k, so multiplying one variable by a factor divides the other by that factor. Check for a constant ratio/product across observations.'),
('Arithmetic Mean and Frequency Tables','Statistics','233-242','For observations x₁,…,xₙ, mean = (Σxᵢ)/n. With values xᵢ and frequencies fᵢ, mean = (Σfᵢxᵢ)/(Σfᵢ). In grouped tables, a representative value such as the class midpoint is used, so state the approximation assumption.'),
]
formulas=[
('Circumference of a circle','Circle Measures','154-156','C=πd=2πr, where d=2r. Use the π precision appropriate to the question; the textbook uses decimal approximations in applied measurement.'),
('Area of a circle','Circle Measures','158-164','A=πr². For an annulus with radii R and r, shaded area = πR²−πr²=π(R²−r²).'),
('Distance and midpoint on a number line','Real Numbers','168-176','Distance(a,b)=|a−b|. Midpoint(a,b)=(a+b)/2. Absolute value is nonnegative and measures distance, irrespective of direction.'),
('Polynomial degree','Polynomials','179-184','For p(x)=aₙxⁿ+…+a₁x+a₀ with aₙ≠0, degree(p)=n. The textbook examples focus on constant, first-degree and second-degree polynomials.'),
('Arc length','Parts of Circles','186-190','For a central angle θ° and radius r: s=(θ/360°)·2πr. The fraction θ/360° is the fraction of one complete circumference traversed.'),
('Sector area','Parts of Circles','190-194','For θ° and radius r: A_sector=(θ/360°)·πr². A sector’s area fraction equals its central-angle fraction.'),
('Prism volume','Prisms','196-200','V=B·h, where B is the area of a base and h is perpendicular distance between the bases. Keep units cubed.'),
('Prism and cylinder surface area','Prisms','201-208','Right prism lateral area L=P·h and total area S=P·h+2B. Cylinder lateral area L=2πr·h and total area S=2πrh+2πr².'),
('Direct and inverse proportion','Proportion','223-232','Direct: y=kx, so y₁/x₁=y₂/x₂=k. Inverse: xy=k, so x₁y₁=x₂y₂=k.'),
('Arithmetic mean','Statistics','234-242','Ungrouped mean x̄=Σx/n. Frequency mean x̄=Σ(fx)/Σf. For grouped intervals, x is represented by the class midpoint; the estimate depends on this assumption.'),
]
exercises=[
('Circle Measures — Circumference and Area','Circle Measures','155-164','Estimate π from polygon approximations; find circumferences, circle areas and ring areas; compare polygon and circle perimeters/areas; and interpret diagrams of inscribed or circumscribed figures.'),
('Real Numbers — Number-Line Reasoning','Real Numbers','169-176','Order rational and irrational values, calculate absolute values, distances and midpoints, and interpret signed changes geometrically on number lines.'),
('Polynomials — Algebraic Measurements','Polynomials','181-184','Write polynomial expressions for changing lengths, perimeters, areas and volumes; identify terms and degree; and use the variable relation to solve measurement problems.'),
('Parts of Circles — Arcs and Sectors','Parts of Circles','189-194','Calculate arc lengths and sector areas from central angles and radii; solve shaded-region problems by adding or subtracting sector and triangle areas.'),
('Prisms — Volume and Surface Area','Prisms','200-208','Find base areas, prism volumes, lateral and total surface areas for polygonal prisms and cylinders; interpret nets and choose units carefully.'),
('Polynomial Pictures — Tables and Graphs','Polynomial Pictures','214-222','Complete value tables, plot polynomial graphs, identify roots and intercepts, and infer linear or quadratic expressions from graph features.'),
('Proportion — Comparing Changes','Proportion','225-232','Test whether paired quantities are directly or inversely proportional, compute missing values and scale factors, and distinguish constant-ratio change from other patterns.'),
('Statistics — Averages and Data Tables','Statistics','234-242','Find means from raw data, frequency tables and grouped intervals; interpret graphs and assumptions; compare categories and reason about missing/estimated observations.'),
]
def write(folder,name,kind,chapter,pages,body,related=()):
    rel='\n'.join('- [['+posixpath.relpath(r,folder)+']]' for r in related) or '- [[../Subject Overview]]'
    tag=kind.lower(); p=BASE/folder/(name+'.md')
    p.write_text(f'''---\nclass: 9\nmedium: English\nsubject: Mathematics\nchapter: "{chapter}"\ntopic: "{name}"\ntype: {tag}\ntextbook: Mathematics Standard IX Part II\nprinted_pages: "{pages}"\ntags: [class/9, medium/english, subject/mathematics, type/{tag}]\n---\n# {name}\n\n{body}\n\n**Textbook reference:** Mathematics Standard IX Part II, printed pp. {pages}.\n\n## Related notes\n{rel}\n''',encoding='utf-8'); return p
nodes=[('Subject Overview Part 2.md',5)]; chapter_files={}; index={}
for i,(t,p,b) in enumerate(chapters,8):
    n=f'Chapter {i:02d} - {t}'; rel=[f'Concepts/{x[0]}' for x in concepts if x[1]==t]+[f'Formulas/{x[0]}' for x in formulas if x[1]==t]+[f'Exercises/{x[0]}' for x in exercises if x[1]==t]
    f=write('Chapters',n,'chapter',t,p,b,rel); k=f'Chapters/{n}.md'; chapter_files[t]=f'n{i-6}'; index[k]=chapter_files[t]; nodes.append((k,5))
for folder,data,color in [('Concepts',concepts,1),('Formulas',formulas,3),('Exercises',exercises,4)]:
    for x in data:
        t,ch,p,b=x; f=write(folder,t,folder[:-1].lower() if folder!='Exercises' else 'exercise',ch,p,b,[f'Chapters/Chapter {i:02d} - {ch}' for i,(ct,_,_) in enumerate(chapters,8) if ct==ch]); k=f'{folder}/{t}.md'; index[k]=f'n{len(nodes)+1}'; nodes.append((k,color))
for a,b in [('Circumference and Pi','Arc Length and Sector Area'),('Circle Area and Rings','Prism Volume and Surface Area'),('Absolute Value, Distance and Midpoint','Signed Arithmetic'),('Polynomial Terms and Degree','Polynomial Graphs and Roots'),('Prism Volume and Surface Area','Direct and Inverse Proportion')]:
    p=BASE/'Concepts'/(a+'.md'); txt=p.read_text(encoding='utf-8').rstrip()+f'\n- [[{b}]]\n'; p.write_text(txt,encoding='utf-8')
overview='''---\nclass: 9\nmedium: English\nsubject: Mathematics\npart: 2\nedition: First Edition 2024\ntype: overview\ntags: [class/9, medium/english, subject/mathematics, type/overview]\n---\n# Mathematics — Part II\n\n**Kerala SCERT Standard IX, First Edition 2024.** All 104 PDF pages were visually reviewed, including circle and sector diagrams, polygon approximations, prism models, graph tables and plots, proportion illustrations, statistics tables, exercises, note pages and civic inserts.\n\n## Chapters\n'''+''.join(f'- [[Chapters/Chapter {i:02d} - {t}|{t}]] — printed pp. {p}\n' for i,(t,p,_) in enumerate(chapters,8))+'''\n## Canvas colour legend\n- Red `#FF6B6B`: concepts\n- Orange `#F4A261`: definitions\n- Yellow `#E9C46A`: formulas\n- Green `#2A9D8F`: examples and exercises\n- Blue `#457B9D`: chapters and overview\n- Purple `#9B5DE5`: cross-chapter links\n\nOpen [[Mathematics Part 2.canvas]] for the visual map.\n'''
(BASE/'Subject Overview Part 2.md').write_text(overview,encoding='utf-8')
combined=BASE/'Subject Overview.md'; s=combined.read_text(encoding='utf-8'); s=s.replace('Part II is awaiting visual review.','[[Subject Overview Part 2|Part II]] covers Circle Measures, Real Numbers, Polynomials, Parts of Circles, Prisms, Polynomial Pictures, Proportion and Statistics.')
combined.write_text(s,encoding='utf-8')
# Combined overview is the navigation hub and canvas centre links to its volume overview.
if not s.startswith('---'): raise ValueError('Invalid overview frontmatter')
allnodes=[('Subject Overview Part 2.md',5)]+nodes[1:]
canvas_nodes=[]
for i,(file,col) in enumerate(allnodes):
    canvas_nodes.append({'id':f'n{i+1}','type':'file','file':file,'x':(i%3)*500,'y':(i//3)*180,'width':360,'height':130,'color':str(col)})
edges=[]
for i in range(8): edges.append({'id':f'e{i+1}','fromNode':'n1','fromSide':'right','toNode':f'n{i+2}','toSide':'left','color':'5'})
lookup={n['file']:n['id'] for n in canvas_nodes}
for folder,data in [('Concepts',concepts),('Formulas',formulas),('Exercises',exercises)]:
    for x in data:
        t,ch,_,_=x; source=chapter_files[ch]; target=lookup[f'{folder}/{t}.md']; edges.append({'id':f'e{len(edges)+1}','fromNode':source,'fromSide':'right','toNode':target,'toSide':'left','color':'5'})
for a,b in [('Circumference and Pi','Arc Length and Sector Area'),('Circle Area and Rings','Prism Volume and Surface Area'),('Polynomial Terms and Degree','Polynomial Graphs and Roots')]: edges.append({'id':f'e{len(edges)+1}','fromNode':lookup[f'Concepts/{a}.md'],'fromSide':'right','toNode':lookup[f'Concepts/{b}.md'],'toSide':'left','color':'6'})
(BASE/'Mathematics Part 2.canvas').write_text(json.dumps({'nodes':canvas_nodes,'edges':edges},indent=2),encoding='utf-8')
