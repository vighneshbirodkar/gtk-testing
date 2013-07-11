import pygtk
pygtk.require('2.0')
import gtk
import cairo

class Base:
    def __init__(self):
        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        self.window.show()
        self.img = gtk.Image()
        self.ims1  = cairo.ImageSurface(cairo.FORMAT_RGB24,512,512)
        self.ims2  = cairo.ImageSurface(cairo.FORMAT_RGB24,512,512)

        
        
        
        self.c1 = cairo.Context(self.ims1)
        self.c2 = cairo.Context(self.ims2)
        
        self.c1.scale (512, 512)
        self.c2.scale (512, 512)
        

        
        #self.ims1.write_to_png ("example.png")
        
        self.img.set_from_file("lenna.png")

        self.window.add(self.img)
        
        
        self.window.show_all()
        
        self.img.connect("expose-event", self._expose)

    def _expose(self, widget, event):
        cr   = self.img.window.cairo_create()
        #w, h = self.allocation.width, self.allocation.height
        cr.set_source_surface(self.ims1)
        cr.paint()
        
        
    
    def drawLine(self):
        self.c1.move_to(0,0)
        self.c1.line_to(.5,.5)
        self.c1.set_source_rgb (0.3, 0.2, 0.5) # Solid color
        self.c1.set_line_width (0.02)
        self.c1.stroke()
        
        return True
        
    def main(self):
        gtk.main()



if __name__ == "__main__":
    base = Base()
    base.drawLine()
    base.main()
