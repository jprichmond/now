////////////////////////////////////////////////////////////
//
//  ENVIRONMENT
//
//  The settings of the setting and interface
//
////////////////////////////////////////////////////////////

////////////////////////////////////// GLOBAL CONSTANTS ////
const CANVAS_SIZE = 800;
const FPS = 60;

const ARENA_SIZE = 4000;
const DRAW_DIST = CANVAS_SIZE / 2 * 1.42;

const PLAYER_SIZE = 100;
const MIN_BOOST = 3;
const MAX_BOOST = 8;

const MIN_ENEMY_SIZE = PLAYER_SIZE / 3;
const MAX_ENEMY_SIZE = PLAYER_SIZE * 1.5;
const MIN_ENEMY_BOOST = MIN_BOOST;
const MAX_ENEMY_BOOST = MIN_BOOST * 2;
const MIN_SIGHT = PLAYER_SIZE * 2;
const MAX_SIGHT = PLAYER_SIZE * 5;

const PELLET_SIZE = 20;

///////////////////////////////////////// GLOBAL COLORS ////
let yellow = [246, 200, 94];
let black = 16;
let skyblue = [100, 200, 250];
let white = 255;
let plum = [129, 29, 70];
let pink = [247, 195, 218];
let green = [100, 255, 100];
let red = [255, 50, 50];

///////////////////////////////////////// GLOBAL ARRAYS ////
// array of different enemy looks
const ENEMY_LOOKS = ["smiley", "cool"];

// array of different pellet colors
const PELLET_COLORS = [pink, "pink", "#fab", "#ffaced"];

// array to use with random() for direction
const FLIP = [-1, 1];

////////////////////////////////////////////////////////////
//
//  POINTER CLASS
//
////////////////////////////////////////////////////////////
class Pointer extends Ball {
  constructor() {
    super(
      "#cccccc88",
      createVector(0, 0),
      12
    );
  }
  draw(center) {
    push();
    fill(this.look);
    stroke("#ffffff88");
    strokeWeight(this.size);
    circle(
      this.pos.x,
      this.pos.y,
      this.size);
    pop();
  }
  move() {
    this.moveWithMouse();
  }
} //////////////////////////////// END OF POINTER CLASS ////

////////////////////////////////////////////////////////////
//
//  ARENA CLASS
//
////////////////////////////////////////////////////////////
class Arena {
  constructor(pos = createVector(0, 0)) {
    this.pos = pos.copy();
    this.size = ARENA_SIZE;
  }
  draw(pos) {
    push();

    translate(pos);
    rectMode(CENTER);

    fill(skyblue);
    stroke("lightblue");
    strokeWeight(4);
    square(this.pos.x, this.pos.y, this.size);

    this.drawLines(Math.floor(ARENA_SIZE / 50));
    pop();
  }
  drawLines(n) {
    translate(
      -this.size / 2 + this.pos.x,
      -this.size / 2 + this.pos.y
    );
    // vertical lines
    for (let i = 1; i < n; i++) {
      if (i == n / 2) {
        strokeWeight(2);
      } else {
        strokeWeight(1);
      }
      line(this.size * i / n, 0,
        this.size * i / n, this.size);
    }
    // horizontal lines
    for (let i = 1; i < n; i++) {
      if (i == n / 2) {
        strokeWeight(2);
      } else {
        strokeWeight(1);
      }
      line(0, this.size * i / n,
        this.size, this.size * i / n);
    }
  }

} ////////////////////////////////// END OF ARENA CLASS ////

////////////////////////////////////////////////////////////
//
//  HELPER FUNCTIONS
//
////////////////////////////////////////////////////////////
function spawnPosition(
  size,
  spawnDist = PLAYER_SIZE * 1.5,
  range = ARENA_SIZE,
  center = createVector(0, 0)
) {
  let v;
  do {
    v = createRandVector(range - size);
  } while (v.dist(center) < spawnDist)
  return v;
}

function createRandVector(range = ARENA_SIZE) {
  range = range / 2;
  return createVector(
    random(-range, range),
    random(-range, range)
  );
}

function circleSizeToArea(size) {
  let r = size / 2;
  return PI * r * r;
} // end of circleSizeToArea()

function circleAreaToSize(area) {
  let r = sqrt(area / PI);
  return r * 2;
} // end of circleAreaToSize()

function calcMass(area1, area2) {
  return 2 * area2 / (area1 + area2);
} // end of calcMass()

function calcForFPS(speed, FPS) {
  return speed * 60 / FPS;
} // end of calcForFPS()

/////////////////////////////// END OF HELPER FUNCTIONS ////

////////////////////////////////////////////////////////////
//
//  INTERFACE FUNCTIONS
//
////////////////////////////////////////////////////////////

// put the instructions in the center of the screen
function startText() {
  fill(white, 64 + max(frameCount % 255,
    255 - frameCount % 255));
  stroke(0);
  textFont("Futura");
  textSize(54);
  textAlign(CENTER);
  text("AWESOME’S",
    width / 2, height * 2 / 13);
  textSize(72);
  text("MEET ’N’ EAT",
    width / 2, height * 1 / 4);
  textSize(48);
  text("CLICK SCREEN TO PLAY",
    width / 2, height * 5 / 6);
  textSize(24);
  text("Point in direction to glide\n" +
    "Press SHIFT or SPACE for boost",
    width / 2, height * 8 / 9);
}

function mouseClicked() {
  noCursor();
  if (!gameStart) {
    gameStart = true;
  } else if (alive == 1 && player.alive) {
    initGame();
  } else if (!player.alive) {
    initGame();
  }
}

function initGame() {
  alive = nEnemies + 1;
  pellets = [];
  enemies = [];
  player = new Player();
  player.setArea();
  pointer = new Pointer();
  for (let i = 0; i < nPellets; i++) {
    pellets.push(new Pellet());
    pellets[i].setArea();
  }
  for (let i = 0; i < nEnemies; i++) {
    enemies.push(new Enemy());
    enemies[i].setArea();
  }
}

// shows number of kills in upper right
function showHUD(eaten, alive) {
  fill(white);
  stroke(black);
  textFont("Futura");
  textSize(32);
  textAlign(RIGHT);
  text(eaten + " EATEN",
    width - 10, height / 25);
  textAlign(LEFT);
  text(alive + " ALIVE",
    10, height / 25);
}

function countStats(face1, face2) {
  if (face1.alive && face1.size == 0) {
    face1.alive = false;
    if (face2 instanceof Player) {
      face2.eaten += 1;
    }
    return 1;
  }
  if (face2.alive && face2.size == 0) {
    face2.alive = false;
    if (face1 instanceof Player) {
      face1.eaten += 1;
    }
    return 1;
  }
  return 0;
}

function debugText(name, val) {
  fill(white);
  stroke(black);
  textSize(32);
  textAlign(LEFT);
  if (val instanceof p5.Vector) {
    text(name + ": " +
      val.x.toFixed(0) + ", " +
      val.y.toFixed(0),
      10, height - 10);
  } else {
    text(name + ": " +
      val.toFixed(0),
      10, height - 10);
  }
}

function showMeter(meter) {
  push();
  rectMode(CORNER);
  fill(white);
  stroke(white);
  strokeWeight(2);
  rect(width / 2 - 120, 10, 240, 20);
  if (meter > 60) {
    fill(green);
  } else {
    fill(red);
  }
  noStroke();
  rect(width / 2 - 120, 10, meter / 120 * 240, 20);
  pop();
}

// put win text up
function showWinText() {
  fill(white, 64 + max(frameCount % 255,
    255 - frameCount % 255));
  stroke(0);
  textFont("Futura");
  textSize(72);
  textAlign(CENTER);
  text("YOU WIN",
    width / 2, height * 1 / 5);
  textSize(48);
  text("CLICK SCREEN TO PLAY AGAIN",
    width / 2, height * 5 / 6);
}

// put lose text up
function showLoseText() {
  fill(white, 64 + max(frameCount % 255,
    255 - frameCount % 255));
  stroke(0);
  textFont("Futura");
  textSize(72);
  textAlign(CENTER);
  text("GAME OVER",
    width / 2, height * 1 / 5);
  textSize(48);
  text("CLICK SCREEN TO PLAY AGAIN",
    width / 2, height * 5 / 6);
}

////////////////////////////////// PERFORMANCE MEASURES ////
p5.disableFriendlyErrors = true;
let lastLoop, thisLoop, frameLoop,
  msg = "",
  nFr = FPS / 2,
  tFPS = 0,
  aFPS = 0,
  tMax = 0,
  aMax = 0

// check performance
function performanceMeasures(check) {
  if (check) {
    thisLoop = millis();

    // sum FPS time
    tFPS += 1000 / (thisLoop - frameLoop);
    frameLoop = thisLoop;
    // sum execution time in draw()
    tMax += 1000 / (thisLoop - lastLoop);

    // every nFr (number of frames), take the average
    if (frameCount % nFr == 0) {
      aFPS = tFPS / nFr;
      aMax = tMax / nFr;
      tFPS = tMax = 0;
    }
    // print it on the screen
    fill(255);
    stroke(0);
    textSize(18);
    textAlign(LEFT);
    text(msg + "  FPS: " + aFPS.toFixed(0) +
      "  Max FPS: " + aMax.toFixed(0),
      10, height - 10);
  }
}

////////////////////////////////////////////////////////////
///////////////////////////////// END OF ENVIRONMENT.JS ////
////////////////////////////////////////////////////////////