# Basic-Apex-Frame-Detection-For-Video-Sequence

Using SMIC database excel information ...
SMIC database have three subdatasets, include HS, VIS, NIR ...

How to get the SMIC database?
1. Sign the SMIC agreement.
2. Sent the agreement to the author (xiaobai.li@oulu.fi)


How to get the Micro-expression Apex Frame in Micro-expression video sequence?
=> Using openCV

說明:
透過OpenCV的library引入，固定onset frame，透過針對每一幀(frame)絕對差分計算，找出最大值，即為所需的apex frame，另外你會發現這就是frame difference method
