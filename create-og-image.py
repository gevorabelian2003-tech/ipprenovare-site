# Script pour générer l'image Open Graph d'IPP Renovare
# Image 1200x630px (taille standard Facebook/WhatsApp/LinkedIn)

from PIL import Image, ImageDraw, ImageFont
import os

LARGEUR = 1200
HAUTEUR = 630
ROUGE = (165, 14, 23)
ROUGE_FONCE = (122, 8, 16)
NOIR = (26, 26, 26)
NOIR_PROFOND = (15, 15, 15)
BLANC = (255, 255, 255)
GRIS_CLAIR = (220, 220, 220)

base_dir = os.path.dirname(os.path.abspath(__file__))
chemin_logo = os.path.join(base_dir, 'assets', 'images', 'logo.png')
chemin_sortie = os.path.join(base_dir, 'assets', 'images', 'og-image.jpg')

# Création du dégradé de fond rouge → noir (oblique)
img = Image.new('RGB', (LARGEUR, HAUTEUR), NOIR)
draw = ImageDraw.Draw(img)
for y in range(HAUTEUR):
    for x in range(LARGEUR):
        # Position relative diagonale
        t = (x + y * 0.6) / (LARGEUR + HAUTEUR * 0.6)
        if t < 0.4:
            # Dégradé rouge IPP → rouge foncé
            ratio = t / 0.4
            r = int(ROUGE[0] * (1 - ratio) + ROUGE_FONCE[0] * ratio)
            g = int(ROUGE[1] * (1 - ratio) + ROUGE_FONCE[1] * ratio)
            b = int(ROUGE[2] * (1 - ratio) + ROUGE_FONCE[2] * ratio)
        elif t < 0.7:
            # Transition rouge foncé → noir
            ratio = (t - 0.4) / 0.3
            r = int(ROUGE_FONCE[0] * (1 - ratio) + NOIR[0] * ratio)
            g = int(ROUGE_FONCE[1] * (1 - ratio) + NOIR[1] * ratio)
            b = int(ROUGE_FONCE[2] * (1 - ratio) + NOIR[2] * ratio)
        else:
            # Noir profond
            ratio = (t - 0.7) / 0.3
            r = int(NOIR[0] * (1 - ratio) + NOIR_PROFOND[0] * ratio)
            g = int(NOIR[1] * (1 - ratio) + NOIR_PROFOND[1] * ratio)
            b = int(NOIR[2] * (1 - ratio) + NOIR_PROFOND[2] * ratio)
        img.putpixel((x, y), (r, g, b))

# Trame subtile par-dessus (effet quadrillage discret)
for x in range(0, LARGEUR, 60):
    draw.line([(x, 0), (x, HAUTEUR)], fill=(255, 255, 255, 20), width=1)
for y in range(0, HAUTEUR, 60):
    draw.line([(0, y), (LARGEUR, y)], fill=(255, 255, 255, 20), width=1)

# Insertion du logo (à gauche)
try:
    logo = Image.open(chemin_logo).convert("RGBA")
    taille_logo = 380
    logo = logo.resize((taille_logo, taille_logo), Image.LANCZOS)
    pos_logo_x = 100
    pos_logo_y = (HAUTEUR - taille_logo) // 2
    img.paste(logo, (pos_logo_x, pos_logo_y), logo)
except Exception as e:
    print(f"Logo non chargé : {e}")

# Chargement des polices Windows
chemin_fonts_windows = "C:/Windows/Fonts/"
try:
    font_titre = ImageFont.truetype(chemin_fonts_windows + "georgiab.ttf", 78)
    font_sous = ImageFont.truetype(chemin_fonts_windows + "arial.ttf", 28)
    font_slogan = ImageFont.truetype(chemin_fonts_windows + "georgiai.ttf", 32)
    font_url = ImageFont.truetype(chemin_fonts_windows + "arialbd.ttf", 22)
except Exception as e:
    print(f"Police par défaut : {e}")
    font_titre = ImageFont.load_default()
    font_sous = ImageFont.load_default()
    font_slogan = ImageFont.load_default()
    font_url = ImageFont.load_default()

# Texte à droite du logo
pos_x = 540
pos_y = 180

# Petit trait rouge en haut
draw.rectangle([(pos_x, pos_y - 30), (pos_x + 60, pos_y - 22)], fill=ROUGE)

# Surtitre en blanc
draw.text((pos_x, pos_y), "ARTISAN PLÂTRIER", font=font_sous, fill=GRIS_CLAIR)

# Titre principal
draw.text((pos_x, pos_y + 45), "IPP Renovare", font=font_titre, fill=BLANC)

# Sous-titre
draw.text((pos_x, pos_y + 145), "Nancy · Laxou · Grand Est", font=font_sous, fill=GRIS_CLAIR)

# Slogan en italique
draw.text((pos_x, pos_y + 195), "« Ensemble, bâtissons un avenir solide »", font=font_slogan, fill=ROUGE)

# URL site en bas
draw.text((pos_x, pos_y + 280), "ipprenovare.com", font=font_url, fill=BLANC)

# Petit accent rouge en bas droite
draw.rectangle([(LARGEUR - 80, HAUTEUR - 80), (LARGEUR - 30, HAUTEUR - 30)], fill=ROUGE)

# Sauvegarde en JPG (compression de qualité)
img.save(chemin_sortie, "JPEG", quality=92, optimize=True)
print(f"Image OG créée : {chemin_sortie}")
print(f"Taille : {LARGEUR}x{HAUTEUR}px")
