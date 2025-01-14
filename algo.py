from surprise.model_selection import cross_validate,train_test_split
from surprise import Dataset,Reader,accuracy
from surprise import SVD, BaselineOnly,get_dataset_dir,KNNBaseline
import os
import pandas as pd

df = pd.read_csv(os.getcwd()+"/movie_list.csv")

class Movie_rec():
    # def __init__(self):
    #     pass
    def Knn(n,sw,k=10):
            
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

        matches,matlis = Movie_rec.search(sw)
        print("THIS IS n VALUE     : ",n)
        print("THIS IS REQ_VALUE   : ",sw)
        print("THIS IS matlis      : ",matlis)
        print("THIS IS matches     : ",matches)

        movie_neighbors_names = []
        movie_neighbors_rawIds = []
       
        if n:
            # Retrieve inner id of the movie Toy Story
            movie_raw_id = name_to_rid[n]
            movie_inner_id = algo.trainset.to_inner_iid(movie_raw_id)

            # Retrieve inner ids of the nearest neighbors of Toy Story. 
            movie_neighbors = algo.get_neighbors(movie_inner_id, k=k)

            # Convert inner ids of the neighbors into names
            for i in movie_neighbors:
                movie_neighbors_rawIds.append(algo.trainset.to_raw_iid(i))

            for rid in movie_neighbors_rawIds:
                movie_neighbors_names.append(rid_to_name[rid])

        return movie_neighbors_names,sorted(matlis),k
        
    
    def search(n):
        
        matlis = list()
        matches = list()
        # print(df["movie"])
        if n:
            print("running search operations......")
            matches = sorted([i for i in df["movie"] if n==(i[0:len(n)]).lower()])
            if matches:
                matlis = map(lambda x:df[df["movie"] == x]["name"].tolist()[0],matches)
            else:
                print("MATCH NOT FOUND!")
                matlis = df["name"]
        else:
            print("ENTER SOMETHING!")
            matlis = df["name"]

        return matches,list(matlis)
    
    def all_movies():
        return sorted(df["name"])        


if __name__ == '__main__':
    Movie_rec.search()
