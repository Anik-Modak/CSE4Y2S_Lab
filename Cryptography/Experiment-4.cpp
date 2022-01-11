//Anik_Modak
#include<bits/stdc++.h>
using namespace std;

string TextToCipher(string text, int width)
{
    string encrypt;

    int step = 0, i = 0;
    while( step < width )
    {
        encrypt += text[i];

        i += width;
        if (i >= text.size())
        {
            i = ++step;
        }
    }
    return encrypt;
}

string CipherToText(string encrypt, int width)
{
    string dercypt(encrypt.size(), '#');

    int step = 0;
    for(int i = 0, j = step; i < encrypt.size(); i++)
    {
        dercypt[j] = encrypt[i];

        j += width;
        if (j >= encrypt.size())
        {
            j = ++step;
        }
    }
    return dercypt;
}


int main(int argc, char const *argv[])
{
    string text = "DEPARTMENT OF COMPUTER SCIENCE AND TECHNOLOGY UNIVERSITY OF RAJSHAHI BANGLADESH";

    int width;
    cout<<"Enter width: ";
    cin>>width;

    cout<<"\nPlain text: "<< text << endl;

    string encrypt = TextToCipher(text, width);
    encrypt = TextToCipher(encrypt, width);

    cout<<"\nEncrypted text: "<< encrypt << endl;

    string dercypt = CipherToText(encrypt, width);
    dercypt = CipherToText(dercypt, width);

    cout<< "\nAfter Reverse Operation Decypted text: "<< dercypt <<endl;
    return 0;
}
