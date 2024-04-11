using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Prog54cConsole {
    class Program {
        static void Main(string[] args) {
            Console.Write("Enter Radius: ");

            double rad = double.Parse(Console.ReadLine());
            double area = (rad * rad) * 3.14159;
            double circ = 2 * rad * 3.14159;

            Console.WriteLine("Area: " + area);
            Console.WriteLine("Circumpherence: " + circ);
            Console.ReadKey();

        }
    }
}
