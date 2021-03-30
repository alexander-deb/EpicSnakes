#include "InterfaceFactory.hpp"
class PineappleCreator : public Creator {
public:
	Product* FactoryMethod() const override {
		return new PineappleCreator();
	}
};