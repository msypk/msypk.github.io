int height;
int width;
PFont nameFont;
color mtcolor1;
color mtcolor2;
color mtcolor;
color linecolor;
color bgcolor1;
color bgcolor2;
color bgcolor;
color namecolor;
int change;
int moonx;
int moony;
int moonx1;
int moonx2;
int moony1;
int moony2;

void setup() {
  height = 250;
  width = 1110;

  nameFont = createFont("Arial", 100);

  mtcolor1 = color(60, 91, 120);
  mtcolor2 = color(0, 0, 0);

  linecolor = color(255);

  bgcolor1 = color(245, 245, 245);
  bgcolor2 = color(62, 83, 102);

  namecolor = color(0);

  moonx1 = 385;
  moonx2 = 725;
  moony1 = 100;
  moony2 = 50;

  bgcolor = bgcolor1;
  mtcolor = mtcolor1;
  moonx = moonx1;
  moony = moony1;

  change = 1;

  size(width, height);
   
}

void draw() {
  transform();
  background(bgcolor);
  clickme();
  moon();
  mountains();
  name(); 
}

void mountains() {

  fill(mtcolor);
  noStroke();
  triangle(12, height, 10+80, height - 50, 10+160, height);
  triangle(100, height, 100+120, height - 80, 100 +240, height);
  triangle(0+205 , height, 100+205, height - 120, 200+205, height);
  triangle(100+205 , height, 200+205, height - 100, 300+205, height);
  triangle(360+55, height, 360+130+55, height - 70, 410 + 200+55, height);
  triangle(560+55, height, 560 + 120+55, height - 160, 560 + 240+55, height);
  triangle(700+55, height, 700+80+55, height - 90, 700 + 150+55, height);
  triangle(800, height, 800+100, height - 80, 800+200, height);
  triangle(1098-160, height, 1098-80, height - 50, 1098, height);

  stroke(linecolor);
  strokeWeight(2);
  line(10+80, height - 50, 10+160, height);
  /*line(100+120, height - 80, 100 +240, height);*/
  line(100+205, height - 120, 200+205, height);
  line(200+205, height - 100, 300+205, height);
  line(360+130+55, height - 70, 410 + 200+55, height);
  line(560 + 120+55, height - 160, 560 + 240+55, height);
  /*line(700+80+55, height - 90, 700 + 150+55, height);*/
  line(800+100, height - 80, 800+200, height);
  
}

void name() {
  fill(namecolor);
  noStroke();
  textFont(nameFont);
  textSize(25);
  text("MICHELLE PARK", width/2 - 100, height/2);
}

void moon() {

  fill(219, 215, 202);
  ellipse(moonx, moony, 50, 50);
}

void transform() {
  color b1;
  color m1;
  color n1;

  if (change == 1) {
    b = bgcolor;
    m = mtcolor;
    n = namecolor;
    x = moonx;
    y = moony;
    bgcolor = lerpColor(b, bgcolor2, .05);
    mtcolor = lerpColor(m, mtcolor2, .05);
    namecolor = lerpColor(n, color(255), .05);
    moonx = lerp(x, moonx2, .05);
    if (moonx < 555) {
      moony = lerp(y, moony2, .05);
    }
    else {
      moony = lerp(y, moony1, .05);
    }
    
  }

  else {
    b1 = bgcolor;
    m1 = mtcolor;
    n1 = namecolor;
    x = moonx;
    y = moony;
    bgcolor = lerpColor(b1, bgcolor1, .6);
    mtcolor = lerpColor(m1, mtcolor1, .05);
    namecolor = lerpColor(n1, color(0), .05);
    moonx = lerp(x, moonx1, .05);
    if (moonx < 555) {
      moony = lerp(y, moony1, .05);
    }
    else {
      moony = lerp(y, moony2, .05);
    }
  }
}
void mouseClicked() {
  if (change == 0) {
    change = 1;
  }
  else if (change == 1) {
    change = 2;
  }
  else if (change == 2) {
    change = 1;
  }
}

void clickme() {
  fill(namecolor);
  noStroke();
  textFont(nameFont);
  textSize(10);
  text("CLICK ME!", 20, 20);
}