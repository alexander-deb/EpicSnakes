#include "Point.hpp"

class Snake{
    private:
    char _velocity;
    Point* _coordinates;
    char _direction;
    char _color;

    public:
    Snake(){
        _velocity = 0;
        _coordinates = NULL;
        _direction = '0';
        _color = '0';
    }
    ~Snake(){}
    void set_velocity(char velocity) {
        _velocity = velocity;
    }
    void set_coordinates(Point* coordinates) {
        _coordinates = coordinates;
    }
    void set_directory(char directory) {
        _direction = directory;
    }
    void set_color(char color) {
        _color = color;
    }
    char get_velocity() {
        return _velocity;
    }
    Point* get_coordinates() {
        return _coordinates;
    }
    char get_directory() {
        return _direction;
    }
    char get_color() {
        return _color;
    }
    void eat(){}; /*TO DO:
                  1) add velocity/health bouns
                  2) then destroy fruit object 
                  */ 
    void next_step(){};
                  /*TO DO:
                  1) 
                  2) then destroy fruit object 
                  */ 
};