class Singleton{
    private:
    static Singleton* instance;
    Singleton();

    public:
    static Singleton* get_instance(){};
};