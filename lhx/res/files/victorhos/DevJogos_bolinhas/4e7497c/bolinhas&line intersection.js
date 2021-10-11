
var game = new Phaser.Game(800, 600, Phaser.CANVAS, 'phaser-example', { preload: preload, create: create, update: update, render: render });

function preload() {

    game.load.spritesheet('balls', 'assets/sprites/balls.png', 17, 17);

}

var bolinha1;
var bolinha2;
var bolinha3;
var bolinha4;

var line1;
var line2;
var line3;
var line4;

function create() {

    game.stage.backgroundColor = '#124184';

    bolinha1 = game.add.sprite(100, 200, 'balls', 0);
    bolinha1.anchor.set(0.5);
    bolinha1.inputEnabled = true;
    bolinha1.input.enableDrag(true);

    bolinha2 = game.add.sprite(400, 300, 'balls', 0);
    bolinha2.anchor.set(0.5);
    bolinha2.inputEnabled = true;
    bolinha2.input.enableDrag(true);

    bolinha3 = game.add.sprite(200, 400, 'balls', 1);
    bolinha3.anchor.set(0.5);
    bolinha3.inputEnabled = true;
    bolinha3.input.enableDrag(true);

    bolinha4 = game.add.sprite(500, 500, 'balls', 1);
    bolinha4.anchor.set(0.5);
    bolinha4.inputEnabled = true;
    bolinha4.input.enableDrag(true);

    line1 = new Phaser.Line(bolinha1.x, bolinha1.y, bolinha2.x, bolinha2.y);
    line2 = new Phaser.Line(bolinha2.x, bolinha2.y, bolinha3.x, bolinha3.y);
    line3 = new Phaser.Line(bolinha3.x, bolinha3.y, bolinha4.x, bolinha4.y);
    line4 = new Phaser.Line(bolinha4.x, bolinha4.y, bolinha1.x, bolinha1.y);
    

}

var c = 'rgb(255,255,255)';
var p12 = new Phaser.Point();
var p13 = new Phaser.Point();
var p14 = new Phaser.Point();

var p21 = new Phaser.Point();
var p23 = new Phaser.Point();
var p24 = new Phaser.Point();

var p31 = new Phaser.Point();
var p32 = new Phaser.Point();
var p34 = new Phaser.Point();

var p41 = new Phaser.Point();
var p42 = new Phaser.Point();
var p43 = new Phaser.Point();

function update() {

    line1.fromSprite(bolinha1, bolinha2, false);
    line2.fromSprite(bolinha2, bolinha3, false);
    line3.fromSprite(bolinha3, bolinha4, false);
    line4.fromSprite(bolinha4, bolinha1, false);

    p12 = line1.intersects(line2, true);
    p13 = line1.intersects(line3, true); 
    p14 = line1.intersects(line4, true);

    p21 = line2.intersects(line1, true);
    p23 = line2.intersects(line3, true);
    p24 = line2.intersects(line4, true);

    p31 = line3.intersects(line1, true);
    p32 = line3.intersects(line2, true);
    p34 = line3.intersects(line4, true);

    p41 = line4.intersects(line1, true);
    p42 = line4.intersects(line2, true);
    p43 = line4.intersects(line3, true);

    if (p12||p13||p14||p21||p23||p24||p31||p32||p34||p41||p42||p43)
    {
        c = 'rgb(0,255,0)';
    }
    else
    {
        c = 'rgb(255,255,255)';
    }
 
}

function render() {

    game.debug.geom(line1, c);
    game.debug.geom(line2, c);
    game.debug.geom(line3, c);
    game.debug.geom(line4, c);


    game.debug.lineInfo(line1, 32, 32);
    game.debug.lineInfo(line2, 32, 100);
    game.debug.lineInfo(line3, 32, 200);
    game.debug.lineInfo(line4, 32, 300);

    if (p12||p13||p14||p21||p23||p24||p31||p32||p34||p41||p42||p43)
    {
        game.context.fillStyle = 'rgb(255,0,255)';
        //game.context.fillRect(p.x - 2, p.y - 2, 5, 5);
        console.log('entrou');
    }
    else
    {
        console.log('passou')
    }

    game.debug.text("Drag the bolinhas", 32, 550);

}