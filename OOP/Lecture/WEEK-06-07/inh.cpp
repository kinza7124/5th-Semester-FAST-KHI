#include <iostream>
using namespace std;

class base{
	protected: 
		int age;
		string name;
	public:
		setage(int i){
			age=i;
		}
		setname(string i){
			name=i;
		}
		
};

class child: private base{
	private:
		int height;
		float age;
			
	
	public:
		setdata(int a, int h, string n){
			age=a;
//			setname(n);
			height=h;
		}
		seth(){
		}
};

class subchild: public child{
	private:
	
};

int main(){
child c;
c.setage(10);
}
