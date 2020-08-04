int height;
int width;
void setup() {
  height = 250;
  width = 1110;
  size(width, height);
  background(255);
  
}

void draw() {
  fill(41, 65, 94);
  noStroke();
  triangle(0+205 , height, 100+205, height - 120, 200+205, height);
  triangle(100+205 , height, 200+205, height - 100, 300+205, height);
  /*triangle(230+55, height, 230+110+55, height - 90, 230 + 220+55, height);*/
  triangle(360+55, height, 360+130+55, height - 70, 410 + 200+55, height);
  triangle(560+55, height, 560 + 120+55, height - 160, 560 + 240+55, height);
  triangle(700+55, height, 700+80+55, height - 90, 700 + 150+55, height);


  stroke(83, 104, 130);
  strokeWeight(2);
  line(100+205, height - 120, 200+205, height);
  line(200+205, height - 100, 300+205, height);
  line(360+130+55, height - 70, 410 + 200+55, height);
  line(560 + 120+55, height - 160, 560 + 240+55, height);
  line(700+80+55, height - 90, 700 + 150+55, height);

  fill(0);
  textsize(32);
  text("Michelle Park", width/2, height/2);
}

