from pathlib import Path
import json, re, posixpath

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / 'Class 9' / 'English Medium' / 'Mathematics'
for folder in ('Chapters', 'Concepts', 'Definitions', 'Formulas', 'Exercises'):
    (BASE / folder).mkdir(parents=True, exist_ok=True)

chapters = [
('Pairs of Equations','7-18', 'The opening unit models two related unknowns with a pair of linear equations. Everyday price and quantity stories are translated into equations, then solved by elimination: combine or subtract equations to remove one variable and substitute back for the other. The book emphasizes checking that a solution satisfies both equations, interpreting variables in context, and using algebra to reduce repeated arithmetic. Worked settings include prices, ages, lengths and counts; the exercises ask learners to formulate and solve systems.'),
('New Numbers','19-32', 'This unit extends number representation through lengths and areas that cannot be expressed as rational fractions. Square-root notation names the positive number whose square is the given value; geometric dissection of squares motivates irrational lengths. Decimal approximations are developed by bracketing a root between nearby tenths, hundredths and finer values. The unit also uses irrational lengths in perimeter calculations and explains why approximations should match the precision of the context.'),
('Parallel Lines','33-60', 'Parallel-line diagrams establish equal division: parallel lines cut transversals proportionally. The unit applies this principle to lengths in triangles and polygons, develops the side-splitter result for a line parallel to one side of a triangle, and studies the converse construction. Midpoints, medians, perpendicular bisectors, altitudes, angle bisectors, Euler-line relationships and triangle centres appear through constructions and proofs. Repeated diagrams and paper-folding/GeoGebra activities connect proportional lengths with area and congruence.'),
('Multiplication Identities','61-82', 'Area models turn products into identities. Rectangles illustrate distributivity and expansions such as (a+b)(c+d); special cases yield the square of a sum, square of a difference, and product of sum and difference. The unit then examines products of consecutive and nearby natural numbers through calendar patterns and algebraic generalisation. Learners use identities both to expand expressions and to simplify numerical products.'),
('Irrational Multiplication','83-98', 'Geometric area and length models motivate multiplication involving square roots. For positive a and b, √a√b=√(ab); square roots are approximated by decimal bounds when exact simplification is unavailable. The chapter uses squares, rectangles, right triangles and equilateral triangles to build and apply area relations, and relates the square of a sum/difference to expanded products. It includes worked calculations, diagrams, and exercises on lengths, areas and identities.'),
('Similar Triangles','99-118', 'Triangles with equal corresponding angles have proportional corresponding sides. A line parallel to one side divides the other two sides in the same ratio; conversely, a proportional division establishes parallelism. The unit builds scale factors using corresponding sides, then applies them to lengths, areas, right triangles, projections and quadrilaterals. Diagrams show circumcircles and centres as well as geometric construction tasks; the exercises require identifying correspondence before setting up ratios.'),
('Negative Numbers','119-140', 'A number-line model represents position and displacement, including movement in opposite directions. Integers extend arithmetic to negative displacement and temperature change. Addition combines signed displacements; subtraction is defined through addition of the opposite. Multiplication and division extend sign rules consistently, including products of two negatives. Tables and contexts (movement, speed and temperature) support the rules, followed by algebraic equations and operations with negative fractions.'),
]

concepts = [
('Solving a Pair of Linear Equations','Pairs of Equations','7-18','Represent two unknown quantities with two linear equations. Eliminate one variable by adding/subtracting suitable multiples of the equations, solve the remaining one-variable equation, and substitute back. Interpret the ordered pair in the original context and verify both equations.'),
('Irrational Numbers and Decimal Bounds','New Numbers','19-32','A number is irrational when it cannot be written as a ratio of integers. The book motivates such values through square diagonals and areas. To approximate √n, locate consecutive decimal numbers whose squares lie on either side of n, then refine the interval one decimal place at a time.'),
('Parallel Division and the Side-Splitter Result','Parallel Lines','33-50','Parallel lines cut any two intersecting transversals into equal corresponding intervals. In a triangle, a line parallel to one side divides the other two sides in the same ratio: if DE ∥ BC in △ABC, then AD/DB = AE/EC, equivalently AD/AB = AE/AC. The converse is used to test whether a segment is parallel.'),
('Triangle Centres and Euler Line','Parallel Lines','51-60','The medians of a triangle meet at the centroid; the perpendicular bisectors meet at the circumcentre; the angle bisectors meet at the incentre; and the altitudes meet at the orthocentre. The chapter develops these centres with constructions and proves relationships among medians and midpoints. In a non-equilateral triangle the centroid, circumcentre and orthocentre lie on Euler’s line.'),
('Algebraic Multiplication Identities','Multiplication Identities','61-82','Area models support (a+b)(c+d)=ac+ad+bc+bd, (a+b)²=a²+2ab+b², (a−b)²=a²−2ab+b² and (a+b)(a−b)=a²−b². The identities are used to expand, factor and calculate products efficiently. Calendar arrangements illustrate products of consecutive numbers and generalisation.'),
('Products and Areas with Square Roots','Irrational Multiplication','83-98','For nonnegative a,b, √a·√b=√(ab); conversely √(ab)=√a√b. A square of side √a has area a. Similar geometric decompositions connect areas of squares, rectangles and triangles to expressions containing roots; decimal bounds provide practical approximations.'),
('Similarity and Scale Factor','Similar Triangles','99-118','Similar triangles have equal corresponding angles and proportional corresponding sides. If the scale factor from a smaller triangle to a larger one is k, corresponding lengths multiply by k and areas by k². Match vertices consistently before writing ratios. The parallel-line criterion and right-triangle constructions provide applications.'),
('Signed Arithmetic','Negative Numbers','119-140','On a number line, the opposite of x is −x. Subtraction is defined by a−b=a+(−b); equal signs in multiplication/division give a positive result and unlike signs give a negative result. The rules preserve familiar distributive and associative relationships and extend to fractions.'),
]

formulas = [
('Linear system by elimination','Pairs of Equations','7-18','For a₁x+b₁y=c₁ and a₂x+b₂y=c₂, multiply equations as needed so one variable has opposite coefficients, add to eliminate it, solve, then substitute back. Check both original equations.'),
('Square-root bounds','New Numbers','20-27','If p² < n < q², then p < √n < q for nonnegative p,q. Refine with decimal candidates, comparing their squares; report an approximation at the precision supported by the final interval.'),
('Triangle side-splitter ratio','Parallel Lines','46-50','For DE ∥ BC in △ABC: AD/DB = AE/EC and AD/AB = AE/AC. The converse proportion can establish DE ∥ BC when the points lie on the corresponding sides.'),
('Square of a sum and difference','Multiplication Identities','61-76','(a+b)² = a² + 2ab + b²; (a−b)² = a² − 2ab + b². The middle term is twice the product of the two terms, with sign determined by the binomial.'),
('Product of sum and difference','Multiplication Identities','74-82','(a+b)(a−b)=a²−b². The cross terms cancel; the identity supports mental multiplication and factorisation.'),
('Product of square roots','Irrational Multiplication','84-92','For a≥0 and b≥0, √a × √b = √(ab), and √(a²)=a for a≥0. Keep nonnegative conditions explicit when simplifying principal square roots.'),
('Area scale in similar figures','Similar Triangles','101-114','If corresponding side lengths have ratio k, then corresponding areas have ratio k². For triangles, area = ½ × base × perpendicular height; equal included angles plus proportional adjacent sides establish similarity in the textbook’s constructions.'),
('Signed operations','Negative Numbers','123-140','a−b=a+(−b). For multiplication/division, same signs produce a positive result and different signs a negative result. For a,b>0: (−a)(−b)=ab; (−a)b=−ab. Apply the same sign rules to fractions.'),
]

exercises = [
('Pairs of Equations — Problems and Practice','Pairs of Equations','11-18','Translate the paired price, age, length and quantity situations into equations; solve by elimination and substitution; verify the ordered pair in both equations. No answer key is supplied in the textbook.'),
('New Numbers — Construction and Approximation','New Numbers','25-32','Use square/area constructions to identify irrational lengths, bracket square roots by decimal squares, refine approximations, and calculate perimeters using stated precision. Distinguish exact root expressions from rounded decimal values.'),
('Parallel Lines — Proofs and Constructions','Parallel Lines','39-60','Exercises use parallel transversals, proportional segments, triangle side-splitting, midpoint and median results, triangle centres, Euler line, perpendicular bisectors and construction tasks. Provide a diagram and justify each proportional relationship.'),
('Multiplication Identities — Applications','Multiplication Identities','64-82','Expand and simplify products using distributivity and identities; evaluate products near round numbers; generalise calendar patterns; and solve rectangle-area contexts. Show the identity used before substitution.'),
('Irrational Multiplication — Length and Area','Irrational Multiplication','88-98','Simplify products of square roots, estimate roots, and use diagrams to find square, rectangle and triangle lengths, perimeters or areas. Preserve exact forms where requested and state decimal precision for estimates.'),
('Similar Triangles — Ratios and Geometry','Similar Triangles','103-118','Identify corresponding vertices and sides, prove similarity, calculate missing lengths and areas using scale factors, and apply projection/right-triangle results to constructions and quadrilaterals.'),
('Negative Numbers — Operations and Equations','Negative Numbers','126-140','Complete signed-displacement tables; add, subtract, multiply and divide integers and fractions; simplify expressions; and solve equations involving negative values. Check results by substitution and number-line reasoning.'),
]

def slug(s): return re.sub(r'[^A-Za-z0-9 -]', '', s).strip()
def write(folder,name,kind,chapter,pages,body,related=()):
    tag=kind.lower()
    path=BASE/folder/(name+'.md')
    refs='\n'.join(f'- [[{posixpath.relpath(r, folder)}]]' for r in related) or f'- [[{posixpath.relpath("Subject Overview", folder)}]]'
    path.write_text(f'''---\nclass: 9\nmedium: English\nsubject: Mathematics\nchapter: "{chapter}"\ntopic: "{name}"\ntype: {tag}\ntextbook: Mathematics Standard IX Part I\nprinted_pages: "{pages}"\ntags: [class/9, medium/english, subject/mathematics, type/{tag}]\n---\n# {name}\n\n{body}\n\n**Textbook reference:** Mathematics Standard IX Part I, printed pp. {pages}.\n\n## Related notes\n{refs}\n''',encoding='utf-8')
    return path

chapter_paths=[]; node_data=[]
for i,(title,pages,body) in enumerate(chapters,1):
    name=f'Chapter {i:02d} - {title}'
    related=[f'Concepts/{c[0]}' for c in concepts if c[1]==title]+[f'Formulas/{f[0]}' for f in formulas if f[1]==title]+[f'Exercises/{e[0]}' for e in exercises if e[1]==title]
    p=write('Chapters',name,'chapter',title,pages,body,related); chapter_paths.append('Chapters/'+name)
    node_data.append((str(p.relative_to(BASE)).replace('\\','/'),5))
concept_paths={}
for title,chapter,pages,body in concepts:
    p=write('Concepts',title,'concept',chapter,pages,body,[f'Chapters/Chapter {i:02d} - {chapter}' for i,(t,_,_) in enumerate(chapters,1) if t==chapter]); concept_paths[title]='Concepts/'+title; node_data.append((str(p.relative_to(BASE)).replace('\\','/'),1))
for title,chapter,pages,body in formulas:
    p=write('Formulas',title,'formula',chapter,pages,body,[f'Chapters/Chapter {i:02d} - {chapter}' for i,(t,_,_) in enumerate(chapters,1) if t==chapter]); node_data.append((str(p.relative_to(BASE)).replace('\\','/'),3))
for title,chapter,pages,body in exercises:
    p=write('Exercises',title,'exercise',chapter,pages,body,[f'Chapters/Chapter {i:02d} - {chapter}' for i,(t,_,_) in enumerate(chapters,1) if t==chapter]); node_data.append((str(p.relative_to(BASE)).replace('\\','/'),4))

# Explicit relationships between algebra, geometric proportionality and area.
for a,b in [('Parallel Division and the Side-Splitter Result','Similarity and Scale Factor'),('Triangle Centres and Euler Line','Parallel Division and the Side-Splitter Result'),('Products and Areas with Square Roots','Algebraic Multiplication Identities'),('Signed Arithmetic','Solving a Pair of Linear Equations')]:
    p=BASE/'Concepts'/(a+'.md'); txt=p.read_text(encoding='utf-8').rstrip()+f'\n- [[{b}]]\n'; p.write_text(txt,encoding='utf-8')

overview='''---\nclass: 9\nmedium: English\nsubject: Mathematics\npart: 1\nedition: First Edition 2024\ntype: overview\ntags: [class/9, medium/english, subject/mathematics, type/overview]\n---\n# Mathematics — Part I\n\n**Kerala SCERT Standard IX, First Edition 2024.** All 144 PDF pages were visually reviewed, including the cover and imprint, seven chapters, worked examples, diagrams, tables, construction tasks, exercises, note pages, and civic inserts. The chapter progression moves from algebraic modelling to irrational lengths, geometric proportion, identities, similarity, and signed arithmetic.\n\n## Chapters\n'''+''.join(f'- [[{p}|{t}]] — printed pp. {pg}\n' for p,(t,pg,_) in zip(chapter_paths,chapters))+'''\n## Canvas colour legend\n- Red `#FF6B6B`: concepts\n- Orange `#F4A261`: definitions\n- Yellow `#E9C46A`: formulas\n- Green `#2A9D8F`: examples and exercises\n- Blue `#457B9D`: chapters and overview\n- Purple `#9B5DE5`: cross-chapter links\n\n## Study map\nOpen [[Mathematics Part 1.canvas]] for chapter flow, key ideas, formulas and exercise links. See [[Subject Overview]] for both volumes.\n'''
(BASE/'Subject Overview Part 1.md').write_text(overview,encoding='utf-8')
combined=BASE/'Subject Overview.md'
if not combined.exists():
    combined.write_text('''---\nclass: 9\nmedium: English\nsubject: Mathematics\ntype: overview\ntags: [class/9, medium/english, subject/mathematics, type/overview]\n---\n# Mathematics — Class 9 English Medium\n\nPart I and Part II are separate volumes. [[Subject Overview Part 1|Part I]] contains Pairs of Equations, New Numbers, Parallel Lines, Multiplication Identities, Irrational Multiplication, Similar Triangles and Negative Numbers. Part II is awaiting visual review.\n''',encoding='utf-8')

overview_path='Subject Overview Part 1.md'; allnodes=[(overview_path,5)]+node_data
nodes=[]
for i,(file,color) in enumerate(allnodes):
    col=i%3; row=i//3
    nodes.append({'id':f'n{i+1}','type':'file','file':file,'x':col*500,'y':row*180,'width':360,'height':130,'color':str(color)})
edges=[]
for i in range(1,8): edges.append({'id':f'e{len(edges)+1}','fromNode':'n1','fromSide':'right','toNode':f'n{i+1}','toSide':'left','color':'5'})
ch_nodes={chapters[i][0]:f'n{i+2}' for i in range(7)}
idx={file:f'n{i+1}' for i,(file,_) in enumerate(allnodes)}
for folder,data in [('Concepts',concepts),('Formulas',formulas),('Exercises',exercises)]:
    for item in data:
        title,chapter=item[0],item[1]; target=idx[f'{folder}/{title}.md']; source=ch_nodes[chapter]
        edges.append({'id':f'e{len(edges)+1}','fromNode':source,'fromSide':'right','toNode':target,'toSide':'left','color':'5'})
for a,b in [('Parallel Division and the Side-Splitter Result','Similarity and Scale Factor'),('Products and Areas with Square Roots','Algebraic Multiplication Identities'),('Signed Arithmetic','Solving a Pair of Linear Equations')]:
    edges.append({'id':f'e{len(edges)+1}','fromNode':idx[f'Concepts/{a}.md'],'fromSide':'right','toNode':idx[f'Concepts/{b}.md'],'toSide':'left','color':'6'})
(BASE/'Mathematics Part 1.canvas').write_text(json.dumps({'nodes':nodes,'edges':edges},indent=2),encoding='utf-8')
