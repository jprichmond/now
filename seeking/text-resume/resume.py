import json
from collections import namedtuple
data = json.load(resume,object_hook=lambda d: namedtuple('X', d.keys())(*d.values()))

##############################################################################################################
print(f'''SKILLS:{(cola-len('SKILLS:'))*" "}{gut*' '}WORK EXPERIENCE:{(colb-len('WORK EXPERIENCE:'))*" "}
{cola*"#"}{gut*' '}{colb*"#"}
{(cola-len()*" "+}{gut*' '}* WORKS!
''')








"""exp = {'wb':{'ac':['Full-stack Web Development','Microservices','REST','Serverless','Angular','Django','MongoDB','MySQL','React','Redux','Jekyll','Typescript','Test-driven Development','Unit Testing'],'em':['Front-end Web Design','Node.js','Docker','Functional Programming','C#','UML'],'ms':['Python','Javascript','HTML','CSS','Git','Object-oriented Programming','Documentation']},'dt':{'ac':['MySQL','MongoDB','Microservices','Pandas','Spark','Hadoop','Numpy','Functional Programming','Machine Learning','AI','Neural Networks'],'em':['SQL','R','C#','Functional Programming','UML','Java'],'ms':['Python','Javascript','Git','Object-oriented Programming','Documentation']},'dv':['C','C++','WebAssembly','GoF Design Patterns','Interpersonal Communication','SuperCollider','Music Production','Songwriting']}  
'role':'Lead Instructor','work':'South Bend Code School','date':'18.09 ~ 20.05','1':'Crafted interactive learning path spanning eleven lessons of around 25k words in p5.js, giving students an introduction to class-based object-oriented programming.','2':'Laid a concrete foundation for primary and secondary school students to build out abstract programming concepts using Scratch, Web Dev, Javascript, Unity, and Python.','3':'Attended to the struggling to help them understand that coding is about embracing failure and not giving up.','4':'Entrusted with running the Elkhart branch and being liazon to local schools keeping the relevant stakeholders happy and extending Code School reach.','role':'Learning Facilitator','work':'Academic Center for Excellence','date':'16.09 ~ 19.05','1':'Equipped dozens of graduates and undergraduates of all levels having trouble grokking the theory and practice of Computer Science with the knowledge and skills to succeed.','2':'Debugged hundreds of student-written programs, usually on a tight deadline before submission without reference to a working answer.','3':'Convinced the department to retain early Friday hours for those getting a head start on the weekend.','4':'Collaborated with professors to help compress the complex world of code into the tangible everyday for entry-level students.','degree':'Master of Science','major':'Computer Science','school':'Indiana University South Bend','1':'Studied a wide spectrum in the discipline, from artificial intelligence to algorithm analysis, networking to neural networks, graphics to games, even writing the opcodes for a simulated CPU to run puck-like robot with programmed with enough AI to navigate a maze.','1':'Implemented a compiler for an original musical language written in 7-bit ASCII, designed to be readable, typeable, singable, and shareable, with chromaticism, music theory, and rhythm built in to complement the diatonicity of traditional notation.','2':'Launching a domain-specific alpha at the end of the summer with sights on publication and a Turing complete beta by the end of 2021.',
"""
