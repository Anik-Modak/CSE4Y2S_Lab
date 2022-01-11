#include<bits/stdc++.h>
using namespace std;

map <string, string> encryptData;
map <string, string> decryptData;

void fn(string str)
{
    ifstream  readChiperLower, readChiperUpper;

    string msg, cipher;

    if(islower(str[0]))
    {
        readChiperLower.open("dictionary.txt");
        while( readChiperLower >> msg >> cipher)
        {
            encryptData[msg] = cipher;
            decryptData[cipher] = msg;
        }
        readChiperLower.close();
    }

    if(isupper(str[0]))
    {
        readChiperUpper.open("dictionary2.txt");
        while(readChiperUpper >> msg >> cipher)
        {
            encryptData[msg] = cipher;
            decryptData[cipher] = msg;
        }
        readChiperUpper.close();
    }
}

string PlaintextToCipher(string text)
{
    replace(text.begin(), text.end(), ' ', '_');
    string block;
    int startPos = 0;

    for(int i = 0; i < text.size(); i++)
    {
        block += text[i];

        if(block.size() == 3)
        {
            block = encryptData[block];

            int x, y;
            for(x = startPos, y = 0; y < 3 ; y++, x++)
            {
                text[x] = block[y];
            }

            startPos = x;
            block.clear();
        }
    }
    return text;
}

string CipherToPlaintext(string encrypt)
{
    string block;
    int startPos = 0;

    for(int i = 0; i < encrypt.length(); i++)
    {
        block += encrypt[i];

        if(block.size() == 3)
        {
            block = decryptData[block];

            int x, y;
            for(x = startPos, y = 0; y < 3 ; y++, x++)
            {
                encrypt[x] = block[y];
            }
            startPos = x;
            block.clear();
        }
    }
    replace(encrypt.begin(), encrypt.end(), '_', ' ');
    return encrypt;
}

int main(int argc, char const *argv[])
{
    string text;
    cout<<"Enter your original text: ";
    getline(cin, text);

    fn(text);
    cout << "......................" <<endl;

    cout << "Plain Text: "<< text << endl << endl;

    string encrypt = PlaintextToCipher(text);

    cout <<"Cipher: " << encrypt << endl << endl;

    string decrypt = CipherToPlaintext(encrypt);

    cout << "After Reverse Operation The Plain Text is: "<< decrypt << endl;

    return 0;
}
