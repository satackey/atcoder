#include <iostream>
#include <algorithm>
#include <vector>
#include <map>
using namespace std;

class Restaurant {
    public:
        string city;
        int score;
        
        Restaurant(string s, int p) {
            city = s;
            score = p;
        }
};

class City {
    string name;
    vector<Restaurant> restaurants;
    public:
        City(string name) {
            
        }

        void addRest(Restaurant rest) {
            restaurants.push_back(rest);
        }

        void sortRests() {
            sort(restaurants.begin(), restaurants.end(), &compare);
        }

        bool compare(Restaurant a, Restaurant b) {
            return a.score < b.score;
        }
};

int main()
{
    int n;
    cin >> n;

    map<string, City> cities;

    for (int i = 0; i < n; i++) {
        string s;
        int p;
        cin >> s >> p;
        Restaurant rest(s, p);

        if (cities.count(s) == 0) {
            cities[s] = City(s);
        }
        cities[s].addRest(rest);
    }
}
