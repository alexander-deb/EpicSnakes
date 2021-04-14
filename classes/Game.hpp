#include "Point.hpp"
#include "SnakeBuilder.hpp"
#include "Apple.hpp"
#include "Pineapple.hpp"
#include "Director.hpp"
#include "PineAppleBuilder.hpp"
#include "AppleBuilder.hpp"
class Game{
    private:
    std::string _name;
    int _score;
    int _weapon;
    Point* _field;
    Snake* _snakes;
    Apple* _apples;
    PineApple* _pineapples;
    //AppleCreator _applecreator;
    //PineappleCreator _pineapplecreator;
    SnakeBuilder _snakebuilder;
    AppleBuilder _applebuilder;
    PineAppleBuilder _pineapplebuilder;

    public:
    Game(){
        _name = "Bob";
        _score = 0;
        _weapon = 0;
        _snakes = new Snake();
        _apples = new Apple();
        _pineapples = new PineApple();
        _snakebuilder = SnakeBuilder();
        _applebuilder = AppleBuilder();
        _pineapplebuilder = PineAppleBuilder();
        _field = { 0 };
    }
    void shoot() {};
    void pause() {};
    void run() {
        Director director;
        director.set_builder(&_snakebuilder);
        _snakes = director.getSnake();
        director.set_builder(&_applebuilder);
        _apples = director.getApple();
        director.set_builder(&_pineapplebuilder);
        _pineapples = director.getPineApple();
    }
};