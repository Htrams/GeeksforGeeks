//same knapsack.py solution in c++
#include<bits/stdc++.h>
using namespace std;
#define ll long long

ll noOfItems,maximumWeight;
ll values[1001]={0},weights[1001]={0};

void printhello() {
    cout<<"hello";
}

void solve() {
    vector<ll> dp[1001][1001];
    for(ll i=-1;i<noOfItems;i++)
    {
        for(ll j=0;j<=maximumWeight;j++)
        {
            if(i==-1) {
                dp[i][j]=0;
                continue;
            }
            else if(j>=weights[i]) {
                dp[i][j] = max(dp[i-1][j-weights[i]]+values[i],
                                dp[i-1][j]
                            );
            }
            else {
                dp[i][j]=dp[i-1][j];
            }
        }
    }
}

int main() {
    ll noOfTestCases,i;
    cin>>noOfTestCases;
    while(noOfTestCases--) {
        cin>>noOfItems>>maximumWeight;
        for(i=0;i<noOfItems;i++) {
            cin>>values[i];
        }
        for(i=0;i<noOfItems;i++) {
            cin>>weights[i];
        }
        printhello();
        solve();
        printhello();
    }
    return 0;
}

