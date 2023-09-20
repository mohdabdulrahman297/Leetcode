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

/*
int main() {
    Solution solution;

    // Define the input values
    int target = 12;  // Target position
    vector<int> position = {10, 8, 0, 5, 3};  // List of positions of cars
    vector<int> speed = {2, 4, 1, 1, 3};  // List of speeds of cars

    // Call the carFleet function with the provided input
    int result = solution.carFleet(target, position, speed);

    // Print the result
    cout << "Number of car fleets: " << result << endl;

    return 0;
}
*/
