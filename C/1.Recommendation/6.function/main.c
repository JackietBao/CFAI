/*
#include "func.h"
//函数的声明与定义



int main() {
    int a=10;
    a=print_star(a);
    print_message();//调用print_message()
    print_star(5);
    return 0;
}


#include <stdio.h>

int f(int n)
{
    if(1==n)
    {
        return 1;
    }
    return n*f(n-1);
}

int step(int n)
{
    if(1==n||2==n)
    {
        return n;
    }
    return step(n-1)+step(n-2);
}


int main() {
    int n;
    scanf("%d",&n);
    int result;
    result=f(n);
    printf("step(%d)=%d\n",n,step(n));
    return 0;
}

#include <stdio.h>

int i=10;//i是一个全局变量,不建议使用
void print(int a)//形参看成一个局部变量
{
    printf("I am print i=%d\n",i);
}

int main() {
    {
        int j=5;
    }//局部变量只在离自己最近的大括号内有效
    int i=5;
    printf("main i=%d\n",i);
    for(int k=0;k<-1;)
    {

    }
//    printf("k=%d\n",k);for循环括号内定义的变量，循环体外不可用
    print(3);
    return 0;
}
 */










#include <stdio.h>

int step(int n)
{
    if(n==1 || n==2)
    {
        return n;
    }
    return step(n-1)+ step(n-2);
}

int main() {
    int n, result;
    scanf("%d",&n);
    result= step(n);
    printf("%d",result);
    return 0;
}



























