#include<bits/stdc++.h>
using namespace std;

string to_string(int i)
{
    ostringstream ss;
    ss<<i;
    return ss.str();
}

int run_length_encode()
{
    ifstream fin;
    fin.open("RunLengthInput.txt");

    ofstream fout;
    fout.open("RunLengthEncoding.txt");

    int en_len = 0;
    string encode, str;
    while(fin>>str)
    {
        int len = str.size();
        for(int i=0; i<len; i++)
        {
            int cnt = 1;
            while(i<len-1 && str[i]==str[i+1])
            {
                cnt++;
                i++;
            }
            encode.push_back(str[i]);
            encode += "("+ to_string(cnt)+")";
        }
        en_len += encode.size();
        fout<<encode<<"\n";
        encode.clear();
    }
    return en_len;
}

int run_length_decode()
{
    ifstream fin;
    fin.open("RunLengthEncoding.txt");

    ofstream fout;
    fout.open("RunLengthDecoding.txt");

    int de_len = 0;
    string str;
    while(fin>>str)
    {
        int len = str.size();
        for(int i=0; i<len; i++)
        {
            if(str[i]=='(')
            {
                int cnt = 0;
                for(int j=i+1; j<str.size() && str[j] != ')'; j++)
                {
                    cnt = cnt*10 + (int)(str[j] - '0');
                }
                for(int j = 0; j<cnt; j++)
                {
                    fout<<str[i-1];
                }
                de_len += cnt;
            }
        }
        fout<<"\n";
    }
    return de_len;
}

int main()
{
    int encodeLen = run_length_encode();
    int decodeLen = run_length_decode();

    double compression_ratio = double(decodeLen)/encodeLen;
    cout<<"\nCompression Ratio: "<<compression_ratio<<endl;
    return 0;
}
