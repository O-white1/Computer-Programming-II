using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Stringinterview16 {
    class Program {
        static void Main(string[] args) {
            Console.Write("Enter String: ");
            string text = Console.ReadLine();
            Console.Write("Enter a subtring to search for: ");
            string word = Console.ReadLine();
            bool result = searchText(text, word);
        }

        static bool searchText(string text, string search) {
            int tlen = text.Length;
            int slen = search.Length;
            if (slen > tlen) return false;
            for (int lcv = 0; lcv <+ tlen - slen; lcv++)
                if (text.Substring(lcv, slen) == search) return true;
            return false;
        }
    }
}
