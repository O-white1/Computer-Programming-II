using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Pg435TicketSales {
    public partial class GeneralForm : Form {
        private Form myParent;
        public GeneralForm(Form myParent) {
            InitializeComponent();
            this.myParent = myParent;

        }

        private void label1_Click(object sender, EventArgs e) {
            this.myParent.Show();
            this.Close();
        }
        private void GeneralForm_FormClosing(object sender, FormClosingEventArgs e) {
            this.myParent.Show();
        }
        decimal decTaxRate = 0.06m; // sales tax
        private decimal CalcTax(decimal cost) {
            return cost * decTaxRate;
        }
    }
}
