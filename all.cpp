#include <bits/stdc++.h>
using namespace std;

int main() {

    string s;
    string t = "";
    int ans = -1;

    getline(cin, s);

    for(int i = 0; i < s.size(); i++){
        //hfbgfhbg
        if(s[i] == ' ' || s[i] == '.' || s[i] == ',' || s[i] == '!' || s[i] == '?' || s[i] == '#' || (s[i] >= '0' && s[i] <= '9')){
            int q = t.size();
            ans = max(ans, q);
            t = "";
        }
        else {
            t += s[i];
        }
    }

    //ksdfjsdf lsdjflsdkjflksdjf
    int q = t.size();
    ans = max(ans, q);
    cout << ans;

    return 0;
}