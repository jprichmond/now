////////////////////////////////////////////////////////////
//
//  GAME FLOW
//
//  The game flow logic of Awesome’s Meet ’n’ Eat
//
////////////////////////////////////////////////////////////

////////////////////// GAME OBJECT VARIABLES AND ARRAYS ////
let gameStart = false;
let arena;
let player;
let pointer;
let pellets = [];
let nPellets = 400;
let enemies = [];
let nEnemies = 20;
let origin;
let zoom;
let alive = 0;

////////////////////////////////////////////////////////////
//
//  SCENE FUNCTIONS
//
////////////////////////////////////////////////////////////

function startScreen() {
  player.zoom = 3;
  
  push();
  translate(width / 2, height / 2);
  arena.draw(origin);
  scale(player.zoom);
  player.draw();
  pop();

  startText();
}

/////////////////////////// EACH FRAME A PLAY IN 5 ACTS ////

// set zoom and position relative to player and draw arena
function setting() {
  background(black);
  // set the zoom level
  if (player.size > 0) {
    zoom = sqrt(PLAYER_SIZE / player.size);
  }
  // ease toward that zoom using linear interpolation
  player.zoom = lerp(player.zoom, zoom, 0.02);

  push();

  // first translate to the center of the canvas and scale
  translate(width / 2, height / 2);
  scale(player.zoom);
  // then translate to player position
  translate(-player.pos.x, -player.pos.y);

  // draw arena at the origin
  arena.draw(origin);
}

// update movement
function action() {
  for (let i = 0; i < nEnemies; i++) {
    for (let pellet of pellets) {
      enemies[i].reactTo(pellet);
    }
    for (let j = i + 1; j < nEnemies; j++) {
      enemies[i].reactTo(enemies[j]);
    }
    enemies[i].reactTo(player);
  }
  player.aim = createVector(
    pointer.pos.x + player.pos.x - width / 2,
    pointer.pos.y + player.pos.y - height / 2
  );
  for (let enemy of enemies) {
    enemy.move();
  }
  player.move();
}

// collisions
function conflict() {
  // detect collision with pellets
  for (let pellet of pellets) {
    if (player.alive) {
      player.collideWith(pellet);
    }
    for (let enemy of enemies) {
      if (enemy.alive) {
        enemy.collideWith(pellet);
      }
    }
  }
  // detect enemy-enemy collisions
  for (let i = 0; i < nEnemies; i++) {
    if (enemies[i].alive) {
      for (let j = i + 1; j < nEnemies; j++) {
        if (enemies[j].alive) {
          enemies[i].collideWith(enemies[j]);
          alive -= countStats(enemies[i], enemies[j]);
        }
      }
    }
  }
  // detect player-enemy collisions
  for (let enemy of enemies) {
    if (enemy.alive) {
      player.collideWith(enemy);
      alive -= countStats(player, enemy);
    }
  }
}

// display only those pellets and enemies in range of the player
function resolution() {
  // draw pellet in range of player
  for (let pellet of pellets) {
    pellet.draw(player);
  }
  // draw the enemy in range of player
  for (let enemy of enemies) {
    enemy.draw(player);
  }
  player.draw();

  pop();
}

// update stats and show win/lose screen if conditions are met
function denouement() {
  showHUD(player.eaten, alive);
  showMeter(player.boostMeter);

  if (alive == 1 && player.alive) {
    showWinText();
  } else if (!player.alive) {
    showLoseText();
  }
  pointer.move();
  pointer.draw();

  // debugText("boostMeter",player.boostMeter); 
}

////////////////////////////////////////////////////////////
//////////////////////////////////// END OF GAMEFLOW.JS ////
////////////////////////////////////////////////////////////