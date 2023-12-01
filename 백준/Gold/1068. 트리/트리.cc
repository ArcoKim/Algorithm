#include <iostream>
#include <algorithm>
using namespace std;

int n, arr[50], result;

void recursive(int era, bool nexts=false) {
    int cnt = 0;
    arr[era] = -2;

    for(int i = 0; i < n; i++) {
        if(arr[i] == era) {
            recursive(i, nexts);
            cnt++;
        }
    }

    if(nexts && cnt == 0) {
        result++;
    }
}

int main() {
    int era;
    cin >> n;

    for(int i = 0; i < n; i++) {
        cin >> arr[i];
    }
    cin >> era;

    recursive(era);

    if(*max_element(arr, arr + n) == -2) {
        cout << 0 << endl;
    } else {
        int* root = find(arr, arr + n, -1);
        recursive(*root, true);
        cout << result << endl;
    }
    return 0;
}
