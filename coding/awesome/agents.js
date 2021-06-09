////////////////////////////////////////////////////////////
//
//  AGENTS
//
//  Player, Pellet, and Enemy classes and their methods
//
////////////////////////////////////////////////////////////

////////////////////////////////////////////////////////////
//
//  PLAYER CLASS
//
////////////////////////////////////////////////////////////
class Player extends Face {
  constructor(
    pos = createVector(0, 0),
    size = PLAYER_SIZE
  ) {
    super(
      "awe",
      pos, // starting position
      size, // starting size
      createVector(0, 0) // start with no velocity
    );
    this.zoom = 1;
    this.eaten = 0;
    this.maxBoost = calcForFPS(MAX_BOOST, FPS);
    this.minBoost = calcForFPS(MIN_BOOST, FPS);
    this.boostMeter = 120;
    this.boostUsed = false;
  }
  move() {
    this.setBoost();
    this.easeToward();
  } // end of this.move()

  setBoost() {
    if (keyIsPressed) {
      if (key === ' ' || keyCode === SHIFT) {
        if (!this.boostUsed) {
          this.accel();
        } else {
          this.decel();
        }
      }
    } else {
      this.decel();
    }
  }

  accel() {
    this.boost = lerp(
      this.boost,
      this.maxBoost,
      // larger meter value accelerates faster
      this.boostMeter / 600
    );
    this.boostMeter -= 1;

    if (this.boostMeter == 0) {
      this.boostUsed = true;
    }
  }

  decel() {
    this.boost = lerp(
      this.boost,
      this.minBoost,
      // smaller value glides better (larger meter)
      (121 - this.boostMeter) / 300
    );
    this.boostMeter += 1;
    this.boostMeter = min(this.boostMeter, 120);
    if (this.boostMeter > 60) {
      this.boostUsed = false;
    }
  }
} ///////////////////////////////// END OF PLAYER CLASS ////

////////////////////////////////////////////////////////////
//
//  PELLETS CLASS
//
////////////////////////////////////////////////////////////
class Pellet extends Ball {
  constructor() {
    super();
    this.spawn();
  } // end of Pellet() constructor

  spawn() {
    this.look = random(PELLET_COLORS);
    this.size = PELLET_SIZE;
    this.pos = createRandVector(ARENA_SIZE - this.size);
    this.speed = createVector(0, 0);
  } // end of this.spawn()

  draw(player) {
    if (this.size == 0) {
      this.spawn();
      this.setArea();
    }
    if (player.pos.dist(this.pos) <
      (DRAW_DIST + this.size / 2) / player.zoom) {
      super.draw();
    }
  } // end of this.draw()

} ///////////////////////////////// END OF PELLET CLASS ////

////////////////////////////////////////////////////////////
//
//  ENEMY CLASS
//
////////////////////////////////////////////////////////////
class Enemy extends Face {
  constructor() {
    super();
    this.spawn();
    this.sight = random(MIN_SIGHT, MAX_SIGHT);
    this.pred = null;
    this.prey = null;
    this.aim = createRandVector();
    this.boost = calcForFPS(
      random(MIN_ENEMY_BOOST, MAX_ENEMY_BOOST),
      FPS
    );
  } // end of Enemy() constructor

  spawn() {
    this.look = random(ENEMY_LOOKS);
    this.size = random(MIN_ENEMY_SIZE, MAX_ENEMY_SIZE);
    this.pos = spawnPosition(this.size, DRAW_DIST);
  } // end of this.spawn()

  draw(player) {
    if (this.alive) {
      if (this.size == 0) {
        return;
      }
      if (player.pos.dist(this.pos) <
        (DRAW_DIST + this.size / 2) / player.zoom) {
        super.draw();
      }
    }
  } // end of this.draw()

  move() {
    if (this.alive) {
      // if there are predators
      if (this.pred) {
        // set aim predator position
        this.easeToward(this.pred.pos, -1);
        this.pred = null;
        return;
      } else if (this.prey) {
        // set sights prey position
        this.aim = this.prey.pos.copy();
        this.prey = null;
      } else {
        this.wander();
      }
      this.easeToward();
    }
  } // end of this.move()

  reactTo(other) {
    if (this.alive && other.size > 0) {
      let rads = (this.size + other.size) / 2;
      if (other.size > this.size * 1.1) {
        if (this.pos.dist(other.pos) <
          this.sight / 2 + rads) {
          this.escape(other);
        }
      } else if (this.size > other.size * 1.1) {
        if (this.pos.dist(other.pos) <
          this.sight + rads) {
          this.pursue(other);
        }
      }
    }
  } // end of this.react()

  pursue(prey) {
    // if prey is already our target, just return
    if (prey == this.prey) {
      return;
    }
    // if currently targeting prey
    if (this.prey) {
      // if distance to other is quite less than current
      if (this.pos.dist(prey.pos) - prey.area <
        this.pos.dist(this.prey.pos) + this.prey.area) {
        // switch to other prey
        this.prey = prey;
      }
      // otherwise pursue prey
    } else {
      this.prey = prey;
    }
  } // end of this.pursue()

  escape(pred) {
    // if prey is already our target, just return
    if (pred == this.pred) {
      return;
    }
    // if predator detected
    if (this.pred) {
      // if other pred is closer
      if (this.pos.dist(pred.pos) <
        this.pos.dist(this.pred.pos)) {
        // run from other pred
        this.pred = pred;
      }
      // otherwise run from new threat
    } else {
      this.pred = pred;
    }
  } // end of this.escape()

  wander() {
    if (this.pos.dist(this.aim) < this.size / 2) {
      this.aim = createRandVector();
    }
  } // end of this.wander()

} ////////////////////////////////// END OF ENEMY CLASS ////

////////////////////////////////////////////////////////////
////////////////////////////////////// END OF AGENTS.JS ////
////////////////////////////////////////////////////////////