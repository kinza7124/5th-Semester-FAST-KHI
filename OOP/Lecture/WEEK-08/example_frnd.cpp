#include<iostream>
using namespace std;

class student{
	private:
		string name;
		int marks;
	public:
		student(string n, int m){
			name=n;
			marks=m;
		}
	friend void GetInfo(student);
	friend void Edit(student &);
};

class course{
	private:
		string course_name;
};

int main(){
	student s("Ali",80);
	course cs101("PF");
	GetInfo(s);
	Edit(s);
	GetInfo(s);
}

void Edit(student &a){
	a.marks=90;
	}

void GetInfo(student a){
	cout<<"\n Name="<<a.name;
	cout<<"\n Marks="<<a.marks;
	cout<<"\n Course Name=";
}




