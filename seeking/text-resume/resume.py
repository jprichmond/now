import json; from collections import namedtuple; from datetime import date as d

resume = open('../data.json')
dat = json.load(resume,object_hook=lambda d: namedtuple('X', d.keys())(*d.values()))
info = dat[0]; ed = dat[1]; work = dat[2]; craft = dat[3]; web = craft.skills.web; data = craft.skills.data
date = d.today().strftime('%Y.%m.%d'); 
coll = 31; gut = 5; colr = 75; back = '~'; tab = 2; 
ace = work.ace
##############################################################################################################
text = f'''{info.name}\n{info.email}\n{info.site}\n{info.phone}
'''; cap = 'WEB DEV SKILLS'; wrk = 'WORK EXPERIENCE'
text += f'''{f'{cap}'+(coll-len(f'{cap}'))*' '}{gut*' '}{(colr-len(f'{wrk}'))*' '}{wrk}
*{(coll-2)*back}*{(gut)*' '}*{(colr-2)*'~'}*
'''; sbcs = work.sbcs; role = sbcs.role.upper(); yrs = f'{sbcs.start} ~ {sbcs.end}'; w = web.acquiring
text += f'''ACQUIRING:{(coll-len('ACQUIRING:'))*' '}{gut*' '}{role}{(colr-len(role)-len(yrs))*' '}{yrs}
{tab*' '}{w[0]+(coll-len(f'{w[0]}')-tab)*' '}{gut*' '}  {sbcs.name.upper()}
{tab*' '}{w[1]+(coll-len(f'{w[1]}')-tab)*' '}{gut*' '}  * {sbcs.text[0][:72]}
{tab*' '}{w[2]+(coll-len(f'{w[2]}')-tab)*' '}{gut*' '}    {sbcs.text[0][72:142]}
{tab*' '}{w[3]+(coll-len(f'{w[3]}')-tab)*' '}{gut*' '}    {sbcs.text[0][142:]}
{tab*' '}{w[4]+(coll-len(f'{w[4]}')-tab)*' '}{gut*' '}  * {sbcs.text[1][:72]}
{tab*' '}{w[5]+(coll-len(f'{w[5]}')-tab)*' '}{gut*' '}    {sbcs.text[1][72:143]}
{tab*' '}{w[6]+(coll-len(f'{w[6]}')-tab)*' '}{gut*' '}    {sbcs.text[1][143:]}
{tab*' '}{w[7]+(coll-len(f'{w[7]}')-tab)*' '}{gut*' '}  * {sbcs.text[2][:72]}
{tab*' '}{w[8]+(coll-len(f'{w[8]}')-tab)*' '}{gut*' '}    {sbcs.text[2][72:142]}
{tab*' '}{w[9]+(coll-len(f'{w[9]}')-tab)*' '}{gut*' '}  * {sbcs.text[3][:68]}
'''; w = web.employing
text += f'''EMPLOYING:{(coll-len('EMPLOYING:'))*' '}{gut*' '}    {sbcs.text[3][68:134]}
{tab*' '}{w[0]+(coll-len(f'{w[0]}')-tab)*' '}{gut*' '}    {sbcs.text[3][135:]}
{tab*' '}{w[1]+(coll-len(f'{w[1]}')-tab)*' '}
{tab*' '}{w[2]+(coll-len(f'{w[2]}')-tab)*' '}{gut*' '}*{(colr-2)*'~'}*
'''; role = ace.role.upper(); yrs = f'{ace.start} ~ {ace.end}'
text += f'''{tab*' '}{w[3]+(coll-len(f'{w[3]}')-tab)*' '}{gut*' '}{role}{(colr-len(role)-len(yrs))*' '}{yrs}
'''; w = web.mastering
text += f'''MASTERING:{(coll-len('MASTERING:'))*' '}{gut*' '}  {ace.name.upper()}
{tab*' '}{w[0]+(coll-len(f'{w[0]}')-tab)*' '}{gut*' '}  * {ace.text[0][:68]}
{tab*' '}{w[1]+(coll-len(f'{w[1]}')-tab)*' '}{gut*' '}    {ace.text[0][69:138]}
{tab*' '}{w[2]+(coll-len(f'{w[2]}')-tab)*' '}{gut*' '}    {ace.text[0][139:]}
{tab*' '}{w[3]+(coll-len(f'{w[3]}')-tab)*' '}{gut*' '}

'''

print(text)


