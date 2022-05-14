#include<bits/stdc++.h>
using namespace std;
void swap(int *a, int *b){
    int temp = *a;
    *a = *b;
    *b = temp; 
}
void selectionsort(vector<int> &v,int n){
    int i, j, min; 
    for (i = 0; i < n-1; i++) 
    {  
        min = i; 
        for (j = i+1; j < n; j++) 
        if (v[j] < v[min]) 
            min = j; 
        swap(&v[min], &v[i]); 
    } 
}
int main(){
    int n;
    cout<<"Enter Number of Elements in array : ";
    cin>>n;
    vector<int> v;
    for(int i=0;i<n;i++){
        int x;
        cout<<"Enter an element : ";
        cin>>x;
        v.push_back(x);
    }
    cout<<"-------------------------------------------------------------------------------"<<endl;
    cout<<"Elements Before sorting : "<<endl;
    cout<<"-------------------------------------------------------------------------------"<<endl;
    for(auto i:v){
        cout<<i<<" ";
    }
    cout<<endl;
    selectionsort(v,n);
    cout<<"-------------------------------------------------------------------------------"<<endl;
    cout<<"Elements After sorting : "<<endl;
    cout<<"-------------------------------------------------------------------------------"<<endl;
    for(auto i:v){
        cout<<i<<" ";
    }
    cout<<endl;
    cout<<"------------------------------------------------------------------------------"<<endl;
    return 0;
}