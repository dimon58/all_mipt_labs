#include <iostream>
#include <string>
#include <sstream>


using std::cin;
using std::cout;
using std::endl;

int nodes = 0;

struct Node {
	int value = 0;
	Node* next = NULL;
	~Node() {
		nodes--;
	}
};

Node* make_node(int val, Node* next) {
	Node* x = new Node;
	x->value = val;
	x->next = next;
	nodes++;
	return x;
}



class LinkedList {
public:

	void push_back(int val) {
		if (root == NULL) {
			root = make_node(val, NULL);
			length++;
			return;
		}
		for (Node* i = root; i != NULL; i = i->next) {
			if (i->next == NULL) {
				//i->next = new Node{ val, NULL };
				i->next = make_node(val, NULL);
				length++;
				return;
			}
		}
	}

	void push_front(int val) {
		root = make_node(val, root);
		length++;
	}

	void add(int value, int pos) {
		if (pos == 0) {
			root = make_node(value, root);
			length++;
			return;
		}
		Node* node = root;
		for (int i = 0; i + 1 < pos;i++) node = node->next;
		node->next = make_node(value, node->next);
		length++;
	}

	int PopFirst() {
		int first_node = root->value;
		Node* next = root->next;
		delete root;
		root = next;
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
		length--;
		root = next;
	}
};

int main() {
	std::string test =
		"13\n"
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
	s.str(test);
	std::istream& inp = s;

	int n, i;
	inp >> n;
	std::string querry;
	LinkedList lst;
	for (int j = 0; j < n;j++) {
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
			cout << lst.PopFirst()<<endl;
		}
		else if (querry == "p") {
			lst.PrintAll();
			cout << std::endl;
		}
	}
	lst.Clear();
	return 0;
}
