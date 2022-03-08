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

bool lehmannAglorithm(ll p, int test)
{
    if(p==2 || p==3)
        return 1;
    if(p==1 || p%2==0)
        return 0;

    for(int i=0; i<test; i++)
    {
        ll a = 2 + (rand() % (p-3));
        ll L = Bigmod(a, (p-1)/2, p);
        if(L != 1 && L != -1 && L != (p-1))
            return 0;
    }
    return 1;
}

int main()
{
    ll num; // 180181
    cout<<"Enter a number: ";
    cin>>num;

    int test;
    cout<< "Enter number of Test: ";
    cin>>test;

    int prime = lehmannAglorithm(num, test);
    if(prime)
        cout<<"May be Prime\n";
    else
        cout<<"Definitely not prime\n";
    return 0;
}


