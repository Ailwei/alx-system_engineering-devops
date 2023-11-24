#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <unistd.h>

/**
 * infinite_while - Infinite loop function
 *
 * Return: Always 0.
 */
int infinite_while(void)
{
    while (1)
    {
        sleep(1);
    }
    return (0);
}

/**
 * main - Entry point of the program
 *
 * Return: Always 0.
 */
int main(void)
{
    pid_t child_pid;
    int i;

    for (i = 0; i < 5; i++)
    {
        child_pid = fork();  /* Create child process */

        if (child_pid == -1)
        {
            perror("Error creating child process");
            return (1);
        }

        if (child_pid == 0)
        {
            /* Inside the child process */
            printf("Zombie process created, PID: %d\n", getpid());
            exit(0);
        }
    }

    infinite_while();  /* Enter infinite loop */

    return (0);
}

