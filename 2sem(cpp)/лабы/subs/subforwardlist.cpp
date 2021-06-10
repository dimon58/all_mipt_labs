struct subforwardlist {
    int data;
    subforwardlist* next = nullptr;
};


bool init(subforwardlist** sfl) {
    *sfl = nullptr;
    return true;
} //инициализация пустого недосписка


bool push_back(subforwardlist** sfl, int d) {
    subforwardlist* old_list = *sfl;
    subforwardlist* new_list = new subforwardlist;
    new_list->data = d;
    if (*sfl == nullptr) {
        *sfl = new_list;
        return true;
    }
    while (old_list->next != nullptr) {
        old_list = old_list->next;
    }
    old_list->next = new_list;
    return true;
} //добавление элемента в конец недосписка


int pop_back(subforwardlist** sfl) {
    subforwardlist* a = *sfl;
    subforwardlist* b;
    if (a == nullptr)  return 0;

    if (a->next == nullptr) {
        *sfl = nullptr;
        int res = a->data;
        delete a;
        return res;
    }

    while (a->next != nullptr) {
        b = a;
        a = a->next;
    }

    int res = a->data;
    delete a;
    b->next = nullptr;
    return res;
} //удаление элемента с конца недосписка


bool push_forward(subforwardlist** sfl, int d) {
    subforwardlist* a = new subforwardlist;
    a->data = d;
    if (*sfl == nullptr) {
        *sfl = a;
        return true;
    }
    a->next = *sfl;
    *sfl = a;
    return true;
} //добавление элемента в начало недосписка


int pop_forward(subforwardlist** sfl) {
    if (*sfl == nullptr)  return 0;

    int res = (*sfl)->data;
    subforwardlist* del = *sfl;
    *sfl = (*sfl)->next;

    delete del;
    return res;
} //удаление элемента из начала недосписка


bool push_where(subforwardlist** sfl, unsigned int where, int d) {
    if (where == 0) return push_forward(sfl, d);
    subforwardlist* prev, * cur, * next;

    prev = *sfl;
    next = prev->next;

    for (int i = 1; i < where; i++) {
        prev = next;
        next = next->next;
    }

    cur = new subforwardlist;
    cur->data = d;
    cur->next = next;
    prev->next = cur;

    return true;
} //добавление элемента с порядковым номером where


bool erase_where(subforwardlist** sfl, unsigned int where) {
    if (where == 0) {
        subforwardlist* del = *sfl;
        *sfl = (*sfl)->next;
        delete del;
        return true;
    }

    subforwardlist* prev, * cur, * next;
    cur = *sfl;

    for (int i = 0; i < where; i++) {
        prev = cur;
        cur = cur->next;
        next = cur->next;
    }

    prev->next = next;
    delete cur;

    return true;
} //удаление элемента с порядковым номером where


unsigned int size(subforwardlist** sfl) {
    if (*sfl == nullptr) return 0;
    subforwardlist* a = *sfl;

    unsigned int i = 1;

    while (a->next != nullptr) {
        a = a->next;
        i++;
    }

    return i;
} //определить размер недосписка


void clear(subforwardlist** sfl) {
    subforwardlist* a = *sfl;
    subforwardlist* b;

    if (a == nullptr) return;

    while (a->next != nullptr) {
        b = a;
        a = a->next;
        delete b;
    }

    delete a;
    *sfl = nullptr;
} //очистить содержимое недосписка