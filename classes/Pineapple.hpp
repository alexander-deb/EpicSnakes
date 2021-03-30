#include "Product.hpp"
#include "Fruit.hpp"
#include<string>
class PineApple: public Fruit{
    public:
    PineApple() {
        _bonus = '0';
        _color = '0';
        _coordinates = { 0,0 };
    }
    ~PineApple();
    std::string Operation() const override {
        return "Created a PineApple!\n";
    }
    void give(){};
};