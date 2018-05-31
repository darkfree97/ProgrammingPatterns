import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtPrintSupport import QPrinter, QPrintDialog

from _4_builder_realisation import InsurancePolicy, HealthInsurancePolicyBuilder, Clerk

"""
class InsurancePolicyAdapter(InsurancePolicy, QTextDocument):
    def __init__(self):
        super().__init__()
        self.setPlainText(InsurancePolicy.__str__(self))
# """


class InsurancePolicyAdapter(QTextDocument):
    def __init__(self, policy: InsurancePolicy, *args):
        super().__init__(*args)
        self.insurance_policy = policy
        self.setPlainText(InsurancePolicy.__str__(self.insurance_policy))


class Printer:
    def __init__(self):
        self.printer = QPrinter(QPrinter.PrinterResolution)
        self.printer.setOutputFormat(QPrinter.PdfFormat)
        self.printer.setPaperSize(QPrinter.A4)

    def print(self, document: QTextDocument):
        dialog = QPrintDialog(self.printer, None)
        if dialog.exec() == QDialog.Rejected:
            pass
        else:
            InsurancePolicyAdapter.print(document, self.printer)


def window():
    app = QApplication(sys.argv)
    w = QPushButton("Роздрукувати страховий поліс")
    w.setMinimumSize(300, 200)
    w.clicked.connect(foo)
    w.show()
    sys.exit(app.exec_())


def foo():
    clerk = Clerk()
    builder = HealthInsurancePolicyBuilder(InsurancePolicy)
    # builder = HealthInsurancePolicyBuilder(InsurancePolicyAdapter)
    clerk.set_insurance_policy_builder(builder)
    policy = clerk.create_insurance_policy()
    InsurancePolicy.set_client(policy, "Mr.Getsby")
    printer = Printer()
    printer.print(InsurancePolicyAdapter(policy))
    # printer.print(policy)


if __name__ == '__main__':
    window()


