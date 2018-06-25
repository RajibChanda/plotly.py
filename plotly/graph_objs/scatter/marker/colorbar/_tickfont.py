from plotly.basedatatypes import BaseTraceHierarchyType


class Tickfont(BaseTraceHierarchyType):

    # color
    # -----
    @property
    def color(self):
        """
        The 'color' property is a color and may be specified as:
          - A hex string (e.g. '#ff0000')
          - An rgb/rgba string (e.g. 'rgb(255,0,0)')
          - An hsl/hsla string (e.g. 'hsl(0,100%,50%)')
          - An hsv/hsva string (e.g. 'hsv(0,100%,100%)')
          - A named CSS color:
                aliceblue, antiquewhite, aqua, aquamarine, azure,
                beige, bisque, black, blanchedalmond, blue,
                blueviolet, brown, burlywood, cadetblue,
                chartreuse, chocolate, coral, cornflowerblue,
                cornsilk, crimson, cyan, darkblue, darkcyan,
                darkgoldenrod, darkgray, darkgrey, darkgreen,
                darkkhaki, darkmagenta, darkolivegreen, darkorange,
                darkorchid, darkred, darksalmon, darkseagreen,
                darkslateblue, darkslategray, darkslategrey,
                darkturquoise, darkviolet, deeppink, deepskyblue,
                dimgray, dimgrey, dodgerblue, firebrick,
                floralwhite, forestgreen, fuchsia, gainsboro,
                ghostwhite, gold, goldenrod, gray, grey, green,
                greenyellow, honeydew, hotpink, indianred, indigo,
                ivory, khaki, lavender, lavenderblush, lawngreen,
                lemonchiffon, lightblue, lightcoral, lightcyan,
                lightgoldenrodyellow, lightgray, lightgrey,
                lightgreen, lightpink, lightsalmon, lightseagreen,
                lightskyblue, lightslategray, lightslategrey,
                lightsteelblue, lightyellow, lime, limegreen,
                linen, magenta, maroon, mediumaquamarine,
                mediumblue, mediumorchid, mediumpurple,
                mediumseagreen, mediumslateblue, mediumspringgreen,
                mediumturquoise, mediumvioletred, midnightblue,
                mintcream, mistyrose, moccasin, navajowhite, navy,
                oldlace, olive, olivedrab, orange, orangered,
                orchid, palegoldenrod, palegreen, paleturquoise,
                palevioletred, papayawhip, peachpuff, peru, pink,
                plum, powderblue, purple, red, rosybrown,
                royalblue, saddlebrown, salmon, sandybrown,
                seagreen, seashell, sienna, silver, skyblue,
                slateblue, slategray, slategrey, snow, springgreen,
                steelblue, tan, teal, thistle, tomato, turquoise,
                violet, wheat, white, whitesmoke, yellow,
                yellowgreen

        Returns
        -------
        str
        """
        return self['color']

    @color.setter
    def color(self, val):
        self['color'] = val

    # family
    # ------
    @property
    def family(self):
        """
        HTML font family - the typeface that will be applied by the web
        browser. The web browser will only be able to apply a font if
        it is available on the system which it operates. Provide
        multiple font families, separated by commas, to indicate the
        preference in which to apply fonts if they aren't available on
        the system. The plotly service (at https://plot.ly or on-
        premise) generates images on a server, where only a select
        number of fonts are installed and supported. These include
        *Arial*, *Balto*, *Courier New*, *Droid Sans*,, *Droid Serif*,
        *Droid Sans Mono*, *Gravitas One*, *Old Standard TT*, *Open
        Sans*, *Overpass*, *PT Sans Narrow*, *Raleway*, *Times New
        Roman*.
    
        The 'family' property is a string and must be specified as:
          - A non-empty string

        Returns
        -------
        str
        """
        return self['family']

    @family.setter
    def family(self, val):
        self['family'] = val

    # size
    # ----
    @property
    def size(self):
        """
        The 'size' property is a number and may be specified as:
          - An int or float in the interval [1, inf]

        Returns
        -------
        int|float
        """
        return self['size']

    @size.setter
    def size(self, val):
        self['size'] = val

    # property parent name
    # --------------------
    @property
    def _parent_path_str(self):
        return 'scatter.marker.colorbar'

    # Self properties description
    # ---------------------------
    @property
    def _prop_descriptions(self):
        return """\
        color

        family
            HTML font family - the typeface that will be applied by
            the web browser. The web browser will only be able to
            apply a font if it is available on the system which it
            operates. Provide multiple font families, separated by
            commas, to indicate the preference in which to apply
            fonts if they aren't available on the system. The
            plotly service (at https://plot.ly or on-premise)
            generates images on a server, where only a select
            number of fonts are installed and supported. These
            include *Arial*, *Balto*, *Courier New*, *Droid Sans*,,
            *Droid Serif*, *Droid Sans Mono*, *Gravitas One*, *Old
            Standard TT*, *Open Sans*, *Overpass*, *PT Sans
            Narrow*, *Raleway*, *Times New Roman*.
        size

        """

    def __init__(self, arg=None, color=None, family=None, size=None, **kwargs):
        """
        Construct a new Tickfont object
        
        Sets the color bar's tick label font

        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of
            plotly.graph_objs.scatter.marker.colorbar.Tickfont
        color

        family
            HTML font family - the typeface that will be applied by
            the web browser. The web browser will only be able to
            apply a font if it is available on the system which it
            operates. Provide multiple font families, separated by
            commas, to indicate the preference in which to apply
            fonts if they aren't available on the system. The
            plotly service (at https://plot.ly or on-premise)
            generates images on a server, where only a select
            number of fonts are installed and supported. These
            include *Arial*, *Balto*, *Courier New*, *Droid Sans*,,
            *Droid Serif*, *Droid Sans Mono*, *Gravitas One*, *Old
            Standard TT*, *Open Sans*, *Overpass*, *PT Sans
            Narrow*, *Raleway*, *Times New Roman*.
        size


        Returns
        -------
        Tickfont
        """
        super(Tickfont, self).__init__('tickfont')

        # Validate arg
        # ------------
        if arg is None:
            arg = {}
        elif isinstance(arg, self.__class__):
            arg = arg.to_plotly_json()
        elif not isinstance(arg, dict):
            raise ValueError(
                """\
The first argument to the plotly.graph_objs.scatter.marker.colorbar.Tickfont 
constructor must be a dict or 
an instance of plotly.graph_objs.scatter.marker.colorbar.Tickfont"""
            )

        # Import validators
        # -----------------
        from plotly.validators.scatter.marker.colorbar import (
            tickfont as v_tickfont
        )

        # Initialize validators
        # ---------------------
        self._validators['color'] = v_tickfont.ColorValidator()
        self._validators['family'] = v_tickfont.FamilyValidator()
        self._validators['size'] = v_tickfont.SizeValidator()

        # Populate data dict with properties
        # ----------------------------------
        v = arg.pop('color', None)
        self.color = color or v
        v = arg.pop('family', None)
        self.family = family or v
        v = arg.pop('size', None)
        self.size = size or v

        # Process unknown kwargs
        # ----------------------
        self._process_kwargs(**dict(arg, **kwargs))
