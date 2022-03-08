#include<bits/stdc++.h>
using namespace std;

string encrypt(string text, int shift)
{
    string str = "";
    for(int i=0; i<text.size(); i++)
    {
        if(isupper(text[i]))
        {
            char ch = (text[i]+shift-'A')%26 + 'A';
            str.push_back(ch);
        }
        else if(islower(text[i]))
        {
            char ch = (text[i]+shift-'a')%26 + 'a';
            str.push_back(ch);
        }
        else
            str.push_back(text[i]);
    }
    return str;
}

string decrypt(string text, int shift)
{
    string str = "";
    for(int i=0; i<text.size(); i++)
    {
        if(isupper(text[i]))
        {
            char ch = (text[i]+shift-'A')%26 + 'A';
            str.push_back(ch);
        }
        else if(islower(text[i]))
        {
            char ch = (text[i]+shift-'a')%26 + 'a';
            str.push_back(ch);
        }
        else
            str.push_back(text[i]);
    }
    return str;
}

int main()
{
    string text;
    cout<<"Enter your original text: ";
    getline(cin, text);

    int shift;
    cout<<"Enter how many shift to the right: ";
    cin>>shift;
    shift = shift%26;

    cout<<"\nPlain Text: "<<text<<endl;

    string chiper = encrypt(text, shift);
    cout << "\nEncrypted Cipher: " << chiper <<endl;

    string original = decrypt(chiper, 26-shift);
    cout << "\nAfter Reverse Operation(Decryption): " << original <<endl;
    return 0;
}
