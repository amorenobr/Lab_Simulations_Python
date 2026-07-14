import streamlit as st

LANGUAGES = {"English": "en", "Español": "es"}

TRANSLATIONS = {
        "en": {
            "app_title": "Welcome to the Physics Lab Simulations",
            "sidebar_select": "Select a simulation above",
            "landing_body": """
            This is an interactive collection of physics lab simulations designed to explore key concepts 
            in classical mechanics. Each simulation allows you to adjust different physical parameters 
            and see the results update in real time.

            ### Available Simulations
            - **Linear Motion** - Model a particle moving in a straight line with constant acceleration. 
            Set the initial position, initial velocity, acceleration, and time to observe the position 
            and velocity evolve over time and read off the final position and velocity.
            - **Projectile Motion** - Launch a projectile with a chosen speed and angle, then visualize 
            its trajectory. The simulation computes and displays the time of flight, maximum height, 
            and horizontal range using the kinematic equations.
            - **Damped Harmonic Oscillator** - Explore the motion of a mass on a spring. Adjust the mass, 
            stiffness, and damping coefficient to observe undamped, underdamped, critically damped, 
            and overdamped motion.

            ### How to Use
            1. Select a simulation from the **Sidebar** on the left
            2. Adjust the physical parameters using the sliders
            3. Click **Run Simulation** to generate the plot and view the results

            ### Documentation
            Full API and simulation documentation is available
            [here](https://amorenobr.github.io/Lab_Simulations_Python/docs/).
            """,

            # --- Shared UI ---
            "sim_parameters": "Simulation Parameters",
            "run_simulation": "Run Simulation",
            "plots": "Plots",
            "sim_results": "Simulation Results",
            "sim_complete": "Simulation Complete!",
            "time_s": "Time (s)",

            # --- Linear Motion ---
            "lm_title": "Linear Motion Simulation",
            "lm_intro": """
            **Linear Motion** describes the path of an object on X with a constant acceleration. 

            Given an initial position $x_0$, and initial velocity $v_0$, a constant acceleration $a$, 
            and a time $t$, we obtain:

            - **Final position:** $x_f = x_0 + (v_0 * t) + \\dfrac{1}{2}*a*t^2$ 
            - **Final velocity:** $v_f = v_0 + a * t$

            Use the sidebar to set the initial position, initial velocity, constant acceleration and 
            time, then click the "Run Simulation" to view the plots and calculated results.
            """,

            "lm_position": "Initial Position (m)",
            "lm_velocity": "Initial Velocity (m/s)",
            "lm_acceleration": "Constant Acceleration (m/s²)",
            "lm_current_params": "Current parameters: **{p} m**, **{v} m/s**, **{a} m/s²** and **{tm} s**",
            "lm_pos_vs_time": "Position vs. Time",
            "lm_vel_vs_time": "Velocity vs. Time",
            "lm_position_axis": "Position (m)",
            "lm_velocity_axis": "Velocity (m/s)",
            "lm_hover_position": "Time: %{x:.2f} s<br>Position: %{y:.2f} m<extra></extra>",
            "lm_hover_velocity": "Time: %{x:.2f} s<br>Velocity: %{y:.2f} m/s<extra></extra>",
            "lm_final_position": "Final Position",
            "lm_final_velocity": "Final Velocity",
            },
        "es": {
            "app_title": "Bienvenido a las Simulaciones de Laboratorio de Física",
            "sidebar_select": "Selecciona una simulación arriba",
            "landing_body": """
            Esta es una colección interactiva de simulaciones de laboratorio de física diseñada para explorar 
            conceptos clave de la mecánica clásica. Cada simulación te permite ajustar diferentes parámetros 
            físicos y ver los resultados actualizarse en tiempo real.

            ### Simulaciones disponibles
            - **Movimiento rectilíneo** - Modela una partícula que se mueve en línea recta con aceleración 
            constante. Define la posición inicial, la velocidad inicial, la aceleración y el tiempo para 
            observar cómo evoluciona la posición y la velocidad, y leer la posición y la velocidad finales.
            - **Movimiento de proyectil** - Lanza un proyectil con una rapidez y un ángulo elegidos y visualiza 
            su trayectoria. La simulación calcula el tiempo de vuelo, la altura máxima y el alcance horizontal 
            usando las ecuaciones cinemáticas.
            - **Oscilador armónico amortiguado** - Explora el movimiento de una masa en un resorte. Ajusta la 
            masa, la rigidez y el coeficiente de amortiguamiento para observar movimiento no amortiguado, 
            subamortiguado, con amortiguamiento crítico y sobreamortiguado.

            ### Cómo usar
            1. Selecciona una simulación en la **barra lateral** de la izquierda
            2. Ajusta los parámetros físicos con los deslizadores
            3. Haz click en **Ejecutar simulación** para generar la gráfica y ver los resultados

            ### Documentación
            La documentación completa de la API y las simulaciones están
            disponibles [aquí](https://amorenobr.github.io/Lab_Simulations_Python/docs/).
            """,

            # --- Shared UI ---
            "sim_parameters": "Parámetros de la Simulación",
            "run_simulation": "Ejecutar Simulación",
            "plots": "Gráficas",
            "sim_results": "Resultados de la Simulación",
            "sim_complete": "Simulación Completa!",
            "time_s": "Tiempo (s)",

            # --- Linear Motion ---
            "lm_title": "Simulación de Movimiento Rectilíneo",
            "lm_intro": """
            El **movimiento rectilíneo** describe la trayectoria de un objeto a lo largo de X con aceleración constante. 

            Dada una posición inicial $x_0$, una velocidad inicial $v_0$, una aceleración constante $a$ y un tiempo $t$, 
            obtenemos:

            - **Posición final:** $x_f = x_0 + v_0 t + \\dfrac{1}{2} a t^2$
            - **Velocidad final:** $v_f = v_0 + a t$ 

            Usa la barra lateral para definir la posición inicial, la velocidad inicial, la aceleración constante y el 
            tiempo; luego haz clic en **Ejecutar Simulación** para ver las gráficas y los resultados.
            """,
            
            "lm_position": "Posición inicial (m)", 
            "lm_velocity": "Velocidad inicial (m/s)", 
            "lm_acceleration": "Aceleración constante (m/s²)", 
            "lm_current_params": "Parámetros actuales: **{p} m**, **{v} m/s**, **{a} m/s²** y **{tm} s**", 
            "lm_pos_vs_time": "Posición vs. Tiempo", 
            "lm_vel_vs_time": "Velocidad vs. Tiempo", 
            "lm_position_axis": "Posición (m)", 
            "lm_velocity_axis": "Velocidad (m/s)", 
            "lm_hover_position": "Tiempo: %{x:.2f} s<br>Posición: %{y:.2f} m<extra></extra>", 
            "lm_hover_velocity": "Tiempo: %{x:.2f} s<br>Velocidad: %{y:.2f} m/s<extra></extra>", 
            "lm_final_position": "Posición final", 
            "lm_final_velocity": "Velocidad final",
            },
        }

def get_lang() -> str:
    """Current language code (defaults to English)."""
    return st.session_state.get("lang", "en")

def t(key: str) -> str:
    """Translate a key for the current language; fall back to English, then the key."""
    lang = get_lang()
    return TRANSLATIONS.get(lang, {}).get(key) or TRANSLATIONS["en"].get(key, key)

def language_selector() -> None:
    """Render the language toggle in the sidebar and store the choice in session_state."""
    choice = st.sidebar.radio(
            "🌐 Language / Idioma",
            list(LANGUAGES.keys()),
            horizontal=True,
            key="lang_selector",
            )
    st.session_state["lang"] = LANGUAGES[choice]
