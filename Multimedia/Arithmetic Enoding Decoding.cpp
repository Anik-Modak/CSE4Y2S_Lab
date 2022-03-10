#include<bits/stdc++.h>
#define pii pair<double, double>
using namespace std;

map<char, double> probability;
map<char, pii> range;

double low_range(char ch)
{
    double low = range[ch].first;
    return low;
}

double high_range(char ch)
{
    double high = range[ch].second;
    return high;
}

double arithmeticEncoding(string str)
{
    double low = 0.0, high = 1.0, range = 1.0;
    for(int i=0; i<str.size(); i++)
    {
        high = low + range*high_range(str[i]);
        low = low + range*low_range(str[i]);
        range = high - low;
        //cout<<low<<" "<<high<<" "<<range<<" "<<endl;
    }
    double tag = (low+high)/2;
    return tag;
}

string arithmeticDecoding(double value)
{
    bool terminate = true;
    string str;
    while(terminate)
    {
        double high, low, rang;
        for(auto it=range.begin(); it != range.end(); it++)
        {
            pii tmp = it->second;
            if(tmp.first <= value && value < tmp.second)
            {
                char ch = it->first;
                //cout<<value<<" "<<ch<<endl;
                str.push_back(ch);
                low = low_range(ch);
                high = high_range(ch);
                rang = high-low;
                value = (value-low)/rang;

                if(ch=='~')
                    terminate = false;
                break;
            }
        }
    }
    return str;
}

int main()
{
    string str;
    freopen("arithmetic_coding_in.txt");
    cin>>str; //last character must be ~

    map<int, int> mp;
    for(int i=0; i<str.size(); i++)
    {
        mp[(int)str[i]] ++;
    }

    double pre = 0;
    cout <<"Symbol\t\t"<<"Probability\t"<<"Range\t"<<endl;
    for(int i=0; i<130; i++)
    {
        if(mp[i])
        {
            double len = str.size();
            char ch = i;
            probability[ch] = mp[i]/len;
            range[ch] = {pre, pre + probability[ch]};
            cout <<ch << "\t\t"<<probability[ch] << "\t\t["<<pre<<"\t"<<pre+probability[ch]<<")\n";
            pre += probability[ch];
        }
    }
    //str = "CAEEG";
    double encode = arithmeticEncoding(str);
    cout<<"\nEncoded Tag: "<<encode<<endl;
    string decode = arithmeticDecoding(encode);
    cout<<"\nDecoded String: "<<decode<<endl;

    return 0;
}
