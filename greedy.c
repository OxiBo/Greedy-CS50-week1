/**
* CS50 week 1 Greedy
*/

#include <stdio.h>
#include <stdio.h>
#include <math.h>
#include <cs50.h>
int main (void) 
{
float x;
int change;
int coins=0;
printf ("O hai!");
do
{
printf ("How much change is owed?\n");
x=get_float();
}
while (x<0);
change=round(x*100);
if (change>=25)
{
    coins=(change-change%25)/25;
    change=change%25;
   } 
if (change>=10)
{
    coins=coins+(change-change%10)/10;
    change=change%10;
}    
if (change>=5)
{
    coins=coins+(change-change%5)/5;
    change=change%5;
}
if (change>=1)
{
    coins=coins+(change-change%1)/1;
    }
    
printf("%d\n", coins);
}