## Visualizing World Happiness
Taking a look at international happiness. Running "happiness3d.py" yields the gif below. 

### ImageMagick for GIF Compilation
```brew install imagemagick```

<img src="/Images/animated_scatter.gif" width="600" height="600" /> 

### Data 
Data from [World Happiness Report 2020](https://worldhappiness.report/ed/2020/#read) Figure 2.1

### Notes
* In creating the gif, 30 .pngs are generated as "slides". Each slide contains a different "camera angle" of the 3D plot, which then get iterated through to mimic animation. While this allows for better optical sense of depth, it does also create 30 .pngs, so be wary!

* The function colorMaker() may not return a valid hex list on its first go. Rerun until it does not throw an error.
