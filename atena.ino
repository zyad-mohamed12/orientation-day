int g=3;
int v=2;
int r=4;
char data='0';
void setup() {
  pinMode(g, OUTPUT);
  pinMode(v, OUTPUT);
  pinMode(r, OUTPUT);
  Serial.begin(9600);
}
void loop() {
  if (Serial.available()){
  data=Serial.read();
  if (data=='1'){
  digitalWrite(v,HIGH);
  }
  if (data=='2'){
  digitalWrite(v,LOW);
  }
  if(data=='3'){
  digitalWrite(r,HIGH);
  }
  if(data=='4'){
  digitalWrite(r,LOW);
  }
  if(data=='5'){
  digitalWrite(g,HIGH);
  }
  if(data=='6'){
  digitalWrite(g,LOW);
  }
}
}
