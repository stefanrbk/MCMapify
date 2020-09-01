#!/usr/bin/env python

# GIMP Python

import time
import gimp
import gimpcolor
from gimpfu import *

map_palette = [
    [gimpcolor.RGB(0.49019607843137253, 0.6901960784313725, 0.21568627450980393, 1.0),      "GRASS Up"],
    [gimpcolor.RGB(0.4235294117647059, 0.592156862745098, 0.1843137254901961, 1.0),         "GRASS Flat"],
    [gimpcolor.RGB(0.34509803921568627, 0.48627450980392156, 0.15294117647058825, 1.0),     "GRASS Down"],

    [gimpcolor.RGB(0.9568627450980391, 0.9019607843137255, 0.6313725490196078, 1.0),        "SAND Up"],
    [gimpcolor.RGB(0.8235294117647058, 0.7803921568627451, 0.5411764705882353, 1.0),        "SAND Flat"],
    [gimpcolor.RGB(0.6745098039215687, 0.6352941176470588, 0.44705882352941173, 1.0),       "SAND Down"],

    [gimpcolor.RGB(0.7725490196078432, 0.7725490196078432, 0.7725490196078432, 1.0),        "WOOL Up"],
    [gimpcolor.RGB(0.6627450980392157, 0.6627450980392157, 0.6627450980392157, 1.0),        "WOOL Flat"],
    [gimpcolor.RGB(0.5411764705882353, 0.5411764705882353, 0.5411764705882353, 1.0),        "WOOL Down"],

    [gimpcolor.RGB(0.9882352941176471, 0.0, 0.0, 1.0),                                      "FIRE Up"],
    [gimpcolor.RGB(0.8509803921568627, 0.0, 0.0, 1.0),                                      "FIRE Flat"],
    [gimpcolor.RGB(0.6980392156862745, 0.0, 0.0, 1.0),                                      "FIRE Down"],

    [gimpcolor.RGB(0.6196078431372549, 0.6196078431372549, 0.9882352941176471, 1.0),        "ICE Up"],
    [gimpcolor.RGB(0.5333333333333333, 0.5333333333333333, 0.8509803921568627, 1.0),        "ICE Flat"],
    [gimpcolor.RGB(0.43529411764705883, 0.43529411764705883, 0.6980392156862745, 1.0),      "ICE Down"],

    [gimpcolor.RGB(0.6470588235294118, 0.6470588235294118, 0.6470588235294118, 1.0),        "METAL Up"],
    [gimpcolor.RGB(0.5568627450980392, 0.5568627450980392, 0.5568627450980392, 1.0),        "METAL Flat"],
    [gimpcolor.RGB(0.4549019607843137, 0.4549019607843137, 0.4549019607843137, 1.0),        "METAL Down"],

    [gimpcolor.RGB(0.0, 0.4823529411764706, 0.0, 1.0),                                      "PLANT Up"],
    [gimpcolor.RGB(0.0, 0.4117647058823529, 0.0, 1.0),                                      "PLANT Flat"],
    [gimpcolor.RGB(0.0, 0.33725490196078434, 0.0, 1.0),                                     "PLANT Down"],

    [gimpcolor.RGB(0.9882352941176471, 0.9882352941176471, 0.9882352941176471, 1.0),        "SNOW Up"],
    [gimpcolor.RGB(0.8509803921568627, 0.8509803921568627, 0.8509803921568627, 1.0),        "SNOW Flat"],
    [gimpcolor.RGB(0.6980392156862745, 0.6980392156862745, 0.6980392156862745, 1.0),        "SNOW Down"],

    [gimpcolor.RGB(0.6352941176470588, 0.6509803921568628, 0.7137254901960784, 1.0),        "CLAY Up"],
    [gimpcolor.RGB(0.5450980392156862, 0.5568627450980392, 0.611764705882353, 1.0),         "CLAY Flat"],
    [gimpcolor.RGB(0.44705882352941173, 0.4588235294117647, 0.4980392156862745, 1.0),       "CLAY Down"],

    [gimpcolor.RGB(0.5843137254901961, 0.4235294117647059, 0.2980392156862745, 1.0),        "DIRT Up"],
    [gimpcolor.RGB(0.5019607843137255, 0.36470588235294116, 0.2549019607843137, 1.0),       "DIRT Flat"],
    [gimpcolor.RGB(0.4117647058823529, 0.29411764705882354, 0.20784313725490194, 1.0),      "DIRT Down"],

    [gimpcolor.RGB(0.43529411764705883, 0.43529411764705883, 0.43529411764705883, 1.0),     "STONE Up"],
    [gimpcolor.RGB(0.37254901960784315, 0.37254901960784315, 0.37254901960784315, 1.0),     "STONE Flat"],
    [gimpcolor.RGB(0.3058823529411765, 0.3058823529411765, 0.3058823529411765, 1.0),        "STONE Down"],

    [gimpcolor.RGB(0.5529411764705883, 0.4627450980392157, 0.2784313725490196, 1.0),        "WOOD Up"],
    [gimpcolor.RGB(0.4784313725490196, 0.396078431372549, 0.2392156862745098, 1.0),         "WOOD Flat"],
    [gimpcolor.RGB(0.38823529411764707, 0.3254901960784314, 0.19215686274509802, 1.0),      "WOOD Down"],

    [gimpcolor.RGB(0.9882352941176471, 0.9764705882352941, 0.9490196078431372, 1.0),        "QUARTZ Up"],
    [gimpcolor.RGB(0.8509803921568627, 0.8392156862745098, 0.8156862745098039, 1.0),        "QUARTZ Flat"],
    [gimpcolor.RGB(0.6980392156862745, 0.6862745098039216, 0.6666666666666666, 1.0),        "QUARTZ Down"],

    [gimpcolor.RGB(0.8352941176470589, 0.49019607843137253, 0.19607843137254902, 1.0),      "COLOR_ORANGE Up"],
    [gimpcolor.RGB(0.7215686274509804, 0.4235294117647059, 0.16862745098039217, 1.0),       "COLOR_ORANGE Flat"],
    [gimpcolor.RGB(0.5882352941176471, 0.34509803921568627, 0.1411764705882353, 1.0),       "COLOR_ORANGE Down"],

    [gimpcolor.RGB(0.6901960784313725, 0.29411764705882354, 0.8352941176470589, 1.0),       "COLOR_MAGENTA Up"],
    [gimpcolor.RGB(0.592156862745098, 0.25098039215686274, 0.7215686274509804, 1.0),        "COLOR_MAGENTA Flat"],
    [gimpcolor.RGB(0.48627450980392156, 0.20392156862745098, 0.5882352941176471, 1.0),      "COLOR_MAGENTA Down"],

    [gimpcolor.RGB(0.396078431372549, 0.592156862745098, 0.8352941176470589, 1.0),          "COLOR_LIGHT_BLUE Up"],
    [gimpcolor.RGB(0.3411764705882353, 0.5098039215686274, 0.7215686274509804, 1.0),        "COLOR_LIGHT_BLUE Flat"],
    [gimpcolor.RGB(0.2784313725490196, 0.4196078431372549, 0.5882352941176471, 1.0),        "COLOR_LIGHT_BLUE Down"],

    [gimpcolor.RGB(0.8862745098039215, 0.8862745098039215, 0.19607843137254902, 1.0),       "COLOR_YELLOW Up"],
    [gimpcolor.RGB(0.7647058823529411, 0.7647058823529411, 0.16862745098039217, 1.0),       "COLOR_YELLOW Flat"],
    [gimpcolor.RGB(0.6235294117647059, 0.6235294117647059, 0.1411764705882353, 1.0),        "COLOR_YELLOW Down"],

    [gimpcolor.RGB(0.49019607843137253, 0.792156862745098, 0.09803921568627451, 1.0),       "COLOR_LIGHT_GREEN Up"], 
    [gimpcolor.RGB(0.4235294117647059, 0.6823529411764706, 0.08235294117647059, 1.0),       "COLOR_LIGHT_GREEN Flat"],
    [gimpcolor.RGB(0.34509803921568627, 0.5568627450980392, 0.06666666666666667, 1.0),      "COLOR_LIGHT_GREEN Down"],

    [gimpcolor.RGB(0.9372549019607843, 0.49019607843137253, 0.6392156862745098, 1.0),       "COLOR_PINK Up"],
    [gimpcolor.RGB(0.803921568627451, 0.4235294117647059, 0.5490196078431373, 1.0),         "COLOR_PINK Flat"],
    [gimpcolor.RGB(0.6588235294117647, 0.34509803921568627, 0.45098039215686275, 1.0),      "COLOR_PINK Down"],

    [gimpcolor.RGB(0.29411764705882354, 0.29411764705882354, 0.29411764705882354, 1.0),     "COLOR_GRAY Up"],
    [gimpcolor.RGB(0.25098039215686274, 0.25098039215686274, 0.25098039215686274, 1.0),     "COLOR_GRAY Flat"],
    [gimpcolor.RGB(0.20392156862745098, 0.20392156862745098, 0.20392156862745098, 1.0),     "COLOR_GRAY Down"],

    [gimpcolor.RGB(0.592156862745098, 0.592156862745098, 0.592156862745098, 1.0),           "COLOR_LIGHT_GRAY Up"],
    [gimpcolor.RGB(0.5098039215686274, 0.5098039215686274, 0.5098039215686274, 1.0),        "COLOR_LIGHT_GRAY Flat"],
    [gimpcolor.RGB(0.4196078431372549, 0.4196078431372549, 0.4196078431372549, 1.0),        "COLOR_LIGHT_GRAY Down"],

    [gimpcolor.RGB(0.29411764705882354, 0.49019607843137253, 0.592156862745098, 1.0),       "COLOR_CYAN Up"], 
    [gimpcolor.RGB(0.25098039215686274, 0.4235294117647059, 0.5098039215686274, 1.0),       "COLOR_CYAN Flat"],
    [gimpcolor.RGB(0.20392156862745098, 0.34509803921568627, 0.4196078431372549, 1.0),      "COLOR_CYAN Down"],

    [gimpcolor.RGB(0.49019607843137253, 0.24313725490196078, 0.6901960784313725, 1.0),      "COLOR_PURPLE Up"],
    [gimpcolor.RGB(0.4235294117647059, 0.20784313725490194, 0.592156862745098, 1.0),        "COLOR_PURPLE Flat"],
    [gimpcolor.RGB(0.34509803921568627, 0.16862745098039217, 0.48627450980392156, 1.0),     "COLOR_PURPLE Down"],

    [gimpcolor.RGB(0.19607843137254902, 0.29411764705882354, 0.6901960784313725, 1.0),      "COLOR_BLUE Up"],
    [gimpcolor.RGB(0.16862745098039217, 0.25098039215686274, 0.592156862745098, 1.0),       "COLOR_BLUE Flat"],
    [gimpcolor.RGB(0.1411764705882353, 0.20392156862745098, 0.48627450980392156, 1.0),      "COLOR_BLUE Down"],

    [gimpcolor.RGB(0.396078431372549, 0.29411764705882354, 0.19607843137254902, 1.0),       "COLOR_BROWN Up"],
    [gimpcolor.RGB(0.3411764705882353, 0.25098039215686274, 0.16862745098039217, 1.0),      "COLOR_BROWN Flat"],
    [gimpcolor.RGB(0.2784313725490196, 0.20392156862745098, 0.1411764705882353, 1.0),       "COLOR_BROWN Down"],

    [gimpcolor.RGB(0.396078431372549, 0.49019607843137253, 0.19607843137254902, 1.0),       "COLOR_GREEN Up"],
    [gimpcolor.RGB(0.3411764705882353, 0.4235294117647059, 0.16862745098039217, 1.0),       "COLOR_GREEN Flat"],
    [gimpcolor.RGB(0.2784313725490196, 0.34509803921568627, 0.1411764705882353, 1.0),       "COLOR_GREEN Down"],

    [gimpcolor.RGB(0.592156862745098, 0.19607843137254902, 0.19607843137254902, 1.0),       "COLOR_RED Up"],
    [gimpcolor.RGB(0.5098039215686274, 0.16862745098039217, 0.16862745098039217, 1.0),      "COLOR_RED Flat"],
    [gimpcolor.RGB(0.4196078431372549, 0.1411764705882353, 0.1411764705882353, 1.0),        "COLOR_RED Down"],

    [gimpcolor.RGB(0.09803921568627451, 0.09803921568627451, 0.09803921568627451, 1.0),     "COLOR_BLACK Up"], 
    [gimpcolor.RGB(0.08235294117647059, 0.08235294117647059, 0.08235294117647059, 1.0),     "COLOR_BLACK Flat"],
    [gimpcolor.RGB(0.06666666666666667, 0.06666666666666667, 0.06666666666666667, 1.0),     "COLOR_BLACK Down"],

    [gimpcolor.RGB(0.9686274509803922, 0.9215686274509803, 0.2980392156862745, 1.0),        "GOLD Up"],
    [gimpcolor.RGB(0.8313725490196078, 0.796078431372549, 0.2549019607843137, 1.0),         "GOLD Flat"],
    [gimpcolor.RGB(0.6823529411764706, 0.6509803921568628, 0.20784313725490194, 1.0),       "GOLD Down"],

    [gimpcolor.RGB(0.3568627450980392, 0.8470588235294118, 0.8235294117647058, 1.0),        "DIAMOND Up"],
    [gimpcolor.RGB(0.3058823529411765, 0.7294117647058823, 0.7098039215686275, 1.0),        "DIAMOND Flat"],
    [gimpcolor.RGB(0.24705882352941178, 0.596078431372549, 0.580392156862745, 1.0),         "DIAMOND Down"],

    [gimpcolor.RGB(0.28627450980392155, 0.49411764705882355, 0.9882352941176471, 1.0),      "LAPIS Up"],  
    [gimpcolor.RGB(0.24313725490196078, 0.42745098039215684, 0.8509803921568627, 1.0),      "LAPIS Flat"],
    [gimpcolor.RGB(0.2, 0.34901960784313724, 0.6980392156862745, 1.0),                      "LAPIS Down"],

    [gimpcolor.RGB(0.0, 0.8392156862745098, 0.22352941176470587, 1.0),                      "EMERALD Up"],               
    [gimpcolor.RGB(0.0, 0.7254901960784313, 0.19215686274509802, 1.0),                      "EMERALD Flat"],          
    [gimpcolor.RGB(0.0, 0.592156862745098, 0.1568627450980392, 1.0),                        "EMERALD Down"],

    [gimpcolor.RGB(0.4980392156862745, 0.3333333333333333, 0.18823529411764706, 1.0),       "PODZOL Up"],
    [gimpcolor.RGB(0.43137254901960786, 0.28627450980392155, 0.16078431372549018, 1.0),     "PODZOL Flat"],
    [gimpcolor.RGB(0.3529411764705882, 0.23137254901960785, 0.13333333333333333, 1.0),      "PODZOL Down"],

    [gimpcolor.RGB(0.43529411764705883, 0.00784313725490196, 0.0, 1.0),                     "NETHER Up"],
    [gimpcolor.RGB(0.37254901960784315, 0.00392156862745098, 0.0, 1.0),                     "NETHER Flat"],
    [gimpcolor.RGB(0.3058823529411765, 0.00392156862745098, 0.0, 1.0),                      "NETHER Down"],

    [gimpcolor.RGB(0.807843137254902, 0.6862745098039216, 0.6235294117647059, 1.0),         "TERRACOTTA_WHITE Up"],
    [gimpcolor.RGB(0.6980392156862745, 0.5882352941176471, 0.5333333333333333, 1.0),        "TERRACOTTA_WHITE Flat"],
    [gimpcolor.RGB(0.5686274509803921, 0.4823529411764706, 0.4392156862745098, 1.0),        "TERRACOTTA_WHITE Down"],

    [gimpcolor.RGB(0.615686274509804, 0.3176470588235294, 0.1411764705882353, 1.0),         "TERRACOTTA_ORANGE Up"], 
    [gimpcolor.RGB(0.5294117647058824, 0.27058823529411763, 0.12156862745098039, 1.0),      "TERRACOTTA_ORANGE Flat"],
    [gimpcolor.RGB(0.43529411764705883, 0.2196078431372549, 0.09803921568627451, 1.0),      "TERRACOTTA_ORANGE Down"],

    [gimpcolor.RGB(0.5764705882352941, 0.33725490196078434, 0.4196078431372549, 1.0),       "TERRACOTTA_MAGENTA Up"],
    [gimpcolor.RGB(0.49411764705882355, 0.2901960784313725, 0.3607843137254902, 1.0),       "TERRACOTTA_MAGENTA Flat"],
    [gimpcolor.RGB(0.40784313725490196, 0.23529411764705882, 0.29411764705882354, 1.0),     "TERRACOTTA_MAGENTA Down"],

    [gimpcolor.RGB(0.43529411764705883, 0.4196078431372549, 0.5333333333333333, 1.0),       "TERRACOTTA_LIGHT_BLUE Up"],
    [gimpcolor.RGB(0.37254901960784315, 0.3607843137254902, 0.4627450980392157, 1.0),       "TERRACOTTA_LIGHT_BLUE Flat"],
    [gimpcolor.RGB(0.3058823529411765, 0.29411764705882354, 0.3764705882352941, 1.0),       "TERRACOTTA_LIGHT_BLUE Down"],

    [gimpcolor.RGB(0.7215686274509804, 0.5137254901960784, 0.1411764705882353, 1.0),        "TERRACOTTA_YELLOW Up"],
    [gimpcolor.RGB(0.6196078431372549, 0.44313725490196076, 0.12156862745098039, 1.0),      "TERRACOTTA_YELLOW Flat"],
    [gimpcolor.RGB(0.5058823529411764, 0.3607843137254902, 0.09803921568627451, 1.0),       "TERRACOTTA_YELLOW Down"],

    [gimpcolor.RGB(0.4, 0.4549019607843137, 0.20392156862745098, 1.0),                      "TERRACOTTA_LIGHT_GREEN Up"],
    [gimpcolor.RGB(0.3411764705882353, 0.38823529411764707, 0.17254901960784313, 1.0),      "TERRACOTTA_LIGHT_GREEN Flat"],
    [gimpcolor.RGB(0.2784313725490196, 0.3176470588235294, 0.14509803921568626, 1.0),       "TERRACOTTA_LIGHT_GREEN Down"],

    [gimpcolor.RGB(0.6196078431372549, 0.2980392156862745, 0.30196078431372547, 1.0),       "TERRACOTTA_PINK Up"],
    [gimpcolor.RGB(0.5333333333333333, 0.2549019607843137, 0.2588235294117647, 1.0),        "TERRACOTTA_PINK Flat"],
    [gimpcolor.RGB(0.43529411764705883, 0.20784313725490194, 0.21176470588235294, 1.0),     "TERRACOTTA_PINK Down"],

    [gimpcolor.RGB(0.2196078431372549, 0.1568627450980392, 0.13725490196078433, 1.0),       "TERRACOTTA_GRAY Up"],
    [gimpcolor.RGB(0.18823529411764706, 0.13725490196078433, 0.11764705882352941, 1.0),     "TERRACOTTA_GRAY Flat"],
    [gimpcolor.RGB(0.1568627450980392, 0.10980392156862745, 0.09411764705882353, 1.0),      "TERRACOTTA_GRAY Down"],

    [gimpcolor.RGB(0.5215686274509804, 0.4156862745098039, 0.3803921568627451, 1.0),        "TERRACOTTA_LIGHT_GRAY Up"],
    [gimpcolor.RGB(0.45098039215686275, 0.3568627450980392, 0.3254901960784314, 1.0),       "TERRACOTTA_LIGHT_GRAY Flat"],
    [gimpcolor.RGB(0.3686274509803922, 0.2901960784313725, 0.26666666666666666, 1.0),       "TERRACOTTA_LIGHT_GRAY Down"],

    [gimpcolor.RGB(0.33725490196078434, 0.3568627450980392, 0.3568627450980392, 1.0),       "TERRACOTTA_CYAN Up"],
    [gimpcolor.RGB(0.2901960784313725, 0.3058823529411765, 0.3058823529411765, 1.0),        "TERRACOTTA_CYAN Flat"],
    [gimpcolor.RGB(0.23529411764705882, 0.24705882352941178, 0.24705882352941178, 1.0),     "TERRACOTTA_CYAN Down"],

    [gimpcolor.RGB(0.4745098039215686, 0.2823529411764706, 0.3411764705882353, 1.0),        "TERRACOTTA_PURPLE Up"],
    [gimpcolor.RGB(0.40784313725490196, 0.2392156862745098, 0.2901960784313725, 1.0),       "TERRACOTTA_PURPLE Flat"],
    [gimpcolor.RGB(0.3333333333333333, 0.19607843137254902, 0.2392156862745098, 1.0),       "TERRACOTTA_PURPLE Down"],

    [gimpcolor.RGB(0.29411764705882354, 0.2392156862745098, 0.3568627450980392, 1.0),       "TERRACOTTA_BLUE Up"],
    [gimpcolor.RGB(0.25098039215686274, 0.20392156862745098, 0.3058823529411765, 1.0),      "TERRACOTTA_BLUE Flat"],
    [gimpcolor.RGB(0.20392156862745098, 0.16470588235294117, 0.24705882352941178, 1.0),     "TERRACOTTA_BLUE Down"],

    [gimpcolor.RGB(0.29411764705882354, 0.19215686274509802, 0.13725490196078433, 1.0),     "TERRACOTTA_BROWN Up"],
    [gimpcolor.RGB(0.25098039215686274, 0.16470588235294117, 0.11764705882352941, 1.0),     "TERRACOTTA_BROWN Flat"],
    [gimpcolor.RGB(0.20392156862745098, 0.13725490196078433, 0.09411764705882353, 1.0),     "TERRACOTTA_BROWN Down"],

    [gimpcolor.RGB(0.29411764705882354, 0.3176470588235294, 0.16078431372549018, 1.0),      "TERRACOTTA_GREEN Up"],
    [gimpcolor.RGB(0.25098039215686274, 0.27058823529411763, 0.1411764705882353, 1.0),      "TERRACOTTA_GREEN Flat"],
    [gimpcolor.RGB(0.20392156862745098, 0.2196078431372549, 0.11372549019607843, 1.0),      "TERRACOTTA_GREEN Down"],

    [gimpcolor.RGB(0.5490196078431373, 0.23137254901960785, 0.1764705882352941, 1.0),       "TERRACOTTA_RED Up"],
    [gimpcolor.RGB(0.4745098039215686, 0.19607843137254902, 0.15294117647058825, 1.0),      "TERRACOTTA_RED Flat"],
    [gimpcolor.RGB(0.38823529411764707, 0.16078431372549018, 0.12549019607843137, 1.0),     "TERRACOTTA_RED Down"],

    [gimpcolor.RGB(0.14509803921568626, 0.08627450980392157, 0.06274509803921569, 1.0),     "TERRACOTTA_BLACK Up"],
    [gimpcolor.RGB(0.12156862745098039, 0.07058823529411765, 0.050980392156862744, 1.0),    "TERRACOTTA_BLACK Flat"],
    [gimpcolor.RGB(0.10196078431372549, 0.058823529411764705, 0.043137254901960784, 1.0),   "TERRACOTTA_BLACK Down"]]

def setup_palette():
    found = False
    palettes = pdb.gimp_palettes_get_list("Minecraft Map In Order")
    for p in palettes[1]:
        if p == "Minecraft Map In Order":
            found = True
            break
    if found == False:
        pdb.gimp_palette_new("Minecraft Map In Order")
        i = 0
        for color in map_palette:
            pdb.gimp_palette_add_entry("Minecraft Map In Order", color[1], color[0])
            i += 1

def scan_image(map, block, height):
    foreground = pdb.gimp_context_get_foreground()

    pdb.gimp_context_set_sample_threshold(0.0)
    for i in xrange(0, 150):
        pdb.gimp_image_select_color(map.image, 2, map, map_palette[i][0])
        pdb.gimp_context_set_foreground(map_palette[(i/3)*3+1][0])
        if pdb.gimp_selection_is_empty(map.image) == True:
            continue
        #time.sleep(1)
        pdb.gimp_edit_bucket_fill(block, 0, 0, 100, 0, False, 0, 0)
        #time.sleep(3)
        if i % 3 == 0:
            pdb.gimp_context_set_foreground(map_palette[21][0])
        if i % 3 == 1:
            pdb.gimp_context_set_foreground(map_palette[31][0])
        if i % 3 == 2:
            pdb.gimp_context_set_foreground(map_palette[83][0])
        pdb.gimp_edit_bucket_fill(height, 0, 0, 100, 0, False, 0, 0)
        gimp.displays_flush()

    pdb.gimp_context_set_foreground(foreground)
    pdb.gimp_selection_none(map.image)

def do_stuff(img, layer, mapswide, mapstall) :
    setup_palette()
    gimp.progress_init("Minecraft Mapifying " + layer.name + "...")

    # Disable Undo as we are creating a new window
    pdb.gimp_image_undo_disable(img)
    new_img = pdb.gimp_image_duplicate(img)
    gimp.Display(new_img)
    gimp.displays_flush()
    pdb.gimp_image_undo_disable(new_img)

    # Calculate the height and width of the new image
    img_ratio = float(layer.width) / float(layer.height)
    map_ratio = float(mapswide) / float(mapstall)

    offset_x = 0
    offset_y = 0
    width = 0
    height = 0

    # If the aspect ratio of the original image is greater than the aspect ratio of the maps, 
    # then the original image needs padding above and below to fit the maps
    if img_ratio > map_ratio: 
        width = mapswide * 128
        height = int(float(width) / img_ratio)
        offset_y = ((map_ratio * 128) - height) / 2
    # otherwise padding is needed to the left and right
    else:
        height = mapstall * 128
        width = int(img_ratio * float(height))
        offset_x = ((map_ratio * 128) - width) / 2

    # Resize the image to the fit the maps requested
    pdb.gimp_context_set_interpolation(INTERPOLATION_CUBIC)
    pdb.gimp_image_scale(new_img, width, height)
    new_img.resize(mapswide * 128, mapstall * 128, int(offset_x), int(offset_y))

    # Create a new background layer, fill it with the background color, and flatten the image to create the padding
    new_img.add_layer(new_img.active_layer.copy(), 1)
    new_img.layers[1].resize(mapswide * 128, mapstall * 128, int(offset_x), int(offset_y))
    new_img.layers[1].fill(BACKGROUND_FILL)
    new_img.flatten()
    new_img.active_layer.name = layer.name

    # Turn the image into the map palette
    pdb.gimp_image_convert_indexed(new_img, CONVERT_DITHER_FS_LOWBLEED, CONVERT_PALETTE_CUSTOM, 0, False, True, "Minecraft Map In Order")
    gimp.displays_flush()

    # Create 2 duplicate layers as they will be used in outputing the build details
    new_img.add_layer(new_img.layers[0].copy(), 1)
    new_img.add_layer(new_img.layers[0].copy(), 2)

    new_img.layers[0].name = layer.name + " [Map]"
    new_img.layers[1].name = layer.name + " [Types]"
    new_img.layers[2].name = layer.name + " [Heights]"

    scan_image(new_img.layers[0], new_img.layers[1], new_img.layers[2])

    # Enable undo again
    pdb.gimp_image_undo_enable(img)
    pdb.gimp_image_undo_enable(new_img)

register(
    "python_fu_minecraft_mapify",
    "Minecraft Mapify",
    "Turn your image into a Minecraft Map",
    "Stefan Kewatt",
    "Stefan Kewatt",
    "2020",
    "<Image>/Filters/Minecraft Mapify(py)...",
    "*", # Alternately use RGB, RGB*, GRAY*, INDEXED etc.
    [
        (PF_INT, "mapswide", "How Many Maps Wide", 1),
        (PF_INT, "mapstall", "How Many Maps Tall", 1)
    ],
    [],
    do_stuff)

main()
