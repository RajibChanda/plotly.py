from plotly.basedatatypes import BaseTraceHierarchyType


class Line(BaseTraceHierarchyType):

    # color
    # -----
    @property
    def color(self):
        """
        Sets the marker.line color. It accepts either a specific color
        or an array of numbers that are mapped to the colorscale
        relative to the max and min values of the array or relative to
        `cmin` and `cmax` if set.
    
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
          - A list or array of any of the above

        Returns
        -------
        str|numpy.ndarray
        """
        return self['color']

    @color.setter
    def color(self, val):
        self['color'] = val

    # colorsrc
    # --------
    @property
    def colorsrc(self):
        """
        Sets the source reference on plot.ly for  color .
    
        The 'colorsrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        return self['colorsrc']

    @colorsrc.setter
    def colorsrc(self, val):
        self['colorsrc'] = val

    # width
    # -----
    @property
    def width(self):
        """
        Sets the width (in px) of the lines bounding the marker points.
    
        The 'width' property is a number and may be specified as:
          - An int or float in the interval [0, inf]
          - A tuple, list, or one-dimensional numpy array of the above

        Returns
        -------
        int|float|numpy.ndarray
        """
        return self['width']

    @width.setter
    def width(self, val):
        self['width'] = val

    # widthsrc
    # --------
    @property
    def widthsrc(self):
        """
        Sets the source reference on plot.ly for  width .
    
        The 'widthsrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        return self['widthsrc']

    @widthsrc.setter
    def widthsrc(self, val):
        self['widthsrc'] = val

    # property parent name
    # --------------------
    @property
    def _parent_path_str(self):
        return 'choropleth.marker'

    # Self properties description
    # ---------------------------
    @property
    def _prop_descriptions(self):
        return """\
        color
            Sets the marker.line color. It accepts either a
            specific color or an array of numbers that are mapped
            to the colorscale relative to the max and min values of
            the array or relative to `cmin` and `cmax` if set.
        colorsrc
            Sets the source reference on plot.ly for  color .
        width
            Sets the width (in px) of the lines bounding the marker
            points.
        widthsrc
            Sets the source reference on plot.ly for  width .
        """

    def __init__(
        self,
        arg=None,
        color=None,
        colorsrc=None,
        width=None,
        widthsrc=None,
        **kwargs
    ):
        """
        Construct a new Line object
        
        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of plotly.graph_objs.choropleth.marker.Line
        color
            Sets the marker.line color. It accepts either a
            specific color or an array of numbers that are mapped
            to the colorscale relative to the max and min values of
            the array or relative to `cmin` and `cmax` if set.
        colorsrc
            Sets the source reference on plot.ly for  color .
        width
            Sets the width (in px) of the lines bounding the marker
            points.
        widthsrc
            Sets the source reference on plot.ly for  width .

        Returns
        -------
        Line
        """
        super(Line, self).__init__('line')

        # Validate arg
        # ------------
        if arg is None:
            arg = {}
        elif isinstance(arg, self.__class__):
            arg = arg.to_plotly_json()
        elif not isinstance(arg, dict):
            raise ValueError(
                """\
The first argument to the plotly.graph_objs.choropleth.marker.Line 
constructor must be a dict or 
an instance of plotly.graph_objs.choropleth.marker.Line"""
            )

        # Import validators
        # -----------------
        from plotly.validators.choropleth.marker import (line as v_line)

        # Initialize validators
        # ---------------------
        self._validators['color'] = v_line.ColorValidator()
        self._validators['colorsrc'] = v_line.ColorsrcValidator()
        self._validators['width'] = v_line.WidthValidator()
        self._validators['widthsrc'] = v_line.WidthsrcValidator()

        # Populate data dict with properties
        # ----------------------------------
        v = arg.pop('color', None)
        self.color = color or v
        v = arg.pop('colorsrc', None)
        self.colorsrc = colorsrc or v
        v = arg.pop('width', None)
        self.width = width or v
        v = arg.pop('widthsrc', None)
        self.widthsrc = widthsrc or v

        # Process unknown kwargs
        # ----------------------
        self._process_kwargs(**dict(arg, **kwargs))
