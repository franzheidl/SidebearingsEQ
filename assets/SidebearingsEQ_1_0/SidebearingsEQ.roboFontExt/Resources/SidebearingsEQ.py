from AppKit import *
import vanilla
import math
from defconAppKit.windows.baseWindow import BaseWindowController

class SidebearingsEQ(BaseWindowController):

    def __init__(self):
        self.w = vanilla.Window((200, 120), "Sidebearings EQ")
        self.w.iconAll = vanilla.ImageView((15, 16, 13, 10))
        self.w.iconAll.setImage(imagePath="allglyphs.png")
        self.w.iconSelected = vanilla.ImageView((15, 43, 13, 10))
        self.w.iconSelected.setImage(imagePath="selectedglyphs.png")
        self.w.scopeRadioGroup = vanilla.RadioGroup((35, 10, -15, 50), ["All Glyphs", "Selected Glyphs"], sizeStyle="small")
        self.w.scopeRadioGroup.set(1)
        self.w.divider1 = vanilla.HorizontalLine((15, 70, -15, 1))
        self.w.applyButton = vanilla.Button((15, 85, -15, 20), "Equalize Sidebearings", sizeStyle="small", callback=self.applyButtonCallback)
        self.w.open()

    def applyButtonCallback(self, sender):
                
        if CurrentFont() is None:
            # warn/alert if no font is open  
            self.showMessage(u"Ergh\u2026", u"\u2026You might want to open a font first?")
        else:        
            font = CurrentFont()
            if self.w.scopeRadioGroup.get() == 0:
                glyphNames = font.keys()
            else:
                glyphNames = font.selection       
            if glyphNames == []:
                # alert if scope is "Selected Glyphs" but no glyphs are selected:
                self.showMessage("Oops!", "Select at least one glyph please.")
            else:
                for glyphName in glyphNames:
                    glyph = font[glyphName]
                    glyph.prepareUndo("Equalize Sidebearings")
                    sidebearings = glyph.leftMargin + glyph.rightMargin
                    
                    if sidebearings % 2 == 0:
                        leftsidebearing = int(sidebearings / 2)
                        rightsidebearing = int(sidebearings / 2)
                    else:
                        leftsidebearing = int(math.floor(sidebearings / 2))
                        rightsidebearing = int(math.ceil(sidebearings / 2))
                    
                    glyph.leftMargin = leftsidebearing
                    glyph.rightMargin = rightsidebearing
                    glyph.performUndo()

SidebearingsEQ()