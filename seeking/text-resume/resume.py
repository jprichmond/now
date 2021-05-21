import json; from collections import namedtuple; from datetime import date as d
##############################################################################################################
resume = open('../data.json')
dat = json.load(resume,object_hook=lambda d: namedtuple('X', d.keys())(*d.values()))
info = dat[0]; ed = dat[1]; work = dat[2]; craft = dat[3]; web = craft.skills.web; data = craft.skills.data
date = d.today().strftime('%Y.%m.%d'); 
cl = 31; gut = 5; cr = 75; bs = '\\'; t = 2; indent = 8; full = cl + gut + cr; nl = '\n'
# DISPLAY NAME IN LARGE ASCII FONT ###########################################################################
def display(l,s=''):
  for i in range(len(l)):
    ((s := f'''{s}{l[i]*'/'}''') if i%2 else (s := f'''{s}{l[i]*' '}''')) # alternate spaces and numbers
  return s
## VALUES FOR DISPLAY FONT ###################################################################################
a = [5,5,3,3,5,4,4,4,3,3,3,2,4,6,3,2,2,5,2,2,3,2,1,3,4,3,3,4,3,3,3,2,1,5]
b = [7,2,2,2,1,2,2,2,6,2,4,2,1,4,2,2,4,2,3,2,2,2,1,2,3,2,1,2,3,2,1,4,2,4,1,2,4,2,1,4,2,2,1,2,2,2]
c = [6,2,1,2,3,2,3,3,3,2,4,2,1,2,1,5,4,6,3,2,1,2,6,7,1,2,1,4,1,2,1,2,4,2,1,2,1,5,1,2,3,2]
d = [0,2,3,2,1,7,6,2,1,2,4,2,1,2,3,3,4,2,3,2,2,2,1,2,3,2,1,2,3,2,1,2,2,2,2,2,1,2,4,2,1,2,3,2,1,2,3,2]
e = [0,5,2,2,3,2,1,6,4,4,3,2,4,2,4,2,4,2,1,2,2,5,2,2,3,2,1,2,6,2,3,4,3,2,3,2,1,6]
# CONTACT INFORMATION AND AIM #################################################################################
info_fields = f'EMAIL: {info.email} ~ TEXT: {info.phone} ~ SITE: {info.site}'
full_column = [nl,display(a),display(b),display(c),display(d),display(e),nl,
f'''{(full-len(info_fields)-7)*' '}{info_fields}\n\n*{(full-2)*'~'}*''',
f'''{indent*' '}* {info.text[0][:91]}\n{indent*' '}  {info.text[0][92:]}''',
f'''{indent*' '}* {info.text[1][:86]}\n{indent*' '}  {info.text[1][87:]}''',
f'''{indent*' '}* {info.text[2][:89]}\n{indent*' '}  {info.text[2][90:180]}''',
f'''{indent*' '}* {info.text[3][:91]}\n*{(full-2)*'~'}*''']
# WEB SKILLS ACQUIRING ########################################################################################
wds = 'web development skills'; lvl = 'acquiring'; w = web.acquiring; 
left_column = [f'''{f'{wds.upper()}'+(cl-len(f'{wds}'))*' '}{gut*' '}''',f'''*{(cl-2)*'~'}*{(gut)*' '}''',
f'''{lvl.upper()}:{(cl-len(lvl+':'))*' '}{gut*' '}''',f'''{t*' '}{w[0]+(cl-len(w[0])-t)*' '}{gut*' '}''',
f'''{t*' '}{w[1]+(cl-len(w[1])-t)*' '}{gut*' '}''',f'''{t*' '}{w[2]+(cl-len(w[2])-t)*' '}{gut*' '}''',
f'''{t*' '}{w[3]+(cl-len(w[3])-t)*' '}{gut*' '}''',f'''{t*' '}{w[4]+(cl-len(w[4])-t)*' '}{gut*' '}''',
f'''{t*' '}{w[5]+(cl-len(w[5])-t)*' '}{gut*' '}''',f'''{t*' '}{w[6]+(cl-len(w[6])-t)*' '}{gut*' '}''',
f'''{t*' '}{w[7]+(cl-len(w[7])-t)*' '}{gut*' '}''',f'''{t*' '}{w[8]+(cl-len(w[8])-t)*' '}{gut*' '}''',
f'''{t*' '}{w[9]+(cl-len(w[9])-t)*' '}{gut*' '}''']
# WEB SKILLS EMPLOYING ########################################################################################
lvl = 'employing'; w = web.employing
left_column += [f'''{lvl.upper()}:{(cl-len(lvl+':'))*' '}{gut*' '}''',
f'''{t*' '}{w[0]+(cl-len(w[0])-t)*' '}{gut*' '}''',f'''{t*' '}{w[1]+(cl-len(w[1])-t)*' '}{gut*' '}''',
f'''{t*' '}{w[2]+(cl-len(w[2])-t)*' '}{gut*' '}''',f'''{t*' '}{w[3]+(cl-len(w[3])-t)*' '}{gut*' '}''',
f'''{t*' '}{w[4]+(cl-len(w[4])-t)*' '}{gut*' '}''',f'''{t*' '}{w[5]+(cl-len(w[5])-t)*' '}{gut*' '}''',
f'''{t*' '}{w[6]+(cl-len(w[6])-t)*' '}{gut*' '}''',f'''{t*' '}{w[7]+(cl-len(w[7])-t)*' '}{gut*' '}''',
f'''{t*' '}{w[8]+(cl-len(w[8])-t)*' '}{gut*' '}''',f'''{(cl+gut)*' '}''']
# DATA SKILLS ACQUIRING #######################################################################################
lvl = 'acquiring'; d = data.acquiring; des = 'data engineering skills'
left_column += [f'''{f'{des.upper()}'+(cl-len(f'{des}'))*' '}{gut*' '}''',f'''*{(cl-2)*'~'}*{(gut)*' '}''',
f'''{lvl.upper()}:{(cl-len(lvl+':'))*' '}{gut*' '}''',f'''{t*' '}{d[0]+(cl-len(d[0])-t)*' '}{gut*' '}''',
f'''{t*' '}{d[1]+(cl-len(d[1])-t)*' '}{gut*' '}''',f'''{t*' '}{d[2]+(cl-len(d[2])-t)*' '}{gut*' '}''',
f'''{t*' '}{d[3]+(cl-len(d[3])-t)*' '}{gut*' '}''',f'''{t*' '}{d[4]+(cl-len(d[4])-t)*' '}{gut*' '}''',
f'''{t*' '}{d[5]+(cl-len(d[5])-t)*' '}{gut*' '}''',f'''{t*' '}{d[6]+(cl-len(d[6])-t)*' '}{gut*' '}''',]
# DATA SKILLS EMPLOYING #######################################################################################
lvl = 'employing'; d = data.employing
left_column += [f'''{lvl.upper()}:{(cl-len(lvl+':'))*' '}{gut*' '}''',
f'''{t*' '}{d[0]+(cl-len(d[0])-t)*' '}{gut*' '}''',f'''{t*' '}{d[1]+(cl-len(d[1])-t)*' '}{gut*' '}''',
f'''{t*' '}{d[2]+(cl-len(d[2])-t)*' '}{gut*' '}''',f'''{t*' '}{d[3]+(cl-len(d[3])-t)*' '}{gut*' '}''',
f'''{t*' '}{d[0]+(cl-len(d[4])-t)*' '}{gut*' '}''']
# OTHER DEV KNOW-HOW ##########################################################################################
other = 'other development know-how'; d = craft.skills.dev
left_column += [f'''{lvl.upper()}:{(cl-len(lvl+':'))*' '}{gut*' '}''',
f'''{t*' '}{d[1]+(cl-len(d[1])-t)*' '}{gut*' '}''',f'''{t*' '}{d[2]+(cl-len(d[2])-t)*' '}{gut*' '}''',
f'''{t*' '}{d[3]+(cl-len(d[3])-t)*' '}{gut*' '}''',f'''{t*' '}{d[4]+(cl-len(d[4])-t)*' '}{gut*' '}''',
f'''{t*' '}{d[5]+(cl-len(d[5])-t)*' '}{gut*' '}''',f'''{t*' '}{d[6]+(cl-len(d[6])-t)*' '}{gut*' '}''',
f'''{t*' '}{d[5]+(cl-len(d[5])-t)*' '}{gut*' '}''',f'''{t*' '}{d[6]+(cl-len(d[6])-t)*' '}{gut*' '}''',
f'''{t*' '}{d[5]+(cl-len(d[7])-t)*' '}{gut*' '}''',f'''{t*' '}{d[6]+(cl-len(d[8])-t)*' '}{gut*' '}''',]
# WORK EXPERIENCE #############################################################################################
wex = 'work experience'; sbcs = work.sbcs; yrs = f'{sbcs.start} ~ {sbcs.end}'
right_column = [f'''{(cr-len(f'{wex}'))*' '}{wex.upper()}''',
f'''*{(cr-2)*'-'}*''',
# SBCS ########################################################################################################
f'''{sbcs.role.upper()}{(cr-len(sbcs.role)-len(yrs))*' '}{yrs}''',f'''  {sbcs.name.upper()}''',
f'''  * {sbcs.text[0][:71]}''',f'''    {sbcs.text[0][72:142]}''',f'''    {sbcs.text[0][142:]}''',
f'''  * {sbcs.text[1][:71]}''',f'''    {sbcs.text[1][72:143]}''',f'''    {sbcs.text[1][143:]}''',
f'''  * {sbcs.text[2][:71]}''',f'''    {sbcs.text[2][72:]}''',
f'''  * {sbcs.text[3][:68]}''','',f'''*{(cr-2)*'~'}*''']
# ACE #########################################################################################################
ace = work.ace; yrs = f'{ace.start} ~ {ace.end}'
right_column += [f'''{ace.role.upper()}{(cr-len(ace.role)-len(yrs))*' '}{yrs}''',
f'''  {ace.name.upper()}''',f'''  * {ace.text[0][:68]}''',f'''    {ace.text[0][69:138]}''',
f'''    {ace.text[0][139:]}''',f'''  * {ace.text[1][:65]}''',f'''    {ace.text[1][66:]}''',
f'''  * {ace.text[2][:71]}''',f'''    {ace.text[2][72:]}''',f'''  * {ace.text[3][:71]}''',
f'''    {ace.text[3][72:140]}''','',f'''*{(cr-2)*'~'}*''']
# EDUCATION ###################################################################################################
edu = 'education'; grad = ed.grad; deg = f'{grad.degree} ~ {grad.major}'; gpa = str(grad.gpa); g = 'gpa: '
right_column += [f'''{(cr-len(f'{edu}'))*' '}{edu.upper()}''',f'''*{(cr-2)*'~'}*''',
# GRAD ########################################################################################################
f'''{deg.upper()}{(cr-len(deg)-len(grad.year))*' '}{grad.year}''',
f'''  {grad.school.upper()}{(cr-len(grad.school)-len(g)-len(gpa)-2)*' '}{g.upper()}{grad.gpa}''',
f'''  * {grad.text[0][:71]}''',f'''    {grad.text[0][72:137]}''',f'''    {grad.text[0][138:208]}''',
f'''    {grad.text[0][209:]}''',f'''*{(cr-2)*'~'}*''']
# PROJECT #####################################################################################################
proj = ed.grad.project
right_column += [f'''{proj.name.upper()} ~ {proj.name}''',
f'''*{(cr-2)*'~'}*''',
f'''  * {grad.text[0][:71]}''',
f'''    {grad.text[0][72:137]}''',
f'''    {grad.text[0][138:208]}''',
f'''    {grad.text[0][209:]}''']
# PRINT TEXT ##################################################################################################
text = ''
for line in full_column:
  text += line + '\n'
leftright = zip(left_column,right_column)
for line in leftright:
  text += line[0] + line[1] + '\n'
# WRITE TO TEXT FILE ##########################################################################################
output = open('../text-resume/resume.txt', 'w')
output.write(text)
print('file should have been written')




