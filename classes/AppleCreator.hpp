#include "InterfaceFactory.hpp"
class AppleCreator : public Creator {
public:
	Product* FactoryMethod() const override {
		return Apple();
	}
};