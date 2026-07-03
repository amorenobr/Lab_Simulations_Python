.. Lab_Simulations_Python documentation master file, created by
   sphinx-quickstart on Thu Feb 19 11:51:53 2026.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Physics Lab Simulations Documentation
=====================================

This is the documentation for all the physics lab simulations. Each simulation is an interactive Streamlit app that lets you 
modify physical parameters and see the results update in real time.

Simulations
-----------


Linear Motion
~~~~~~~~~~~~~

Models a particle moving along a straight line under constant acceleration. Given an initial position :math:`x_0`,
initial velocity :math:`v_0`, constant acceleration :math:`a`, and elapsed time :math:`t`, the app plots position and
velocity against time and reports the final position :math:`x_f = x_0 + v_0 t + \frac{1}{2} a t^2` and final velocity
:math:`v_f = v_0 + a t`. The underlying calculations are implemented in the :mod:`linear_motion` module.


Projectile Motion
~~~~~~~~~~~~~~~~~

Models the flight of an object launched into the air under the influence of gravity alone, with air resistance
neglected. The horizontal and vertical motions are treated independently: the horizontal velocity remains constant, while 
the vertical motion accelerates downward at :math:`g = 9.81\ \mathrm{m/s^2}`. Given an initial speed and launch angle, 
the app plots the trajectory and reports the time of flight, maximum height, and horizontal range. The underlying 
calculations are implemented in the :mod:`projectile` module.


Damped Harmonic Oscillator
~~~~~~~~~~~~~~~~~~~~~~~~~~

Models a mass on a spring subject to a damping force proportional to velocity, governed by :math:`m\ddot{x} + b\dot{x} + kx = 0`. 
By varying the mass, spring stiffness, and damping coefficient, you can explore the four regimes of motion (undamped, 
underdamped, critically damped, and overdamped), determined by the damping ratio :math:`\zeta = b / (2\sqrt{km})`. The app 
plots displacement over time and reports the natural period, natural frequency, and damping ratio. The underlying calculations are implemented in the :mod:`oscillations` module.


API Reference
~~~~~~~~~~~~~

Add your content using ``reStructuredText`` syntax. See the
`reStructuredText <https://www.sphinx-doc.org/en/master/usage/restructuredtext/index.html>`_
documentation for details.


.. toctree::
   :maxdepth: 2
   :caption: Contents:

   api
