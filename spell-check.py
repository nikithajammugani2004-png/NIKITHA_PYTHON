import tkinter as tk
from tkinter import scrolledtext, messagebox
from spellchecker import SpellChecker
import pyperclip  # Install via: pip install pyperclip

class VisualSpellChecker:
    def __init__(self, root):
        self.root = root
        self.root.title("AI Spell Checker Pro")
        self.root.geometry("800x600")
        self.root.configure(bg="#ffffff")
        
        self.spell = SpellChecker()
        self.setup_styles()
        self.setup_ui()

    def setup_styles(self):
        self.primary_color = "#4f46e5"  # Modern Indigo
        self.secondary_color = "#f8fafc"
        self.accent_color = "#ef4444"    # Red for errors
        self.text_color = "#1e293b"

    def setup_ui(self):
        # --- Header ---
        header = tk.Frame(self.root, bg=self.primary_color, height=80)
        header.pack(fill="x")
        tk.Label(header, text="✨ AI SPELL CHECKER PRO", font=("Segoe UI", 18, "bold"), 
                 bg=self.primary_color, fg="white").pack(pady=20)

        # --- Main Container ---
        main_frame = tk.Frame(self.root, bg="white", padx=30, pady=20)
        main_frame.pack(fill="both", expand=True)

        # --- Input Section ---
        tk.Label(main_frame, text="YOUR TEXT", font=("Segoe UI", 10, "bold"), 
                 bg="white", fg="#64748b").pack(anchor="w")
        
        self.input_area = scrolledtext.ScrolledText(main_frame, height=8, font=("Segoe UI", 12),
                                                   bd=2, relief="flat", bg=self.secondary_color,
                                                   highlightthickness=1, highlightbackground="#e2e8f0")
        self.input_area.pack(fill="x", pady=(5, 15))
        self.input_area.bind("<KeyRelease>", self.update_char_count)

        # --- Controls (Buttons) ---
        btn_frame = tk.Frame(main_frame, bg="white")
        btn_frame.pack(fill="x", pady=10)

        self.check_btn = tk.Button(btn_frame, text="Check Spelling", command=self.process_text,
                                   bg=self.primary_color, fg="white", font=("Segoe UI", 11, "bold"), 
                                   padx=25, pady=8, relief="flat", cursor="hand2")
        self.check_btn.pack(side="left")
        
        self.copy_btn = tk.Button(btn_frame, text="Copy Result", command=self.copy_text,
                                  bg="#10b981", fg="white", font=("Segoe UI", 11, "bold"), 
                                  padx=25, pady=8, relief="flat", cursor="hand2")
        self.copy_btn.pack(side="left", padx=10)

        self.info_label = tk.Label(btn_frame, text="Chars: 0", font=("Segoe UI", 10), bg="white", fg="#94a3b8")
        self.info_label.pack(side="right", pady=10)

        # --- Output Section ---
        tk.Label(main_frame, text="CORRECTED RESULT", font=("Segoe UI", 10, "bold"), 
                 bg="white", fg="#64748b").pack(anchor="w")

        self.output_area = tk.Text(main_frame, height=8, font=("Segoe UI", 12),
                                  bd=0, bg=self.secondary_color, padx=10, pady=10,
                                  highlightthickness=1, highlightbackground="#e2e8f0", state='disabled')
        self.output_area.pack(fill="x", pady=5)
        
        # Tags for styling corrections
        self.output_area.tag_configure("correction", foreground=self.accent_color, font=("Segoe UI", 12, "bold", "underline"))

    def update_char_count(self, event=None):
        count = len(self.input_area.get("1.0", tk.END).strip())
        self.info_label.config(text=f"Chars: {count}")

    def copy_text(self):
        corrected_text = self.output_area.get("1.0", tk.END).strip()
        if corrected_text:
            pyperclip.copy(corrected_text)
            messagebox.showinfo("Success", "Text copied to clipboard!")

    def process_text(self):
        raw_text = self.input_area.get("1.0", tk.END).strip()
        if not raw_text: 
            return

        # Split text but keep punctuation
        import re
        tokens = re.findall(r"[\w']+|[.,!?;:]", raw_text)
        
        self.output_area.config(state='normal')
        self.output_area.delete("1.0", tk.END)

        for word in tokens:
            # Only check if it's alphanumeric (skip dots, commas)
            if word.isalnum():
                correction = self.spell.correction(word)
                if correction and correction.lower() != word.lower():
                    self.output_area.insert(tk.END, correction, "correction")
                    self.output_area.insert(tk.END, " ")
                else:
                    self.output_area.insert(tk.END, word + " ")
            else:
                # Append punctuation directly to the previous word
                self.output_area.delete("end-2c", "end-1c") # remove last space
                self.output_area.insert(tk.END, word + " ")

        self.output_area.config(state='disabled')

if __name__ == "__main__":
    root = tk.Tk()
    # Adding a simple fade-in effect feel
    root.attributes('-alpha', 0.0)
    app = VisualSpellChecker(root)
    
    # Smooth fade in
    alpha = 0.0
    while alpha < 1.0:
        alpha += 0.1
        root.attributes('-alpha', alpha)
        root.update()
        import time
        time.sleep(0.02)
        
    root.mainloop()
