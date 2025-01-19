#include <iostream>
#include <climits>
using namespace std;
int main() {
    int n;
    cin >> n;
    int a[n];
    for(int i=0; i<n; i++){
        cin>>a[i];
    }
    int max = INT_MIN;
    int cnt=0;
    for(int i=0; i<n; i++){
        if(a[i] > max) {
            max = a[i];
            cnt = 1;
        }
        else if (max == a[i]) {
            cnt ++;
        }
    }
    cout<<cnt<<endl;
    return 0;

}