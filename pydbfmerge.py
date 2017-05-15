#!/usr/bin/python
# -*- coding: windows-1251 -*-

# Сделано на основе https://gist.github.com/bertspaan/8220892
# И переработано "с нуля", используя http://grishaev.me/2012/08/29/1/
# Решена проблема сохранения записей: newRecord+store()

from sys import argv,exit

if len(argv) < 3: exit()

from dbfpy import dbf
# dbfpy-2.3.1.win32.exe (2015)
# https://sourceforge.net/projects/dbfpy/files/dbfpy/

# открыть все файлы, кроме последнего, на чтение
dbfs = [dbf.Dbf(name) for name in argv[1:-1]]
print len(dbfs)

# создать по имени последнего аргумента командной строки
db3 = dbf.Dbf(argv[-1], new=True)

# справочный абзац
from pprint import pprint
names = [ x.name for x in dbfs[0].header.fields ]
schema = [ x.fieldInfo() for x in dbfs[0].header.fields ]
print schema
pprint(schema)

# прописать заголовок в новый файл
db3.addField(*schema)

def wr(db):
  for rec0 in db:
    rec3 = db3.newRecord()
    #rec3.store
    for k in names:
      rec3[k] = rec0[k]
    db3.append(rec3)

# добавить контент всех предыдущих файлов в новый
for db in dbfs:
  wr(db)
  db.close()

db3.flush() # сбросить буфер и закрыть
db3.close()
