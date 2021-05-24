

fs = require('fs')
const job = ``
const position = job? job : `a Software Engineer`

const info = {
  name:`Jason Richmond`,
  email:`me@jason.richmond.is`,
  site:`jason.richmond.is`,
  phone:`574.855.6954`,
  text: [`M.S. in Computer Science familiar with a diverse array of languages, platforms, and domains seeking to further expand software development capabilities as ${position}.`,`Offers five years experience crafting programs in an academic setting in addition to teaching students of all ages and aptitudes the art of programming.`,`Thrives in collaborative work environments where ego takes a backseat to doing great work and solving the problem at hand.`,`Dealt with clients and built solutions for small businesses in prior career.`]
}
const ed = {
  name: `Academic Experience`,
  grad: {
    school:`Indiana University South Bend`,
    gpa:3.7,
    degree:`Master of Science`,
    year:`2021`,
    major:`Computer Science`,
    text: [`Studied a wide spectrum in the discipline, from artificial intelligence to algorithm analysis, networking to neural networks, graphics to games, even writing the opcodes for a simulated CPU to run a puck-like robot with programmed with enough AI to navigate a maze.`],
    project: {
      name:`Master’s Project`,
      title:`Counternote Compiler`,
      text: [`Implemented a compiler for an original musical language written in 7-bit ASCII, designed to be readable, typeable, singable, and shareable, with chromaticism, music theory, and rhythm built in to complement the diatonicity of traditional notation.`,`Launching a domain-specific alpha at the end of the summer with sights on publication and a Turing complete beta by the end of 2021.`]
    }
  },
  undergrad: {
    degree:`Bachelor of Arts`,
    school:`Indiana University Bloomington`,
    gpa: 3.1,
    major: {
      anth:`Anthropology`,
      econ:`Economics`,
      ling:`Linguistics`
    }
  }
}
const work = {
  name: `Work Experience`,
  sbcs: {
    name:`South Bend Code school`,
    role:`Lead Instructor`,
    start:2018,
    end:2020,
    text: [`Crafted interactive learning path spanning eleven lessons of around 25k words in p5.js, giving students an introduction to class-based object-oriented programming.`,`Laid a concrete foundation for primary and secondary school students to build out abstract programming concepts using Scratch, Web Dev, Unity, Javascript, and Python.`,`Attended to the struggling to help them understand that coding is about embracing failure and not giving up.`,`Entrusted with running the Elkhart branch and being liazon to local schools keeping the relevant stakeholders happy and extending Code School reach.`]
  },
  ace: {
    name:`Academic Center for Excellence`,
    start:2016,
    end:2019,
    role:`Learning Facilitator`,
    cs:`Computer Science`,
    text: [`Equipped dozens of graduates and undergraduates of all levels having trouble grokking the theory and practice of Computer Science with the knowledge and skills to succeed.`,`Debugged hundreds of student-written programs, usually on a tight deadline before submission without reference to a working answer.`,`Convinced the department to retain early Friday hours for those getting a head start on the weekend.`,`Collaborated with professors to help compress the complex world of code into the tangible everyday for entry-level students.`]
  }
}

const craft = {
skills: {
  web: {
    name: `Web Development Skills`,
    acquiring: [
      `Full-stack Development`,
      `Microservices`,
      `REST`,
      `Serverless`,
      `Angular`,
      `Django`,
      `NoSQL`,
      `React`,
      `Redux`,
      `Typescript`,
    ],
    employing: [
      `Front-end Web Design`,
      `Node.js`,
      `Docker`,
      `p5.js`,
      `Javascript`,
      `HTML`,
      `CSS`,
      `Markdown`,
    ],
  },
  data: {
    name: `Data Engineering Skills`,
    acquiring: [
      `MySQL`,
      `Pandas`,
      `PySpark`,
      `Hadoop`,
      `R`,
    ],
    employing: [
      `Machine Learning`,
      `Neural Networks`,
      `AI`,
      `SQL`,
      `Java`,
      `Python`,
    ],
  },
  dev: {
    name: `Additional Know-how`,
    employing: [
      `Object-oriented Programming`,
      `Procedural Programming`,
      `Functional Programming`,
      `Unit Testing`,
      `Gang of Four Design Patterns`,
      `UI/UX Design`,
      `Git`,
      `C/C++`
    ]
  }
}}

out = [info,ed,work,craft]
out = JSON.stringify(out)
// console.log(out)

const err = new Error('failed to write to file')
fs.writeFile('../data.json', out, (err) => {
  err? console.log(err) : console.log("file written successfully")
});