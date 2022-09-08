import kivy
#kivy.require('1.9.1')
from kivy.app import App
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import StringProperty
from test2 import func
import datetime
# from android.permissions import request_permissions, Permission

# request_permissions([
#     Permission.CAMERA,
#     Permission.WRITE_EXTERNAL_STORAGE,
#     Permission.READ_EXTERNAL_STORAGE
# ])

# Window.fullscreen = True
Window.size = (500,900)
class FirstWindow(Screen):
    pass
class SecondWindow(Screen):
    pass
class GalleryWindow(Screen):
    pass
class CameraWindow(Screen):
    pass
    path = StringProperty()
    def capture(self):
        time = datetime.datetime.now() - datetime.timedelta(seconds=0)
        timestr = time.strftime("%Y-%m-%d %H.%M.%S")
        self.path = str(timestr)+".jpg"
        print("captured")
    def change_cam(self,instance):
        camera = instance.parent.parent.ids.xcamera
        if camera.index == 0:
            camera.index = int(camera.index)+1
        elif camera.index == 1:
            camera.index = int(camera.index)-1
        else:
            camera.index = camera.index
# class CameraWindow(Screen):
#     pass
#     path = StringProperty()
#     def capture(self):
#         '''
#         Function to capture the images and give them the names
#         according to their captured time and date.
#         '''
#         camera = self.ids['camera']
#         timestr = time.strftime("%Y-%m-%d %H.%M.%S")
#         self.path = str(timestr)+".jpg"
#         camera.export_to_png("{}.jpg".format(timestr))
#         print("Captured")
class ConfirmWindow(Screen):
    pass
class ResultWindow(Screen):
    pass
class WindowManager(ScreenManager):
    image_source = StringProperty()
    def selected(self,filename):
        try:
            if len(filename[0])==1:
                self.image_source = filename
            else:
                self.image_source = filename[0]
        except:
            pass
    result = StringProperty()
    def spliting(self,image):
        try:
            self.result = func(image)
            print("Converted")
        except:
            pass
class DemoApp(App):
    pass

if __name__ == '__main__':
    DemoApp().run()