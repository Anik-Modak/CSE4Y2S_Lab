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

bool RobinMiller(ll p)
{
    ll m = p - 1, b = 0;
    while(m%2==0)
    {
        m /= 2;
        b++;
    }

    ll a = 1 + rand()%(p-1);
    ll j = 0, z = Bigmod(a, m, p);
    if(z==1 || z==p-1)
        return 1;
L:
    if(j>0 && z==1)
        return 0;
    j = j + 1;
    if(j < b && z != p-1)
    {
        z = (z*z)%p;
        goto L;
    }
    if(z==p-1)
        return 1;
    if(j==b && z != p-1)
        return 0;
}

bool IsPrime(ll p, ll iter)
{
    if (p == 2 || p == 3)
        return true;
    if (p == 1 || p % 2 == 0)
        return false;

    for (long long i = 0; i < iter; i++)
    {
        if (RobinMiller(p) == false)
            return false;
    }
    return true;
}

int main()
{
    ll num; // 180181
    cout<<"Enter a number: ";
    cin>>num;

    int test;
    cout<< "Enter number of Test: ";
    cin>>test;

    if(IsPrime(num, test))
        cout<<"May be Prime\n";
    else
        cout<<"Definitely not prime\n";
    return 0;
}



