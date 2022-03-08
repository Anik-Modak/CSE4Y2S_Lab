#include<bits/stdc++.h>
using namespace std;

string encrypt(string text)
{
    string str, pad;
    ifstream fin;
    fin.open("pad_encrypt.txt");
    fin>>pad;
    fin.close();

    int cnt = 0;
    for(int i=0; i<text.size(); i++)
    {
        if(isupper(text[i]))
        {
            char ch = (((text[i] - 'A') + (pad[cnt] - 'A')) % 26) + 'A';
            str.push_back(ch);
            cnt++;
        }
        else
            str.push_back(text[i]);
    }

    ofstream fout;
    fout.open("pad_encrypt.txt");
    pad = pad.substr(cnt, pad.size() - cnt);
    fout<<pad;
    fout.close();

    return str;
}

string decrypt(string text)
{
    string str, pad;
    ifstream fin;
    fin.open("pad_decrypt.txt");
    fin>>pad;
    fin.close();

    int cnt = 0;
    for(int i=0; i<text.size(); i++)
    {
        if(isupper(text[i]))
        {
            char ch = (((text[i] - 'A') + 26 - (pad[cnt] - 'A')) % 26) + 'A';
            str.push_back(ch);
            cnt++;
        }
        else
            str.push_back(text[i]);
    }

    ofstream fout;
    fout.open("pad_decrypt.txt");
    pad = pad.substr(cnt, pad.size() - cnt);
    fout<<pad;
    fout.close();

    return str;
}

int main()
{
    string text;
    cout<<"Enter your original text: ";
    getline(cin, text);

    cout<<"\nPlain Text: "<<text<<endl;

    string chiper = encrypt(text);
    cout << "\nEncrypted Cipher: " << chiper <<endl;

    string original = decrypt(chiper);
    cout << "\nAfter Reverse Operation(Decryption): " << original <<endl;
    return 0;
}

