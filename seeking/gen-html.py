import json
from collections import namedtuple
from datetime import date as d

resume = open('data.json')
data = json.load(resume,
                 object_hook=lambda d: namedtuple('X', d.keys())(*d.values()))
info = data[0]; ed = data[1]; work = data[2]; craft = data[3]
date = d.today().strftime('%Y.%m.%d')

def spannerWorks(data):
  l = len(data)
  notHere = 'I&rsquo;m not here'
  notHaps = 'This isn&rsquo;t happening'
  begin = '<span>'
  hidden = '<span class="howToDisappearCompletely">'
  close = '</span>'
  data = f'{data[:l*6//7]}{close}{data[l*6//7:]}'
  data = f'{data[:l*5//7]}{close}{data[l*5//7:]}'
  data = f'{data[:l*4//7]}{hidden}{notHaps}{close}{data[l*4//7:]}'
  data = f'{data[:l*3//7]}{begin}{data[l*3//7:]}'
  data = f'{data[:l*2//7]}{hidden}{notHere}{close}{data[l*2//7:]}'
  data = f'{data[:l*1//7]}{begin}{data[l*1//7:]}'
  return list(data)

def obfuscate(data):
  return dict(sorted(list(zip(range(len(data)), data)), key=lambda i: i[1]))

scrambledPhone = obfuscate(spannerWorks(info.phone))
scrambledEmail = obfuscate(spannerWorks(info.email))

def unpack(array):
  h = ''
  for val in array:
    h += f'{val}, '
  h = h[:-2]
  return h

T = True; F = False
def wrap(n,l,t,c,v): # newline, indent level, html tag, html class, value
  s = '  '
  n = f'\n{s*l}' if n else ''
  c = f' class="{c}"' if c else ''
  return f'{n}<{t}{c}>\n{s*l}  {v}\n{s*l}</{t}>'

def iter(a,l): # array of text strings, indent level
  s = ''
  for i in range(len(a)):
    s += wrap(i,l,'li','',a[i])
  return s

unscrambleJS = '''\
const unscramble = (dict) => {
  let text = ``, length = Object.keys(dict).length
  for (let i = 0; i < length; i++)
    text = `${text}${dict[i]}`
  return text
}\
'''
head = f'''
<!doctype html>
<html lang="en">
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">

<title>Jason Paul Richmond</title>

<!-- Fonts -->
<link rel="preconnect" href="https://fonts.gstatic.com">
<link href="https://fonts.googleapis.com/css2?family=Montserrat:ital,wght@0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,200;1,300;1,400;1,500;1,600;1,700;1,800;1,900&family=Zilla+Slab:ital,wght@0,300;0,400;0,500;0,600;0,700;1,300;1,400;1,500;1,600;1,700&display=swap" rel="stylesheet">

<link rel="stylesheet" href="style.css">
<script>
{unscrambleJS}
</script>
'''
body = wrap(F,0,'body','content',
  wrap(F,1,'header','info',
    wrap(F,2,'h1','name',
      wrap(F,3,'a href="home.html"','',info.name)
    )+
    wrap(T,2,'ul','info',
      wrap(F,2,'li','email',
        wrap(F,3,'script','',f'document.write(unscramble({scrambledEmail}))')
      )+
      wrap(T,2,'li','site',info.site)+
      wrap(T,2,'li','phone',
        wrap(F,3,'script','',f'document.write(unscramble({scrambledPhone}))')
      )+
      wrap(T,2,'li','site',date)
    )
  )+
  wrap(T,1,'section','aim',
    wrap(F,2,'ul','',
      iter(info.text,3)
    )
  )+
  wrap(T,1,'section','skills',
    wrap(F,2,'h2','title',f'{craft.name}')+
    wrap(T,2,'ul','',
      wrap(T,3,'li','',f'<span class="bullet">{craft.dev.lang.title.upper()}</span>: {unpack(craft.dev.lang.names)}')+
      wrap(T,3,'li','',f'<span class="bullet">{craft.dev.tool.title.upper()}</span>: {unpack(craft.dev.tool.names)}')+
      wrap(T,3,'li','',f'<span class="bullet">{craft.dev.meth.title.upper()}</span>: {unpack(craft.dev.meth.names)}')+
      wrap(T,3,'li','',f'<span class="bullet">{craft.dev.doms.title.upper()}</span>: {unpack(craft.dev.doms.names)}')
    )
  )+
  wrap(T,1,'section','work',
    wrap(F,2,'h2','heading','Work Experience')+
    wrap(T,2,'h3','role',work.aun.role)+
    wrap(T,2,'h4','place',work.aun.name.upper()+
      wrap(F,0,'span','right',f'{work.aun.start}'+' ~ '+f'{work.aun.end}')
    )+
    wrap(T,2,'ul','aun',
      iter(work.aun.text,3)
    )+
    wrap(T,2,'h3','role',work.sbcs.role)+
    wrap(T,2,'h4','place',work.sbcs.name.upper()+
      wrap(F,0,'span','right',f'{work.sbcs.start}'+' ~ '+f'{work.sbcs.end}')
    )+
    wrap(T,2,'ul','sbcs',
      iter(work.sbcs.text,3)
    )+
    wrap(T,2,'h3','role',work.ace.role+' ~ '+work.ace.sub)+
    wrap(T,2,'h4','place',work.ace.name.upper()+
      wrap(F,0,'span','right',f'{work.ace.start}'+' ~ '+f'{work.ace.end}')
    )+
    wrap(F,2,'ul','ace',
      iter(work.ace.text,3)
    )
  )+
  wrap(T,1,'section','education',
    wrap(F,2,'h2','heading','Academic Experience')+
    wrap(T,2,'h3','role',ed.grad.degree+' ~ '+ed.grad.major)+
    wrap(T,2,'h4','place',ed.grad.school.upper()+
      wrap(F,0,'span','right',ed.grad.year)
    )+
    wrap(T,2,'ul','grad',
      wrap(F,3,'li','',ed.grad.text[0])
    )
  )
)

open('../seeking.html', 'w').write(head + body)