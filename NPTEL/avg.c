#include<stdio.h>
int main(){
int a[10],i,avg1,avg2,avg3;

i=0;
while(a[i]==-1){
scanf("%d",&a[i]);
i++;
}
avg1 = a[0];
avg2 = (a[0]+a[1])/2;
avg3 = (a[0]+a[1]+a[2])/3;
printf("%d %d %d",avg1,avg2,avg3);

}
