using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace LP4_2 {
    class Program {
        static void Main(string[] args) {
            Console.Write("Enter Weight: ");  int weight = int.Parse(Console.ReadLine());
            Console.Write("Enter Length: ");  int length = int.Parse(Console.ReadLine());
            Console.Write("Enter Height: ");  int height = int.Parse(Console.ReadLine());
            Console.Write("Enter width: ");  int  width = int.Parse(Console.ReadLine());
            int volume = length * weight * height;

            if (weight > 27 && volume > 100000) Console.WriteLine("Package is too heavy and too large!");
            else if (weight > 27)               Console.WriteLine("Pacakge is too heavy!");
            else if (volume > 100000)           Console.WriteLine("Pacakge is too large!");
            else                                Console.WriteLine("You're good to go!");
            Console.ReadKey();
        }
    }
}
