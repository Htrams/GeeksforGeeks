//attempted code in c++
#include<bits/stdc++.h>
using namespace std;

#define ll long long

class node
{
public:
    int i;
    int j;
    int value;
    int weight;
    bool completed;
    node(int m,int n,int o)
    {
        i=m;
        j=n;
        value=o;
        completed=false;
        weight=10001;
    }
    node(){}
};

node grid[100][100];
int gridSize;

struct nodeComparisions
{
    bool operator()(const node* p1,const node* p2) {
        return (*p1).value > (*p2).value;
    }
};


priority_queue< node*,vector<node*>, nodeComparisions> pq;

//void updatePQ (int i,int j,int newWeight)
//{
//    grid[i][j].
//}

void dijkstra(int i,int j) {
    grid[i][j].weight=0;

}

void solve()
{
    int i,j,temp;
    cin>>gridSize;
    for(i=0;i<gridSize;i++) {
        for(j=0;j<gridSize;j++) {
            cin>>temp;
            grid[i][j]=node(i,j,temp);
            pq.push(&grid[i][j]);
            //cout<< pq.top()->value;
            //pq.pop();
        }
    }
    cout<<pq.top()->value<<pq.top()->weight;
    grid[0][0].value=1;
    pq.pop();
    cout<<pq.top()->value<<pq.top()->weight;
    dijkstra(0,0);
}

int main()
{
    int t;
    cin>>t;
    while(t--)
    {
        solve();
    }
}
