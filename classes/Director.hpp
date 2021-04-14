class Director {
private:
	Builder* _builder;
public:
	void set_builder(Builder* newBuilder) {
		_builder = newBuilder;
	}
	Apple* getApple() {
		Apple* apple = new Apple();

		apple->set_color(_builder->get_color());
		apple->set_coordinates(_builder->get_coordinates()[0]);
		apple->set_bonus(_builder->get_bonus());

		return apple;
	}
	PineApple* getPineApple() {
		PineApple* pineapple = new PineApple();

		pineapple->set_color(_builder->get_color());
		pineapple->set_coordinates(_builder->get_coordinates()[0]);
		pineapple->set_bonus(_builder->get_bonus());

		return pineapple;
	}
	Snake* getSnake() {
		Snake* snake = new Snake();

		snake->set_color(_builder->get_color());
		snake->set_coordinates(_builder->get_coordinates());
		//snake->set_velocity(_builder->get_velocity());
		//snake->set_directory(_builder->get_directory());

		return snake;
	}
};