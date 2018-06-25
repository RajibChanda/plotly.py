from plotly.basedatatypes import BaseTraceHierarchyType


class Selected(BaseTraceHierarchyType):

    # marker
    # ------
    @property
    def marker(self):
        """
        The 'marker' property is an instance of Marker
        that may be specified as:
          - An instance of plotly.graph_objs.bar.selected.Marker
          - A dict of string/value properties that will be passed
            to the Marker constructor
    
            Supported dict properties:
                
                color
                    Sets the marker color of selected points.
                opacity
                    Sets the marker opacity of selected points.

        Returns
        -------
        plotly.graph_objs.bar.selected.Marker
        """
        return self['marker']

    @marker.setter
    def marker(self, val):
        self['marker'] = val

    # textfont
    # --------
    @property
    def textfont(self):
        """
        The 'textfont' property is an instance of Textfont
        that may be specified as:
          - An instance of plotly.graph_objs.bar.selected.Textfont
          - A dict of string/value properties that will be passed
            to the Textfont constructor
    
            Supported dict properties:
                
                color
                    Sets the text font color of selected points.

        Returns
        -------
        plotly.graph_objs.bar.selected.Textfont
        """
        return self['textfont']

    @textfont.setter
    def textfont(self, val):
        self['textfont'] = val

    # property parent name
    # --------------------
    @property
    def _parent_path_str(self):
        return 'bar'

    # Self properties description
    # ---------------------------
    @property
    def _prop_descriptions(self):
        return """\
        marker
            plotly.graph_objs.bar.selected.Marker instance or dict
            with compatible properties
        textfont
            plotly.graph_objs.bar.selected.Textfont instance or
            dict with compatible properties
        """

    def __init__(self, arg=None, marker=None, textfont=None, **kwargs):
        """
        Construct a new Selected object
        
        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of plotly.graph_objs.bar.Selected
        marker
            plotly.graph_objs.bar.selected.Marker instance or dict
            with compatible properties
        textfont
            plotly.graph_objs.bar.selected.Textfont instance or
            dict with compatible properties

        Returns
        -------
        Selected
        """
        super(Selected, self).__init__('selected')

        # Validate arg
        # ------------
        if arg is None:
            arg = {}
        elif isinstance(arg, self.__class__):
            arg = arg.to_plotly_json()
        elif not isinstance(arg, dict):
            raise ValueError(
                """\
The first argument to the plotly.graph_objs.bar.Selected 
constructor must be a dict or 
an instance of plotly.graph_objs.bar.Selected"""
            )

        # Import validators
        # -----------------
        from plotly.validators.bar import (selected as v_selected)

        # Initialize validators
        # ---------------------
        self._validators['marker'] = v_selected.MarkerValidator()
        self._validators['textfont'] = v_selected.TextfontValidator()

        # Populate data dict with properties
        # ----------------------------------
        v = arg.pop('marker', None)
        self.marker = marker or v
        v = arg.pop('textfont', None)
        self.textfont = textfont or v

        # Process unknown kwargs
        # ----------------------
        self._process_kwargs(**dict(arg, **kwargs))
