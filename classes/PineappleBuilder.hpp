class PineAppleBuilder :public Builder {
private:
	PineApple _pineapple;

public:
	PineAppleBuilder() {
		_pineapple = PineApple();
	}
	void set_bonus(char bonus) {
		_pineapple.set_bonus(bonus);
	}
	void set_velocity(char velocity) {
		return;
	}
	void set_coordinates(Point* coordinates) {
		Point coord = { coordinates[0] };
		_pineapple.set_coordinates({coord.x, coord.y});
	}
	void set_color(char color) {
		_pineapple.set_color(color);
	}
	void set_directory(char directory) {
		return;
	}
	char get_color() { return _pineapple.get_color(); }
	Point* get_coordinates() {
		Point coord[2] = { {_pineapple.get_coordinates().x, _pineapple.get_coordinates().y}, 0 };
		return coord;
	}
	char get_bonus() { return _pineapple.get_bonus(); }
	PineApple get_result() {
		return _pineapple;
	}
};