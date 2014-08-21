#SidebearingsEQ
**A tiny extension for [RoboFont](http://doc.robofont.com/) to equalize sidebearings for all or a selection of glyphs in a font.**


![SidebearingsEQ Screenshot](screenshot.png)
 


##Using SidebearingsEQ
Once installed, SidebaringsEQ can be accessed via RoboFont's Extension Menu.

In the SidebearingsEQ window, select whether you wish to equalize the sidebearings of all glyphs in your font, or just the glyphs you currently have selected.

SidebearingsEQ will take the sidebearings of each glyph individually, and distribute them equally to the left and right of your glyph. If the sum of your existing sidebearings is an odd number of UPM, it will add the one remaining UPM to the right sidebearing of the glyph.

That small bit of functionality should be pretty useful especially in early stages of design when you haven't yet cared much about spacing but want to have something to start with.

SidebearingsEQ treats the glyphs individually, it is NOT meant to set the sidebearings of a selection of multiple glyphs to an identical value for all the selected glyphs.


##Installing and De-installing SidebearingsEQ
To install SidebearingsEQ, simply double-click the extension. RoboFontsExtension Manager will take care of the rest. 

To de-install SidebearingsEQ, double-click again, and RoboFont will ask you whether you wish to de-install or re-install the extension.

SidebearingsEQ can also be installed and de-installed via [Mechanic](https://github.com/jackjennings/Mechanic), a package manager for RoboFont by Jack Jennings. Mechanic will also notify you and install updates of SidebearingsEQ.


##Bugs, Feature and Help requests
Just open an issue here.

##License
Oh come on. Download, use and abuse as you wish, just do so at your own risk. I've built SidebearingsEQ mainly for my own use and it's made public as is.