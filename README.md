<h1 align="center">
  Image Generator
  <br>
  <br>
</h1>

## Description
This python script was developed by [Ostap Filipenko](https://www.linkedin.com/in/ostap-filipenko-7b7945165) and [Luca Kramberger](https://www.linkedin.com/in/luca-kramberger-6298b6201) to generate random images from components that are located in the Components directory.

## Some of the generated images

![NFT-1](https://github.com/OstapFilipenko/Image-Generator/blob/main/Generated%20Images/NFT_1.png)
![NFT-4](https://github.com/OstapFilipenko/Image-Generator/blob/main/Generated%20Images/NFT_4.png)
![NFT-6](https://github.com/OstapFilipenko/Image-Generator/blob/main/Generated%20Images/NFT_6.png)
![NFT-9](https://github.com/OstapFilipenko/Image-Generator/blob/main/Generated%20Images/NFT_9.png)
![NFT-12](https://github.com/OstapFilipenko/Image-Generator/blob/main/Generated%20Images/NFT_12.png)
![NFT-14](https://github.com/OstapFilipenko/Image-Generator/blob/main/Generated%20Images/NFT_14.png)
![NFT-16](https://github.com/OstapFilipenko/Image-Generator/blob/main/Generated%20Images/NFT_16.png)
![NFT-18](https://github.com/OstapFilipenko/Image-Generator/blob/main/Generated%20Images/NFT_18.png)
![NFT-22](https://github.com/OstapFilipenko/Image-Generator/blob/main/Generated%20Images/NFT_22.png)
![NFT-23](https://github.com/OstapFilipenko/Image-Generator/blob/main/Generated%20Images/NFT_23.png)
![NFT-27](https://github.com/OstapFilipenko/Image-Generator/blob/main/Generated%20Images/NFT_27.png)
![NFT-28](https://github.com/OstapFilipenko/Image-Generator/blob/main/Generated%20Images/NFT_28.png)
![NFT-29](https://github.com/OstapFilipenko/Image-Generator/blob/main/Generated%20Images/NFT_29.png)


## How does it work?
There are 5 layers, which have specific variety of components, those components can be sqaure, triange, circle... They can be filled or outlined it depends on the layer components. The script takes a random color from the color file and paints the random chosen layer component into that color. This is happaning maximal 5 times, because there are 5 layers. After each painting process the latest layer is combined with the layer before. At the end all layers are combined into one svg graphic that is then converted into a png file. In the GUI the user can choose the path where to save the generated images and the user is also able to enter the number of images that are going to be generated.

## License

[MIT](LICENSE). Copyright (c) [Ostap Filipenko](https://www.linkedin.com/in/ostap-filipenko-7b7945165) and [Luca Kramberger](https://www.linkedin.com/in/luca-kramberger-6298b6201).
