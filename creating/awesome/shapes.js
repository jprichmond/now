////////////////////////////////////////////////////////////
//
//  SHAPES
//
//  The Ball and Face classes and their methods
//
////////////////////////////////////////////////////////////

////////////////////////////////////////////////////////////
//
//  BALL CLASS
//
////////////////////////////////////////////////////////////
class Ball {
  constructor(look, pos, size, speed) {
    this.look = look;
    if (pos instanceof p5.Vector) {
      this.pos = createVector(pos.x, pos.y);
    }
    this.size = size;
    if (speed instanceof p5.Vector) {
      this.speed = speed.copy();
    }
    this.momentum = createVector(0, 0);
    this.aim = null;
    this.boost = calcForFPS(MIN_BOOST, FPS);
    this.dir = random(FLIP);
    this.area = 0;
  } // end of Ball() constructor

  setArea() {
    this.area = circleSizeToArea(this.size);
  }

  // draw ball of color and size at given position
  draw() {
    push();
    fill(this.look);
    circle(this.pos.x, this.pos.y, this.size);
    pop();
  } // end of this.draw()

  // set object position to mouse position
  moveWithMouse() {
    this.pos.x = mouseX;
    this.pos.y = mouseY;
    this.keepOnCanvas();
  } // end of this.moveWithMouse()

  // keep ball on the visible canvas
  keepOnCanvas() {
    let rad = this.size / 2;
    this.pos.x = constrain(this.pos.x, rad, width - rad);
    this.pos.y = constrain(this.pos.y, rad, height - rad);
  } // end of this.keepOnCanvas()

  easeToward(target = this.aim, dir = 1) {
    target = target.copy();
    let magnitude = min(this.pos.dist(target), 200);
    if (this.size > 0) {
      magnitude = sqrt(
        magnitude / this.size
      ) * this.boost;
    } else {
      magnitude = 1;
    }
    magnitude *= dir;
    this.speed = target.sub(this.pos);
    this.speed.setMag(magnitude);
    if (dir == -1) {
      this.turnFromWall();
    }
    this.momentum.x = lerp(
      this.momentum.x,
      this.speed.x,
      0.1
    );
    this.momentum.y = lerp(
      this.momentum.y,
      this.speed.y,
      0.1
    );
    this.pos.add(this.momentum);
    this.keepInRange();
  } // end of this.easeToward()

  turnFromWall() {
    let range = ARENA_SIZE / 2;
    let rad = this.size / 2
    if (abs(this.pos.x) > range - rad ||
      abs(this.pos.y) > range - rad) {
      this.dir *= -1;
    }
    if (abs(this.pos.x) > range - this.size ||
      abs(this.pos.y) > range - this.size) {
      this.speed.rotate(random(85, 95) * this.dir);
    }
  } // end of this.turnFromWall()

  // keep ball in range
  keepInRange(range = ARENA_SIZE / 2) {
    let rad = this.size / 2;
    this.pos.x = constrain(
      this.pos.x,
      -range + rad,
      range - rad);
    this.pos.y = constrain(
      this.pos.y,
      -range + rad,
      range - rad);
  } // end of this.keepInRange()

  isCollision(other) {
    return this.pos.dist(other.pos) <
      (this.size + other.size) / 2;
  } // end of this.isCollision()

  collideWith(other) {
    if (this.isCollision(other)) {
      if (this.area > other.area * 1.5) {
        this.consume(other);
      } else if (other.area > this.area * 1.5) {
        other.consume(this);
      } else {
        this.obstruct(other);
      }
    }
  } // end of this.collideWith();

  consume(other) {
    if (this.alive) {
      let diffArea = this.area - other.area;

      diffArea = min(diffArea, other.area);

      this.area += diffArea;
      other.area -= diffArea;

      this.size = circleAreaToSize(this.area);
      other.size = circleAreaToSize(other.area);
    }
  } // end of this.consume()

  obstruct(other) {
    let thisPos = this.pos.copy();
    let otherPos = other.pos.copy();
    let rads = (this.size + other.size) / 2;
    let distance = this.pos.dist(other.pos);
    distance = (rads - distance) / 2;

    thisPos.sub(other.pos);
    thisPos.normalize();
    thisPos.setMag(
      distance * calcMass(this.area, other.area)
    );

    otherPos.sub(this.pos);
    otherPos.normalize();
    otherPos.setMag(
      distance * calcMass(other.area, this.area)
    );

    this.pos.add(thisPos);
    other.pos.add(otherPos);
  } // end of this.obstruct();

} /////////////////////////////////// END OF BALL CLASS ////

////////////////////////////////////////////////////////////
//
//  FACE CLASS
//
////////////////////////////////////////////////////////////
class Face extends Ball {
  constructor(look, pos, size, speed) {
    super(look, pos, size, speed);
    this.alive = true;
  } // end of Face() constructor

  // draws face, defaults to Ball.draw()
  draw() {
    if (this.look == "awe") {
      this.drawAwesome();
    } else if (this.look == "smiley" ||
      this.look == "cool") {
      this.drawSmiley();
    } else {
      super.draw();
    }
  } // end of this.draw()

  // draw the smiley face
  drawSmiley() {
    push();
    translate(this.pos.x, this.pos.y);
    scale(this.size / 300);

    strokeWeight(4);
    stroke(black);
    fill(yellow);
    circle(0, 0, 300);

    fill(black);
    ellipse(-50, -15, 30, 40);
    ellipse(50, -15, 30, 40);

    arc(0, 20, 200, 150, 20, 160);
    fill(yellow);
    arc(0, 15, 220, 130, 19, 161);
    pop();
    if (this.look == "cool") {
      this.drawSunglasses();
    }
  } // end of this.drawSmiley()

  // draw sunglasses
  drawSunglasses() {
    push();
    translate(this.pos.x, this.pos.y);
    scale(this.size * 2 / 300);

    strokeWeight(0);
    fill(black);
    arc(-30, -20, 58, 68, 0, 180, CHORD);
    arc(30, -20, 58, 68, 0, 180, CHORD);
    rectMode(CENTER);
    rect(0, -19, 128, 8);
    fill(100);

    arc(-30, -20, 52, 63, 0, 180, CHORD);
    arc(30, -20, 52, 63, 0, 180, CHORD);
    pop();
  } // end of this.drawSunglasses()

  // draw awesome face
  drawAwesome() {
    push();
    translate(this.pos.x, this.pos.y);
    scale(this.size / 300);

    strokeWeight(4);
    stroke(black);
    fill(yellow);
    circle(0, 0, 300);

    fill(white);
    arc(-80, -25, 88, 100, 157.5, 22.5, CHORD);
    arc(40, -28, 100, 100, 157.5, 22.5, CHORD);

    fill(black);
    circle(-62, -52, 30);
    circle(64, -52, 30);

    noStroke();
    fill(white);
    circle(-70, -60, 10);
    circle(56, -60, 10);

    fill(plum);
    arc(-6, 24, 200, 200, 0, 180, CHORD);

    fill(pink);
    beginShape();
    vertex(62, 96);
    bezierVertex(42, 68, -16, 80, -5, 123);
    bezierVertex(17, 123, 42, 114, 62, 96);
    endShape();

    stroke(black);
    noFill();
    arc(-6, 24, 200, 200, 0, 180, CHORD);
    pop();
  } // end of this.drawAwesome()

} /////////////////////////////////// END OF FACE CLASS ////

////////////////////////////////////////////////////////////
////////////////////////////////////// END OF SHAPES.JS ////
////////////////////////////////////////////////////////////