#include<iostream>
using namespace std;

class car{
	int model;
	
	public :
		car(int y){
			model=y;
		}
		
		void display(){
			cout<<model<<endl;
		}
		
		//>,<,>==,<==,== and !=
		void operator ++(int){
			model= model+2;
		}
		void operator--(int){
			model= model-5;
		}
		
		int operator>(car c){
				if(model > c.model)
						return 1;
				else
						return 0;
						
	}
		
		
};



int main(){
	
	car c1(2010),c2(2015);
	
	if(c1>c2){ // c1.>(c2)
		cout<<"c1 is latest";
		c1.display();
	}
	else
	{
		cout<<"c2 is latest";
		c2.display() ;
	}
	
	}


