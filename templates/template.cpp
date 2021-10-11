#include <bits/stdc++.h>

using namespace std;

#define pb push_back
#define fi first
#define se second
#define DBG 0
#define DEBUG() if(DBG)
#define FOR(i, n) for(i = 0; i < n; i++)
#define FOR1(i, n) for(i = 1; i <= n; i++)

typedef long long int number;
typedef vector<number> vi;
typedef vector<vi> vvi;
typedef pair<number, number> ii;
typedef vector<ii> vii;
typedef vector<vii> vvii;
typedef vector<bool> vb;

vector<string> split (const string &s, char delim) {
	vector<string> result;
	stringstream ss (s);
	string item;

	while (getline (ss, item, delim)) {
		result.push_back (item);
	}

	return result;
}

void print_arr(vector<number> vec) {
	for(auto v : vec) {
		cout << v << " ";
	}
	cout << endl;
}

void read_arr(vector<number> &vec, number n) {
	number x, i;
	FOR(i, n) {
		cin >> x;
		vec.pb(x);
	}
}

int main() {
	ios_base::sync_with_stdio(false);
    cin.tie(NULL);
	return 0;
}