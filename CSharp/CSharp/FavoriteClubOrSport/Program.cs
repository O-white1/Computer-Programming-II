using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace FavoriteClubOrSport
{
    class Program {
        static void Main(string[] args) {
            Console.Write("Favrite Sport or Club: ");
            string ClubOrSport = Convert.ToString(Console.ReadLine());
            Console.WriteLine("Your favorite Sport/Club is " + ClubOrSport + "?  What a loser!");
        }
    }
}
