class Solution {
public:
    int carFleet(int target, vector<int>& position, vector<int>& speed) {
        int n = position.size();
        vector<pair<int, int>> cars;

        for (int i = 0; i < n; i++) {
            cars.push_back({position[i], speed[i]});
        }

        sort(cars.rbegin(), cars.rend());

        vector<double> stack;

        for (const auto& car : cars) {
            int p = car.first;
            int s = car.second;

            double time = static_cast<double>(target - p) / s;

            if (!stack.empty() && time <= stack.back()) {
                continue;
            }

            stack.push_back(time);
        }

        return stack.size();
    }
};
