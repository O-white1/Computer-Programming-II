﻿using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Prog54b_Form {
    public partial class Form1 : Form {
        public Form1() { InitializeComponent(); }

        private void button1_Click(object sender, EventArgs e) {
            int num1 = int.Parse(textBox1.Text);
            int num2 = int.Parse(textBox2.Text);
            int sum = (num1 + num2);
            double avg = (double)sum / 2;
            label1.Text = ("Sum: " + sum + " Average: " + avg);
        }
        private void button2_Click(object sender, EventArgs e) { label3.Text = ""; label2.Text = ""; label1.Text = ""; }
        private void button3_Click(object sender, EventArgs e) { Application.Exit(); }
    }
}