from sentence_transformers import SentenceTransformer, InputExample,losses
from torch.utils.data import DataLoader

model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')

trainset = []
with open("text.txt",'r') as file:  
    data = file.readlines()
    data = [line.rstrip('\n') for line in data]

for i in data:
  trainset.append(InputExample(texts=[i, i, i]))

train_dataloader = DataLoader(trainset, shuffle=True, batch_size=16)
train_loss = losses.TripletLoss(model=model)
model.fit(train_objectives=[(train_dataloader, train_loss)], epochs=5)
model.save('FineTuned')

