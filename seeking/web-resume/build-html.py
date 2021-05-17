import json
from collections import namedtuple
from datetime import date as d

resume = open('../data.json')
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

T = True; F = False; w = F; web_dev = 'Web Dev'; data_sci = 'Data Science'
def wrap(n,l,t,c,v): # newline, indent level, html tag, html class, value
  s = '  '
  n = f'\n{s*l}' if n else ''
  c = f' class="{c}"' if c else ''
  return f'{n}<{t}{c}>\n{s*l}  {v}\n{s*l}</{t}>'

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
<link href="https://fonts.googleapis.com/css2?family=Merriweather+Sans:ital,wght@0,300;0,400;0,500;0,600;0,700;0,800;1,300;1,400;1,500;1,600;1,700;1,800&family=Merriweather:ital,wght@0,300;0,400;0,700;0,900;1,300;1,400;1,700;1,900&family=Montserrat:ital,wght@0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,200;1,300;1,400;1,500;1,600;1,700;1,800;1,900&family=Zilla+Slab:ital,wght@0,300;0,400;0,500;0,600;0,700;1,300;1,400;1,500;1,600;1,700&display=swap" rel="stylesheet">

<link rel="stylesheet" href="style.css">
<script>
{unscrambleJS}
</script>
'''
body = wrap(F,0,'body','content',
  wrap(F,1,'header','info',
    wrap(F,2,'h1','name',info.name)+
    wrap(T,2,'ul','info',
      wrap(F,2,'li','site',date)+
      wrap(T,2,'li','site',info.site)+
      wrap(T,2,'li','email',
        wrap(F,3,'script','',f'document.write(unscramble({scrambledEmail}))')
      )+
      wrap(T,2,'li','phone',
        wrap(F,3,'script','',f'document.write(unscramble({scrambledPhone}))')
      )
    )
  )+
  wrap(T,1,'section','aim',
    wrap(F,2,'ul','',
      wrap(F,3,'li','',info.text[0])+
      wrap(T,3,'li','',info.text[1])+
      wrap(T,3,'li','',info.text[2])+
      wrap(T,3,'li','',info.text[3])
    )
  )+
  wrap(T,1,'section','work',
    wrap(F,2,'h2','heading','Work Experience')+
    wrap(T,2,'h3','role',work.sbcs.role)+
    wrap(T,2,'h4','workplace',work.sbcs.name.upper()+
      wrap(F,0,'span','',f'{work.sbcs.start}'+' ~ '+f'{work.sbcs.end}')
    )+
    wrap(T,2,'ul','sbcs',
      wrap(F,3,'li','',work.sbcs.text[0])+ # FIX DATA
      wrap(T,3,'li','',work.sbcs.text[1])+
      wrap(T,3,'li','',work.sbcs.text[2])+
      wrap(T,3,'li','',work.sbcs.text[3])
    )+
    wrap(T,2,'h3','work',work.ace.role+' ~ '+work.ace.cs
    )+
    wrap(T,2,'h4','work',work.ace.name.upper()+
      wrap(F,0,'span','',f'{work.ace.start}'+' ~ '+f'{work.ace.end}')
    )+
    wrap(F,2,'ul','ace',
      wrap(F,3,'li','',work.ace.text[0])+
      wrap(T,3,'li','',work.ace.text[1])+
      wrap(T,3,'li','',work.ace.text[2])+
      wrap(T,3,'li','',work.ace.text[3])
    )
  )+
  wrap(T,1,'section','skills',
    wrap(F,2,'h2','title',f'{web_dev if w else data_sci} Skills')+
    (wrap(T,2,'ul','',
      wrap(F,3,'li','','ACQUIRING: '+unpack(craft.skills.web.acquiring))+
      wrap(T,3,'li','','EMPLOYING: '+unpack(craft.skills.web.employing))+
      wrap(T,3,'li','','MASTERING: '+unpack(craft.skills.web.mastering))
    ) if w else '' )+
    (wrap(T,2,'ul','',
      wrap(F,3,'li','','ACQUIRING: '+unpack(craft.skills.data.acquiring))+
      wrap(T,3,'li','','EMPLOYING: '+unpack(craft.skills.data.employing))+
      wrap(T,3,'li','','MASTERING: '+unpack(craft.skills.data.mastering))
    ) if not w else '')
  )+
  wrap(T,1,'section','additional',
    wrap(F,2,'h2','title','Additional Skills')+
    wrap(T,2,'ul','',
      wrap(F,3,'li','',unpack(craft.skills.dev))
    )
  )+
  wrap(T,1,'section','education',
    wrap(F,2,'h2','heading','Academic Experience')+
    wrap(T,2,'h3','role',ed.grad.degree)+
    wrap(T,2,'h4','place',ed.grad.school.upper()+
      wrap(F,0,'span','',ed.grad.year)
    )+
    wrap(T,2,'ul','sbcs',
      wrap(F,3,'li','',ed.grad.text[0])
    )+

    wrap(T,2,'h4','project',ed.grad.project.name.upper())+
    wrap(F,2,'ul','project',
      wrap(F,3,'li','',ed.grad.project.text[0])+
      wrap(T,3,'li','',ed.grad.project.text[1])
    )
  )
)


output = open('../../resume.html', 'w')

output.write(head + body)








# sk = '{h}: {s}'; n = '\n';

'''
<body>
  <div class="blue">
    <h1 class="top"><a href="resume/index.md">{info.name}</a></h1>
  </div>
  <div class="content">
    <section class="">
      <h5 class="info">
        <span class=""><i>date</i>:&nbsp;{date}</span>
        <span class="">
        <i>phone</i>:&nbsp;<script>
          document.write(unscramble({scrambledPhone}))
        </script>
        </span>
        <span class="">
        <i>email</i>:&nbsp;<script>
          document.write(unscramble({scrambledEmail}))
        </script></span>
      </h5>
      <article>
        <p>{info.text}</p> <<<<###############################
      </article>
    </section>

    <section class="">
      <h2>WORK EXPERIENCE</h2>

      <header class="left">
        <h3>
          {work.sbcs.role}
          <span class="">{work.sbcs.start} ~ {work.sbcs.end}</span>
        </h3>
        <h3>{work.sbcs.name.upper()}</h3>
      </header>

      <article>
        <p>{work.sbcs.text} </p>
      </article>

      <header class="">
        <h3>{work.ace.role} ~ {work.ace.cs}
        <span class="">{work.ace.start} ~ {work.ace.end}</span></h3>
        <h3>{work.ace.name.upper()}</h3>
      </header>

      <article>
        <p>{work.ace.text} </p>
      </article>
    </section>

    <section class="">
      <h2>EDUCATION</h2>

      <header>
        <h3>
          {ed.grad.degree.upper()}: <i>{ed.grad.major}</i>
          <span class="">{ed.grad.year}<span>
        </h3>
        <h3>
          {ed.grad.school.upper()}<span class=""> GPA: {ed.grad.gpa}<span>
        </h3>
      </header>

      <article>
        <p>{ed.grad.text}</p>
      </article>

      <header class="">
        <h4>
          {ed.grad.project.name.upper()}: <i>{ed.grad.project.title}</i>
        </h4>
      </header>

      <article>
        <p>{ed.grad.project.text} </p>
      </article>

      <header class="">
        <h4>
          {ed.undergrad.degree.upper()}: <i>{ed.undergrad.major.ling}, {ed.undergrad.major.anth}, {ed.undergrad.major.econ}</i>
        </h4>
        <h4>
          {ed.undergrad.school.upper()}
        </h4>
      </header>
    </section>

    <section class="">
      <h2>ASSORTED KNOW-HOW</h2>

        <h3>SKILLS</h3>
        <p><span class="mono-thin">
        ACQUIRING:<span> {unpack(craft.skills.web.acquiring)}, 
        {unpack(craft.skills.dev.acquiring)}</p>
        <p><span class="mono-thin">
        EMPLOYING:<span> {unpack(craft.skills.web.employing)}, 
        {unpack(craft.skills.dev.employing)}</p>
        <p><span class="mono-thin">
        MASTERING:<span> {unpack(craft.skills.web.mastering)}</p>

        <h3>TOOLS</h3>
        <p><span class="mono-thin">
        ACQUIRING:<span> {unpack(craft.tools.web.acquiring)}, 
        {unpack(craft.tools.dev.acquiring)}</p>
        <p><span class="mono-thin">
        EMPLOYING:<span> {unpack(craft.tools.web.employing)}, 
        {unpack(craft.tools.dev.employing)}</p>
        <p><span class="mono-thin">
        MASTERING:<span> {unpack(craft.tools.web.mastering)}
        </p>

        <h3>LANGUAGES</h3>
        <p><span class="mono-thin">
        ACQUIRING:<span> {unpack(craft.languages.dev.acquiring)}
        {unpack(craft.languages.other.acquiring)}</p>
        <p><span class="mono-thin">
        EMPLOYING:<span> {unpack(craft.languages.dev.employing)}, 
        {unpack(craft.languages.other.employing)}</p>
        <p><span class="mono-thin">
        MASTERING:<span> {unpack(craft.languages.dev.mastering)}, 
        {unpack(craft.languages.other.mastering)}</p>
  
    </section>
  </div>
<body>
</html>
'''