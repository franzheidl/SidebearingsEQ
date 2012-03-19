#SidebearingsEQ
**A tiny extension for [RoboFont](http://doc.robofont.com/) to equalize sidebearings for all or a selection of glyphs in a font.**

![SidebearingsEQ Screenshot](http://github.com/franzheidl/SidebearingsEQ/raw/master/screenshot.png)
 


##Using SidebearingsEQ
Once installed, SidebaringsEQ can be accessed via RoboFont's Extension Menu.

In the SidebearingsEQ window, select whether you wish to equalize the sidebearings of all glyphs in your font, or just the glyphs you currently have selected.

SidebearingsEQ will take the sidebearings of each glyph individually, and distribute them equally to the left and right of your glyph. If the sum of your existing sidebearings is an odd number of UPM, it will add the one remaining UPM to the right sidebearing of the glyph.

That small bit of functionality should be pretty useful especially in early stages of design when you haven't yet cared much about spacing but want to have something to start with.

SidebearingsEQ treats the glyphs individually, it is NOT meant to set the sidebearings of a selection of multiple glyphs to an identical value for all the selected glyphs.

## Getting SidebearingsEQ
You may either fork or clone in to this repository, [download the repo tarball](http://github.com/franzheidl/SidebearingsEQ/zipball/master/ "Download the SidebearingsEQ repo tarball") , or, if you don't want to do all the git fluff and just want to use SidebearingsEQ, you can simply [download the extension and readme as a .zip here.](http://github.com/downloads/franzheidl/SidebearingsEQ/SidebearingsEQ_1_0.zip)

##Installing and De-installing SidebearingsEQ
To install SidebearingsEQ, simply double-click the extension. RoboFontsExtension Manager will take care of the rest. 

To de-install SidebearingsEQ, double-click again, and RoboFont will ask you whether you wish to de-install or re-install the extension.

##Bugs, Feature and Help requests
Just open an issue here.