#include <iostream>
#include <vector>
#include <utility>


void PrintCoords(const std::vector<std::vector<int>>& vec, const int n, const int m) {
	for (int y = 0;y < n;y++) {
		for (int x = 0;x < m;x++) std::cout << vec[x + 1][y + 1]<<" ";
		std::cout << std::endl;
	};
}

void AddBomb(std::vector<std::vector<int>>& vec, int x, int y) {
	std::vector<std::pair<int, int>> coords = {
		{-1,-1},
		{-1,0},
		{-1,1},
		{0,-1},
		{0,0},
		{0,1},
		{1,-1},
		{1,0},
		{1,1},
	};

	for (auto p : coords) {
		int& cell = vec[x + p.first][y + p.second];
		if (cell != -1) ++cell;
	};

	vec[x][y] = -1;

}

int main() {
	int n, m, k, x, y;
	std::cin >> n >> m >> k;

	std::vector<std::vector<int>> coords;

	for (int i = 0; i < m + 2;i++) coords.push_back(std::vector<int>(n + 2, 0));

	for (int i = 0;i < k;i++) {
		std::cin >> x >> y;
		AddBomb(coords, y, x);
	}

	PrintCoords(coords, n, m);

	return 0;
}