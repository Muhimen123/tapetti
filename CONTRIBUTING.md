NOTE: Make sure to fork the `dev` branch instead of `main`

## Understanding The File Structure

```
main.py 
├───data
│   └───images
├───utils
  
```

 - `main.py` The file you need to run to interact with the application.
 - `data/images` Contains downloaded images, wallpaper and preview image.
 - `utils` Various features of the application.

## Adding Platform Support

 Navigate to `utils/imageSaver.py`. There, you will find three functions.
  - change_windows_wallpaper (completed)
  - change_mac_wallpaper (yet to complete)
  - change_linux_wallpaper (yet to complete)

Now, you can write the platform specific logic for the OS you want in the respective function. That's all!

