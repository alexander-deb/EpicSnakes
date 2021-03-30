#include "Point.hpp"
#include"Product.hpp"
class Fruit : public Product {
protected:
	char _bonus;
	char _color;
	Point _coordinates;

public:
	Fruit() {
		_bonus = '0';
		_color = '0';
		_coordinates = Point();
	}
	virtual void set_color(char color) {
		_color = color;
	}
	virtual void set_bonus(char bonus) {
		_bonus = bonus;
	}
	virtual void set_coordinates(Point coordinates) {
		_coordinates = coordinates;
	}
	virtual char get_color() {
		return _color;
	}
	virtual char get_bonus() {
		return _bonus;
	}
	virtual Point get_coordinates() {
		return _coordinates;
	}
	virtual void give() = 0;
};