# cli.py
import argparse
import requests
import csv

def get_character_info(character_id):
    api_url = f"https://rickandmortyapi.com/api/character/{character_id}"
    response = requests.get(api_url)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: Unable to fetch character information for ID {character_id}. Status code: {response.status_code}")
        return None

def save_to_csv(character_info, filename):
    keys = character_info.keys()

    with open(filename, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=keys)
        writer.writeheader()
        writer.writerow(character_info)

def main():
    parser = argparse.ArgumentParser(description="Fetch character information from the Rick and Morty API.")

    parser.add_argument("character_id", type=int, help="ID of the character to fetch")

    args = parser.parse_args()

    character_id = args.character_id
    character_info = get_character_info(character_id)

    if character_info:
        print("Character Information:")
        print(f"Name: {character_info['name']}")
        print(f"Location: {character_info['location']}")
        print(f"Episode: {character_info['episode']}")

# Save to CSV
        csv_filename = f'character_info_{character_id}.csv'
        save_to_csv(character_info, csv_filename)
        print(f"Character information saved to {csv_filename}")

if __name__ == "__main__":
    main()