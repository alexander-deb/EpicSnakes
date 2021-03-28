#include "InterfaceBuilder.hpp"
#include "Snake.hpp"

class SnakeBuilder: public Builder{
    private:
    Snake _snake;

    public:
    void reset(){};
    void set_coordinates(){};
    void set_color(){};
    Snake get_result(){};

};