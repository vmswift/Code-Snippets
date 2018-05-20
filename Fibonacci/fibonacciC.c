//Fibonacci series in C
//Example by John Knowles

#include <stdio.h>
#include <stdlib.h>

int Fibonacci(int);

int main()
{
    int iterations = 0;

    printf("Enter number of Fibonacci iterations: ");
    scanf("%d", &iterations);
    //read number of iterations from user input

    for(int i = 1;i < iterations + 1; ++i)
    {
        printf(" %i", Fibonacci(i));
        //output current iteration from 1 to n iterations
    }

    printf("\n");
    return 0;

}


int Fibonacci(int n)
{
    if(n<=0)
    {
        printf("Incorrect number of iterations!\n");
    }
    else if(n==1)
    {
        return 0;
    }
    else if(n==2)
    {
        return 1;
    }
    else
    {
        return(Fibonacci(n-1)+Fibonacci(n-2));
    }

    return 0;
    //required to avoid compiler warning
}
