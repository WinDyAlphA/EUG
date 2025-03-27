import sys

def generate_usernames(input_file: str):
    try:
        with open(input_file, 'r') as file:
            names = file.readlines()
    except FileNotFoundError:
        print(f"Erreur: Le fichier '{input_file}' n'existe pas.")
        sys.exit(1)
    except Exception as e:
        print(f"Erreur lors de la lecture du fichier: {str(e)}")
        sys.exit(1)

    # Créer un set pour stocker les usernames uniques
    usernames = set()

    for name in names:
        # Nettoyer le nom des espaces et retours à la ligne
        name = name.strip()
        if not name:  # Ignorer les lignes vides
            continue
            
        # Split le nom en prénom et nom
        first_name, last_name = name.split(" ")[0], name.split(" ")[-1]
        
        # Ajouter toutes les combinaisons au set
        usernames.add(first_name + "." + last_name)
        usernames.add(first_name + last_name)
        usernames.add(last_name)
        usernames.add(first_name)
        
        for i in range(len(first_name)):
            first = first_name[:i+1]
            usernames.add(first + last_name)
            usernames.add(last_name + first)
            first_but_in_reverse = first_name[i:]
            usernames.add(first_but_in_reverse + last_name)
            usernames.add(last_name + first_but_in_reverse)
            
            for j in range(len(last_name)):
                last = last_name[:j+1]
                last_but_in_reverse = last_name[j:]
                if last.strip():
                    usernames.add(first + last)
                    usernames.add(last + first)
                    usernames.add(first + last_but_in_reverse)
                    usernames.add(last_but_in_reverse + first)
                    usernames.add(first_but_in_reverse + last_but_in_reverse)
                    usernames.add(last_but_in_reverse + first_but_in_reverse)

    # Écrire les usernames uniques dans le fichier
    with open('usernames.txt', 'w') as file:
        for username in sorted(usernames):  # sorted() pour avoir une liste triée
            file.write(username + "\n")

    print(f"Génération terminée. {len(usernames)} usernames uniques ont été créés.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python names.py <fichier_noms>")
        print("Example: python names.py names.txt")
        sys.exit(1)
        
    input_file = sys.argv[1]
    generate_usernames(input_file)

        
