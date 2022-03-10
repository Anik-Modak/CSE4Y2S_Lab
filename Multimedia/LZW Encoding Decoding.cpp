#include<bits/stdc++.h>
using namespace std;

map<string, int>enDictionary;
map<int, string>deDictionary;

int LZW_encoding(string text)
{
    string s;
    s.push_back(text[0]);

    vector<int> encode;
    int code = enDictionary.size();
    for(int i=1; i<text.size(); i++)
    {
        char c = text[i];
        if(enDictionary[s+c] > 0)
            s = s + c;
        else
        {
            encode.push_back(enDictionary[s]);
            enDictionary[s+c] = ++code;
            s = c;
        }
    }
    encode.push_back(enDictionary[s]);

    ofstream fout;
    fout.open("lzw_encoded.txt");

    for(int i=0; i<encode.size(); i++)
        fout<<encode[i]<<" ";
    return encode.size();
}

int LZW_decoding()
{
    ifstream fin;
    fin.open("lzw_encoded.txt");

    int n;
    vector<int> encode;
    while(fin>>n)
        encode.push_back(n);

    int code = deDictionary.size();
    string decode = "", s = "";
    for(int i=0; i<encode.size(); i++)
    {
        int k = encode[i];
        string entry = deDictionary[k];
        decode += entry;

        if(!s.empty())
        {
            s.push_back(entry[0]);
            deDictionary[++code] = s;
        }
        s = entry;
    }

    ofstream fout;
    fout.open("lzw_decoded.txt");
    fout<<decode;
    return decode.size();
}

int main()
{
    string orginal, str;
    freopen("LZW_input.txt","r",stdin);
    cin>>orginal;

    int code;
    while(cin>>code>>str)
    {
        enDictionary[str] = code;
        deDictionary[code] = str;
    }

    int enLen = LZW_encoding(orginal);
    int deLen = LZW_decoding();
    double compression_ratio = double(deLen)/enLen;
    cout<<"\nCompression Ratio: "<<compression_ratio<<endl;
    return 0;
}

