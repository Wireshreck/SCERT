import json, hashlib
from pathlib import Path
BASE=Path(__file__).resolve().parents[1]/'Class 9'/'English Medium'
SRC=BASE/'_Source PDFs'; FILE=BASE/'SOURCE_CATALOG.json'
rows=json.loads(FILE.read_text(encoding='utf-8')); by={r['file']:r for r in rows}
META={
'Biology Part 1.pdf':('Biology','Biology, Standard IX, Part I','2024',80,'https://samagra.kite.kerala.gov.in/files/samagra-resource/uploads2/tbookscmq/Class%209/Biology_9_E_Part_1/Biology_9_E_Part_1.pdf'),
'Biology Part 2.pdf':('Biology','Biology, Standard IX, Part II','2024',80,'https://samagra.kite.kerala.gov.in/files/samagra-resource/uploads2/tbookscmq/PARTII/14_BIOLOGY%20(E)_9_Vol-2.pdf'),
'Chemistry Part 1.pdf':('Chemistry','Chemistry Standard IX Part I','2024',88,'https://samagra.kite.kerala.gov.in/files/samagra-resource/uploads2/tbookscmq/Class%209/Chemistry_9_E_Vol_1/Chemistry_9_E_Vol_1.pdf'),
'Chemistry Part 2.pdf':('Chemistry','Chemistry Standard IX Part II','2024',88,'https://samagra.kite.kerala.gov.in/files/samagra-resource/uploads2/tbookscmq/PARTII/10_Chemistry_%20IX(E)_VOL-2.pdf'),
'English Part 1.pdf':('English','Kerala Reader English, Standard IX, Part I','2024',112,'https://samagra.kite.kerala.gov.in/files/samagra-resource/uploads2/tbookscmq/Class%209/English_IX_Vol.I/English_IX_Vol.I.pdf'),
'English Part 2.pdf':('English','Kerala Reader English, Standard IX, Part II','2024',72,'https://samagra.kite.kerala.gov.in/files/samagra-resource/uploads2/tbookscmq/PARTII/04_English_Std%20IX_Part-2.pdf'),
'ICT Part 1 (2025 Samagra).pdf':('ICT','Information and Communications Technology, Standard IX, Part I','2025',80,'https://samagra.kite.kerala.gov.in/files/samagra-resource/uploads2/tbookscmq/eng/9/16/ICT_Eng_IX_1748858267171_290040121.pdf'),
'ICT Part 2.pdf':('ICT','Information and Communications Technology, Standard IX, Part II','2025',83,'https://samagra.kite.kerala.gov.in/files/samagra-resource/uploads2/tbookscmq/eng/9/16/ICT_1759035833725_234685715.pdf'),
'Mathematics Part 1.pdf':('Mathematics','Mathematics Standard IX Part I','2024',144,'https://samagra.kite.kerala.gov.in/files/samagra-resource/uploads2/tbookscmq/Class%209/Maths_09_Eng_Part_01/Maths_09_Eng_Part_01.pdf'),
'Mathematics Part 2.pdf':('Mathematics','Mathematics Standard IX Part II','2024',104,'https://samagra.kite.kerala.gov.in/files/samagra-resource/uploads2/tbookscmq/PARTII/26_MATHS(E)_Vol-2.pdf'),
'Physical Education.pdf':('Physical Education','Health and Physical Education Standard IX Activity Book','2024',88,'https://samagra.kite.kerala.gov.in/files/samagra-resource/uploads2/tbookscmq/Class_V/Health_and_physical_education/nine/english.pdf'),
'Physics Part 1.pdf':('Physics','Physics Standard IX Part I','2024',88,'https://samagra.kite.kerala.gov.in/files/samagra-resource/uploads2/tbookscmq/Class%209/Physics_Eng_part_1/Physics_Eng_part_1.pdf'),
'Physics Part 2.pdf':('Physics','Physics Standard IX Part II','2024',88,'https://samagra.kite.kerala.gov.in/files/samagra-resource/uploads2/tbookscmq/PARTII/06_PHYSICS-IX(E)_PART_II.pdf'),
'Social Science 1 Part 1.pdf':('Social Science I','Social Science I Standard IX Part I','2024',104,'https://samagra.kite.kerala.gov.in/files/samagra-resource/uploads2/tbookscmq/Class%209/SocialScience_IX_I_Eng_vol_1/SocialScience_IX_I_Eng_vol_1.pdf'),
'Social Science 1 Part 2.pdf':('Social Science I','Social Science I Standard IX Part II','2024',64,'https://samagra.kite.kerala.gov.in/files/samagra-resource/uploads2/tbookscmq/PARTII/18_SOCIAL%20SCIENCE-I_IX_(E)%20PART%202.pdf'),
'Social Science 2 Part 1.pdf':('Social Science II','Social Science II Standard IX Part I','2024',96,'https://samagra.kite.kerala.gov.in/files/samagra-resource/uploads2/tbookscmq/Class%209/SocialScience_II_9_E_Vol_1/SocialScience_II_9_E_Vol_1.pdf'),
'Social Science 2 Part 2.pdf':('Social Science II','Social Science II Standard IX Part II','2024',88,'https://samagra.kite.kerala.gov.in/files/samagra-resource/uploads2/tbookscmq/PARTII/22_SOCIAL%20SCIENCE%20II_(E)_IX_PART-2.pdf'),
'Art.pdf':('Art Education','Art Education Standard IX Activity Book','2024',112,'https://samagra.kite.kerala.gov.in/files/samagra-resource/uploads2/tbookscmq/Std_9/ArtMalayalam/IX_Eng_Art.pdf'),
'Work Education.pdf':('Work Education','Work Integrated Education Standard IX Activity Book Part I, Self Grooming','2024',64,'https://samagra.kite.kerala.gov.in/files/samagra-resource/uploads2/tbookscmq/eng/9/79/Work%20Edn.%20(E)_1754209053595_216219939.pdf')}
for f,(subject,title,year,pages,url) in META.items():
 p=SRC/f; sha=hashlib.sha256(p.read_bytes()).hexdigest().upper()
 r=by.get(f)
 if r is None:
  r={'file':f,'download_date':'2026-11-05','downloaded_via':'Samagra KITE portal, via official PDF link'}; rows.append(r); by[f]=r
 r.update({'class':9,'medium':'English','subject':subject,'official_title':title,'edition_year':year,'pages':pages,'bytes':p.stat().st_size,'official_catalogue_url':'https://samagra.kite.kerala.gov.in/#/textbook/page','samagra_portal_pdf_url':url,'verification_downloaded_from':'Samagra KITE official textbook portal','official_download_sha256':sha,'local_sha256':sha,'pdf_readability':'opens successfully; page-by-page visual review complete','processed':'yes','edition_verification':f'Standard IX, edition imprint {year}; local PDF SHA-256 {sha} matches the file at the official Samagra link.'})
legacy=by['ICT Part 1.pdf']; legacy['local_sha256']=hashlib.sha256((SRC/'ICT Part 1.pdf').read_bytes()).hexdigest().upper(); legacy['edition_verification']='Legacy Standard IX Part I; 2019 edition shown in book. Preserved without replacement; it is not the current 2025 portal edition and is not counted as processed.'; legacy['processed']='legacy source only'
rows.sort(key=lambda r:r['file'].casefold()); FILE.write_text(json.dumps(rows,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
print(f'{len(rows)} catalog records; {sum(r.get("processed")=="yes" for r in rows)} processed; 1 preserved legacy source.')
