from docx import Document
import os
from summarizer import Summarizer

def save_to_docx(text, file_name):
    cur_directory = os.getcwd()

    output_dir = os.path.join(cur_directory, "output")

    filepath = os.path.join(output_dir, file_name)

    document = Document()
    for paragraph in text.split("\n"):
        if (len(paragraph) >= 1):
            document.add_paragraph(
                paragraph, #style='List Bullet'
            )

    document.save(filepath)

def summarize(combined_text):
    summarizer = Summarizer(combined_text)
    summary = summarizer.summarize()
    return summary

def load_input_file():
    f = open('input.txt', 'r')
    strings = f.readlines()
    f.close()

    combined_text = []
    for str in strings:
        combined_text.append((str[2:], str[:2]))

    return combined_text

def main():
    combined_text = load_input_file()
    summarized_text = summarize(combined_text)
    save_to_docx(summarized_text, "output.docx")

if __name__ == '__main__':
    main()