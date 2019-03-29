import streams
from riverdi.displays.bt81x import ctp50
from bridgetek.bt81x import bt81x

streams.serial()

new_resource('RiverdiLogo.png')

LOGO_W = 642
LOGO_H = 144
linestride = LOGO_W * 2 # with ARGB1555 and ARGB4 formats, 2 bytes per pixel


layout = (bt81x.ARGB4, linestride)  # choose this layout for RiverdiLogo.png

riverdi_logo = bt81x.Bitmap(1, 0, layout,
                    (bt81x.BILINEAR, bt81x.BORDER, bt81x.BORDER, LOGO_W, LOGO_H))

bt81x.init(SPI0, D4, D5, D34)

bt81x.load_image(0, 0, 'RiverdiLogo.png')

bt81x.dl_start()
bt81x.clear_color(rgb=(0xff, 0xff, 0xff))
bt81x.clear(1, 1, 0)

riverdi_logo.prepare_draw()
riverdi_logo.draw(((bt81x.display_conf.width - LOGO_W)//2, (bt81x.display_conf.height - LOGO_H)//2), vertex_fmt=0)

bt81x.display()
bt81x.swap_and_empty()
