# Guidelines Generator

## Overview

The **Guidelines Generator** is a Python script that leverages OpenAI's GPT-3 API to generate secure coding guidelines for different programming languages and frameworks. It assists developers in writing secure code from the start by providing tailored guidelines.

## Prerequisites

Before using this script, ensure that you have the following prerequisites:

1. **OpenAI API Key**: You need an API key from OpenAI. Make sure to set it as an environment variable with the name `OPENAI_API_KEY`.

## Usage

1. Clone or download the repository to your local machine.

2. Open a terminal or command prompt.

3. Navigate to the directory containing the script (`guidelines-generator.py`).

4. Run the script using the following command:
   ```
   python guidelines-generator.py
   ```

5. You will be prompted to enter the programming language and framework (if applicable) for which you want to generate secure coding guidelines.

6. The script will utilize OpenAI's GPT-3 model to generate guidelines based on your input.

7. You can choose to save the guidelines to a file or print them to the console.

## Example

Here's an example of how to use the script:

```bash
python guidelines-generator.py
```

You will then be prompted to enter the programming language and framework:

```
Enter the programming language: Python
Enter the framework (if any): Django
```

The script will generate secure coding guidelines for Python with the Django framework.
