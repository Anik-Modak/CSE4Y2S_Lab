#include<bits/stdc++.h>
using namespace std;

map <string, string> encryptData;
map <string, string> decryptData;

void fn(char ch)
{
    ifstream  fileLower, fileUpper;
    string msg, cipher;

    if(islower(ch))
    {
        fileLower.open("dictionary.txt");
        while( fileLower >> msg >> cipher)
        {
            encryptData[msg] = cipher;
            decryptData[cipher] = msg;
        }
        fileLower.close();
    }

    if(isupper(ch))
    {
        fileUpper.open("dictionary2.txt");
        while(fileUpper >> msg >> cipher)
        {
            encryptData[msg] = cipher;
            decryptData[cipher] = msg;
        }
        fileUpper.close();
    }
}

string encrypt(string text)
{
    string block, str = "";
    replace(text.begin(), text.end(), ' ', '_');
    for(int i=0; i<text.size(); i++)
    {
        block.push_back(text[i]);
        if(block.size()==3)
        {
            str += encryptData[block];
            //cout<<block<<" "<<encryptData[block]<<endl;
            block.clear();
        }
    }
    return str;
}

string decrypt(string text)
{
    string block, str = "";
    for(int i=0; i<text.size(); i++)
    {
        block.push_back(text[i]);
        if(block.size()==3)
        {
            str += decryptData[block];
            //cout<<block<<" "<<encryptData[block]<<endl;
            block.clear();
        }
    }
    replace(str.begin(), str.end(), '_', ' ');
    return str;
}

int main()
{
    string text;
    cout<<"Enter your original text: ";
    getline(cin, text);

    int n, len = text.size();
    if(len%3)
    {
        n = len + (3-len%3);
        text.resize(n, ' ');
    }

    fn(text[0]);
    cout<<"\nPlain Text: "<<text<<endl;

    string chiper = encrypt(text);
    cout << "\nEncrypted Cipher: " << chiper <<endl;

    string original = decrypt(chiper);
    cout << "\nAfter Reverse Operation(Decryption): " << original <<endl;
    return 0;
}

