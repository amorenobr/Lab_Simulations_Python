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
