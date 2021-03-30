#include "InterfaceBuilder.hpp"
#include "Pineapple.hpp"
class PineAppleBuilder :public Builder {
private:
	PineApple _pineapple;

public:
	PineAppleBuilder() {
		_pineapple = PineApple();
	}
	void set_bonus(char bonus) {
		_pineapple.set_bouns(bonus);
	}
	void set_velocity(char velocity) {
		return;
	}
	void set_coordinates(Point* coordinates) {
		_pineapple.set_coordinates(coordinates);
	}
	void set_color(char color) {
		_pineapple.set_color(color);
	}
	void set_directory(char directory) {
		return;
	}
	char get_velocity() { return; }
	char get_color() { return _pineapple.get_color(); }
	char get_directory() { return; }
	Point* get_coordinates() { return _pineapple.get_coordinates(); }
	char get_bonus() { return _pineapple.get_bonus(); }
	PineApple get_result() {
		return _pineapple;
	}
};