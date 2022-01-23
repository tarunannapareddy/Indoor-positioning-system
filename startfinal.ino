#include "Stepper.h"
#include "complex.h"
#include "Math.h"

double d,r,r1,r2,r3,d1;
double dist1,dist2,dist3;
Complex guess(5,0);
Complex c1(0,0);
Complex c2(2,0);
Complex c3(0,2);
int left_in1Pin = 1;
int left_in2Pin = 2;
int left_in3Pin= 3;
int left_in4Pin = 4;
int right_in1Pin = 5;
int right_in2Pin = 6;
int right_in3Pin = 7;
int right_in4Pin = 8;

#define STEPS 200
 
Stepper motorleft(STEPS, left_in1Pin,left_in2Pin,left_in3Pin,left_in4Pin); 
Stepper motorright(STEPS, right_in1Pin, right_in2Pin, right_in3Pin, right_in4Pin); 
 
void setup(){
  pinMode(left_in1Pin, OUTPUT);
  pinMode(left_in2Pin, OUTPUT);
  pinMode(left_in3Pin, OUTPUT);
  pinMode(left_in4Pin, OUTPUT);
  pinMode(right_in1Pin, OUTPUT);
  pinMode(right_in2Pin, OUTPUT);
  pinMode(right_in3Pin, OUTPUT);
  pinMode(right_in4Pin, OUTPUT);
   
  Serial.begin(115200);
  motorright.setSpeed(60);
  motorleft.setSpeed(60);
  Serial.println("start");
    
 }

void moveStright(double distance)
{  
   int no_of_steps=int((distance*100)/(3.14*r));
   int k=0;
 
   while( k< no_of_steps)
   {   
     motorright.step(1);
     motorleft.step(1);
     k++;
   }
}

void moveBack(double distance)
{  
  int no_of_steps=int((distance*100)/(3.14*r));
   int k=0;
 
   while( k> no_of_steps)
   {   
     motorright.step(1);
     motorleft.step(1);
     k--;
   }
}

void turn(double degree){

   int no_of_steps=int((d*degree)/(800*3.14*r));
   int k=0;
 
   while( k< no_of_steps)
   {   
     motorright.step(-1);
     motorleft.step(1);
     k++;
   }

}  

double slope(double x, double y){
  double angle = 1.57 - atan((y-2)/x);
  return angle;
}
  
double dist(double x, double y){
  double distance = (x*x) + (y-2)*(y-2);
  return sqrt(distance);  
}

char a1[7]={};
char a2[7]={};
char a3[7]={};

Complex trilateration(double r1, double r2, double r3){
  
  Complex proj1(0,0);
  Complex proj2(0,0);
  Complex proj3(0,0);
  
  for(int i=1; i<=100; i++){
   proj1 = c1 + ((guess-c1)*r1 / (guess-c1).modulus());
   proj2 = c2 + ((guess-c2)*r2 / (guess-c2).modulus());
   proj3 = c3 + ((guess-c3)*r3 / (guess-c3).modulus());
   guess = (proj1 + proj2 + proj3)/3.0;
  }
  return guess;  
}

int command =0;

void loop(){
     
 if(Serial.available())
   {
      for(int i = 0; i<6; i++)
        a1[i] = char(Serial.read());
      a1[6] = '\0';
      String b1 = a1;
      d1 = b1.toFloat();
      
      if(command==0)
      {
        dist1=d1;
        moveStright(200);
        Serial.println(dist1);
      }
      if(command ==1) 
      {
        dist2=d1;
        turn(1.57);
      }
      if(command ==2)
      { 
        dist3=d1;
        moveStright(200);
        Serial.println(dist3);
      }
      if(command ==3)
      {
          Complex com1 = trilateration(dist1,dist2,dist3); // check
          double a_1= dist(c1.real(),c1.imag());
          double b_1 = slope(c1.real(),c1.imag());
          turn(b_1);
          moveStright(a_1);
          Serial.println("reached");     
      }
      command++;
  }
}
