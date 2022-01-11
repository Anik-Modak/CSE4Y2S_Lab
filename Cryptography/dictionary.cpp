#include<bits/stdc++.h>
using namespace std;

int main()
{
    string msg, chiper;
    freopen("dictionary.txt","r",stdin);
    freopen("dictionary2.txt","w",stdout);
    while(cin>>msg>>chiper)
    {
        transform(msg.begin(), msg.end(), msg.begin(), ::toupper);
        transform(chiper.begin(), chiper.end(), chiper.begin(), ::toupper);
        cout<<msg<<" "<<chiper<<endl;
    }
    return 0;
}
