# JARVIS - Langchain Voice Assistant Project

This Voice Assistant project leverages the power of the OpenAI GPT model, pyttsx3 for text-to-speech, speech_recognition for converting spoken language into text, and python-dotenv for managing environment variables. It's designed to provide an interactive and conversational AI experience, inspired by Jarvis from the Iron Man series.

## Features

- **Dynamic Conversations**: Utilizes `langchain` and `langchain_openai` for complex and coherent chat capabilities.
- **Customizable Settings**: Configure model, voice, volume, and more via command-line arguments or environment variables.
- **Session Management**: Supports dynamic session IDs for managing conversation history.
- **Speech Recognition**: Includes phrase time limit settings for improved responsiveness.

## Requirements

- Python 3.7+
- An OpenAI API key

## Installation

Before you begin, ensure you have Python installed on your system. Then, clone this repository and navigate into the project directory.

1. **Clone the Repository**

```bash
git clone https://github.com/meirm/jarvis
cd jarvis
```

2. **Install Dependencies**

```bash
pip install -r requirements.txt
```

Your `requirements.txt` file should contain the following:

```
langchain
pyttsx3
speech_recognition
python-dotenv
```

If the `speech_recognition` package didn't install successfully, alternatively you can install the package directly from the source code by cloning the Git repository and running the setup.py script:
```
git clone https://github.com/Uberi/speech_recognition.git
cd speech_recognition
python setup.py install
```


3. **Environment Setup**

Create a `.env` file in the root of your project directory. Add your OpenAI API key like so:

```env
OPENAI_API_KEY=your_api_key_here
```

Replace `your_api_key_here` with your actual OpenAI API key.

## Usage

Run the assistant using the following command:

```bash
python jarvis.py
```

List available options by calling --help

```bash
python jarvis --help
```

List available voices

```bash
python jarvis --list_voices
```

You can customize the behavior of the assistant by providing command-line arguments. For example:

```bash
python jarvis.py --model gpt-3.5-turbo --voice com.apple.speech.synthesis.voice.Ralph
```

For a full list of options, use the help command:

```bash
python jarvis.py --help
```

## Credits

Project based on the original work of @ShaunLinTW https://github.com/ShaunLinTW/Voice_Assistant_Jarvis_Based_on_ChatGPT_API

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue if you have suggestions or improvements.

## License

This project is open-sourced under the MIT License. See the LICENSE file for more details.
