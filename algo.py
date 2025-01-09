from surprise.model_selection import cross_validate,train_test_split
from surprise import Dataset,Reader,accuracy
from surprise import SVD, BaselineOnly,get_dataset_dir,KNNBaseline
import re

class Movie_rec():
    def __init__(self):
        pass
    def Knn(self,n):
            
        def read_item_name():
            file_name = get_dataset_dir() + "/ml-100k/ml-100k/u.item"
            rid_to_name = {}
            name_to_rid = {}
            with open(file_name) as f:
                for line in f:
                    line = line.split("|")
                    rid_to_name[line[0]] = line[1]
                    name_to_rid[line[1]] = line[0]

            return rid_to_name,name_to_rid

        data = Dataset.load_builtin("ml-100k")
        trainset = data.build_full_trainset()
        sim_options = {"name": "pearson_baseline", "user_based": False}
        algo = KNNBaseline(sim_options=sim_options)
        algo.fit(trainset)


        # Read the mappings raw id <-> movie name
        rid_to_name, name_to_rid = read_item_name()

        # Retrieve inner id of the movie Toy Story
        toy_story_raw_id = name_to_rid["Four Rooms (1995)"]
        toy_story_inner_id = algo.trainset.to_inner_iid(toy_story_raw_id)

        # Retrieve inner ids of the nearest neighbors of Toy Story.
        toy_story_neighbors = algo.get_neighbors(toy_story_inner_id, k=10)

        # Convert inner ids of the neighbors into names
        toy_story_neighbors_rawIds = []
        for i in toy_story_neighbors:
            toy_story_neighbors_rawIds.append(algo.trainset.to_raw_iid(i))

        toy_story_neighbors_names = []
        for rid in toy_story_neighbors_rawIds:
            toy_story_neighbors_names.append(rid_to_name[rid])


        print("The 10 nearest neighbors of Toy Story are:")
        for movie in toy_story_neighbors_names:
            print(movie)

if __name__ == '__main__':
    Movie_rec
