/*

#include <stdio.h>

//练习if与else
int main() {
    int i;
    while(scanf("%d",&i))
    {
        if(i>0)//if下面加一个大括号
        {
            printf("i is bigger than 0\n");
        }else{
            printf("i is not bigger than 0\n");
        }
    }

    return 0;
}


#include <stdio.h>
//计算从1到100的和

int main() {
    int i=1,total=0;
    while(i<=100)//在这里加分号会造成死循环
    {
        if(i%2==0)
        {
            i++;
            continue;//continue下面的代码均不会得到执行
        }
        total=total+i;//把i加到total上
        i++;//i++等价于 i+=1; 在循环体内没有让while判断表达式趋近于假的操作，死循环
    }
    printf("total=%d\n",total);
    return 0;
}



#include <stdio.h>
//for 循环实现从1加到100
int main() {
    int i,total;
    for(i=1,total=0;i<=100;i++)//for小括号后不要加分号
    {
        total+=i;
    }
    printf("total=%d\n",total);
    return 0;
}


#include <stdio.h>
//for 循环实现从1加到100
//使用continue
int main() {
    int i,total;
    for(i=1,total=0;i<=100;i++)//for小括号后不要加分号
    {
        if(i%2==0)
        {
            continue;//continue下面的代码均不会得到执行
        }
        total+=i;
    }
    printf("total=%d\n",total);
    return 0;
}

#include <stdio.h>
//for 循环实现从1加到100
int main() {
    int i,total;
    for(i=1,total=0;i<=100;i++)//for小括号后不要加分号
    {
        if(total>2000)
        {
            break;//当和大于2000时，循环结束
        }
        total+=i;
    }
    printf("total=%d,i=%d\n",total,i);
    return 0;
}



#include <stdio.h>
//课时4作业1 判断一个数是否是对称数
int main() {
    int a,b=0,backup_a;
    scanf("%d",&a);//读取一个整型数
    backup_a=a;//把a的值备份一下
    while(a)
    {
        b=b*10+a%10;//b把原有的值乘以10，然后再加余数
        a=a/10;
    }
//    printf("b=%d\n",b);//为了辅助自己理解
    if(b==backup_a)
    {
        printf("yes\n");
    }else{
        printf("no\n");
    }
    return 0;
}

#include <stdio.h>
//课时4作业2
//求n的阶乘
int main() {
    int n;
    scanf("%d",&n);
    int i,result=1;
    for(i=1;i<=n;i++)
    {
        result*=i;
    }
    printf("%d\n",result);
    return 0;
}




#include <stdio.h>
//课时4作业3
//换钞票
int main() {
    int a,b,c,d,count=0;
    for(a=1;a<=10;a++)
    {
        for(b=1;b<=20;b++)
        {
            for(c=1;c<=37;c++)
            {
                for(d=1;d<=37;d++)
                {
                    if(a+b+c+d ==40 && 10*a+5*b+2*c+d==100)
                    {
                        count++;//换法加1
                    }
                }
            }
        }
    }
    printf("%d\n",count);
    return 0;
}

#include <stdio.h>

int main() {
    int n;
    scanf("%d",&n);
    int i,result=1;
    for(i=1;i<=n;i++)
    {
        result*=i;
    }
    printf("%d",result);
    return 0;
}
 */







#include <stdio.h>
int main() {
    int i,j,k,l,count=0;
    for(i=1;i<=10;i++)
    {
        for(j=1;j<=20;j++)
        {
            for(k=1;k<=37;k++)
            {
                for(l=1;l<=37;l++)
                {
                    if(i+j+k+l == 40 && i*10+j*5+k*2+l == 100)
                    {
                        count++;
                    }
                }
            }
        }
    }
    printf("%d",count);
    return 0;
}

















