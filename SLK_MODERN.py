import tkinter as tk
from tkinter import ttk
import threading
import time
import random
import os
import sys
import winsound

class SLKModern:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("SLK Security System")
        self.root.geometry("1000x800")
        self.root.configure(bg='#0a0a0a')
        self.root.resizable(False, False)
        
        # BLOQUER
        self.root.protocol("WM_DELETE_WINDOW", lambda: None)
        
        # Centrer
        self.center_window(self.root, 1000, 800)
        
        # Toujours au-dessus
        self.root.attributes('-topmost', True)
        
        # Couleurs MODERNES
        self.bg = '#0a0a0a'
        self.bg_card = '#1a1a1a'
        self.accent = '#FFD700'
        self.accent2 = '#FFA500'
        self.red = '#FF3366'
        self.green = '#00FF88'
        self.blue = '#00BFFF'
        self.purple = '#9D4EDD'
        
        # Compteur
        self.soumis_count = 0
        
        # MUSIQUE
        self.start_music()
        
        # Interface MODERNE
        self.create_modern_page()
        
    def get_sound_path(self):
        if getattr(sys, 'frozen', False):
            base = sys._MEIPASS
        else:
            base = os.path.dirname(os.path.abspath(__file__))
        return os.path.join(base, 'slk_sound.wav')
    
    def start_music(self):
        def play():
            sound_path = self.get_sound_path()
            if os.path.exists(sound_path):
                while True:
                    try:
                        winsound.PlaySound(sound_path, winsound.SND_FILENAME)
                    except:
                        time.sleep(0.1)
            else:
                while True:
                    winsound.Beep(1000, 300)
                    winsound.Beep(1500, 300)
                    time.sleep(0.2)
        threading.Thread(target=play, daemon=True).start()
        
    def center_window(self, window, width, height):
        sw = window.winfo_screenwidth()
        sh = window.winfo_screenheight()
        x = (sw - width) // 2
        y = (sh - height) // 2
        window.geometry(f"{width}x{height}+{x}+{y}")
        
    def create_modern_page(self):
        # CONTAINER PRINCIPAL
        main = tk.Frame(self.root, bg=self.bg)
        main.pack(fill=tk.BOTH, expand=True, padx=30, pady=30)
        
        # === HEADER CARD ===
        header = tk.Frame(main, bg=self.bg_card, highlightbackground=self.accent,
                         highlightthickness=3, relief='flat')
        header.pack(fill=tk.X, pady=(0, 20))
        
        # Mini label TOP
        top_label = tk.Label(header, text="SECURITY SYSTEM v2.0",
                            font=('Segoe UI', 9),
                            fg='#888888', bg=self.bg_card)
        top_label.pack(pady=(15, 5))
        
        # TITRE MODERNE avec dégradé simulé
        title_frame = tk.Frame(header, bg=self.bg_card)
        title_frame.pack(pady=(0, 10))
        
        title1 = tk.Label(title_frame, text="SLK",
                         font=('Segoe UI Black', 80, 'bold'),
                         fg=self.accent, bg=self.bg_card)
        title1.pack(side=tk.LEFT)
        
        title2 = tk.Label(title_frame, text=" LE ROI",
                         font=('Segoe UI Black', 80, 'bold'),
                         fg=self.accent2, bg=self.bg_card)
        title2.pack(side=tk.LEFT)
        
        # Sous-titre
        subtitle = tk.Label(header, text="👑 SYSTÈME DE CONTRÔLE ABSOLU 👑",
                           font=('Segoe UI', 14, 'bold'),
                           fg='#CCCCCC', bg=self.bg_card)
        subtitle.pack(pady=(0, 20))
        
        # === STATUS BAR ===
        status_bar = tk.Frame(main, bg=self.bg_card, highlightbackground=self.red,
                             highlightthickness=2)
        status_bar.pack(fill=tk.X, pady=(0, 20))
        
        status_left = tk.Frame(status_bar, bg=self.bg_card)
        status_left.pack(side=tk.LEFT, padx=20, pady=15)
        
        tk.Label(status_left, text="● STATUT",
                font=('Segoe UI', 10, 'bold'),
                fg=self.red, bg=self.bg_card).pack(anchor=tk.W)
        
        tk.Label(status_left, text="Système activé",
                font=('Segoe UI', 9),
                fg='#999999', bg=self.bg_card).pack(anchor=tk.W)
        
        # === BOUTON PRINCIPAL MODERNE ===
        btn_container = tk.Frame(main, bg=self.bg)
        btn_container.pack(pady=30)
        
        # Effet de glow simulé avec plusieurs frames
        glow3 = tk.Frame(btn_container, bg='#664400', highlightthickness=0)
        glow3.place(relx=0.5, rely=0.5, anchor='center', width=560, height=130)
        
        glow2 = tk.Frame(btn_container, bg='#885500', highlightthickness=0)
        glow2.place(relx=0.5, rely=0.5, anchor='center', width=540, height=110)
        
        glow1 = tk.Frame(btn_container, bg='#AA6600', highlightthickness=0)
        glow1.place(relx=0.5, rely=0.5, anchor='center', width=520, height=90)
        
        self.main_btn = tk.Button(btn_container,
                                  text="⚡ IMPLORER LE ROI SLK ⚡",
                                  font=('Segoe UI Black', 28, 'bold'),
                                  fg='#000000',
                                  bg=self.accent,
                                  activebackground=self.accent2,
                                  activeforeground='#000000',
                                  relief='flat',
                                  bd=0,
                                  cursor='hand2',
                                  command=self.create_soumis_modern,
                                  padx=40,
                                  pady=25)
        self.main_btn.pack()
        
        # === ENCRYPTION PANEL ===
        crypto_panel = tk.Frame(main, bg=self.bg_card,
                               highlightbackground=self.red,
                               highlightthickness=2)
        crypto_panel.pack(fill=tk.BOTH, expand=True, pady=(20, 0))
        
        # Header du panel
        crypto_header = tk.Frame(crypto_panel, bg='#2a0a0a')
        crypto_header.pack(fill=tk.X)
        
        tk.Label(crypto_header, text="🔒 PROCESSUS DE CRYPTAGE",
                font=('Segoe UI', 16, 'bold'),
                fg=self.red, bg='#2a0a0a').pack(side=tk.LEFT, padx=20, pady=15)
        
        tk.Label(crypto_header, text="● EN COURS",
                font=('Segoe UI', 10, 'bold'),
                fg='#FF6666', bg='#2a0a0a').pack(side=tk.RIGHT, padx=20)
        
        # Contenu crypto
        crypto_content = tk.Frame(crypto_panel, bg=self.bg_card)
        crypto_content.pack(fill=tk.BOTH, expand=True, padx=25, pady=20)
        
        # File actuel
        self.file_lbl = tk.Label(crypto_content,
                                text="📁 C:\\Users\\Documents\\passwords.txt",
                                font=('Consolas', 11),
                                fg=self.green, bg=self.bg_card,
                                anchor=tk.W)
        self.file_lbl.pack(fill=tk.X, pady=(0, 15))
        
        # Progress bar MODERNE
        prog_frame = tk.Frame(crypto_content, bg='#0a0a0a',
                             highlightbackground='#333333',
                             highlightthickness=1)
        prog_frame.pack(fill=tk.X, pady=(0, 10))
        
        self.prog_canvas = tk.Canvas(prog_frame, height=30, bg='#0a0a0a',
                                     highlightthickness=0)
        self.prog_canvas.pack(fill=tk.X, padx=2, pady=2)
        
        # Pourcentage
        self.pct = tk.Label(crypto_content,
                           text="0% • 0 / 15,847 fichiers cryptés",
                           font=('Segoe UI', 12, 'bold'),
                           fg='#FFFFFF', bg=self.bg_card)
        self.pct.pack(pady=(5, 15))
        
        # Warning
        warning_frame = tk.Frame(crypto_content, bg='#2a0000',
                                highlightbackground=self.red,
                                highlightthickness=1)
        warning_frame.pack(fill=tk.X)
        
        tk.Label(warning_frame, text="⚠️ ATTENTION",
                font=('Segoe UI', 11, 'bold'),
                fg='#FF6666', bg='#2a0000').pack(side=tk.LEFT, padx=15, pady=10)
        
        tk.Label(warning_frame, text="Ne pas éteindre l'ordinateur pendant le processus",
                font=('Segoe UI', 10),
                fg='#CCCCCC', bg='#2a0000').pack(side=tk.LEFT, padx=5, pady=10)
        
        # ANIMATIONS
        self.anim_crypto()
        self.anim_btn()
        self.anim_files()
        
    def anim_crypto(self):
        def update_progress():
            pct = [0]
            while True:
                for i in range(101):
                    # Dessiner la barre
                    self.prog_canvas.delete('all')
                    width = self.prog_canvas.winfo_width()
                    if width > 1:
                        filled = int((i / 100) * width)
                        # Fond
                        self.prog_canvas.create_rectangle(0, 0, width, 30,
                                                         fill='#1a0000', outline='')
                        # Barre gradient rouge
                        for x in range(filled):
                            color_val = int(255 - (x / width * 100))
                            color = f'#{255:02x}{color_val:02x}{color_val:02x}'
                            self.prog_canvas.create_line(x, 0, x, 30, fill=color)
                    
                    # Texte
                    f = int((i / 100) * 15847)
                    self.pct.config(text=f"{i}% • {f:,} / 15,847 fichiers cryptés")
                    time.sleep(0.03)
                time.sleep(0.5)
        threading.Thread(target=update_progress, daemon=True).start()
    
    def anim_files(self):
        files = [
            "📁 C:\\Users\\Documents\\passwords.txt",
            "📁 C:\\Users\\Pictures\\family_photos.jpg",
            "📁 C:\\Users\\Desktop\\work_important.docx",
            "📁 C:\\Windows\\System32\\critical.dll",
            "📁 C:\\Users\\Downloads\\bank_statement.pdf",
            "📁 C:\\Discord\\tokens.db",
            "📁 C:\\AppData\\cookies.json",
            "📁 C:\\Users\\crypto_wallet.dat",
            "📁 C:\\Users\\Desktop\\private_keys.txt",
            "📁 C:\\Windows\\System32\\drivers\\network.sys"
        ]
        
        def change():
            self.file_lbl.config(text=random.choice(files))
            self.root.after(700, change)
        change()
    
    def anim_btn(self):
        colors = [self.accent, self.accent2, '#FFBB00', self.accent]
        i = [0]
        
        def pulse():
            self.main_btn.config(bg=colors[i[0] % len(colors)])
            i[0] += 1
            self.root.after(500, pulse)
        pulse()
    
    def create_soumis_modern(self):
        self.soumis_count += 1
        
        w = tk.Toplevel(self.root)
        w.title(f"SLK System #{self.soumis_count}")
        
        if self.soumis_count == 1:
            width, height = 1100, 750
        else:
            width = max(500, 1100 - (self.soumis_count * 60))
            height = max(400, 750 - (self.soumis_count * 50))
        
        w.geometry(f"{width}x{height}")
        w.configure(bg='#000000')
        
        if self.soumis_count > 1:
            x = random.randint(50, 400)
            y = random.randint(50, 250)
            w.geometry(f"{width}x{height}+{x}+{y}")
        else:
            self.center_window(w, width, height)
        
        w.attributes('-topmost', True)
        w.protocol("WM_DELETE_WINDOW", lambda: self.on_close(w))
        
        # BACKGROUND avec gradient simulé
        bg_frame = tk.Frame(w, bg='#000000')
        bg_frame.pack(fill=tk.BOTH, expand=True)
        
        # Gradient layers
        for i in range(5):
            layer = tk.Frame(bg_frame, bg=f'#0{i}0{i}0{i}')
            layer.place(relx=0, rely=i*0.2, relwidth=1, relheight=0.2)
        
        # CONTENU
        content = tk.Frame(w, bg='#000000')
        content.place(relx=0.5, rely=0.5, anchor='center', relwidth=0.9, relheight=0.9)
        
        # URL LABEL EN HAUT
        url_frame = tk.Frame(content, bg='#1a1a1a', highlightbackground=self.accent,
                            highlightthickness=2)
        url_frame.pack(pady=(0, 30))
        
        tk.Label(url_frame, text="🌐 https://nexus-webshop.mysellauth.com",
                font=('Segoe UI', 14, 'bold'),
                fg=self.accent, bg='#1a1a1a').pack(padx=30, pady=15)
        
        # SOUMIS - Taille adaptative
        if self.soumis_count == 1:
            fs = 140
        else:
            fs = max(50, 140 - (self.soumis_count * 15))
        
        # Container pour SOUMIS avec effet néon
        soumis_container = tk.Frame(content, bg='#000000')
        soumis_container.pack(expand=True)
        
        # Effet glow SOUMIS
        glow_lbl3 = tk.Label(soumis_container, text="SOUMIS",
                            font=('Segoe UI Black', fs, 'bold'),
                            fg='#664400', bg='#000000')
        glow_lbl3.place(relx=0.5, rely=0.5, anchor='center')
        
        glow_lbl2 = tk.Label(soumis_container, text="SOUMIS",
                            font=('Segoe UI Black', fs, 'bold'),
                            fg='#AA6600', bg='#000000')
        glow_lbl2.place(relx=0.501, rely=0.501, anchor='center')
        
        main_lbl = tk.Label(soumis_container, text="SOUMIS",
                           font=('Segoe UI Black', fs, 'bold'),
                           fg=self.accent, bg='#000000')
        main_lbl.place(relx=0.502, rely=0.502, anchor='center')
        
        # Compteur
        if self.soumis_count > 1:
            count_frame = tk.Frame(content, bg='#1a1a1a',
                                  highlightbackground=self.blue,
                                  highlightthickness=2)
            count_frame.pack(side=tk.BOTTOM, pady=20)
            
            tk.Label(count_frame, text=f"FENÊTRE #{self.soumis_count}",
                    font=('Segoe UI', 16, 'bold'),
                    fg=self.blue, bg='#1a1a1a').pack(padx=25, pady=12)
        
        # Décorations première fenêtre
        if self.soumis_count == 1:
            # Top decoration
            top_dec = tk.Frame(content, bg='#000000')
            top_dec.pack(side=tk.TOP, pady=20)
            
            tk.Label(top_dec, text="✨ ⭐ 👑 ⭐ ✨ 💎 ✨ ⭐ 👑 ⭐ ✨",
                    font=('Segoe UI', 32),
                    fg=self.accent, bg='#000000').pack()
            
            # Message
            msg_frame = tk.Frame(content, bg='#0a0a0a',
                               highlightbackground=self.accent,
                               highlightthickness=2)
            msg_frame.pack(side=tk.BOTTOM, pady=30)
            
            tk.Label(msg_frame,
                    text="Tu as reconnu la suprématie absolue de SLK LE ROI",
                    font=('Segoe UI', 18, 'bold'),
                    fg='#FFFFFF', bg='#0a0a0a').pack(padx=30, pady=15)
        
        # Animation
        self.anim_soumis_modern(main_lbl)
        
    def on_close(self, w):
        w.destroy()
        if self.soumis_count < 10:
            self.create_soumis_modern()
            self.root.after(100, self.create_soumis_modern)
        elif self.soumis_count < 20:
            self.create_soumis_modern()
    
    def anim_soumis_modern(self, lbl):
        colors = [self.accent, self.red, self.green, self.blue, self.purple, self.accent]
        i = [0]
        
        def change():
            try:
                lbl.config(fg=colors[i[0] % len(colors)])
                i[0] += 1
                lbl.after(400, change)
            except:
                pass
        change()
        
    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = SLKModern()
    app.run()
