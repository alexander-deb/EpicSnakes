#include "InterfaceBuilder.hpp"
#include "Snake.hpp"

class SnakeBuilder: public Builder{
    private:
    Snake _snake;

    public:
    SnakeBuilder(){
        _snake = Snake();
    }
    //void reset(){
    //    _snake = Snake();
    //}
    void set_bonus(char bonus) {
        return;
    }
    void set_velocity(char velocity) {
        _snake.set_velocity(velocity);
    }
    void set_coordinates(Point* coordinates){
        _snake.set_coordinates(coordinates);
    }
    void set_color(char color){
        _snake.set_color(color);
    }
    void set_directory(char directory) {
        _snake.set_directory(directory);
    }
    char get_velocity() { return _snake.get_velocity(); }
    char get_color() { return _snake.get_color(); }
    char get_directory() { return _snake.get_directory(); }
    Point* get_coordinates() { return _snake.get_coordinates(); }
    char get_bonus() { return '0'; }
    Snake get_result(){
        return _snake;
    }
};