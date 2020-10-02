
#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<ctype.h>

typedef char* string;

int isUniqueAlpha(string alphabets);
string substituteCipher(string plainText, string key);

int main(int agrc, string argv[])
{
    string key = malloc(sizeof(char) * 26);
    if (isUniqueAlpha(argv[1]) && argv[1] != NULL)
    {
        //Checking for key less than 26
        if (strlen(argv[1]) != 26)
        {
            printf("Key must contain 26 characters.\n");
            return 1;
        }
        else
        {
            key = argv[1];
        }
    }
    //To do if key is not valid
    else
    {
        printf("Usage: ./substitution key\n");
        return 1;
    }

    //getting plain text from user
    printf("plaintext: ");
    string plainText;
    gets(plainText);

    //getting cipher from cipher function
    string cipherText = substituteCipher(plainText, key);
    printf("ciphertext: %s\n", cipherText);
}


int isUniqueAlpha(string key)
{
    //Checking if key is null
    if (key == NULL)
    {
        return 0;
    }
    int n = strlen(key);
    //Checking for non alpha characters

    for (int i = 0; i < n; i++)
    {

        if (!isalpha(key[i]))
        {
            return 0;
        }
    }

    //Checking for non-unique characters
    for (int i = 0; i < n; i++)
    {
        int count = 0;
        for (int j = 0; j < n; j++)
        {
            if (key[i] == key[j])
            {
                count++;
            }
        }
        if (count > 1)
        {
            return 0;
        }
    }
    //return 1 if key is valid
    return 1;
}

//Definition of Substitute Cipher
string substituteCipher(string plainText, string key)
{
    string cipher = malloc(sizeof(plainText));
    for (int i = 0, n = strlen(plainText); i < n; i++)
    {
        if (plainText[i] >= 97 && plainText[i] <= 122)
        {
            int letter = plainText[i];
            cipher[i] = tolower(key[letter - 97]);
        }
        else if (plainText[i] >= 65 && plainText[i] <= 90)
        {
            int letter = plainText[i];
            cipher[i] = toupper(key[letter - 65]);
        }
        else
        {
            cipher[i] = plainText[i];
        }
    }
    // printf("%s\n", cipher);
    return cipher;
}
