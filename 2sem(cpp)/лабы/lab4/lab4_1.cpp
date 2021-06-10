#include <iostream>
#include <string>
#include <cstdint>


using std::cin;
using std::cout;
using std::endl;

struct Node {
	int64_t value = 0;
	Node* next = NULL;
};


void push_back(Node* node, int64_t value) {
	node->next = new Node({value, NULL});
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

int main() {

	return 0;
}
