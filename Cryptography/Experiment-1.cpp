#include<bits/stdc++.h>
using namespace std;

string encrypt(string text, int s)
{
    string result = "";
    for (int i=0; i<text.length(); i++)
    {
        // Encrypt Uppercase letters
        if (isupper(text[i]))
            result += char(int(text[i]+s-65)%26 +65);
        // Encrypt Lowercase letters
        else if(islower(text[i]))
            result += char(int(text[i]+s-97)%26 +97);
        else
            result += text[i];
    }
    return result;
}

string decrypt(string text, int s)
{
    s = 26 - s;
    string result = "";
    for (int i=0; i<text.length(); i++)
    {
        // Encrypt Uppercase letters
        if (isupper(text[i]))
            result += char(int(text[i]+s-65)%26 +65);
        // Encrypt Lowercase letters
        else if(islower(text[i]))
            result += char(int(text[i]+s-97)%26 +97);
        else
            result += text[i];
    }
    return result;
}

int main()
{
    string text;
    cout<<"Enter your original text: ";
    getline(cin, text);

    int shift;
    cout<<"Enter how many shift to the right: ";
    cin>>shift;

    string chiper = encrypt(text, shift%26);
    cout << "\nCipher: " << chiper <<endl;

    string original = decrypt(chiper, shift);
    cout << "\nAfter Reverse Operation: " << original <<endl;
    return 0;
}

