#!/usr/bin/env python
'''Code for plotting streamlines.

@author: Zach Hafen
@contact: zachary.h.hafen@gmail.com
'''

import numpy as np

import matplotlib
matplotlib.use('PDF')
import matplotlib.pyplot as plt
import matplotlib.collections as collections
import matplotlib.colors as colors

########################################################################

def streamline_plot(
        ax,
        x_data,
        y_data,
        color1 = 'black',
        color2 = 'white',
        color_power = 2.,
        linewidth = 5,
    ):
    '''Plot the path taken by a single particle.

    Args:
        ax (axes object) :
            Axes on which to plot the streamlines.

        x_data, y_data (array-like) :
            X- and Y- position of the particle at subsequent time steps.

        color1, color2 (str) :
            The color of the line goes from color 1 to color 2. For given data point, closer the index of that data point is to
            the start of the array, the more it will be color1.

        linewidth (int) :
            How thick should the line be, starting out? (The line segment x_data[0], y_data[0] will have a linewidth
            of this size.

        color_power (float) :
            This determines how fast the color transitions from one to another. Higher values mean more of color2,
            lower values mean more of color1.
    '''

    # This array determines color of the line
    z_data = np.linspace(0., 1., x_data.size )

    # Make it so that we spend more time at the specified color.
    # (This goes from 0 to 1, and the more time at 0, the less time
    # the color is white.)
    z_data = z_data**color_power

    # Make the colormap
    color_list = [ color1, color2 ]
    cmap = colors.LinearSegmentedColormap.from_list(
        'sequential',
        color_list,
        N = 256
    )

    # Format the data
    combined_arr = np.array( [ x_data, y_data ] ).transpose()
    reshaped_arr = combined_arr.reshape( -1, 1, 2 )
    segments = np.concatenate( [ reshaped_arr[:-1], reshaped_arr[1:] ], axis=1 )

    lc = collections.LineCollection(
        segments,
        cmap = cmap,
        norm = plt.Normalize(0, 1),
        linewidths = np.linspace( linewidth, 0, x_data.size ),
        array = z_data,
    )

    ax.add_collection( lc )

