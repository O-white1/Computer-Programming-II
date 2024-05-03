using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace MassAndWeight273
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button2_Click(object sender, EventArgs e)
        {
            double w = 9.8 * double.Parse(textBox1.Text);
            if (w > 1000) { label1.Text = "Too Heavy!  Weight is: " + w; }
            else if (w < 10) { label1.Text = "Too Light!  Weight is: " + w; }
            else { label1.Text = "Weight is:" + w; }

        }

        private void button1_Click(object sender, EventArgs e)
        {
            label1.Text = "";
            textBox1.Text = "";
        }

        private void button3_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }
    }
}
