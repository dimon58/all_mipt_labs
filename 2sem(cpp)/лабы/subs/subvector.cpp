#include <iostream>
using namespace std;

struct subvector {
	int* mas = NULL;
	unsigned int top = 0;
	unsigned int capacity = 0;
};

bool init(subvector* qv) {
	qv->mas = (int*)malloc(sizeof(int));
	qv->top = 0;
	qv->capacity = 1;

	return true;
} //инициализация пустого недовектора


bool push_back(subvector* qv, int d) {
	if (qv->capacity == 0) init(qv);
	if (qv->top >= qv->capacity) {
		qv->capacity *= 2;
		qv->mas = (int*)realloc(qv->mas, qv->capacity * sizeof(int));
	}
	qv->mas[qv->top] = d;
	qv->top++;
	return true;
} //добавление элемента в конец недовектора
//с выделением дополнительной памяти при необходимости


int pop_back(subvector* qv) {
	if (qv->top == 0) return 0;
	
	qv->top--;
	int ret = qv->mas[qv->top];

	return ret;
} //удаление элемента с конца недовектора


bool resize(subvector* qv, unsigned int new_capacity) {
	qv->mas = (int*)realloc(qv->mas, new_capacity * sizeof(int));
	qv->capacity = new_capacity;

	return true;
} //увеличить емкость недовектора


void shrink_to_fit(subvector* qv) {
	qv->mas = (int*)realloc(qv->mas, qv->top * sizeof(int));
	qv->capacity = qv->top;
} //очистить неиспользуемую память


void clear(subvector* qv) {
	qv->top = 0;
} //очистить содержимое недовектора, занимаемое место
//при этом не меняется


void destructor(subvector* qv) {
	free(qv->mas);
	qv->top = 0;
	qv->capacity = 0;
} //очистить всю используемую память, инициализировать недовектор как пустой