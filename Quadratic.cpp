#include<iostream>
#include<math.h>
using namespace std;
void quadratic(int a,int b,int c){
	float x1,x2;
	float d=pow(b,2)-4*a*c;
	if(d>0){
		 x1=(-b+sqrt(d))/(2*a);
		 x2=(-b-sqrt(d))/(2*a);
	}
	else if(d==0){
		x1=-b/(2*a);
		x2=-b/(2*a);
	}
	else if(d<0){
		float real,img;
		real=-b/(2*a);
		img=sqrt(-d)/(2*a);
		//%d%d%d is %.2f and %.2f"
		cout<<"Quaratic equation\n";
	cout<<a<<"x^2+"<<b<<"x+"<<c;
	cout<<"\nHas Roots:\n"<<"Value1:"<<real<<"+"<<img<<"i "<<"Value2:"<<real<<"-"<<img<<"i";
	
	}
	if(d>0&& d==0){
	cout<<"Quaratic equation\n";
	cout<<a<<"x^2+"<<b<<"x+"<<c;
	cout<<"\nHas roors \nValue1:"<<x1<<"  Value2:"<<x2;
	}
}

int main(){
	int a,b,c;
	cout<<"A quadratic equation is of the form\nAx^2+Bx+c";
	cout<<"\nEnter A:";
	cin>>a;
	cout<<"\nEnter B:";
	cin>>b;
	cout<<"\nEnter C:";
	cin>>c;
	if(a!=0)
	quadratic(a,b,c);
	else{
		cout<<"Values inputed invalid";
	}
	return 0;
}