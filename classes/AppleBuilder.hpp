class AppleBuilder :public Builder {
private:
	Apple _apple;

public:
	AppleBuilder() {
		_apple = Apple();
	}
	void set_bonus(char bonus) {
		_apple.set_bonus(bonus);
	}
	void set_velocity(char velocity) {
		return;
	}
	void set_coordinates(Point* coordinates) {
		Point coord = {coordinates[0]};
		_apple.set_coordinates({coord.x, coord.y});
	}
	void set_color(char color) {
		_apple.set_color(color);
	}
	void set_directory(char directory) {
		return;
	}
	char get_color() { return _apple.get_color(); }
	Point* get_coordinates() { 
		Point coord[2] = { {_apple.get_coordinates().x, _apple.get_coordinates().y}, 0 };
		return coord;
	}
	char get_bonus() { return _apple.get_bonus(); }
	Apple get_result() {
		return _apple;
	}
};