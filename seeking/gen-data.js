

fs = require('fs')
const job = ``
const position = job? job : `a Software Engineer`

const info = {
  name:`Jason Richmond`,
  email:`me@jason.richmond.is`,
  site:`jason.richmond.is`,
  phone:`574.855.6954`,
  text: [`Software Engineer with a Master’s in Computer Science familiar with a diverse array of languages and platforms seeking opportunity to build something great.`,`Offers seven years experience crafting programs collaborating with peers, and mentoring students in startup and academic settings.`,`Thrives in collaborative work environments where ego takes a backseat to solving hard problems and doing great work.`,`Experienced in remote/hybrid work environments and committed to building and maintaining a solid, productive team.`,`Approaches challenges and setbacks with a growth mindset.`]
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
      text: [`Implementing a compiler for an original musical language written in 7-bit ASCII, designed to be readable, typeable, singable, and shareable, with chromaticism, music theory, and rhythm built in to complement the diatonicity of traditional notation.`,`Launching a domain-specific alpha at the end of the summer with sights on publication and a Turing complete beta by the end of 2021.`]
    }
  },
  undergrad: {
    degree:`Bachelor of Arts`,
    school:`Indiana University Bloomington`,
    year:`2008`,
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
  aun: {
    name:`Aunalytics`,
    role:`Software Engineer`,
    start:2021,
    end:2023,
    text: [`Programmed solo and on teams to improve the backend of our data solutions platform written in Node.js.`,`Pushed for and piloted new team structure to better communicate and increase collaboration.`,`Contributed to initiatives to improve the robustness and fault-tolerance of our data pipeline, including features that sped up our data delivery by an order of magnitude helping us achieve our on-time delivery goal over a quarter after seldom delivering that a week.`,`Took the reins on implementing two-phase procedure of data manipulation so that only valid data would replace existing good data.`,`Investigated and implemented a dynamic solution to a logging failure impacting our ability to audit our deliverables.`,`Raised the alarm to terminate a maintenance initiative that introduced widespread and subtle bugs in our soon-to-be legacy backend.`,`Engaged in weekly learning discussions and the designing of our next generation platform written in Typescript using React.`,`Employed Agile methodologies to track planning and execution of tickets.`]
  },
  sbcs: {
    name:`South Bend Code School`,
    role:`Lead Instructor`,
    start:2018,
    end:2020,
    text: [`Crafted interactive learning path spanning eleven lessons of around 25k words in p5.js, giving students an introduction to class-based object-oriented programming.`,`Laid a concrete foundation for primary and secondary school students to build out abstract programming concepts using Scratch, Web Dev, Unity, Javascript, and Python.`,`Attended to the struggling to help them understand that coding is about embracing failure and not giving up.`,`Entrusted with running the Elkhart branch and being liaison to local schools keeping the relevant stakeholders happy and extending Code School reach.`]
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
  name: `Software Development Skills`,
  dev: [
    `Full-stack Development`,
    `Microservices`,
    `REST`,
    `React`,
    `Redux`,
    `MongoDB`,
    `Typescript`,
    `Node.js`,
    `Docker`,
    `Javascript`,
    `HTML`,
    `CSS`,
    `Hadoop`,
    `Machine Learning`,
    `Neural Networks`,
    `AI`,
    `SQL`,
    `Java`,
    `Python`,
    `Object-oriented Programming`,
    `Procedural Programming`,
    `Functional Programming`,
    `Unit Testing`,
    `UI/UX Design`,
    `Git`,
    `C/C++`,
    `CI/CD`,

  ]
}


out = [info,ed,work,craft]
out = JSON.stringify(out)
// console.log(out)

const err = new Error('failed to write to file')
fs.writeFile('data.json', out, (err) => {
  err? console.log(err) : console.log("file written successfully")
});