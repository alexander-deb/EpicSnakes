#include "InterfaceBuilder.hpp"
#include "Apple.hpp"
class AppleBuilder :public Builder {
private:
	Apple _apple;

public:
	AppleBuilder() {
		_apple = Apple();
	}
	void set_bonus(char bonus) {
		_apple.set_bouns(bonus);
	}
	void set_velocity(char velocity) {
		return;
	}
	void set_coordinates(Point* coordinates) {
		_apple.set_coordinates(coordinates);
	}
	void set_color(char color) {
		_apple.set_color(color);
	}
	void set_directory(char directory) {
		return;
	}
	char get_velocity() { return; }
	char get_color() { return _apple.get_color(); }
	char get_directory() { return; }
	Point* get_coordinates() { return _apple.get_coordinates(); }
	char get_bonus() { return _apple.get_bonus(); }
	Apple get_result() {
		return _apple;
	}
};