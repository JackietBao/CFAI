/*
#include <stdio.h>
//符号常量
#define PI 3+2
int main() {
    int i=PI*2;//i就是一个整型变量
    printf("i=%d\n",i);//printf是用来输出的
    printf("i size=%d\n",sizeof(i));//sizeof可以用来计算某个变量的空间大小
    return 0;
}


//浮点型
#include <stdio.h>

int main() {
    float f=3e-3;
    printf("f=%f\n",f);
    return 0;
}






 //字符型
#include <stdio.h>
//大写表小写
int main() {
    char c='A';
    printf("%c\n",c+32);//以字符形式输出
    printf("%d\n",c);//以数值形式输出
    return 0;
}



#include <stdio.h>
//强制类型转换
int main() {
    int i=5;
    float f=i/2;//这里做的是整型运算，因为左右操作数都是整型
    float k=(float)i/2;
    printf("%f\n",f);
    printf("%f\n",k);
    return 0;
}




#include <stdio.h>
//练习printf
int main() {
    int age=21;
    printf("Hello %s, you are %d years old\n", "Bob", age);
    int i=10;
    float f=96.3;
    printf("student number=%-3d,score=%5.2f\n",i,f);//默认是右对齐，加一个负号代表左对齐
    //内容的最小宽度为5，并保留两位小数
    i=100;
    f=98.21;
    printf("student number=%3d,score=%5.2f\n",i,f);
    return 0;
}



//进制转换
#include <stdio.h>

int main() {
    int i=0x7b;
    printf("%d\n",i);//十进制输出
    printf("%o\n",i);//八进制
    printf("%x\n",i);//十六进制
    return 0;
}






//scanf读取

#include <stdio.h>

//scanf用来读取标准输入，scanf把标准输入内的内容，需要放到某个变量空间里，因此变量必须取地址
//scanf会阻塞，是因为标准输入缓冲区是空的
int main() {
    int i;
    char c;
    float f;
    scanf("%d",&i);
    printf("i=%d\n",i);//把标准缓冲区中的整型数读走了
    fflush(stdin);//清空标准输入缓冲区
    scanf("%c",&c);
    printf("c=%c\n",c);//输出字符变量c
//    scanf("%f",&f);
//    printf("f=%f\n",f);
    return 0;
}




#include <stdio.h>
//scanf一次读多种数据类型
int main() {
    int i,ret;
    float f;
    char c;
    ret=scanf("%d %c%f",&i,&c,&f);//ret是指scanf匹配成功的个数
    printf("i=%d,c=%c,f=%5.2f\n",i,c,f);
    return 0;
}



//作业

#include <stdio.h>

int main() {
    printf("hello wangdao\n");
    return 0;
}



#include <stdio.h>

//scanf练习和加法运算
int main() {
    int a,b,c;
    scanf("%d%d",&a,&b);
    c=a+b;
    printf("%d\n",c);
    return 0;
}


#include <stdio.h>

//读取一个整型数，以字符形式输出
int main() {
    int i;
    scanf("%d",&i);
    printf("%c\n",i);
    return 0;
}

 */






//scanf读取

#include <stdio.h>

//scanf用来读取标准输入，scanf把标准输入内的内容，需要放到某个变量空间里，因此变量必须取地址
//scanf会阻塞，是因为标准输入缓冲区是空的
int main() {
    int i;
    char c;
    float f;
    scanf("%d",&i);
    printf("i=%d\n",i);//把标准缓冲区中的整型数读走了
    fflush(stdin);//清空标准输入缓冲区
    scanf("%c",&c);
    printf("c=%c\n",c);//输出字符变量c
//    scanf("%f",&f);
//    printf("f=%f\n",f);
    return 0;
}























































































