<h1 align="center">
  Image Generator
  <br>
  <br>
</h1>

## Description
This python script was developed by [Ostap Filipenko](https://www.linkedin.com/in/ostap-filipenko-7b7945165) and [Luca Kramberger](https://www.linkedin.com/in/luca-kramberger-6298b6201) to generate random images from components that are located in the Components directory.

## Some of the generated images

![NFT-1](/Generated Images/NFT_1.png?raw=true "NFT-1")
![NFT-4](./Generated Images/NFT_4.png?raw=true "NFT-4")
![NFT-6](./Generated Images/NFT_6.png?raw=true "NFT-6")
![NFT-9](./Generated Images/NFT_9.png?raw=true "NFT-9")
![NFT-12](./Generated Images/NFT_12.png?raw=true "NFT-12")
![NFT-14](./Generated Images/NFT_14.png?raw=true "NFT-14")
![NFT-16](./Generated Images/NFT_16.png?raw=true "NFT-16")
![NFT-18](./Generated Images/NFT_18.png?raw=true "NFT-18")
![NFT-22](./Generated Images/NFT_22.png?raw=true "NFT-22")
![NFT-23](./Generated Images/NFT_23.png?raw=true "NFT-23")
![NFT-27](./Generated Images/NFT_27.png?raw=true "NFT-27")
![NFT-28](./Generated Images/NFT_28.png?raw=true "NFT-28")
![NFT-29](./Generated Images/NFT_29.png?raw=true "NFT-29")


## How does it work?
There are 5 layers, which have specific variety of components, those components can be sqaure, triange, circle... They can be filled or outlined it depends on the layer components. The script takes a random color from the color file and paints the random chosen layer component into that color. This is happaning maximal 5 times, because there are 5 layers. After each painting process the latest layer is combined with the layer before. At the end all layers are combined into one svg graphic that is then converted into a png file. In the GUI the user can choose the path where to save the generated images and the user is also able to enter the number of images that are going to be generated.

## License

[MIT](LICENSE). Copyright (c) [Ostap Filipenko](https://www.linkedin.com/in/ostap-filipenko-7b7945165) and [Luca Kramberger](https://www.linkedin.com/in/luca-kramberger-6298b6201).
