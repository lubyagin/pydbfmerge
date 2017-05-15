# pydbfmerge
Merge DBF-files, console app

Программа объединения произвольного кол-ва DBF файлов с одинаковой заголовочной структурой.
Написана по той причине, что в Microsoft Excel 2007 и старше - нет сохранения в формат DBF IV (такая возможность была в Excel 2003).
В файле README приведён пример правильного использования newRecord+store().

```
#!/usr/bin/python
# -*- coding: windows-1251 -*-

# Help
# http://dbfpy.sourceforge.net/
# dbfpy version 2.0.0

# Distrib at https://sourceforge.net/projects/dbfpy/files/dbfpy/
# dbfpy-2.3.1.win32.exe (2015)

from dbfpy import dbf

SCHEMA = [
('F', 'C', 1)
]

db = dbf.Dbf("store.dbf", new=True)
db.addField(*SCHEMA)

# See help(db) for hints

rec = db.newRecord()
rec["F"] = "1"
db.append(rec)
#rec.store

rec = db.newRecord()
rec["F"] = "2"
db.append(rec)
#rec.store

#print db.changed

db.flush()
db.close()
```
