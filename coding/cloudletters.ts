const log = console.log
const size = 17, maxWord = 15, held = 1, seized = 2

const playData = {
  player: 0,
  row: 0,
  col: 0,
  dir: 0
}

class Sky {
  static alpha = `abcdefghijklmnopqrstuvwxyz`
  static blue = [ [ 0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0 ],
                 [ 0,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0 ],
                [ 0,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0 ],
               [ 1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0 ],
              [ 1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0 ],
             [ 1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0 ],
            [ 0,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0 ],
           [ 0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0 ],
          [ 0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0 ],
         [ 0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0 ],
        [ 0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,0 ],
       [ 0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1 ],
      [ 0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1 ],
     [ 0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1 ],
    [ 0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,0 ],
   [ 0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,0 ],
  [ 0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0 ]]
  constructor(sky) {
    !sky? this.sky = deepCopy(Sky.blue) : this.sky = deepCopy(sky)
  }
  match(sky) {
    this.sky = deepCopy(sky)
  }
  update(val, pos) {
    this.sky[pos.y][pos.x] = val
  }
  display() {
    let s = `           layer↓  A B C D E F G H I J K L M N O P Q→RAY↙︎\n`
    let space = 18, l = 0
    for (let layer of this.sky) {
      for (let sp = 0; sp < space; sp++)
        space - sp === 2? s += `${Sky.alpha.charAt(space-2)}` : s += ` `
      for (let ray of layer)
        ray === 0? s += `/ ` : s += `. `
      s += `\n`
      space--
    }
    log(s)
  }
}

class Cloud {
  constructor() {
    this.letters = [
      'e','e','e','e','e','e','e','e','e','e','e',
      't','t','t','t','t','t','t','t','t',
      'a','a','a','a','a','a','a','a','a',
      'o','o','o','o','o','o','o','o',
      'i','i','i','i','i','i','i','i',
      'n','n','n','n','n','n',
      's','s','s','s','s','s',
      'h','h','h','h','h','h',
      'r','r','r','r','r','r',
      'd','d','d','d','d','d',
      'l','l','l','l',
      'u','u','u','u',
      'm','m','m','m',
      'w','w','w','w',
      'f','f','f','f',
      'g','g','g','g',
      'y','y','y',
      'p','p','p',
      'b','b','b',
      'v','v',
      'k','k',
      'x','x',
      'j','j',
      'q','q',
      'z','z'
    ]
    this.letters = scramble(this.letters)
    this.letters = split(this.letters)
  }
  // init() {
  //   scramble(this.letters)
  // }
  display() {
    let s = `\n`
    for (let i = 0; i < this.letters.length; i++) {
      for (let j = 0; j < this.letters[i].length; j++) {
        s += `${this.letters[i][j]}  `
      }
      s += `\n`
    }
    log(s)
  }
}

class Play {
  constructor(player, row, col, dir) {
    this.player = player
    this.row = row
    this.col = col
    this.dir = dir
  }
}

function scramble(letters) {
  let l = [...letters]
  for (let n, i = l.length-1; i > 0; i--) {
    n = Math.floor(Math.random() * (i + 1))
    let v = l[i]
    l[i] = l[n]
    l[n] = v
  }
  return l
}

function split(letters) {
  let l1 = [], l2 = [], l3 = [], l4 = []
  for (let i = 0; i < letters.length; i++) {
    switch (i % 4) {
      case 0: l1.push(letters[i]); continue
      case 1: l2.push(letters[i]); continue
      case 2: l3.push(letters[i]); continue
      case 3: l4.push(letters[i]); continue
    }
  }
  return [l1,l2,l3,l4]
}

function deepCopy(from) {
  let to, key, val 
  if (typeof from !== "object" || from === null) {
    return from // return if primitive or nonexistent
  }
  // create array or object to hold values
  to = Array.isArray(from)? [] : {}
  // set each value
  for (key in from) {
    val = from[key]
    // recursive call to deepCopy
    to[key] = deepCopy(val)
  }
  return to
}

const stratos = new Sky()
const tropos = new Cloud()

stratos.display()
tropos.display()
