#include "Point.hpp"

class Snake{
    private:
    char _velocity;
    Point* _coordinates;
    char _direction;
    char color;

    public:
    Snake();
    ~Snake();
    void eat(){};
    void next_step(){};

};