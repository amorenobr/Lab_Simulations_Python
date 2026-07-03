import streamlit as st

st.set_page_config(page_title="Physics Lab Simulations", layout="wide")

st.title("Welcome to the Physics Lab Simulations")

st.markdown(
        """
        This is an interactive collection of physics lab simulations designed to explore key concepts in classical mechanics.
        Each simulation allows you to adjust different physical parameters and see the results update in real time.

        ### Available Simulations
        - **Linear Motion** - Model a particle moving in a straight line with constant acceleration. Set the initial
        position, initial velocity, acceleration, and time to observe the position and velocity evolve over time and read 
        off the final position and velocity.
        - **Projectile Motion** - Launch a projectile with a chosen speed and angle, then visualize its trajectory. 
        The simulation computes and displays the time of flight, maximum height, and horizontal range using the 
        kinematic equations.
        - **Damped Harmonic Oscillator** - Explore the motion of a mass on a spring. Adjust the mass, stiffness, 
        and damping coefficient to observe undamped, underdamped, critically damped, and overdamped motion.

        ### How to Use

        1. Select a simulation from the **Sidebar** on the left
        2. Adjust the physical parameters using the sliders
        3. Click **Run Simulation** to generate the plot and view the results

        ### Documentation

        Full API and simulation documentation is available
        [here](https://amorenobr.github.io/Lab_Simulations_Python/docs/).


        """
        )

st.sidebar.success("Select a simulation above")
