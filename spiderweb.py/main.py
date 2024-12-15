from spider_functions import *
import turtle

window = create_window()
spider = create_spider()

build_frame(spider)
pos = spider.pos()
print(pos)
build_stucture(spider)

draw_spider(spider)



window.mainloop()

