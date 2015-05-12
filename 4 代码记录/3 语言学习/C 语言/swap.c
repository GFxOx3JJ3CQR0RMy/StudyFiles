include "stdio.h"
int swap(int a,int b){
	int c;
	c = a;
	a = b;
	b = c;
	return 1;
}

int swap2(int *a,int *b){
	int c;
	c = *a;
	*a = *b;
	*b = c;
	return 1;
}

int swap3(int &a,int &b){
	int c;
	c = a;
	a = b;
	b = c;
	return 1;
}


int main(int argc, char* argv[])
{
	int a,b;
	a = 20;
	b = 40;
	printf("before swap : a= %d, b = %d.\n",a,b);

	swap3(a,b);

	printf("after  swap : a= %d, b = %d.\n",a,b);
		
	return 0;
}
