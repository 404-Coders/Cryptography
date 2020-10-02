#include<ctype.h>
#include <stdlib.h>
#include<stdio.h>
#include<string.h>

typedef char* string;

//Declaration of Encryping and Number Checker Function
string encryptCaesar(string plainText, int key);
int isNumber(string s);

int main(int argc, string argv[])
{
    //Check for Command Line Arguments
    int key = 0;
    if (argc == 2 && isNumber(argv[1]))
    {
        key = atoi(argv[1]);
    }
    else
    {
        printf("Usage: ./caesar key\n");
        return 1;
    }

    //Getting Plain Text from User
    string plainText; 
    printf("plaintext: ");
    gets(plainText);

    //Getting Caesar Cipher by Calling method
    string cipherText = encryptCaesar(plainText, key);
    printf("ciphertext: %s\n", cipherText);
    return 0;
}

//Definition of Caesar Ciper Function
string encryptCaesar(string plainText, int key)
{
    string cipherText = malloc(sizeof(plainText));
    for (int i = 0, n = strlen(plainText); i <= n; i++)
    {
        if (plainText[i] >= 97 && plainText[i] <= 122)
        {
            int a = ((int)plainText[i] - 97 + key) % 26;
            cipherText[i] = (int)(97 + a);
        }
        else if (plainText[i] >= 65 && plainText[i] <= 90)
        {
            int a = ((int)plainText[i] - 65 + key) % 26;
            cipherText[i] = (int)(65 + a);
        }
        else
        {
            cipherText[i] = plainText[i];
        }
    }
    return cipherText;
}

//Function for Checking Number
int isNumber(string s)
{
    for (int i = 0, n = strlen(s); i < n; i++)
    {
        if (!isdigit(s[i]))
        {
            return 0;
        }
    }
    //checking for non negative keys
    return atoi(s) > 0;
}
