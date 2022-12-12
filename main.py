import tkinter
from tkinter import filedialog
from PdfConvertr.PdfConverter import convertor


def browse(entry):
    filepath = filedialog.askopenfilename(initialdir=".\\PdfConvertor", title="Select a file"
                                          , filetypes=(("pdf files", "*.pdf"), ("all files", "*.*")))
    entry.insert(0, filepath)


root = tkinter.Tk()
root.geometry("700x200")
root.title("PDF to Word Convertor")

welcome_label = tkinter.Label(root, text="Welcome to our convertor!\nIn the input field below you can write the path "
                                         "of the pdf file you want to convert ot search it by using the browse button")
welcome_label.grid(row=0, column=0, columnspan=3)

file_field = tkinter.Entry(root, width=80)
file_field.grid(row=1, column=0)

browse_btn = tkinter.Button(root, text="Browse", command=lambda: browse(file_field))
browse_btn.grid(row=1, column=1)


convert_btn = tkinter.Button(root, text="Convert", command=lambda: convertor.covert_to_word(file_field.get()))
convert_btn.grid(row=2, column=0)

convert_highlight_btn = tkinter.Button(root, text="Convert highlighted parts only",
                                       command=lambda: convertor.convert_highlights_to_word(file_field.get()))
convert_highlight_btn.grid(row=2, column=1)

root.mainloop()


