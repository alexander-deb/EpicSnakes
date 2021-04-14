#include<string>
class PineApple: public Fruit {
    public:
    PineApple() {
        _bonus = '0';
        _color = '0';
        _coordinates = { 0,0 };
    }
    std::string Operation() const override {
        return "Created a PineApple!\n";
    }
    void give(Snake snake){};
};