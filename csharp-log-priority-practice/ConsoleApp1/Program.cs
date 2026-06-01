public class Program {

    public static void Main(string[] args) {

        Queue<string> queue = new Queue<string>();

        queue.Insert("string1");
        queue.Insert("string2");
        Console.WriteLine(queue.Count());
        Console.WriteLine(queue.Pop());

        List<Dictionary<string, string>> list = new List<Dictionary<string, string>>();

        while (true) {
            Console.Write("Would you like to add an entry to our log? : ");
            string input = Console.ReadLine() ?? "";

            if (input.ToLower().Equals("yes")) {
                Console.Write("What is the name of the category? : ");
                string category = Console.ReadLine() ?? "";
                Console.Write("What is the description? : ");
                string description = Console.ReadLine() ?? "";
                Console.Write("What priority number? : ");
                string priority = Console.ReadLine() ?? "0";
                list.Add(new Dictionary<string, string>(){
                    {"Category", category},
                    {"Description", description},
                    {"Priority", priority},
                });
            } else {
                list.Sort((e1, e2) => Convert.ToInt32(e1["Priority"]).CompareTo(Convert.ToInt32(e2["Priority"])));
                foreach(Dictionary<string, string> entry in list) {
                    Console.WriteLine("The category is " + entry["Category"]);
                    Console.WriteLine("The description is " + entry["Description"]);
                    Console.WriteLine("The priority is " + entry["Priority"]);
                    Console.WriteLine("----------------------------------");
                }
                break;
            }
        }

    }

}
