import rdflib
import os

def add_species(species_file):
    g = rdflib.Graph()
    g.parse(species_file, format="ttl")

    # Connect to RDF store and update data
    store = rdflib.Graph('SPARQLStore')
    store.open('http://localhost:3030/treekipedia')

    for stmt in g:
        store.add(stmt)

    store.commit()
    print(f"Added species data from {species_file}")

if __name__ == "__main__":
    data_dir = "../data"
    for filename in os.listdir(data_dir):
        if filename.endswith(".ttl"):
            add_species(os.path.join(data_dir, filename))
