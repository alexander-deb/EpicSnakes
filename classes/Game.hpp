#include <string>

class Game{
    private:
    string _name;
    int _score;
    int _weapon;

    public:
    Game();
    ~Game();
    void shoot();
    void pause();
    void run();
};