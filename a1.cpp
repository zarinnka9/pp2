#include <iostream>
#include <climits>
using namespace std;
int main(){
    int n;
    cin>>n;
    int a[n];
    for(int i=0; i<n; i++){
        cin>> a[i];
    }
    int minx = INT_MAX;
    for(int i=0; i<n; i++){
        if(a[i] % 2 == 0){
            minx = min(minx, a[i]);
        }
    }
    int sum=0;
    for(int i=0; i<n; i++){
        if(a[i] % 2 == 1){
            sum += a[i] * a[i];
        }
    }
cout << minx << endl << sum;
return 0;
}