"""Direct semistandard cell recursion; no branching or dimension formula."""
from collections import Counter
from pathlib import Path
from hashlib import sha256
import json

HERE=Path(__file__).resolve().parent
shape=(7,5,3)
cells=[(row,column) for row,length in enumerate(shape) for column in range(length)]
position={cell:index for index,cell in enumerate(cells)}
entries=[0]*len(cells)
tableaux=[]
visited=Counter()

def fill(index):
    visited[index]+=1
    if index==len(cells):
        tableaux.append(tuple(entries))
        return
    row,column=cells[index]
    minimum=1
    if column:
        minimum=max(minimum,entries[position[row,column-1]])
    if row:
        minimum=max(minimum,entries[position[row-1,column]]+1)
    for value in range(minimum,5):
        entries[index]=value
        fill(index+1)
    entries[index]=0

fill(0)
assert len(set(tableaux))==len(tableaux)
for tableau in tableaux:
    assert all(1<=value<=4 for value in tableau)
    for (row,column),index in position.items():
        if column:
            assert tableau[index]>=tableau[position[row,column-1]]
        if row:
            assert tableau[index]>tableau[position[row-1,column]]

counts=Counter(tableau.count(4) for tableau in tableaux)
assert dict(sorted(counts.items()))=={0:27,1:81,2:162,3:270,4:300,5:252,6:126,7:42}
total=sum(counts.values())
weighted=sum(k*m for k,m in counts.items())
even=sum(m for k,m in counts.items() if k%2==0)
odd=sum(m for k,m in counts.items() if k%2==1)
assert (total,weighted,even,odd)==(1260,4725,615,645)
content_sums=[sum(tableau.count(letter) for tableau in tableaux) for letter in range(1,5)]
assert content_sums==[4725]*4
serialized='\n'.join(''.join(map(str,tableau)) for tableau in tableaux)+'\n'
(HERE/'tableaux.txt').write_text(serialized)
receipt={'status':'pass','shape':shape,'alphabet':[1,2,3,4],
         'cell_order':cells,'method':'Row-major cell recursion; weak row and strict column constraints checked at every extension; no branching/dimension formula.',
         'multiplicity_by_number_of_fours':dict(sorted(counts.items())),
         'total':total,'weighted_sum':weighted,'even_count':even,'odd_count':odd,
         'signature':even-odd,'content_sums':content_sums,
         'visited_partial_tableaux_by_number_of_filled_cells':dict(sorted(visited.items())),
         'tableau_list_sha256':sha256((HERE/'tableaux.txt').read_bytes()).hexdigest()}
(HERE/'verification.json').write_text(json.dumps(receipt,indent=2)+'\n')
print(json.dumps({'status':'pass','counts':dict(sorted(counts.items())),'total':total,'weighted':weighted,'even':even,'odd':odd}))
