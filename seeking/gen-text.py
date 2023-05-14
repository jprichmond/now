# GENERATE TEXT RESUME FROM DATA ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
import json
from collections import namedtuple
from datetime import date as d

data = json.load(open('data.json'), object_hook=lambda d: namedtuple('X', d.keys())(*d.values()))
info, ed, work, craft, cl, gut, cr, t, sp = data[0], data[1], data[2], data[3], 31, 5, 75, 2, ' '
text, date, full = '', d.today().strftime('%Y.%m.%d'), cl + gut + cr

def display(l, s=''): # display one line at a time
  for i in range(len(l)):
    (s := f'''{s}{l[i]*'/'}''') if i%2 else (s := f'''{s}{l[i]*sp}''') # alternate spaces and numbers
  return s

_1 = [5,5,3,3,5,4,4,4,3,3,3,2,4,6,3,2,2,5,2,2,3,2,1,3,4,3,3,4,3,3,3,2,1,5] # values for display
_2 = [7,2,2,2,1,2,2,2,6,2,4,2,1,4,2,2,4,2,3,2,2,2,1,2,3,2,1,2,3,2,1,4,2,4,1,2,4,2,1,4,2,2,1,2,2,2]
_3 = [6,2,1,2,3,2,3,3,3,2,4,2,1,2,1,5,4,6,3,2,1,2,6,7,1,2,1,4,1,2,1,2,4,2,1,2,1,5,1,2,3,2]
_4 = [0,2,3,2,1,7,6,2,1,2,4,2,1,2,3,3,4,2,3,2,2,2,1,2,3,2,1,2,3,2,1,2,2,2,2,2,1,2,4,2,1,2,3,3,1,2,3,2]
_5 = [0,5,2,2,3,2,1,6,4,4,3,2,4,2,4,2,4,2,1,2,2,5,2,2,3,2,1,2,6,2,3,4,3,2,4,2,1,6]

def bullet(s, mx, dent): # generate bullet
  a, s, i = [], sp*dent+'* '+s, 0
  while (len(s) > mx):
    i = mx
    while (s[i] != sp): i -= 1
    a.append(s[:i])
    s = sp*dent+sp+s[i:]
  a.append(s)
  return a

def bullets(arr, mx, dent): # generate bullets
  a = []
  [a.extend(bullet(s, mx, dent)) for s in arr]
  return a

info_fields = f'EMAIL: {info.email} ~ TEXT: {info.phone} ~ SITE: {info.site} ~ DATE: {date}'
full_column = ['\n', display(_1), display(_2), display(_3), display(_4), display(_5), '\n',
f'''{(full-len(info_fields)-7)*sp}{info_fields}\n\n*{(full-2)*'~'}*'''] + bullets(info.text, 103, 8)
full_column += [f'''\n*{(full-2)*'~'}*''']

def skills(obj): # generate skills text
  a = []
  a.append(f'''{obj.title.upper()+':'+(cl-len(obj.title)+1-t)*sp}{gut*sp}''') 
  [a.append(f'''{t*sp}{n+(cl-len(n)-t)*sp}{gut*sp}''') for n in obj.names]
  a.append(cl*sp+gut*sp)
  return a

dev = craft.dev
left_column = [f'''{craft.name.upper()}{(cl-len(craft.name))*sp}{gut*sp}''', f'''*{(cl-2)*'~'}*{(gut)*sp}''']
left_column += skills(dev.prog) + skills(dev.lang) + skills(dev.meth) + skills(dev.tool) + skills(dev.doms)

def jobs(emp, sub=False): # generate work text 
  a = [f'''*{(cr-2)*'~'}*''']; subject = f'''{emp.role.upper()}{' ~ '+emp.sub if sub else ''}'''
  a.append(f'''{subject}{(cr-len(subject)-len(yrs := f'{emp.start} ~ {emp.end}'))*sp}{yrs}''')
  a.extend([f'''  {emp.name.title()}'''] + bullets(emp.text, 71, 2))
  return a

right_column = [f'''{(cr-len(f'{work.name}'))*sp}{work.name.upper()}''']
right_column += jobs(work.aun) + jobs(work.sbcs) + jobs(work.ace, True)

deg, g = f'{ed.grad.degree.upper()} ~ {ed.grad.major.title()}', 'gpa: '
right_column += ['', f'''{(cr-len(f'{ed.name}'))*sp}{ed.name.upper()}''', f'''*{(cr-2)*'~'}*''',
f'''{deg}{(cr-len(deg)-len(ed.grad.year))*sp}{ed.grad.year}''', 
f'''  {ed.grad.school.title()}{(cr-len(ed.grad.school)-len(g)-len(str(ed.grad.gpa))-2)*sp}''' +
f'''{g.upper()}{ed.grad.gpa}'''] + bullets(ed.grad.text, 71, 2)

for line in full_column: # print text
  text += line + '\n'
leftright = zip(left_column, right_column)
for line in leftright:
  text += line[0] + line[1] + '\n'
text += f'''\n\n{(full//2-len('~ * ~')//2)*sp}~ * ~\n\n\n'''
                                                    
open('seeking.txt', 'w').write(text)
# THE END ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#