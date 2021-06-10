#pragma once


struct subvector {
	int* mas;
	unsigned int top;
	unsigned int capacity;
};

void Print(subvector* qv);

bool init(subvector* qv); //������������� ������� �����������

bool push_back(subvector* qv, int d); //���������� �������� � ����� �����������
//� ���������� �������������� ������ ��� �������������

int pop_back(subvector* qv); //�������� �������� � ����� �����������

bool resize(subvector* qv, unsigned int new_capacity); //��������� ������� �����������

void shrink_to_fit(subvector* qv); //�������� �������������� ������

void clear(subvector* qv); //�������� ���������� �����������, ���������� �����
//��� ���� �� ��������

void destructor(subvector* qv); //�������� ��� ������������ ������, ����������������
//���������� ��� ������

bool init_from_file(subvector* qv, char* filename); //���������������� ���������� �� �����
