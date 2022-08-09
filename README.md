# DBV_rename
Pythonscript to rename service billings ("Leistungsabrechnung") from DBV (Deutsche Beamtenversicherung - Part of AXA Insurance)

**Before conversion:**

> 2-AXA384274625.pdf.pdf


**After converting:**

> 2018-12-03_DKB_Leistungsabrechnung.pdf

**How to/Installation:** 

Install dependency packages:
```
pip install sys
pip install os
pip install re
pip install PyPDF2
pip install pathlib
```

Just download the consors_unname.py and drag and drop your documents on it. 

(!) BE CAREFUL -> They'll be converted / renamed automatically (!)

Make sure you'll have them backup'ed. 

**Requirements:**
- python 3.x
- Used packages: pathlib, os, sys, re, PyPDF2
- Windows OS (Linux need's a bit of adjustment))
