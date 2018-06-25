from plotly.basedatatypes import BaseTraceHierarchyType


class ErrorX(BaseTraceHierarchyType):

    # array
    # -----
    @property
    def array(self):
        """
        Sets the data corresponding the length of each error bar.
        Values are plotted relative to the underlying data.
    
        The 'array' property is an array that may be specified as a tuple,
        list, numpy array, or pandas Series

        Returns
        -------
        numpy.ndarray
        """
        return self['array']

    @array.setter
    def array(self, val):
        self['array'] = val

    # arrayminus
    # ----------
    @property
    def arrayminus(self):
        """
        Sets the data corresponding the length of each error bar in the
        bottom (left) direction for vertical (horizontal) bars Values
        are plotted relative to the underlying data.
    
        The 'arrayminus' property is an array that may be specified as a tuple,
        list, numpy array, or pandas Series

        Returns
        -------
        numpy.ndarray
        """
        return self['arrayminus']

    @arrayminus.setter
    def arrayminus(self, val):
        self['arrayminus'] = val

    # arrayminussrc
    # -------------
    @property
    def arrayminussrc(self):
        """
        Sets the source reference on plot.ly for  arrayminus .
    
        The 'arrayminussrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        return self['arrayminussrc']

    @arrayminussrc.setter
    def arrayminussrc(self, val):
        self['arrayminussrc'] = val

    # arraysrc
    # --------
    @property
    def arraysrc(self):
        """
        Sets the source reference on plot.ly for  array .
    
        The 'arraysrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        return self['arraysrc']

    @arraysrc.setter
    def arraysrc(self, val):
        self['arraysrc'] = val

    # color
    # -----
    @property
    def color(self):
        """
        Sets the stoke color of the error bars.
    
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

    # copy_ystyle
    # -----------
    @property
    def copy_ystyle(self):
        """
        The 'copy_ystyle' property must be specified as a bool
        (either True, or False)

        Returns
        -------
        bool
        """
        return self['copy_ystyle']

    @copy_ystyle.setter
    def copy_ystyle(self, val):
        self['copy_ystyle'] = val

    # symmetric
    # ---------
    @property
    def symmetric(self):
        """
        Determines whether or not the error bars have the same length
        in both direction (top/bottom for vertical bars, left/right for
        horizontal bars.
    
        The 'symmetric' property must be specified as a bool
        (either True, or False)

        Returns
        -------
        bool
        """
        return self['symmetric']

    @symmetric.setter
    def symmetric(self, val):
        self['symmetric'] = val

    # thickness
    # ---------
    @property
    def thickness(self):
        """
        Sets the thickness (in px) of the error bars.
    
        The 'thickness' property is a number and may be specified as:
          - An int or float in the interval [0, inf]

        Returns
        -------
        int|float
        """
        return self['thickness']

    @thickness.setter
    def thickness(self, val):
        self['thickness'] = val

    # traceref
    # --------
    @property
    def traceref(self):
        """
        The 'traceref' property is a integer and may be specified as:
          - An int (or float that will be cast to an int)
            in the interval [0, 9223372036854775807]

        Returns
        -------
        int
        """
        return self['traceref']

    @traceref.setter
    def traceref(self, val):
        self['traceref'] = val

    # tracerefminus
    # -------------
    @property
    def tracerefminus(self):
        """
        The 'tracerefminus' property is a integer and may be specified as:
          - An int (or float that will be cast to an int)
            in the interval [0, 9223372036854775807]

        Returns
        -------
        int
        """
        return self['tracerefminus']

    @tracerefminus.setter
    def tracerefminus(self, val):
        self['tracerefminus'] = val

    # type
    # ----
    @property
    def type(self):
        """
        Determines the rule used to generate the error bars. If
        *constant`, the bar lengths are of a constant value. Set this
        constant in `value`. If *percent*, the bar lengths correspond
        to a percentage of underlying data. Set this percentage in
        `value`. If *sqrt*, the bar lengths correspond to the sqaure of
        the underlying data. If *array*, the bar lengths are set with
        data set `array`.
    
        The 'type' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['percent', 'constant', 'sqrt', 'data']

        Returns
        -------
        Any
        """
        return self['type']

    @type.setter
    def type(self, val):
        self['type'] = val

    # value
    # -----
    @property
    def value(self):
        """
        Sets the value of either the percentage (if `type` is set to
        *percent*) or the constant (if `type` is set to *constant*)
        corresponding to the lengths of the error bars.
    
        The 'value' property is a number and may be specified as:
          - An int or float in the interval [0, inf]

        Returns
        -------
        int|float
        """
        return self['value']

    @value.setter
    def value(self, val):
        self['value'] = val

    # valueminus
    # ----------
    @property
    def valueminus(self):
        """
        Sets the value of either the percentage (if `type` is set to
        *percent*) or the constant (if `type` is set to *constant*)
        corresponding to the lengths of the error bars in the bottom
        (left) direction for vertical (horizontal) bars
    
        The 'valueminus' property is a number and may be specified as:
          - An int or float in the interval [0, inf]

        Returns
        -------
        int|float
        """
        return self['valueminus']

    @valueminus.setter
    def valueminus(self, val):
        self['valueminus'] = val

    # visible
    # -------
    @property
    def visible(self):
        """
        Determines whether or not this set of error bars is visible.
    
        The 'visible' property must be specified as a bool
        (either True, or False)

        Returns
        -------
        bool
        """
        return self['visible']

    @visible.setter
    def visible(self, val):
        self['visible'] = val

    # width
    # -----
    @property
    def width(self):
        """
        Sets the width (in px) of the cross-bar at both ends of the
        error bars.
    
        The 'width' property is a number and may be specified as:
          - An int or float in the interval [0, inf]

        Returns
        -------
        int|float
        """
        return self['width']

    @width.setter
    def width(self, val):
        self['width'] = val

    # property parent name
    # --------------------
    @property
    def _parent_path_str(self):
        return 'histogram'

    # Self properties description
    # ---------------------------
    @property
    def _prop_descriptions(self):
        return """\
        array
            Sets the data corresponding the length of each error
            bar. Values are plotted relative to the underlying
            data.
        arrayminus
            Sets the data corresponding the length of each error
            bar in the bottom (left) direction for vertical
            (horizontal) bars Values are plotted relative to the
            underlying data.
        arrayminussrc
            Sets the source reference on plot.ly for  arrayminus .
        arraysrc
            Sets the source reference on plot.ly for  array .
        color
            Sets the stoke color of the error bars.
        copy_ystyle

        symmetric
            Determines whether or not the error bars have the same
            length in both direction (top/bottom for vertical bars,
            left/right for horizontal bars.
        thickness
            Sets the thickness (in px) of the error bars.
        traceref

        tracerefminus

        type
            Determines the rule used to generate the error bars. If
            *constant`, the bar lengths are of a constant value.
            Set this constant in `value`. If *percent*, the bar
            lengths correspond to a percentage of underlying data.
            Set this percentage in `value`. If *sqrt*, the bar
            lengths correspond to the sqaure of the underlying
            data. If *array*, the bar lengths are set with data set
            `array`.
        value
            Sets the value of either the percentage (if `type` is
            set to *percent*) or the constant (if `type` is set to
            *constant*) corresponding to the lengths of the error
            bars.
        valueminus
            Sets the value of either the percentage (if `type` is
            set to *percent*) or the constant (if `type` is set to
            *constant*) corresponding to the lengths of the error
            bars in the bottom (left) direction for vertical
            (horizontal) bars
        visible
            Determines whether or not this set of error bars is
            visible.
        width
            Sets the width (in px) of the cross-bar at both ends of
            the error bars.
        """

    def __init__(
        self,
        arg=None,
        array=None,
        arrayminus=None,
        arrayminussrc=None,
        arraysrc=None,
        color=None,
        copy_ystyle=None,
        symmetric=None,
        thickness=None,
        traceref=None,
        tracerefminus=None,
        type=None,
        value=None,
        valueminus=None,
        visible=None,
        width=None,
        **kwargs
    ):
        """
        Construct a new ErrorX object
        
        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of plotly.graph_objs.histogram.ErrorX
        array
            Sets the data corresponding the length of each error
            bar. Values are plotted relative to the underlying
            data.
        arrayminus
            Sets the data corresponding the length of each error
            bar in the bottom (left) direction for vertical
            (horizontal) bars Values are plotted relative to the
            underlying data.
        arrayminussrc
            Sets the source reference on plot.ly for  arrayminus .
        arraysrc
            Sets the source reference on plot.ly for  array .
        color
            Sets the stoke color of the error bars.
        copy_ystyle

        symmetric
            Determines whether or not the error bars have the same
            length in both direction (top/bottom for vertical bars,
            left/right for horizontal bars.
        thickness
            Sets the thickness (in px) of the error bars.
        traceref

        tracerefminus

        type
            Determines the rule used to generate the error bars. If
            *constant`, the bar lengths are of a constant value.
            Set this constant in `value`. If *percent*, the bar
            lengths correspond to a percentage of underlying data.
            Set this percentage in `value`. If *sqrt*, the bar
            lengths correspond to the sqaure of the underlying
            data. If *array*, the bar lengths are set with data set
            `array`.
        value
            Sets the value of either the percentage (if `type` is
            set to *percent*) or the constant (if `type` is set to
            *constant*) corresponding to the lengths of the error
            bars.
        valueminus
            Sets the value of either the percentage (if `type` is
            set to *percent*) or the constant (if `type` is set to
            *constant*) corresponding to the lengths of the error
            bars in the bottom (left) direction for vertical
            (horizontal) bars
        visible
            Determines whether or not this set of error bars is
            visible.
        width
            Sets the width (in px) of the cross-bar at both ends of
            the error bars.

        Returns
        -------
        ErrorX
        """
        super(ErrorX, self).__init__('error_x')

        # Validate arg
        # ------------
        if arg is None:
            arg = {}
        elif isinstance(arg, self.__class__):
            arg = arg.to_plotly_json()
        elif not isinstance(arg, dict):
            raise ValueError(
                """\
The first argument to the plotly.graph_objs.histogram.ErrorX 
constructor must be a dict or 
an instance of plotly.graph_objs.histogram.ErrorX"""
            )

        # Import validators
        # -----------------
        from plotly.validators.histogram import (error_x as v_error_x)

        # Initialize validators
        # ---------------------
        self._validators['array'] = v_error_x.ArrayValidator()
        self._validators['arrayminus'] = v_error_x.ArrayminusValidator()
        self._validators['arrayminussrc'] = v_error_x.ArrayminussrcValidator()
        self._validators['arraysrc'] = v_error_x.ArraysrcValidator()
        self._validators['color'] = v_error_x.ColorValidator()
        self._validators['copy_ystyle'] = v_error_x.CopyYstyleValidator()
        self._validators['symmetric'] = v_error_x.SymmetricValidator()
        self._validators['thickness'] = v_error_x.ThicknessValidator()
        self._validators['traceref'] = v_error_x.TracerefValidator()
        self._validators['tracerefminus'] = v_error_x.TracerefminusValidator()
        self._validators['type'] = v_error_x.TypeValidator()
        self._validators['value'] = v_error_x.ValueValidator()
        self._validators['valueminus'] = v_error_x.ValueminusValidator()
        self._validators['visible'] = v_error_x.VisibleValidator()
        self._validators['width'] = v_error_x.WidthValidator()

        # Populate data dict with properties
        # ----------------------------------
        v = arg.pop('array', None)
        self.array = array or v
        v = arg.pop('arrayminus', None)
        self.arrayminus = arrayminus or v
        v = arg.pop('arrayminussrc', None)
        self.arrayminussrc = arrayminussrc or v
        v = arg.pop('arraysrc', None)
        self.arraysrc = arraysrc or v
        v = arg.pop('color', None)
        self.color = color or v
        v = arg.pop('copy_ystyle', None)
        self.copy_ystyle = copy_ystyle or v
        v = arg.pop('symmetric', None)
        self.symmetric = symmetric or v
        v = arg.pop('thickness', None)
        self.thickness = thickness or v
        v = arg.pop('traceref', None)
        self.traceref = traceref or v
        v = arg.pop('tracerefminus', None)
        self.tracerefminus = tracerefminus or v
        v = arg.pop('type', None)
        self.type = type or v
        v = arg.pop('value', None)
        self.value = value or v
        v = arg.pop('valueminus', None)
        self.valueminus = valueminus or v
        v = arg.pop('visible', None)
        self.visible = visible or v
        v = arg.pop('width', None)
        self.width = width or v

        # Process unknown kwargs
        # ----------------------
        self._process_kwargs(**dict(arg, **kwargs))
