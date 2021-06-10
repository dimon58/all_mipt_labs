#include <iostream>
#include <vector>
#include <list>
#include <utility>
#include <cmath>
#include <iomanip>
#include <tuple>

using namespace std;

struct Person
{
	string name;
	int type;
	bool alive;
};

template< typename T>
void print_vector(vector<T> vec) {
	for (auto elem : vec) cout << elem << endl;
}

int main() {

	int N, n;
	cin >> N >> n;

	bool news = true;
	if (n == 0) news = false;

	vector<Person> people;

	string name;
	int t;

	for (int i = 0; i < N;i++) {
		cin >> name >> t;
		people.push_back({ name, t, true });
	}

	int M;
	cin >> M;

	int pos = 0;
	int alives = N;

	for(int day=0; day<M;day++) {


		if (!people[pos].alive) {
			continue;
			++pos %=N;
		}

		if (people[pos].type == 1 && !news) {
			people[pos].alive = false;
			alives--;
		}

		if (people[pos].type == 0) {
			news = !news;
			if (news) people[pos].type = 1;
		}

		++pos %= N;

		if (alives == 1) break;
	}

	for (auto person : people) {
		if (person.alive) cout<<person.name<<" "<<person.type<<endl;
	}

	return 0;
}