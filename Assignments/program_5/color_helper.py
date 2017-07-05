import json
import random
import os,sys

DIRPATH = os.path.dirname(os.path.realpath(__file__))

#####################################################################################
#####################################################################################
colors = [{
		"html": "#4b0082",
		"name": "indigo",
		"rgb": [
			75,
			0,
			130
		]
	},
	{
		"html": "#ffd700",
		"name": "gold",
		"rgb": [
			255,
			215,
			0
		]
	},
	{
		"html": "#b22222",
		"name": "firebrick",
		"rgb": [
			178,
			34,
			34
		]
	},
	{
		"html": "#cd5c5c",
		"name": "indianred",
		"rgb": [
			205,
			92,
			92
		]
	},
	{
		"html": "#ffff00",
		"name": "yellow",
		"rgb": [
			255,
			255,
			0
		]
	},
	{
		"html": "#556b2f",
		"name": "darkolivegreen",
		"rgb": [
			85,
			107,
			47
		]
	},
	{
		"html": "#8fbc8f",
		"name": "darkseagreen",
		"rgb": [
			143,
			188,
			143
		]
	},
	{
		"html": "#708090",
		"name": "slategrey",
		"rgb": [
			112,
			128,
			144
		]
	},
	{
		"html": "#2f4f4f",
		"name": "darkslategrey",
		"rgb": [
			47,
			79,
			79
		]
	},
	{
		"html": "#c71585",
		"name": "mediumvioletred",
		"rgb": [
			199,
			21,
			133
		]
	},
	{
		"html": "#ba55d3",
		"name": "mediumorchid",
		"rgb": [
			186,
			85,
			211
		]
	},
	{
		"html": "#7fff00",
		"name": "chartreuse",
		"rgb": [
			127,
			255,
			0
		]
	},
	{
		"html": "#7b68ee",
		"name": "mediumslateblue",
		"rgb": [
			123,
			104,
			238
		]
	},
	{
		"html": "#000000",
		"name": "black",
		"rgb": [
			0,
			0,
			0
		]
	},
	{
		"html": "#00ff7f",
		"name": "springgreen",
		"rgb": [
			0,
			255,
			127
		]
	},
	{
		"html": "#dc143c",
		"name": "crimson",
		"rgb": [
			220,
			20,
			60
		]
	},
	{
		"html": "#ffa07a",
		"name": "lightsalmon",
		"rgb": [
			255,
			160,
			122
		]
	},
	{
		"html": "#a52a2a",
		"name": "brown",
		"rgb": [
			165,
			42,
			42
		]
	},
	{
		"html": "#40e0d0",
		"name": "turquoise",
		"rgb": [
			64,
			224,
			208
		]
	},
	{
		"html": "#6b8e23",
		"name": "olivedrab",
		"rgb": [
			107,
			142,
			35
		]
	},
	{
		"html": "#00ffff",
		"name": "cyan",
		"rgb": [
			0,
			255,
			255
		]
	},
	{
		"html": "#c0c0c0",
		"name": "silver",
		"rgb": [
			192,
			192,
			192
		]
	},
	{
		"html": "#87ceeb",
		"name": "skyblue",
		"rgb": [
			135,
			206,
			235
		]
	},
	{
		"html": "#808080",
		"name": "gray",
		"rgb": [
			128,
			128,
			128
		]
	},
	{
		"html": "#00ced1",
		"name": "darkturquoise",
		"rgb": [
			0,
			206,
			209
		]
	},
	{
		"html": "#daa520",
		"name": "goldenrod",
		"rgb": [
			218,
			165,
			32
		]
	},
	{
		"html": "#006400",
		"name": "darkgreen",
		"rgb": [
			0,
			100,
			0
		]
	},
	{
		"html": "#9400d3",
		"name": "darkviolet",
		"rgb": [
			148,
			0,
			211
		]
	},
	{
		"html": "#a9a9a9",
		"name": "darkgray",
		"rgb": [
			169,
			169,
			169
		]
	},
	{
		"html": "#ffb6c1",
		"name": "lightpink",
		"rgb": [
			255,
			182,
			193
		]
	},
	{
		"html": "#008080",
		"name": "teal",
		"rgb": [
			0,
			128,
			128
		]
	},
	{
		"html": "#8b008b",
		"name": "darkmagenta",
		"rgb": [
			139,
			0,
			139
		]
	},
	{
		"html": "#fafad2",
		"name": "lightgoldenrodyellow",
		"rgb": [
			250,
			250,
			210
		]
	},
	{
		"html": "#e6e6fa",
		"name": "lavender",
		"rgb": [
			230,
			230,
			250
		]
	},
	{
		"html": "#9acd32",
		"name": "yellowgreen",
		"rgb": [
			154,
			205,
			50
		]
	},
	{
		"html": "#d8bfd8",
		"name": "thistle",
		"rgb": [
			216,
			191,
			216
		]
	},
	{
		"html": "#ee82ee",
		"name": "violet",
		"rgb": [
			238,
			130,
			238
		]
	},
	{
		"html": "#000080",
		"name": "navy",
		"rgb": [
			0,
			0,
			128
		]
	},
	{
		"html": "#696969",
		"name": "dimgrey",
		"rgb": [
			105,
			105,
			105
		]
	},
	{
		"html": "#da70d6",
		"name": "orchid",
		"rgb": [
			218,
			112,
			214
		]
	},
	{
		"html": "#0000ff",
		"name": "blue",
		"rgb": [
			0,
			0,
			255
		]
	},
	{
		"html": "#f8f8ff",
		"name": "ghostwhite",
		"rgb": [
			248,
			248,
			255
		]
	},
	{
		"html": "#f0fff0",
		"name": "honeydew",
		"rgb": [
			240,
			255,
			240
		]
	},
	{
		"html": "#6495ed",
		"name": "cornflowerblue",
		"rgb": [
			100,
			149,
			237
		]
	},
	{
		"html": "#00008b",
		"name": "darkblue",
		"rgb": [
			0,
			0,
			139
		]
	},
	{
		"html": "#bdb76b",
		"name": "darkkhaki",
		"rgb": [
			189,
			183,
			107
		]
	},
	{
		"html": "#9370db",
		"name": "mediumpurple",
		"rgb": [
			147,
			112,
			219
		]
	},
	{
		"html": "#fff8dc",
		"name": "cornsilk",
		"rgb": [
			255,
			248,
			220
		]
	},
	{
		"html": "#ff0000",
		"name": "red",
		"rgb": [
			255,
			0,
			0
		]
	},
	{
		"html": "#ffe4c4",
		"name": "bisque",
		"rgb": [
			255,
			228,
			196
		]
	},
	{
		"html": "#708090",
		"name": "slategray",
		"rgb": [
			112,
			128,
			144
		]
	},
	{
		"html": "#008b8b",
		"name": "darkcyan",
		"rgb": [
			0,
			139,
			139
		]
	},
	{
		"html": "#f0e68c",
		"name": "khaki",
		"rgb": [
			240,
			230,
			140
		]
	},
	{
		"html": "#f5deb3",
		"name": "wheat",
		"rgb": [
			245,
			222,
			179
		]
	},
	{
		"html": "#00bfff",
		"name": "deepskyblue",
		"rgb": [
			0,
			191,
			255
		]
	},
	{
		"html": "#663399",
		"name": "rebeccapurple",
		"rgb": [
			102,
			51,
			153
		]
	},
	{
		"html": "#8b0000",
		"name": "darkred",
		"rgb": [
			139,
			0,
			0
		]
	},
	{
		"html": "#4682b4",
		"name": "steelblue",
		"rgb": [
			70,
			130,
			180
		]
	},
	{
		"html": "#f0f8ff",
		"name": "aliceblue",
		"rgb": [
			240,
			248,
			255
		]
	},
	{
		"html": "#778899",
		"name": "lightslategrey",
		"rgb": [
			119,
			136,
			153
		]
	},
	{
		"html": "#dcdcdc",
		"name": "gainsboro",
		"rgb": [
			220,
			220,
			220
		]
	},
	{
		"html": "#48d1cc",
		"name": "mediumturquoise",
		"rgb": [
			72,
			209,
			204
		]
	},
	{
		"html": "#fffaf0",
		"name": "floralwhite",
		"rgb": [
			255,
			250,
			240
		]
	},
	{
		"html": "#ff7f50",
		"name": "coral",
		"rgb": [
			255,
			127,
			80
		]
	},
	{
		"html": "#800080",
		"name": "purple",
		"rgb": [
			128,
			0,
			128
		]
	},
	{
		"html": "#d3d3d3",
		"name": "lightgrey",
		"rgb": [
			211,
			211,
			211
		]
	},
	{
		"html": "#e0ffff",
		"name": "lightcyan",
		"rgb": [
			224,
			255,
			255
		]
	},
	{
		"html": "#e9967a",
		"name": "darksalmon",
		"rgb": [
			233,
			150,
			122
		]
	},
	{
		"html": "#f5f5dc",
		"name": "beige",
		"rgb": [
			245,
			245,
			220
		]
	},
	{
		"html": "#f0ffff",
		"name": "azure",
		"rgb": [
			240,
			255,
			255
		]
	},
	{
		"html": "#b0c4de",
		"name": "lightsteelblue",
		"rgb": [
			176,
			196,
			222
		]
	},
	{
		"html": "#fdf5e6",
		"name": "oldlace",
		"rgb": [
			253,
			245,
			230
		]
	},
	{
		"html": "#adff2f",
		"name": "greenyellow",
		"rgb": [
			173,
			255,
			47
		]
	},
	{
		"html": "#4169e1",
		"name": "royalblue",
		"rgb": [
			65,
			105,
			225
		]
	},
	{
		"html": "#20b2aa",
		"name": "lightseagreen",
		"rgb": [
			32,
			178,
			170
		]
	},
	{
		"html": "#ffe4e1",
		"name": "mistyrose",
		"rgb": [
			255,
			228,
			225
		]
	},
	{
		"html": "#a0522d",
		"name": "sienna",
		"rgb": [
			160,
			82,
			45
		]
	},
	{
		"html": "#f08080",
		"name": "lightcoral",
		"rgb": [
			240,
			128,
			128
		]
	},
	{
		"html": "#ff4500",
		"name": "orangered",
		"rgb": [
			255,
			69,
			0
		]
	},
	{
		"html": "#ffdead",
		"name": "navajowhite",
		"rgb": [
			255,
			222,
			173
		]
	},
	{
		"html": "#00ff00",
		"name": "lime",
		"rgb": [
			0,
			255,
			0
		]
	},
	{
		"html": "#98fb98",
		"name": "palegreen",
		"rgb": [
			152,
			251,
			152
		]
	},
	{
		"html": "#deb887",
		"name": "burlywood",
		"rgb": [
			222,
			184,
			135
		]
	},
	{
		"html": "#fff5ee",
		"name": "seashell",
		"rgb": [
			255,
			245,
			238
		]
	},
	{
		"html": "#00fa9a",
		"name": "mediumspringgreen",
		"rgb": [
			0,
			250,
			154
		]
	},
	{
		"html": "#ff00ff",
		"name": "fuchsia",
		"rgb": [
			255,
			0,
			255
		]
	},
	{
		"html": "#ffefd5",
		"name": "papayawhip",
		"rgb": [
			255,
			239,
			213
		]
	},
	{
		"html": "#ffebcd",
		"name": "blanchedalmond",
		"rgb": [
			255,
			235,
			205
		]
	},
	{
		"html": "#cd853f",
		"name": "peru",
		"rgb": [
			205,
			133,
			63
		]
	},
	{
		"html": "#7fffd4",
		"name": "aquamarine",
		"rgb": [
			127,
			255,
			212
		]
	},
	{
		"html": "#ffffff",
		"name": "white",
		"rgb": [
			255,
			255,
			255
		]
	},
	{
		"html": "#2f4f4f",
		"name": "darkslategray",
		"rgb": [
			47,
			79,
			79
		]
	},
	{
		"html": "#ff6347",
		"name": "tomato",
		"rgb": [
			255,
			99,
			71
		]
	},
	{
		"html": "#fffff0",
		"name": "ivory",
		"rgb": [
			255,
			255,
			240
		]
	},
	{
		"html": "#1e90ff",
		"name": "dodgerblue",
		"rgb": [
			30,
			144,
			255
		]
	},
	{
		"html": "#fffacd",
		"name": "lemonchiffon",
		"rgb": [
			255,
			250,
			205
		]
	},
	{
		"html": "#d2691e",
		"name": "chocolate",
		"rgb": [
			210,
			105,
			30
		]
	},
	{
		"html": "#ffa500",
		"name": "orange",
		"rgb": [
			255,
			165,
			0
		]
	},
	{
		"html": "#228b22",
		"name": "forestgreen",
		"rgb": [
			34,
			139,
			34
		]
	},
	{
		"html": "#a9a9a9",
		"name": "darkgrey",
		"rgb": [
			169,
			169,
			169
		]
	},
	{
		"html": "#808000",
		"name": "olive",
		"rgb": [
			128,
			128,
			0
		]
	},
	{
		"html": "#f5fffa",
		"name": "mintcream",
		"rgb": [
			245,
			255,
			250
		]
	},
	{
		"html": "#faebd7",
		"name": "antiquewhite",
		"rgb": [
			250,
			235,
			215
		]
	},
	{
		"html": "#ff8c00",
		"name": "darkorange",
		"rgb": [
			255,
			140,
			0
		]
	},
	{
		"html": "#5f9ea0",
		"name": "cadetblue",
		"rgb": [
			95,
			158,
			160
		]
	},
	{
		"html": "#ffe4b5",
		"name": "moccasin",
		"rgb": [
			255,
			228,
			181
		]
	},
	{
		"html": "#32cd32",
		"name": "limegreen",
		"rgb": [
			50,
			205,
			50
		]
	},
	{
		"html": "#8b4513",
		"name": "saddlebrown",
		"rgb": [
			139,
			69,
			19
		]
	},
	{
		"html": "#808080",
		"name": "grey",
		"rgb": [
			128,
			128,
			128
		]
	},
	{
		"html": "#483d8b",
		"name": "darkslateblue",
		"rgb": [
			72,
			61,
			139
		]
	},
	{
		"html": "#87cefa",
		"name": "lightskyblue",
		"rgb": [
			135,
			206,
			250
		]
	},
	{
		"html": "#ff1493",
		"name": "deeppink",
		"rgb": [
			255,
			20,
			147
		]
	},
	{
		"html": "#dda0dd",
		"name": "plum",
		"rgb": [
			221,
			160,
			221
		]
	},
	{
		"html": "#00ffff",
		"name": "aqua",
		"rgb": [
			0,
			255,
			255
		]
	},
	{
		"html": "#b8860b",
		"name": "darkgoldenrod",
		"rgb": [
			184,
			134,
			11
		]
	},
	{
		"html": "#800000",
		"name": "maroon",
		"rgb": [
			128,
			0,
			0
		]
	},
	{
		"html": "#f4a460",
		"name": "sandybrown",
		"rgb": [
			244,
			164,
			96
		]
	},
	{
		"html": "#ff00ff",
		"name": "magenta",
		"rgb": [
			255,
			0,
			255
		]
	},
	{
		"html": "#d2b48c",
		"name": "tan",
		"rgb": [
			210,
			180,
			140
		]
	},
	{
		"html": "#bc8f8f",
		"name": "rosybrown",
		"rgb": [
			188,
			143,
			143
		]
	},
	{
		"html": "#ffc0cb",
		"name": "pink",
		"rgb": [
			255,
			192,
			203
		]
	},
	{
		"html": "#add8e6",
		"name": "lightblue",
		"rgb": [
			173,
			216,
			230
		]
	},
	{
		"html": "#db7093",
		"name": "palevioletred",
		"rgb": [
			219,
			112,
			147
		]
	},
	{
		"html": "#3cb371",
		"name": "mediumseagreen",
		"rgb": [
			60,
			179,
			113
		]
	},
	{
		"html": "#6a5acd",
		"name": "slateblue",
		"rgb": [
			106,
			90,
			205
		]
	},
	{
		"html": "#696969",
		"name": "dimgray",
		"rgb": [
			105,
			105,
			105
		]
	},
	{
		"html": "#b0e0e6",
		"name": "powderblue",
		"rgb": [
			176,
			224,
			230
		]
	},
	{
		"html": "#2e8b57",
		"name": "seagreen",
		"rgb": [
			46,
			139,
			87
		]
	},
	{
		"html": "#fffafa",
		"name": "snow",
		"rgb": [
			255,
			250,
			250
		]
	},
	{
		"html": "#0000cd",
		"name": "mediumblue",
		"rgb": [
			0,
			0,
			205
		]
	},
	{
		"html": "#191970",
		"name": "midnightblue",
		"rgb": [
			25,
			25,
			112
		]
	},
	{
		"html": "#afeeee",
		"name": "paleturquoise",
		"rgb": [
			175,
			238,
			238
		]
	},
	{
		"html": "#eee8aa",
		"name": "palegoldenrod",
		"rgb": [
			238,
			232,
			170
		]
	},
	{
		"html": "#f5f5f5",
		"name": "whitesmoke",
		"rgb": [
			245,
			245,
			245
		]
	},
	{
		"html": "#9932cc",
		"name": "darkorchid",
		"rgb": [
			153,
			50,
			204
		]
	},
	{
		"html": "#fa8072",
		"name": "salmon",
		"rgb": [
			250,
			128,
			114
		]
	},
	{
		"html": "#778899",
		"name": "lightslategray",
		"rgb": [
			119,
			136,
			153
		]
	},
	{
		"html": "#7cfc00",
		"name": "lawngreen",
		"rgb": [
			124,
			252,
			0
		]
	},
	{
		"html": "#90ee90",
		"name": "lightgreen",
		"rgb": [
			144,
			238,
			144
		]
	},
	{
		"html": "#d3d3d3",
		"name": "lightgray",
		"rgb": [
			211,
			211,
			211
		]
	},
	{
		"html": "#ff69b4",
		"name": "hotpink",
		"rgb": [
			255,
			105,
			180
		]
	},
	{
		"html": "#ffffe0",
		"name": "lightyellow",
		"rgb": [
			255,
			255,
			224
		]
	},
	{
		"html": "#fff0f5",
		"name": "lavenderblush",
		"rgb": [
			255,
			240,
			245
		]
	},
	{
		"html": "#faf0e6",
		"name": "linen",
		"rgb": [
			250,
			240,
			230
		]
	},
	{
		"html": "#66cdaa",
		"name": "mediumaquamarine",
		"rgb": [
			102,
			205,
			170
		]
	},
	{
		"html": "#008000",
		"name": "green",
		"rgb": [
			0,
			128,
			0
		]
	},
	{
		"html": "#8a2be2",
		"name": "blueviolet",
		"rgb": [
			138,
			43,
			226
		]
	},
	{
		"html": "#ffdab9",
		"name": "peachpuff",
		"rgb": [
			255,
			218,
			185
		]
	}
]

class ColorHelper(object):

    """
    Opens a json file of web colors.
    """
	
    def __init__(self):
	    self.content = colors
	    self.used = []

    def get_unique_random_color(self):
        """
        Returns a random color not previously selected
        """
        r = random.randint(0,len(self.content)-1)
        while r in self.used:
            r = random.randint(0,len(self.content)-1)
            self.used.append(r)
        c = self.content[r]
        return (c['rgb'][0],c['rgb'][1],c['rgb'][2])

    def get_random_color(self):
        """
        Returns a random rgb tuple from the color dictionary
        Args:
            None
        Returns:
            color (tuple) : (r,g,b)
        Usage:
            c = Colors()
            some_color = c.get_random_color()
            # some_color is now a tuple (r,g,b) representing some lucky color
        """
        r = random.randint(0,len(self.content)-1)
        c = self.content[r]
        return (c['rgb'][0],c['rgb'][1],c['rgb'][2])

    def get_random_pastel(self,mix=None):
        red = random.randint(0,256)
        green = random.randint(0,256)
        blue = random.randint(0,256)

        if mix is not None:
            red = (red + mix[0]) / 2
            green = (green + mix[1]) / 2
            blue = (blue + mix[2]) / 2

        return (red,green,blue)


    def get_rgb(self,name):
        """
        Returns a named rgb tuple from the color dictionary
        Args:
            name (string) : name of color to return
        Returns:
            color (tuple) : (r,g,b)
        Usage:
            c = Colors()
            lavender = c.get_rgb('lavender')
            # lavender is now a tuple (230,230,250) representing that color
        """
        for c in self.content:
            if c['name'] == name:
                return (c['rgb'][0],c['rgb'][1],c['rgb'][2])
        return None

    def __getitem__(self,color_name):
        """
        Overloads "[]" brackets for this class so we can treat it like a dict.
        Usage:
            c = Colors()
            current_color = c['violet']
            # current_color contains: (238,130,238)
        """
        return self.get_rgb(color_name)

if __name__=='__main__':
    c = Colors()
    print(c.get_random_color())
    print(c['red'])