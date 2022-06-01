from turtle import *    #chỉ khai báo


#hình chữ nhật đỏ
goto(-200,150)
color("red")
begin_fill()
for i in range(2):
    forward(600)
    right(90)
    forward(350)
    right(90)
end_fill()


#sao vàng
goto(0,0)            #dịch chuyển đến vị trí này
color("yellow")      # màu này 
begin_fill()
for i in range(5):
    forward(200)    #đi về phía trước
    right(144)      # quay phải 144 độ
end_fill()

color("red")
goto(-200,150)

done()
