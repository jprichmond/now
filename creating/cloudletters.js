const log = console.log
const size = 17, maxWord = 15, held = 1, seized = 2


class Sky {
  static blue = [[ 0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0 ],
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
        space - sp === 2? s += `${Cloud.alpha[space-2]}` : s += ` `
      for (let ray of layer)
        ray === 0? s += `/ ` : s += `${ray} `
      s += `\n`
      space--
    }
    log(s)
  }
}

class Cloud {
  static alpha = [`a`,`b`,`c`,`d`,`e`,`f`,`g`,`h`,`i`,`j`,`k`,`l`,`m`,`n`,`o`,`p`,`q`,`r`,`s`,`t`,`u`,`v`,`w`,`x`,`y`,`z`]
  static letters = [
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
}

class Play {
  constructor(player, row, col, dir) {
    this.player = player
    this.row = row
    this.col = col
    this.dir = dir
  }
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

const current = new Sky()
current.display()
