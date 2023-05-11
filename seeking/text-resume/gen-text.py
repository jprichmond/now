import json; from collections import namedtuple; from datetime import date as d
###############################################################################################################
resume = open('../data.json'); date = d.today().strftime('%Y.%m.%d'); nl = '\n'; text = ''
dat = json.load(resume,object_hook=lambda d: namedtuple('X', d.keys())(*d.values()))
info = dat[0]; ed = dat[1]; work = dat[2]; craft = dat[3]; skl = craft.skills.name; dev = craft.skills.dev
cl = 31; gut = 5; cr = 75; t = 2; dent = 8; full = cl + gut + cr
# DISPLAY NAME IN LARGE ASCII FONT ############################################################################
def display(l,s=''):
  for i in range(len(l)):
    ((s := f'''{s}{l[i]*'/'}''') if i%2 else (s := f'''{s}{l[i]*' '}''')) # alternate spaces and numbers
  return s
## VALUES FOR DISPLAY FONT ####################################################################################
a = [5,5,3,3,5,4,4,4,3,3,3,2,4,6,3,2,2,5,2,2,3,2,1,3,4,3,3,4,3,3,3,2,1,5]
b = [7,2,2,2,1,2,2,2,6,2,4,2,1,4,2,2,4,2,3,2,2,2,1,2,3,2,1,2,3,2,1,4,2,4,1,2,4,2,1,4,2,2,1,2,2,2]
c = [6,2,1,2,3,2,3,3,3,2,4,2,1,2,1,5,4,6,3,2,1,2,6,7,1,2,1,4,1,2,1,2,4,2,1,2,1,5,1,2,3,2]
d = [0,2,3,2,1,7,6,2,1,2,4,2,1,2,3,3,4,2,3,2,2,2,1,2,3,2,1,2,3,2,1,2,2,2,2,2,1,2,4,2,1,2,3,3,1,2,3,2]
e = [0,5,2,2,3,2,1,6,4,4,3,2,4,2,4,2,4,2,1,2,2,5,2,2,3,2,1,2,6,2,3,4,3,2,4,2,1,6]
# CONTACT INFORMATION AND AIM #################################################################################
info_fields = f'EMAIL: {info.email} ~ TEXT: {info.phone} ~ SITE: {info.site} ~ DATE: {date}'
full_column = [nl,display(a),display(b),display(c),display(d),display(e),nl,
f'''{(full-len(info_fields)-7)*' '}{info_fields}\n\n*{(full-2)*'~'}*''',
f'''{dent*' '}* {info.text[0][:91]}\n{dent*' '}  {info.text[0][92:]}''',
f'''{dent*' '}* {info.text[1][:86]}\n{dent*' '}  {info.text[1][87:]}''',
f'''{dent*' '}* {info.text[2][:89]}\n{dent*' '}  {info.text[2][90:180]}''',
f'''{dent*' '}* {info.text[3][:91]}\n*{(full-2)*'~'}*''']
# DEV SKILLS ##################################################################################################
left_column = [f'''{skl.upper()}{(cl-len(skl.name))*' '}{gut*' '}''',f'''*{(cl-2)*'~'}*{(gut)*' '}''',
f'''{t*' '}{d[0]+(cl-len(dev[0])-t)*' '}{gut*' '}''',f'''{t*' '}{d[1]+(cl-len(dev[1])-t)*' '}{gut*' '}''',
f'''{t*' '}{d[0]+(cl-len(dev[2])-t)*' '}{gut*' '}''',f'''{t*' '}{d[1]+(cl-len(dev[3])-t)*' '}{gut*' '}''',
f'''{t*' '}{d[0]+(cl-len(dev[4])-t)*' '}{gut*' '}''',f'''{t*' '}{d[1]+(cl-len(dev[5])-t)*' '}{gut*' '}''',
f'''{t*' '}{d[0]+(cl-len(dev[6])-t)*' '}{gut*' '}''',f'''{t*' '}{d[1]+(cl-len(dev[7])-t)*' '}{gut*' '}''',
f'''{t*' '}{d[0]+(cl-len(dev[8])-t)*' '}{gut*' '}''',f'''{t*' '}{d[1]+(cl-len(dev[9])-t)*' '}{gut*' '}''',
f'''{t*' '}{d[0]+(cl-len(dev[10])-t)*' '}{gut*' '}''',f'''{t*' '}{d[1]+(cl-len(dev[11])-t)*' '}{gut*' '}''',
f'''{t*' '}{d[0]+(cl-len(dev[12])-t)*' '}{gut*' '}''',f'''{t*' '}{d[1]+(cl-len(dev[13])-t)*' '}{gut*' '}''',
f'''{t*' '}{d[0]+(cl-len(dev[14])-t)*' '}{gut*' '}''',f'''{t*' '}{d[1]+(cl-len(dev[15])-t)*' '}{gut*' '}''',
f'''{t*' '}{d[0]+(cl-len(dev[16])-t)*' '}{gut*' '}''',f'''{t*' '}{d[1]+(cl-len(dev[17])-t)*' '}{gut*' '}''',
f'''{t*' '}{d[0]+(cl-len(dev[18])-t)*' '}{gut*' '}''',f'''{t*' '}{d[1]+(cl-len(dev[19])-t)*' '}{gut*' '}''',]
# WORK EXPERIENCE #############################################################################################
wex = work.name; sbcs = work.sbcs; yrs = f'{sbcs.start} ~ {sbcs.end}'
right_column = [f'''{(cr-len(f'{wex}'))*' '}{wex.upper()}''',f'''*{(cr-2)*'~'}*''',
# SBCS ########################################################################################################
f'''{sbcs.role.upper()}{(cr-len(sbcs.role)-len(yrs))*' '}{yrs}''',f'''  {sbcs.name.title()}''',
f'''  * {sbcs.text[0][:71]}''',f'''    {sbcs.text[0][72:142]}''',f'''    {sbcs.text[0][142:]}''',
f'''  * {sbcs.text[1][:71]}''',f'''    {sbcs.text[1][72:143]}''',f'''    {sbcs.text[1][143:]}''',
f'''  * {sbcs.text[2][:71]}''',f'''    {sbcs.text[2][72:]}''',f'''  * {sbcs.text[3][:67]}''',
f'''    {sbcs.text[3][68:134]}''',f'''    {sbcs.text[3][135:]}''','',f'''*{(cr-2)*'~'}*''']
# ACE #########################################################################################################
ace = work.ace; yrs = f'{ace.start} ~ {ace.end}'
right_column += [f'''{ace.role.upper()}{(cr-len(ace.role)-len(yrs))*' '}{yrs}''',
f'''  {ace.name.title()}''',f'''  * {ace.text[0][:68]}''',f'''    {ace.text[0][69:138]}''',
f'''    {ace.text[0][139:]}''',f'''  * {ace.text[1][:70]}-''',f'''    {ace.text[1][70:]}''',
f'''  * {ace.text[2][:71]}''',f'''    {ace.text[2][72:]}''',f'''  * {ace.text[3][:71]}''',
f'''    {ace.text[3][72:]}''','',f'''*{(cr-2)*'~'}*''']
# ACADEMIC EXPERIENCE #########################################################################################
aex = ed.name; grad = ed.grad; deg = f'{grad.degree.upper()} ~ {grad.major.title()}'; g = 'gpa: '
right_column += [f'''{(cr-len(f'{aex}'))*' '}{aex.upper()}''',f'''*{(cr-2)*'~'}*''']
# GRAD ########################################################################################################
right_column += [f'''{deg}{(cr-len(deg)-len(grad.year))*' '}{grad.year}''', 
f'''  {grad.school.title()}{(cr-len(grad.school)-len(g)-len(str(grad.gpa))-2)*' '}{g.upper()}{grad.gpa}''',
f'''  * {grad.text[0][:71]}''',f'''    {grad.text[0][72:137]}''',f'''    {grad.text[0][138:208]}''',
f'''    {grad.text[0][209:]}''','',f'''*{(cr-2)*'~'}*'''];  proj = ed.grad.project
# PROJECT #####################################################################################################
right_column += [f'''{proj.name.upper()} ~ {proj.title.title()}''',f'''  * {proj.text[0][:66]}''',
f'''    {proj.text[0][67:134]}-''',f'''    {proj.text[0][134:199]}-''',f'''    {proj.text[0][199:]}''','',
f'''*{(cr-2)*'~'}*''']
# UNDERGRAD ###################################################################################################
un = ed.undergrad; maj = f'''{un.major.anth.title()}, {un.major.ling.title()}, {un.major.econ.title()}'''
right_column += [f'''{un.degree.upper()} ~ {maj}''',f'''  {un.school.title()}''']
# PRINT TEXT ##################################################################################################
for line in full_column:
  text += line + '\n'
leftright = zip(left_column,right_column)
for line in leftright:
  text += line[0] + line[1] + '\n'
# WRITE TO TEXT FILE ##########################################################################################
output = open('../text-resume/seeking.txt', 'w');output.write(text)
# GENERATE HTML VERSION OF TEXT FILE
output = open('../../seeking-text.html', 'w');output.write(f'''\
<!doctype html>
<html lang="en">
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">

<title>Jason Paul Richmond</title>

<!-- Fonts -->
<link rel="preconnect" href="https://fonts.gstatic.com">
<link href="https://fonts.googleapis.com/css2?family=Merriweather+Sans:ital,wght@0,300;0,400;0,500;0,600;0,700;0,800;1,300;1,400;1,500;1,600;1,700;1,800&family=Merriweather:ital,wght@0,300;0,400;0,700;0,900;1,300;1,400;1,700;1,900&family=Montserrat:ital,wght@0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,200;1,300;1,400;1,500;1,600;1,700;1,800;1,900&family=Zilla+Slab:ital,wght@0,300;0,400;0,500;0,600;0,700;1,300;1,400;1,500;1,600;1,700&family=DM+Mono:ital,wght@0,300;0,400;0,500;1,300;1,400;1,500&display=swap" rel="stylesheet">

<link rel="stylesheet" href="style.css">
<body class="content"><pre>
{text}
</pre>''')