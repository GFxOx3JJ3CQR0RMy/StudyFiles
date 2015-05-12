#include <stdio.h>
#include "stdlib.h"
int main(int argc, char* argv[])
{
	int a,b;
	if(argc != 3){
		printf("%s [num1]  [num2] \n",argv[0]);
	}
	else{
		a = atoi(argv[1]);
		b = atoi(argv[2]);
		printf("%d + %d = %d\n", a,b, a+b);
	}

	return 0;
}


#include <stdio.h>
int main(int argc, char* argv[])
{
	int a,b;

	printf("input a :");
	scanf("%d",&a);
	printf("input b :");
	scanf("%d",&b);
	printf("%d + %d = %d\n", a,b, a+b);
	
	return 0;
}