# GENERATE TEXT RESUME FROM DATA ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
import json
from collections import namedtuple
from datetime import date as d

data = json.load(open('data.json'), object_hook=lambda d: namedtuple('X', d.keys())(*d.values()))
letters = json.load(open('ascii.json'))
info, ed, work, craft, cl, gut, cr, t, sp = data[0], data[1], data[2], data[3], 31, 5, 75, 2, ' '
text, date, full, dev = '', d.today().strftime('%Y.%m.%d'), cl + gut + cr, craft.dev
deg, g = f'{ed.grad.degree.upper()} ~ {ed.grad.major.title()}', 'gpa: '

def display_name(n, letters, char, italic=True): # display name in ascii characters
  s, lines = '', []
  for line in range(len(letters[' '])):
    lines.append('')
  for ch in n.upper():
    for line in range(len(letters[ch])):
      for l in letters[ch][line]:
        lines[line] = f'''{lines[line]} ''' if l == sp else f'''{lines[line]}{char}'''
      lines[line] += sp
  for i in range(len(lines)):
    x = len(lines[i])-1
    while lines[i][x] == sp: x -= 1
    s += (sp*(len(lines)-i) if italic else '') + lines[i][:x+1] + '\n'
  return s

def bullet(s, mx, dent): # generate bullet
  a, s, i = [], sp*dent+'* '+s, 0
  while len(s) > mx:
    i = mx
    while s[i] != sp: i -= 1
    a.append(s[:i])
    s = sp*dent+sp+s[i:]
  a.append(s)
  return a

def bullets(arr, mx, dent): # generate bullets
  a = []
  [a.extend(bullet(s, mx, dent)) for s in arr]
  return a

def skills(obj): # generate skills text
  a = []
  a.append(f'''{obj.title.upper()+':'+(cl-len(obj.title)+1-t)*sp}{gut*sp}''') 
  [a.append(f'''{t*sp}{n+(cl-len(n)-t)*sp}{gut*sp}''') for n in obj.names]
  a.append(cl*sp+gut*sp)
  return a

def jobs(emp, sub=False): # generate work text 
  a, subject = [f'''*{(cr-2)*'~'}*'''], f'''{emp.role.upper()}{' ~ '+emp.sub if sub else ''}'''
  a.append(f'''{subject}{(cr-len(subject)-len(yrs := f'{emp.start} ~ {emp.end}'))*sp}{yrs}''')
  a.extend([f'''  {emp.name.title()}'''] + bullets(emp.text, 71, 2))
  return a

info_fields = f'EMAIL: {info.email} ~ TEXT: {info.phone} ~ SITE: {info.site} ~ DATE: {date}'
full_column = ['\n', display_name(info.name, letters, '/'), '']
full_column += [f'''{(full-len(info_fields)-7)*sp}{info_fields}\n\n*{(full-2)*'~'}*''']
full_column += bullets(info.text, 103, 8) +[f'''\n*{(full-2)*'~'}*''']
left_column = [f'''{craft.name.upper()}{(cl-len(craft.name))*sp}{gut*sp}''', f'''*{(cl-2)*'~'}*{(gut)*sp}''']
left_column += skills(dev.lang) + skills(dev.meth) + skills(dev.tool) + skills(dev.doms)
right_column = [f'''{(cr-len(f'{work.name}'))*sp}{work.name.upper()}''']
right_column += jobs(work.aun) + jobs(work.sbcs) + jobs(work.ace, True)
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