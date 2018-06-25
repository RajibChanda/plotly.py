from plotly.basedatatypes import BaseLayoutHierarchyType


class Domain(BaseLayoutHierarchyType):

    # column
    # ------
    @property
    def column(self):
        """
        If there is a layout grid, use the domain for this column in
        the grid for this mapbox subplot .
    
        The 'column' property is a integer and may be specified as:
          - An int (or float that will be cast to an int)
            in the interval [0, 9223372036854775807]

        Returns
        -------
        int
        """
        return self['column']

    @column.setter
    def column(self, val):
        self['column'] = val

    # row
    # ---
    @property
    def row(self):
        """
        If there is a layout grid, use the domain for this row in the
        grid for this mapbox subplot .
    
        The 'row' property is a integer and may be specified as:
          - An int (or float that will be cast to an int)
            in the interval [0, 9223372036854775807]

        Returns
        -------
        int
        """
        return self['row']

    @row.setter
    def row(self, val):
        self['row'] = val

    # x
    # -
    @property
    def x(self):
        """
        Sets the horizontal domain of this mapbox subplot (in plot
        fraction).
    
        The 'x' property is an info array that may be specified as a
        list or tuple of 2 elements where:
    
    (0) The 'x[0]' property is a number and may be specified as:
          - An int or float in the interval [0, 1]
    (1) The 'x[1]' property is a number and may be specified as:
          - An int or float in the interval [0, 1]

        Returns
        -------
        list
        """
        return self['x']

    @x.setter
    def x(self, val):
        self['x'] = val

    # y
    # -
    @property
    def y(self):
        """
        Sets the vertical domain of this mapbox subplot (in plot
        fraction).
    
        The 'y' property is an info array that may be specified as a
        list or tuple of 2 elements where:
    
    (0) The 'y[0]' property is a number and may be specified as:
          - An int or float in the interval [0, 1]
    (1) The 'y[1]' property is a number and may be specified as:
          - An int or float in the interval [0, 1]

        Returns
        -------
        list
        """
        return self['y']

    @y.setter
    def y(self, val):
        self['y'] = val

    # property parent name
    # --------------------
    @property
    def _parent_path_str(self):
        return 'layout.mapbox'

    # Self properties description
    # ---------------------------
    @property
    def _prop_descriptions(self):
        return """\
        column
            If there is a layout grid, use the domain for this
            column in the grid for this mapbox subplot .
        row
            If there is a layout grid, use the domain for this row
            in the grid for this mapbox subplot .
        x
            Sets the horizontal domain of this mapbox subplot (in
            plot fraction).
        y
            Sets the vertical domain of this mapbox subplot (in
            plot fraction).
        """

    def __init__(
        self, arg=None, column=None, row=None, x=None, y=None, **kwargs
    ):
        """
        Construct a new Domain object
        
        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of plotly.graph_objs.layout.mapbox.Domain
        column
            If there is a layout grid, use the domain for this
            column in the grid for this mapbox subplot .
        row
            If there is a layout grid, use the domain for this row
            in the grid for this mapbox subplot .
        x
            Sets the horizontal domain of this mapbox subplot (in
            plot fraction).
        y
            Sets the vertical domain of this mapbox subplot (in
            plot fraction).

        Returns
        -------
        Domain
        """
        super(Domain, self).__init__('domain')

        # Validate arg
        # ------------
        if arg is None:
            arg = {}
        elif isinstance(arg, self.__class__):
            arg = arg.to_plotly_json()
        elif not isinstance(arg, dict):
            raise ValueError(
                """\
The first argument to the plotly.graph_objs.layout.mapbox.Domain 
constructor must be a dict or 
an instance of plotly.graph_objs.layout.mapbox.Domain"""
            )

        # Import validators
        # -----------------
        from plotly.validators.layout.mapbox import (domain as v_domain)

        # Initialize validators
        # ---------------------
        self._validators['column'] = v_domain.ColumnValidator()
        self._validators['row'] = v_domain.RowValidator()
        self._validators['x'] = v_domain.XValidator()
        self._validators['y'] = v_domain.YValidator()

        # Populate data dict with properties
        # ----------------------------------
        v = arg.pop('column', None)
        self.column = column or v
        v = arg.pop('row', None)
        self.row = row or v
        v = arg.pop('x', None)
        self.x = x or v
        v = arg.pop('y', None)
        self.y = y or v

        # Process unknown kwargs
        # ----------------------
        self._process_kwargs(**dict(arg, **kwargs))
