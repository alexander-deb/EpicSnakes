#include "InterfaceBuilder.hpp"
#include "Fruit.hpp"

class FruitBuilder: public Builder{
    private:
    Fruit _snake;

    public:
    void reset(){};
    void set_coordinates(){};
    void set_color(){};
    void set_bonuss(){};
    Fruit get_result(){};

};