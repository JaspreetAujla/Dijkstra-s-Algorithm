# Dijkstra-algorithm

#include<iostream>
#include<climits>
using namespace std;

int miniDist(int dist[], bool Tset[]) 
{
    int min=INT_MAX,ind;
              
    for(int k=0;k<5;k++) 
    {
        if(Tset[k]==false && dist[k]<=min)      
        {
            min=dist[k];
            ind=k;
        }
    }
    return ind;
}

void Dijkstra(int graph[5][5],int src) 
{
    int dist[5];                              
    bool Tset[5];
    
     
    for(int k = 0; k<5; k++)
    {
        dist[k] = INT_MAX;
        Tset[k] = false;    
    }
    
    dist[src] = 0;              
    
    for(int k = 0; k<5; k++)                           
    {
        int m=miniDist(dist,Tset); 
        Tset[m]=true;
        for(int k = 0; k<5; k++)                  
        {
            
            if(!Tset[k] && graph[m][k] && dist[m]!=INT_MAX && dist[m]+graph[m][k]<dist[k])
                dist[k]=dist[m]+graph[m][k];
        }
    }
    cout<<"Vertex\t\tDistance from source vertex"<<endl;
    for(int k = 0; k<5; k++)                      
    { 
        char str=65+k;
        cout<<str<<"\t\t\t"<<dist[k]<<endl;
    }
}

int main()
{
    int graph[5][5]=
      {
        {0, 1, 2, 2, 1},
        {1, 3, 0, 1, 0},
        {2, 1, 0, 3, 3},
        {1, 4, 2, 1, 2},
        {1, 1, 2, 2, 3}
      };
    Dijkstra(graph,0);
    return 0;                           
}
