#include <iostream>
#include <string>
#include <sstream>
#include <map>

using namespace std;

struct Bracket {
	char smb;
	string map_smb;
	int type; // 1 если открывающая, -1 иначе
	string other;
};

bool operator<(const Bracket& lhs, const Bracket& rhs) {
	return lhs.map_smb < rhs.map_smb;
}

bool IsCoorect(string& seq, const map<char, Bracket>& char_to_brack) {
	int pos = 0, end;
	char ch;
	string sub;
	while (true) {
		ch = seq[pos];
		Bracket obrack = char_to_brack.at(ch);
		if (obrack.type == -1) return false;
		end = seq.find(obrack.other, pos);
		sub = seq.substr(pos, end - pos);
		if (!IsCoorect(sub, char_to_brack)) return false;
		else if (end = seq.size()) return true;
		else pos = end + 1;
	}
	return true;
}

int main() {
	//string seq="()())(((()))";
	////getline(cin, seq);
	//int o = 0, c = 0;
	//bool is_correct = true;
	//for (char brac : seq) {
	//	if (brac == '(') o++;
	//	if (brac == ')') c++;

	//	if (c > o) {
	//		is_correct = false;
	//		break;
	//	}
	//}

	//if (c != o) is_correct = false;

	//if (is_correct) cout << "YES";
	//else cout << "NO";
	//return 0;

	int N;
	cin >> N;

	char obrack, cbrack;

	map<string, int> brackets;
	map<char, Bracket> char_to_brack;

	stringstream format;


	for (int i = 0; i < N; i++) {
		cin >> obrack >> cbrack;
		format << obrack << cbrack;
		cout << format.str();
		string map_smb = string(1, obrack) + string(1, cbrack);

		Bracket oBracket, cBracket;

		oBracket.smb = obrack;
		oBracket.type = 1;
		oBracket.map_smb = format.str();
		oBracket.other = cbrack;

		cBracket.smb = cbrack;
		cBracket.type = -1;
		cBracket.map_smb = format.str();
		cBracket.other = obrack;

		format.str("");
	}


	string seq;
	cin >> seq;
	bool is_correct = IsCoorect(seq, char_to_brack);

	if (is_correct) cout << "YES";
	else cout << "NO";

	return 0;
}
