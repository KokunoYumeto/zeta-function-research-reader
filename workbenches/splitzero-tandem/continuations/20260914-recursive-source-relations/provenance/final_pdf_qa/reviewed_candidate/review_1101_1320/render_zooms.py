from pathlib import Path
import subprocess,json
P=Path(__file__).parent
pdf=Path(r'repository:\Split_Zero_Cohomology_and_Arithmetic_Weight_Control.pdf')
poppler=r'local:user-profile\.cache\codex-runtimes\codex-primary-runtime\dependencies\native\poppler\Library\bin\pdftoppm.exe'
pages=[1113,1136,1137,1144,1179,1199,1205,1208,1219,1222,1233,1244,1249,1257,1258,1263,1265,1267,1276,1278,1283,1291,1295,1297,1300,1309,1310,1318]
for page in pages:
 subprocess.run([poppler,'-f',str(page),'-l',str(page),'-r','144','-singlefile','-png',str(pdf),str(P/'zooms'/f'page_{page}')],check=True)
print(json.dumps({'zoom_pages':pages}))
