from pathlib import Path
import re

path=Path(__file__).with_name("single_primary_boundary_control.tex")
body=path.read_text(encoding="utf-8")
sequence=re.findall(r"\\tag\{SP\.(\d+)\}",body)
if sequence==[str(n) for n in list(range(1,30))+[35,36,30,31,32,33,34]]:
    mapping={35:30,36:31,30:32,31:33,32:34,33:35,34:36}
    body=re.sub(r"SP\.(\d+)",
                lambda x: "SP."+str(mapping.get(int(x.group(1)),int(x.group(1)))),
                body)
    path.write_text(body,encoding="utf-8")
assert re.findall(r"\\tag\{SP\.(\d+)\}",body)==[str(n) for n in range(1,37)]
