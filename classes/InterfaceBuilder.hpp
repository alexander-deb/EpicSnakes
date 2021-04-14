class Builder{
    public:
    //virtual void reset() = 0;
    //virtual void set_velocity(char velocity) = 0;
    virtual void set_color(char color) = 0;
    virtual void set_bonus(char bonus) = 0;
    //virtual void set_directory(char directory) = 0;
    virtual void set_coordinates(Point* coordinates) = 0;
    //virtual char get_velocity() = 0;
    virtual char get_color() = 0;
    virtual char get_bonus() = 0;
    //virtual char get_directory() = 0;
    virtual Point* get_coordinates() = 0;
};