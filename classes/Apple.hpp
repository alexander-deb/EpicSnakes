#include "Fruit.hpp"
#include<string>
class Apple : public Fruit {
public:
    Apple() {
        _bonus = '0';
        _color = '0';
        _coordinates = { 0 };
    }
    ~Apple() {

    }
    std::string Operation() const override {
        return "Created a Apple!\n";
    }
    void give(Snake snake) {
        return;
    }
};