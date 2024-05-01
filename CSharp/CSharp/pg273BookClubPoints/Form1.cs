using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace pg273BookClubPoints {
    public partial class Form1 : Form {
        public Form1()
        {InitializeComponent(); }
        private void button2_Click(object sender, EventArgs e) {
            int books = int.Parse(textBox1.Text);
            int points = 0;
            if (books > 0 && books < 4) points = books;
            else if (books > 4) points = 4;
            else label2.Text = "Invalid Number of Books!";
            label2.Text = ("You Earned " + points + " Points");
        }
        private void button1_Click(object sender, EventArgs e) { label2.Text = " "; }
        private void button3_Click(object sender, EventArgs e) { Application.Exit(); }
    }
}
