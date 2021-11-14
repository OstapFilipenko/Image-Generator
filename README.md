<h1 align="center">
  Image Generator
  <br>
  <br>
</h1>

## Description
This python script was developed by [Ostap Filipenko](https://www.linkedin.com/in/ostap-filipenko-7b7945165) and [Luca Kramberger](https://www.linkedin.com/in/luca-kramberger-6298b6201) to generate random images from components that are located in the Components directory.

## Some of the generated images

Example

## How does it work?
There are 5 layers, which have specific variety of components, those components can be sqaure, triange, circle... They can be filled or outlined it depends on the layer components. The script takes a random color from the color file and paints the random chosen layer component into that color. This is happaning maximal 5 times, because there are 5 layers. After each painting process the latest layer is combined with the layer before. At the end all layers are combined into one svg graphic that is then converted into a png file. In the GUI the user can choose the path where to save the generated images and the user is also able to enter the number of images that are going to be generated.

## License

[MIT](LICENSE). Copyright (c) [Ostap Filipenko](https://www.linkedin.com/in/ostap-filipenko-7b7945165) and [Luca Kramberger](https://www.linkedin.com/in/luca-kramberger-6298b6201).
