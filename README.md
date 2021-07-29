<div align="center">

![Tapetti Banner](http://res.cloudinary.com/muhimen/image/upload/v1626590712/xlqpowgocxe2jd5wbxiv.png)

</div>

<div align="center">

![platform](https://img.shields.io/badge/Platform-Windows-blue?style=flat-square&logo=windows) ![language](https://img.shields.io/badge/Language-Python%203-yellow?style=flat-square&logo=python) ![license](https://img.shields.io/badge/License-MIT-blueviolet?style=flat-square&logo=files)

</div>

# TAPETTI

Tapetti is a wallpaper manager that you never asked for. Feature-rich yet minimalistic, powerful yet simple to use. Save, download, manage all your wallpapers in one go!

<div align="center"> 

  <a href="#">
    <img src="http://res.cloudinary.com/muhimen/image/upload/v1627527483/rpkze0dnsa75yjojdcyv.png" alt="download" height="20%" width="20%">
  <a/>

  <a href="#">
    <img src="http://res.cloudinary.com/muhimen/image/upload/v1627527506/r1vwf88npvmjph2cpyed.png" alt="bug" height="20%" width="20%">
  <a/>

  <a href="#">
    <img src="http://res.cloudinary.com/muhimen/image/upload/v1627527521/kjt1xssckyoisc6ij9jy.png" alt="contribute" height="20%" width="20%">
  <a/>

</div>

# Featuers

Tapetti currently ships with 6 commands. Which is probably more than you need. 

  - <details> 
    <summary> browse </summary>

    Prints a table. All the available wallpapers in the the [TID](https://github.com/Muhimen123/TID) repository.

    ![Browse](http://res.cloudinary.com/muhimen/image/upload/v1627529732/uvjzovzs1kec6d9urfwq.gif)

  </details>

  - <details> 
    <summary> download </summary>

    Download an image without setting it as wallpaper. It will require `download link`, `path` & `file name`.

    ![Download](http://res.cloudinary.com/muhimen/image/upload/v1627529770/o9jriwscuirivsqrjn2i.gif)

  </details>

  - <details> 
    <summary> help </summary>

    Prints a table. Shows all the available commands.

  </details>

  - <details> 
    <summary> save </summary>

    Set an image as wallpaper. You have three options for setting wallpaper. From `TID Repo`, `Image Path` or `Download Link`.

    ![Save](http://res.cloudinary.com/muhimen/image/upload/v1627529816/ifxuser8jkjabygtfkvo.gif)

  </details>

  - <details> 
    <summary> search </summary>
    
    Search for an image in the TID repo. Currently you can only filter search results by tag name.

  </details>

  - <details> 
    <summary> view </summary>
    
    Previews an image. Previews an image from `TID Repo` or `Image URL`.

    ![View](http://res.cloudinary.com/muhimen/image/upload/v1627529852/khb5ljzjipyakf2xqkkl.gif)

  </details>

# Installation

For now, you can run it from the source. More installation methods coming soon. 

  - <details>
    <summary>Download Binary</summary>

    The easiest way to download and run tapetti is via the binary executable. Navigate to the [release](https://github.com/Muhimen123/tapetti/releases) page. Currently you will find two executalbe. One for linux and another for windows. Download the executalbe you need. And in the same directory create an empty directory called `data`. This will be your default directory for storing images and other data. 
    It's recommended to run the binary from the terminal. 

  </details>

  - <details>
    <summary> Install From The Source </summary>

    Assuming that you have both [git](https://git-scm.com/downloads) and [python](https://www.python.org/downloads/) properly installed, you can run the following commands to set up Tapetti for your machine. 

    First, clone the repository.

    ```
    git clone https://github.com/Muhimen123/tapetti.git
    ```

    Navigate to the directory.

    ```
    cd tapetti
    ```

    Download the requirements.

    ```
    pip install -r requirements.txt
    ```

    Now, run the `main.py` script and enjoy!!

    ```
    python main.py
    ```

  </details>

# Need Help!

The wallpaper change feature only works for windows since changing wallpaper is different accross different platforms. It will be a great help if you can help me up with `GNU\Linux`(partial support available) and `MacOS` integration. Check [CONTRIBUTING.md](https://github.com/Muhimen123/tapetti/blob/main/CONTRIBUTING.md) for further help. Thanks!

