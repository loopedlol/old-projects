class Program
{
    public static void Main(string[] args)
    {
        Program rectangle = new Program(5, 10);
        Console.WriteLine(rectangle.calculateArea());
        rectangle.doubleHeight();
        Console.WriteLine(rectangle.calculateArea());
    }

    double height;
    double width;

    public Program(double height, double width)
    {

        this.height = height;
        this.width = width;

    }

    public double calculateArea()
    {

        return height * width;

    }

    public double calculateArea(int a)
    {
        return a * height * width;
    }

    public void doubleHeight()
    {

        height *= 2;

    }
    
}
