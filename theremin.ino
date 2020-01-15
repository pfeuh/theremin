
#define VC_PIN A0
#define DURATION 1000;

long unsigned milestone;


void setup()
{
    Serial.begin(9600);
    milestone = millis() + DURATION;
}


void loop()
{
    int val = analogRead(VC_PIN);  // read the input pin
    Serial.println(val);  
    //~ while(millis() < milestone);
    //~ milestone = millis() + DURATION;
}
