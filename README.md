# Tech-Focused News Agent

This project demonstrates the execution of tasks using a tech-focused crew configuration with enhanced feedback. The implementation includes web interfaces built using both Streamlit and Gradio.

## Table of Contents

- [Overview](#overview)
- [Installation](#installation)
- [Usage](#usage)
  - [Streamlit Interface](#streamlit-interface)
  - [Gradio Interface](#gradio-interface)
- [Contributing](#contributing)
- [License](#license)

## Overview

This project forms a tech-focused crew with enhanced configuration and executes tasks sequentially. The crew consists of agents and tasks managed by the `crewai` library. Users can input a topic for research, and the crew will execute the task and provide the results.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/Zeeshanunique/news_agent.git
    cd tech-focused-crew
    ```

2. Create a virtual environment and activate it:
    ```bash
    python -m venv venv
    # On Windows
    venv\Scripts\activate
    # On macOS/Linux
    source venv/bin/activate
    ```

3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

### Streamlit Interface

1. Save the Streamlit app code in a file named `app_streamlit.py`.

2. Run the Streamlit app:
    ```bash
    streamlit run app_streamlit.py
    ```

### Gradio Interface

1. Save the Gradio app code in a file named `app_gradio.py`.

2. Run the Gradio app:
    ```bash
    python app_gradio.py
    ```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
