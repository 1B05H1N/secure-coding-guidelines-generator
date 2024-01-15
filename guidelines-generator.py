import os
import sys
from openai import OpenAI

# Ensure the OpenAI API key is set in environment variables
api_key = os.getenv('OPENAI_API_KEY')
if not api_key:
    print("Error: OPENAI_API_KEY environment variable not set.")
    sys.exit(1)

client = OpenAI(api_key=api_key)

# Function to generate secure coding guidelines
def generate_secure_coding_guidelines(language, framework):
    try:
        # Construct the prompt for OpenAI's GPT-3 model
        prompt = (
            f"Generate secure coding guidelines for {language} with {framework} framework."
            # You can add more context or specific questions here if needed.
        )

        # Generating the guidelines using OpenAI API
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are going to help generate secure coding guidelines."},
                {"role": "user", "content": prompt}
            ],
        )
        response_message = response.choices[0].message.content

        # Check if the response is empty
        if not response_message.strip():
            print("Received an empty response from OpenAI. Please try again.")
            return None

        return response_message.strip()
    except Exception as e:
        print(f"Error generating secure coding guidelines: {e}")
        return None

def main():
    # Prompt the user for the programming language and framework
    language = input("Enter the programming language: ")
    framework = input("Enter the framework (if any): ")

    # Generate secure coding guidelines
    guidelines = generate_secure_coding_guidelines(language, framework)

    if guidelines:
        # Print or save the guidelines based on user preference
        output_format = input("Do you want to save the guidelines to a file? (yes/no): ").lower()
        if output_format == "yes":
            file_name = input("Enter the file name (e.g., guidelines.txt): ")
            try:
                with open(file_name, 'w') as file:
                    file.write(guidelines)
                print(f"Guidelines saved to {file_name}")
            except Exception as e:
                print(f"Error saving the guidelines to the file: {e}")
        else:
            # Print the guidelines to the console
            print("\nSecure Coding Guidelines:")
            print(guidelines)

if __name__ == "__main__":
    main()
