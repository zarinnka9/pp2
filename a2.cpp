#include <bits/stdc++.h>
using namespace std;

int main() {

    int n, a[1005];
    int mn = INT_MAX, sum = 0;

    cin >> n;

    for(int i = 1; i <= n; i++){
        cin >> a[i];
        if(a[i] % 2 == 0) mn = min(mn, a[i]);
        if(a[i] % 2 == 1) {
            sum += a[i] * a[i];
        }
    }
    if(mn == INT_MAX){
        cout << -1 << endl;
    }
    else cout << mn << endl;
    cout << sum;

    return 0;
}