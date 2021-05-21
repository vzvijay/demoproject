from Pages.Table_Page import TablesPage
from Tests.test_base import BaseTest


class Test_TableSortTest(BaseTest):

    def test_table_sort_by_due_column(self):
        self.tablePage = TablesPage(self.driver)

        """open tables page"""
        self.driver.get("http://the-internet.herokuapp.com/tables")

        """click on due header """
        self.tablePage.clickOnDueTheadColumn()

        """fetch all the due columns text"""
        elements = self.tablePage.getAllDueElement()
        print("here")

        """converted into list"""
        result = list(map(lambda x: float(x.text.replace('$', '')), elements))
        print(result)

        """sorted the list """
        output = sorted(result, key=lambda x: float(x))
        print(output)
        """compare both the list """
        assert result == output
