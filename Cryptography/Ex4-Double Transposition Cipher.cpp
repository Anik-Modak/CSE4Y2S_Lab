#include<bits/stdc++.h>
using namespace std;

string encrypt(string text, int width)
{
    string str;
    int col = 0, i = 0;
    while(col < width)
    {
        str.push_back(text[i]);
        i += width;
        if(i >= text.size())
            i = ++col;
    }
    return str;
}

string decrypt(string text, int width)
{
    string str(text.size(), ' ');
    int col = 0, j = 0;
    for(int i=0; i<text.size(); i++)
    {
        str[j] = text[i];
        j += width;
        if(j >= text.size())
            j = ++col;
    }
    return str;
}

int main()
{
    string text = "DEPARTMENT OF COMPUTER SCIENCE AND TECHNOLOGY UNIVERSITY OF RAJSHAHI BANGLADESH";

    int width;
    cout<<"Enter width: ";
    cin>>width;

    cout<<"\nPlain Text: "<<text<<endl;

    string chiper = encrypt(text, width);
    chiper = encrypt(chiper, width);
    cout << "\nEncrypted Cipher: " << chiper <<endl;

    string original = decrypt(chiper, width);
    original = decrypt(original, width);
    cout << "\nAfter Reverse Operation(Decryption): " << original <<endl;
    return 0;
}

