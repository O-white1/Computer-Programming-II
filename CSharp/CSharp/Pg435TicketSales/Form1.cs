﻿using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Pg435TicketSales {
    public partial class Form1 : Form {

        public Form1() { InitializeComponent(); }
        private void Form1_Load(object sender, EventArgs e) {}
        private void label1_Click(object sender, EventArgs e) {}
        private void button2_Click(object sender, EventArgs e) {
            Form frm = new GeneralForm(this);
            // python: frm = GeneralForm(self)
            frm.Show();
            this.Hide();
        }
        private void button1_Click(object sender, EventArgs e) {
            Form frm = new GeneralForm(this);
            frm.Show();
            this.Hide();
        }
        private void button3_Click(object sender, EventArgs e) { Application.Exit(); }
    }
}
