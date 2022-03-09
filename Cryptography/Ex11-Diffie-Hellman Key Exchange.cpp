#include<bits/stdc++.h>
#define ll long long
using namespace std;

ll Bigmod(ll a, ll b, ll m)
{
    ll res = 1;
    for(ll i = 1; i<=b; i++)
    {
        res = (res*a) % m;
    }
    return res;
}

int main()
{
    srand(time(NULL));
    ll q = 353, a = 3;
    ll xa = 1 + rand()%(q-1);
    ll xb = 1 + rand()%(q-1);

    ll ya = Bigmod(a, xa, q);
    ll yb = Bigmod(a, xb, q);

    cout<<"A computes K: "<<Bigmod(yb, xa, q)<<endl;
    cout<<"B computes K: "<<Bigmod(ya, xb, q)<<endl;
    return 0;
}



