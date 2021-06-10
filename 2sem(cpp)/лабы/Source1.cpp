#include<iostream>
#include<cstdint>
#include<vector>

using namespace std;

struct Node {
    int64_t value;
    Node* next;
};

Node* get_last_node(Node* node) {
    while (node->next != NULL) {
        node = node->next;
    }
    return node;
}


void push_back(Node* current_node, int64_t value) {
    Node* tmp = new Node{ value, NULL };
    if (current_node) {
        current_node->next = tmp;
    }
}

Node* create_list(vector<int64_t> values) {
    Node* result = new Node{ values[0], NULL };
    for (size_t i = 1; i < values.size(); ++i) {
        push_back(get_last_node(result), values[i]);
    }
    return result;
}

Node* delete_list(Node* node) {
    while (node != NULL) {
        Node* tmp = node->next;
        delete node;
        node = tmp;
    }
}

vector<int64_t> to_vector(Node* node) {
    vector<int64_t> result;
    while (node != NULL) {
        result.push_back(node->value);
        node = node->next;
    }
    return result;
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

void test1() {
    Node* l1 = create_list({ 2, 4, 6 });
    Node* l2 = create_list({ 1, 3, 5 });
    vector<int64_t> expected = { 1, 2, 3, 4, 5, 6 };
    Node* res = mergeLists(l1, l2);
    if (expected == to_vector(res)) {
        cout << "test 1 ok" << endl;
    }
    else {
        cout << "test 1 failed" << endl;
        cout << "your output: ";
        for (auto it : to_vector(res)) {
            cout << it << " ";
        }
        cout << endl;
        cout << "expected output: ";
        for (auto it : to_vector(res)) {
            cout << it << " ";
        }
        cout << endl;
    }
    delete_list(l1);
    delete_list(l2);
    delete_list(res);
}



int main() {
    test1();
    return 0;
}
