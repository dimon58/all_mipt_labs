#include <iostream>
#include <string>

using std::cin;
using std::cout;
using std::endl;

struct Node {
	int data = 0;
	Node* next = NULL;
};

class LinkedList {
public:

	void push_back(int val) {
		for (Node* i = root; i != NULL; i = i->next) {
			if (i->next == NULL) i->next = new Node({ val, NULL });
		}
	}

	void push_front(int val) {
		root = new Node({ val, root });
	}

	int PopFirst() {
		auto* first_node = root;
		root = first_node->next;
		return first_node->data;
	}

	void PrintAll() {
		/*Node* node = root;
		while (true)
		{
			if (node != NULL) {
				cout << node->data << " ";
				node = node->next;
			}
			else break;
		}*/
		for (Node* i = root; i != NULL; i = i->next) {
			cout << i->data << " ";
		}
	}

	void Clear() {
		while (root != NULL) remove_first();
	}

private:
	Node* root = NULL;

	void remove_first() {
		Node* next = root->next;
		delete root;
		root = next;
	}
};

int main() {
	LinkedList lst;
	lst.push_front(1);
	lst.push_front(2);
	lst.push_front(3);
	lst.push_front(4);
	lst.push_front(5);
	lst.push_front(6);
	lst.PrintAll();
}
