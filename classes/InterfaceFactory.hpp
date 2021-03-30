#include"Product.hpp"
#include<string>
class Creator {
public:
	virtual ~Creator() {};
	virtual Product* FactoryMethod() const = 0;
	virtual std::string SomeMethod() {
		Product* product = this->FactoryMethod();
		std::string result = "In Creator: \n product was created " + product->Operation();
		delete product;
		return result;
	}
	void Draw() {}; //TO DO: Will draw the productss
};