#include <iostream>
#include <string>
#include <cstdint>
#include <sstream>


using std::cin;
using std::cout;
using std::endl;

struct Node {
	int64_t value = 0;
	Node* next = NULL;
};


void push_back(Node* node, int64_t value) {
	node->next = new Node({ value, NULL });
}

Node* mergeLists(Node* first, Node* second) {
	Node new_node;

	if (first == NULL) return second;
	if (second == NULL) return first;

	if (first->value > second->value) {
		new_node = *first;
		mergeLists(first->next, second);
	}
	else {
		new_node = *second;
		mergeLists(first, second->next);
	}

	return new Node(new_node);

}


class LinkedList {
public:

	void push_back(int val) {
		if (root == NULL) {
			root = new Node({ val, NULL });
			length++;
			return;
		}
		for (Node* i = root; i != NULL; i = i->next) {
			if (i->next == NULL) {
				i->next = new Node({ val, NULL });
				length++;
				return;
			}
		}
	}

	void push_front(int val) {
		root = new Node({ val, root });
		length++;
	}

	void add(int value, int pos) {
		if (pos == 0) {
			root = new Node({ value, root });
			length++;
			return;
		}
		Node* node = root;
		for (int i = 0; i + 1 < pos;i++) node = node->next;
		node->next = new Node({ value, node->next });
		length++;
	}

	int PopFirst() {
		int first_node = root->value;
		root = root->next;
		length--;
		return first_node;
	}

	void PrintAll() {
		for (Node* i = root; i != NULL; i = i->next) {
			cout << i->value << " ";
		}
	}

	void Clear() {
		while (root != NULL) remove_first();
	}

	int getLength() {
		return length;
	}

private:
	Node* root = NULL;
	int length = 0;

	void remove_first() {
		Node* next = root->next;
		delete root;
		root = next;
	}
};

int main() {


	/*std::string test =
		"14\n"
		"+ 1\n"
		"+ 2\n"
		"+ 3\n"
		"+ 4\n"
		"+ 5\n"
		"* 7\n"
		"p\n"
		"-\n"
		"-\n"
		"-\n"
		"-\n"
		"-\n";
	std::istringstream s;
	s.str(test);*/
	std::istream& inp = cin;

	int n, i;
	inp >> n;
	std::string querry;
	LinkedList lst;
	for (int i = 0; i < n+1;i++) {
		inp >> querry;
		if (querry == "+") {
			inp >> i;
			lst.push_back(i);
		}
		else if (querry == "*") {

			inp >> i;
			lst.add(i, (lst.getLength() + 1) / 2);

		}
		else if (querry == "-") {
			cout << lst.PopFirst();
		}
		else if (querry == "p") {
			lst.PrintAll();
			cout << std::endl;
		}
	}
	return 0;
}
