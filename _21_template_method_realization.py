# Шаблон проектування Template Method ( Шаблонний метод )
"""
Шаблонний метод — це поведінковий патерн проектування, 
який визначає кістяк алгоритму, перекладаючи відповідальність 
за деякі його кроки на підкласи. Патерн дозволяє підкласам 
перевизначати кроки алгоритму, не змінюючи його загальної структури.
"""

from abc import ABCMeta, abstractmethod
from reportlab.pdfgen import canvas


class InsurancePolicy:
    def __init__(self, client, insurance):
        self.client = client
        self.insurance = insurance

    def __str__(self):
        return "Insurance policy:\n\tClient - " + str(self.client) + "\n\tInsurance - " + str(self.insurance)


class PrintTemplate(metaclass=ABCMeta):
    def __init__(self, obj: InsurancePolicy, source_file_name: str):
        self._source = obj
        self._file_source = source_file_name
        self._file = None
        self._data = None

    @abstractmethod
    def _prepare_data(self):
        pass

    @abstractmethod
    def _prepare_output_source(self):
        pass

    @abstractmethod
    def _write(self):
        pass

    @abstractmethod
    def _do_methods(self):
        pass

    @abstractmethod
    def _finish(self):
        pass

    def run_method(self):
        self._prepare_data()
        self._do_methods()
        self._write()
        self._finish()


class PDFPrint(PrintTemplate):
    def __init__(self, obj: InsurancePolicy, source_file_name: str):
        super().__init__(obj, str("files/" + source_file_name + ".pdf"))

    def _prepare_output_source(self):
        self._file = canvas.Canvas(self._file_source)

    def _prepare_data(self):
        self._data = "PDF Version of InsurancePolicy", \
                      "Client: " + str(self._source.client), \
                      "Insurance: " + str(self._source.insurance)

    def _write(self):
        y = 600
        for data in self._data:
            self._file.drawString(150, y, str(data))
            y -= 100

    def _finish(self):
            self._file.save()

    def _do_methods(self):
        self._prepare_output_source()


class TextPrint(PrintTemplate):
    def __init__(self, obj: InsurancePolicy, source_file_name: str):
        super().__init__(obj, str("files/" + source_file_name + ".txt"))

    def _prepare_output_source(self):
        self._file = open(self._file_source, "w")

    def _prepare_data(self):
        self._data = "TextFile Version of InsurancePolicy\n\t" \
                      "Client: " + str(self._source.client) + "\n\t" \
                      "Insurance: " + str(self._source.insurance)

    def _write(self):
        self._file.write(self._data)

    def _finish(self):
        try:
            self._file.close()
        except AttributeError:
            pass

    def _do_methods(self):
        self._prepare_output_source()


if __name__ == '__main__':
    policy = InsurancePolicy(input("Input client name -> "), input("Input insurance policy -> "))
    methods = PDFPrint(policy, "template"), TextPrint(policy, "template")
    for method in methods:
        method.run_method()
