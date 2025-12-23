from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.graphics import Color, Line, Rectangle
from kivy.properties import ListProperty, NumericProperty, StringProperty


class DrawingArea(Widget):
    # Çizgi rengi ve kalınlığı
    line_color = ListProperty([0, 0, 0, 1])
    line_width = NumericProperty(3)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Arka planı beyaz yapmak için
        with self.canvas.before:
            Color(1, 1, 1, 1)
            self.bg_rect = Rectangle(pos=self.pos, size=self.size)
        self.bind(pos=self._update_bg, size=self._update_bg)

    # Arka plan boyut ayarı
    def _update_bg(self, *args):
        self.bg_rect.pos = self.pos
        self.bg_rect.size = self.size

    # Çizime başlama
    def on_touch_down(self, touch):
        if not self.collide_point(*touch.pos):
            return False
        with self.canvas:
            Color(*self.line_color)
            touch.ud["line"] = Line(points=[touch.x, touch.y],
                                    width=self.line_width)
        return True

    # Parmağı hareket ettirdikçe çizgi çizme
    def on_touch_move(self, touch):
        if "line" in touch.ud:
            touch.ud["line"].points += [touch.x, touch.y]

    # Temizle butonu için fonksiyon
    def clear_canvas(self):
        self.canvas.clear()
        # Arka planı tekrar ekle
        with self.canvas.before:
            Color(1, 1, 1, 1)
            self.bg_rect = Rectangle(pos=self.pos, size=self.size)
        self.bind(pos=self._update_bg, size=self._update_bg)


class MainLayout(BoxLayout):
    current_color = ListProperty([0, 0, 0, 1])  # Varsayılan siyah
    brush_width = NumericProperty(3)
    info_text = StringProperty("Parmağınızla veya fareyle alanda çizim yapabilirsiniz.")

    # Renk seçme fonksiyonu
    def set_color(self, r, g, b, a=1):
        self.current_color = [r, g, b, a]

    # Tuvali temizleme fonksiyonu
    def clear_canvas(self):
        self.ids.cizim_alani.clear_canvas()

    # Kalınlık slider'ı
    def update_brush_width(self, value):
        self.brush_width = int(value)


class DokunmatikCizimApp(App):
    def build(self):
        return MainLayout()


if __name__ == "__main__":
    DokunmatikCizimApp().run()
