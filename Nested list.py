# if __name__ == '__main__':
    
#     database = []
#     for _ in range(int(input())):
#         name = input()
#         score = float(input())
#         database.append([name, score])
#         database.sort(key=lambda x: x[1])
#         data = {
#             "name": database[0][0],
#             "score": database[0][1]
#         }
#     print(data['name'])
#Kurang literasi (Lowest)
      
     
     
if __name__ == '__main__':
    database = []

    for _ in range(int(input())):
        name = input()
        score = float(input())
        database.append([name, score])

    database.sort(key=lambda x: x[1])
    
    #[['nama', 30.0]
       #[0]    #[1]
       
    lowest_score = database[0][1]
    for name,score in database:
        if score > lowest_score:
            second_lowest_score = score
            break
        
    for name,score in sorted(database):
        if score == second_lowest_score:
            print(name)
        

  

            
        

        
     
        
       