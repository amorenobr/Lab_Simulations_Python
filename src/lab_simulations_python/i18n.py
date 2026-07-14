import streamlit as st

LANGUAGES = {"English": "en", "Español": "es"}

TRANSLATIONS = {
        "en": {
            "app_title": "Welcome to the Physics Lab Simulations",
            "sidebar_select": "Select a simulation above",
            "nav_home": "Home",
            "nav_linear": "Linear Motion",
            "nav_projectile": "Projectile Motion",
            "nav_oscillator": "Damped Oscillator",
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

            # --- Projectile Motion ---
            "pj_title": "Projectile Motion Simulation",
            "pj_intro": """
            **Projectile Motion** describes the path of an object launched into the air, 
            moving under the influence of gravity alone (air resistance is neglected). The horizontal and 
            vertical motions are independent: the horizontal velocity remains constant while the 
            vertical motion accelerates downward with acceleration $g = 9.81\\ \\mathrm{m/s^2}$. 

            Given an initial speed $v_0$ and launch angle $\\theta$, the key quantities are:

            - **Time of flight:** $t = \\dfrac{2 v_0 \\sin\\theta}{g}$
            - **Maximum height:** $h = \\dfrac{v_0^2 \\sin^2\\theta}{2g}$
            - **Horizontal range:** $R = \\dfrac{v_0^2 \\sin(2\\theta)}{g}$ 
            
            Use the sidebar to set the initial speed and launch angle, then click **Run Simulation** 
            to view the trajectory and calculated results.
            """,

            "pj_velocity": "Initial Velocity (m/s)", 
            "pj_angle": "Launch Angle (degrees)", 
            "pj_current_params": "Current parameters: **{v} m/s** at **{a}°**", 
            "pj_trajectory_plot": "Trajectory Plot", 
            "pj_traj_title": "Projectile Trajectory", 
            "pj_range_axis": "Range (m)", 
            "pj_height_axis": "Height (m)", 
            "pj_hover": "Range: %{x:.2f} m<br>Height: %{y:.2f} m<extra></extra>", 
            "pj_time_of_flight": "Time of Flight", 
            "pj_max_height": "Maximum Height", 
            "pj_horizontal_range": "Horizontal Range",

            # --- Oscillations ---
            "osc_title": "Damped Harmonic Oscillator Simulation",
            "osc_intro": """
            A **damped harmonic oscillator** models an object of a mass $m$ attached to a spring of stiffness $k$, 
            subject to a damping force proportional to its velocity (with damping coefficient $b$). Its motion 
            follows $m\\ddot{x} + b\\dot{x} + kx = 0$. 

            The system's behavior is determined by the **damping ratio** $\\zeta = \\dfrac{b}{2\\sqrt{km}}$, which defines 
            four regimes:

            - **Undamped** ($\\zeta = 0$): oscillates indefinitely at the natural frequency $\\omega_0 = \\sqrt{k/m}$
            - **Underdamped** ($\\zeta < 1$): oscillates with a gradually decaying amplitude
            - **Critically damped** ($\\zeta = 1$): returns to equilibrium as quickly as possible without oscillating
            - **Overdamped** ($\\zeta > 1$): returns to equilibrium without oscillating, more slowly than 
            the critically damped case 

            Set the mass, stiffness, initial amplitude, and damping coefficient in the sidebar, then click **Run Simulation** 
            to see the displacement over time.
            """,

            "osc_mass": "Mass (kg)",
            "osc_spring": "Spring Constant k (N/m)",
            "osc_amplitude": "Initial Amplitude (m)",
            "osc_damping": "Damping Coefficient b (kg/s)",
            "osc_current_params": "Current parameters: mass **{m} kg**, k **{k} N/m**, amplitude **{amp} m**, damping **{b} kg/s**",
            "osc_displacement_vs_time": "Displacement vs. Time",
            "osc_plot_title": "Oscillator Displacement",
            "osc_displacement_axis": "Displacement (m)",
            "osc_hover": "Time: %{x:.2f} s<br>Displacement: %{y:.3f} m<extra></extra>",
            "osc_complete_regime": "Simulation complete — regime: **{regime}**",
            "osc_natural_period": "Natural Period",
            "osc_natural_frequency": "Natural Frequency",
            "osc_damping_ratio": "Damping Ratio",
            "regime_undamped": "undamped",
            "regime_underdamped": "underdamped",
            "regime_critically damped": "critically damped",
            "regime_overdamped": "overdamped",
            },
        "es": {
            "app_title": "Bienvenido a las Simulaciones de Laboratorio de Física",
            "sidebar_select": "Selecciona una simulación arriba",
            "nav_home": "Inicio",
            "nav_linear": "Movimiento Rectilíneo",
            "nav_projectile": "Movimiento de Proyectil",
            "nav_oscillator": "Oscilador Amortiguado",
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

            # --- Projectile Motion ---
            "pj_title": "Simulación de Movimiento de Proyectil",
            "pj_intro": """
            El **movimiento de proyectil** describe la trayectoria de un objeto lanzado al aire, que se mueve únicamente 
            bajo la influencia de la gravedad (se desprecia la resistencia del aire). Los movimientos horizontal y vertical 
            son independientes: la velocidad horizontal permanece constante mientras que el movimiento vertical acelera 
            hacia abajo con aceleración $g = 9.81\\ \\mathrm{m/s^2}$. 

            Dada una rapidez inicial $v_0$ y un ángulo de lanzamiento $\\theta$, las cantidades clave son:
            - **Tiempo de vuelo:** $t = \\dfrac{2 v_0 \\sin\\theta}{g}$
            - **Altura máxima:** $h = \\dfrac{v_0^2 \\sin^2\\theta}{2g}$
            - **Alcance horizontal:** $R = \\dfrac{v_0^2 \\sin(2\\theta)}{g}$

            Usa la barra lateral para definir la rapidez inicial y el ángulo de lanzamiento; luego haz clic en **Ejecutar 
            Simulación** para ver la trayectoria y los resultados.
            """,

            "pj_velocity": "Velocidad inicial (m/s)",
            "pj_angle": "Ángulo de lanzamiento (grados)",
            "pj_current_params": "Parámetros actuales: **{v} m/s** a **{a}°**",
            "pj_trajectory_plot": "Gráfica de trayectoria",
            "pj_traj_title": "Trayectoria del proyectil",
            "pj_range_axis": "Alcance (m)",
            "pj_height_axis": "Altura (m)",
            "pj_hover": "Alcance: %{x:.2f} m<br>Altura: %{y:.2f} m<extra></extra>",
            "pj_time_of_flight": "Tiempo de vuelo",
            "pj_max_height": "Altura máxima",
            "pj_horizontal_range": "Alcance horizontal",

            # --- Oscillations ---
            "osc_title": "Simulación de Oscilador Armónico Amortiguado",
            "osc_intro": """
            Un **oscilador armónico amortiguado** modela un objeto de masa $m$ unido a un resorte de rigidez $k$, sujeto a 
            una fuerza de amortiguamiento proporcional a su velocidad (con coeficiente de amortiguamiento $b$). Su movimiento 
            sigue $m\\ddot{x} + b\\dot{x} + kx = 0$.

            El comportamiento del sistema está determinado por la **razón de amortiguamiento** $\\zeta = \\dfrac{b}{2\\sqrt{km}}$, 
            que define cuatro regímenes:
            
            - **No amortiguado** ($\\zeta = 0$): oscila indefinidamente a la frecuencia natural $\\omega_0 = \\sqrt{k/m}$
            - **Subamortiguado** ($\\zeta < 1$): oscila con una amplitud que decae gradualmente
            - **Amortiguamiento crítico** ($\\zeta = 1$): regresa al equilibrio lo más rápido posible sin oscilar
            - **Sobreamortiguado** ($\\zeta > 1$): regresa al equilibrio sin oscilar, más lentamente que el caso de 
            amortiguamiento crítico

            Define la masa, la rigidez, la amplitud inicial y el coeficiente de amortiguamiento en la barra lateral; luego 
            haz clic en **Ejecutar Simulación** para ver el desplazamiento en el tiempo.
            """,

            "osc_mass": "Masa (kg)",
            "osc_spring": "Constante del resorte k (N/m)",
            "osc_amplitude": "Amplitud inicial (m)",
            "osc_damping": "Coeficiente de amortiguamiento b (kg/s)",
            "osc_current_params": "Parámetros actuales: masa **{m} kg**, k **{k} N/m**, amplitud **{amp} m**, amortiguamiento **{b} kg/s**",
            "osc_displacement_vs_time": "Desplazamiento vs. Tiempo",
            "osc_plot_title": "Desplazamiento del oscilador",
            "osc_displacement_axis": "Desplazamiento (m)",
            "osc_hover": "Tiempo: %{x:.2f} s<br>Desplazamiento: %{y:.3f} m<extra></extra>",
            "osc_complete_regime": "Simulación completa — régimen: **{regime}**",
            "osc_natural_period": "Periodo natural",
            "osc_natural_frequency": "Frecuencia natural",
            "osc_damping_ratio": "Razón de amortiguamiento",
            "regime_undamped": "no amortiguado",
            "regime_underdamped": "subamortiguado",
            "regime_critically damped": "con amortiguamiento crítico",
            "regime_overdamped": "sobreamortiguado",
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
    """Render the sidebar: hide the default nav, add language toggle + translated nav."""
    st.markdown("""<style> 
                [data-testid="stSidebarNav"] { display: none; }
                section[data-testid="stMain"],
                [data-testid="stAppViewContainer"] { scrollbar-gutter: stable; }
                </style>""",
                unsafe_allow_html=True)
    choice = st.sidebar.radio(
            "🌐 Language / Idioma",
            list(LANGUAGES.keys()),
            horizontal=True,
            key="lang_selector",
            )
    st.session_state["lang"] = LANGUAGES[choice]

    # Translated page navigation (replaces the hidden, English-only default nav)
    st.sidebar.page_link("Simulations.py", label=t("nav_home"), icon="🏠")
    st.sidebar.page_link("pages/1_Linear_Motion.py", label=t("nav_linear"), icon="➡️")
    st.sidebar.page_link("pages/2_Projectile_Motion.py", label=t("nav_projectile"), icon="🎯")
    st.sidebar.page_link("pages/3_Oscillations.py", label=t("nav_oscillator"), icon="🌊")
