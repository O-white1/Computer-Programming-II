using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace p266LargeSmall {
    public partial class Form1 : Form {
        public Form1() { InitializeComponent(); }

        private void button1_Click(object sender, EventArgs e) {
            int num1 = int.Parse(textBox1.Text);
            int num2 = int.Parse(textBox2.Text);
            string lrg = "";
            if (num1 > num2) lrg = "num1";
            else lrg = "num2";
            label3.Text = "The Larger one is " + lrg;
        }

        private void button2_Click(object sender, EventArgs e) {
            textBox2.Text = "";
            textBox1.Text = "";
            label3.Text = "";
        }

        private void button3_Click(object sender, EventArgs e) { Application.Exit(); }
    }
}
