from plotly.basedatatypes import BaseLayoutHierarchyType


class Fill(BaseLayoutHierarchyType):

    # outlinecolor
    # ------------
    @property
    def outlinecolor(self):
        """
        Sets the fill outline color. Has an effect only when `type` is
        set to *fill*.
    
        The 'outlinecolor' property is a color and may be specified as:
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
        return self['outlinecolor']

    @outlinecolor.setter
    def outlinecolor(self, val):
        self['outlinecolor'] = val

    # property parent name
    # --------------------
    @property
    def _parent_path_str(self):
        return 'layout.mapbox.layer'

    # Self properties description
    # ---------------------------
    @property
    def _prop_descriptions(self):
        return """\
        outlinecolor
            Sets the fill outline color. Has an effect only when
            `type` is set to *fill*.
        """

    def __init__(self, arg=None, outlinecolor=None, **kwargs):
        """
        Construct a new Fill object
        
        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of
            plotly.graph_objs.layout.mapbox.layer.Fill
        outlinecolor
            Sets the fill outline color. Has an effect only when
            `type` is set to *fill*.

        Returns
        -------
        Fill
        """
        super(Fill, self).__init__('fill')

        # Validate arg
        # ------------
        if arg is None:
            arg = {}
        elif isinstance(arg, self.__class__):
            arg = arg.to_plotly_json()
        elif not isinstance(arg, dict):
            raise ValueError(
                """\
The first argument to the plotly.graph_objs.layout.mapbox.layer.Fill 
constructor must be a dict or 
an instance of plotly.graph_objs.layout.mapbox.layer.Fill"""
            )

        # Import validators
        # -----------------
        from plotly.validators.layout.mapbox.layer import (fill as v_fill)

        # Initialize validators
        # ---------------------
        self._validators['outlinecolor'] = v_fill.OutlinecolorValidator()

        # Populate data dict with properties
        # ----------------------------------
        v = arg.pop('outlinecolor', None)
        self.outlinecolor = outlinecolor or v

        # Process unknown kwargs
        # ----------------------
        self._process_kwargs(**dict(arg, **kwargs))
