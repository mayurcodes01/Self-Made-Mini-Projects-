# Personalized Quote Generator

A desktop application built with **Python** and **CustomTkinter** that fetches random quotes from the ZenQuotes API and transforms them into different styles such as funny, motivational, or poetic.

---

## Features

- Fetches quotes in real time from [ZenQuotes API](https://zenquotes.io)
- Displays both the original and a personalized version of the quote
- Three personalization styles available:
  - Funny Style (word replacements using synonyms)
  - Motivational Style (uplifting message)
  - Poetic Style (artistic transformation)
- Dark mode interface with modern **CustomTkinter** design

---

## Project Structure

```
Quote_Generator/
│
├── main.py            # Main GUI application
├── style_utils.py     # Contains quote styling functions
└── requirements.txt   # Required dependencies
```

---

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/mayurcodes01/Self-Made-Mini-Projects-/tree/main/API%20Projects/Quote_Generator
   cd Quote_Generator
   ```

2. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Linux/Mac
   venv\Scripts\activate      # On Windows
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

## Usage

Run the application with:
```bash
python main.py
```

- Click on **Generate Quote** to fetch a new random quote.
- The application will display both the **original quote** and a **personalized version** in one of the available styles.

---

## Dependencies

- Python 3.8+
- [customtkinter](https://github.com/TomSchimansky/CustomTkinter)
- requests
- nltk

Ensure that you have the **WordNet** corpus installed for NLTK:
```python
import nltk
nltk.download('wordnet')
```

---

## Example

- Original Quote:  
  *The best way to get started is to quit talking and begin doing.*

- Personalized Quote (Motivational Style):  
  *Remember: The best way to get started is to quit talking and begin doing. Keep going!*

---

## License

This project is open-source and available under the MIT License.

