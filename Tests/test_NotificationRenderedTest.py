from Pages.Notification_Rendered_Page import NotificationPage
from Tests.test_base import BaseTest
import time


class Test_NotificationPageRendered(BaseTest):

    def test_NotificationPageRendered(self):
        self.notificationPage = NotificationPage(self.driver)

        self.driver.get("http://the-internet.herokuapp.com/notification_message_rendered")

        self.notificationPage.loopedScript()
